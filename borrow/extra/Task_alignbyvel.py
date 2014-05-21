# This task aligns one cube to another so that the spectral axes of
# the two output cubes match in velocity. This differs from the curent
# imregrid, which aligns the two cubes by frequency. Useful for, e.g.,
# comparing two different transitions or spectral lines in the same
# source.
#
# v0.1 - aleroy, aug 11

import numpy as np
import os, sys

from taskinit import *

def alignbyvel(infile = None
               , outfile = None
               , template = None
               , overwrite = True):

    casalog.origin('alignbyvel')

    # ===============================
    # ERROR CHECKING
    # ===============================
    
    if infile=='':
        casalog.post("ERROR: you must specify a file to align (INFILE).", \
                         priority='ERROR')
        return

    if outfile=='':
        casalog.post("ERROR: you must specify an output file name (OUTFILE).", \
                         priority='ERROR')
        return

    if template=='':
        casalog.post("ERROR: you must specify a template image (TEMPLATE).", \
                         priority='ERROR')
        return

    # ===============================
    # DELETE PREVIOUS OUTPUT OR FAIL
    # ===============================

    if os.path.isfile(outfile):
        if overwrite:
            casalog.post("Removing old version of "+outfile, 
                         priority = 'WARN')
            os.system("rm "+outfile)
        else:
            casalog.post("Output file exists and overwrite is False. Returning",
                         priority = 'ERROR')
            return

    # ===============================
    # WORK OUT TARGET COORDSYS
    # ===============================

    casalog.post("Working out target CoordSys...",priority="NORMAL")

    # --- EXTRACT INFO FROM INPUT

    casalog.post("... adopting template astrometry.",priority="NORMAL")

    # Extract the coordinate system and shape of the template cube. We
    # will force the output cube to match these.
    template_ia = ia.newimage(template)
    template_cs = template_ia.coordsys()
    target_shape = template_ia.shape()
    template_ia.close()

    inp_ia = ia.newimage(infile)
    inp_cs = inp_ia.coordsys()
    inp_ia.close()

    # Work out the spectral axis. This step is needed because we have
    # no guarantees on the spectral / stokes order.
    spec_axis = template_cs.axiscoordinatetypes().index("Spectral")
    
    # Define a new coordinate system that begins as a copy of the
    # template coordinate system.
    new_cs = template_cs.copy()

    # --- REFERENCE PIXEL

    casalog.post("... setting reference and rest frequency.",priority="NORMAL")

    # Work out the new reference frequency. This will be the frequency
    # that corresponds to the same velocity as the template reference
    # frequency but using the new rest frequency.
    orig_ref_freq = template_cs.referencevalue('n')['numeric'][spec_axis]
    orig_ref_vel = template_cs.frequencytovelocity(orig_ref_freq)

    # Set the new coordinate system to have the output reference
    # frequency
    new_cs.setrestfrequency(inp_cs.restfrequency())

    # Work out the new reference frequency using this rest frequency
    new_ref_freq = new_cs.velocitytofrequency(orig_ref_vel)
    new_cs.setreferencevalue(new_ref_freq,"spectral")

    # --- INCREMENT

    casalog.post("... setting frequency increment.",priority="NORMAL")

    # We want the increment in the target coordinate system to match
    # the velocity spacing in the original cube, but adjusted to the
    # new rest frequency.

    old_increment = new_cs.increment()['numeric'][spec_axis]
    new_increment = \
        inp_cs.restfrequency()['value'] / template_cs.restfrequency()['value']* \
        old_increment
    new_cs.setincrement(new_increment,type="spectral")

    # ===============================
    # REGRIDDING
    # ===============================

    casalog.post("Carrying out alignment...",priority="NORMAL")

    ia.open(infile)
    ia.regrid(outfile=outfile,
              shape=target_shape,
              csys=new_cs.torecord(),
              overwrite=False)
    ia.close()

    casalog.post("Success!", priority="NORMAL")

    return
    
    

