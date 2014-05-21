"""
Generate a list of mosaic pointings with a specified center, radius,
and mask.
"""

import pylab as pl
import numpy as np
import os

from tasks import *
from taskinit import *
import casac

from utils import geoutils as geo
from utils import constutils as const
from utils import axisutils as axes

def buildmosaic(
    outfile=None, # output file
    format="ds9", # text file format
    mask=None,  # mask (1s/0s) ... keep only pointings in mask
    direction=None, # center of mosaic
    max_radius=10.0, # maximum radius of mosaic in degrees
    spacing_deg=None, # force the spacing to this value in degrees
    posang=0.0, # position angle of mosaic
    calcspacing=False, # calculate the spacing
    freq=None, # frequency of observation
    diam=25.0, # diameter of telescope
    beamspacing=0.5, # spacing in beam units
    epoch="J2000", # epoch for output
    sourceroot="", # root of field name for output
    groupname="", # group name for output
    coordsys="Equatorial", # coordinate system for output
    refframe="LSRK", # velocity for output
    convention="Radio", # velocity for output
    velocity="0.0", # velocity for output
    tag="", # tag piped to simdata or ds9 output
    overwrite=False # overwrite output file?
    ):
    """
    Build a hexagonally sampled mosaic pattern with the specified
    center, spacing, and maximum radial extent. Optionally hash this
    against a mask and keep only pointings inside the mask. Outputs
    the pointing list to a text file for use by simdata, conversion to
    an EVLA catalog, or calculation of a sensitivity map.    
    """

    # ===============================
    # ERROR CHECKING
    # ===============================

    # Checks on output file
    if outfile != None:
        
        if os.path.isfile(outfile):
            if overwrite:
                casalog.post("Removing old version of "+outfile, 
                             priority = 'WARN')
                os.system("rm "+outfile)
            else:
                casalog.post("Output file exists and overwrite "+\
                                 "is False. Returning",
                             priority = 'ERROR')
                return

        if format != "ds9" and format != "simdata" and format != "evlapst":
                casalog.post("Invalid output format requested. "+\
                                 "Choose 'ds9', 'simdata', 'evlapst'.", 
                             priority = 'ERROR')
                return

    # Checks on knowing the HPBW
    if freq == None or diam == None:
        casalog.post("Not enough information to calculate primary beam."+\
                         " I will default to 0.5 degrees.", 
                     priority = 'WARN')
        hpbw = 0.5
    else:
        hpbw = const.hpbw(freq_hz = freq, diam_m = diam, units=False) / \
            const.dtor

    # ===============================
    # DERIVE BASIC MOSAIC
    # ===============================

    # Calculate the spacing as fractions of the HPBW if requested
    if calcspacing == True:
        spacing_deg = beamspacing * hpbw

    # Work out the mosaic center (use the QA tool for string parsing)
    center = direction.split(" ")
    ra_ctr = qa.quantity(center[0])
    dec_ctr = qa.quantity(center[1])

    # Generate a hex grid at the requested center
    ra, dec = geo.hex_grid(ctr_x=ra_ctr['value'], 
                           ctr_y=dec_ctr['value'], 
                           spacing=spacing_deg, 
                           radec=True,
                           radius=max_radius,
                           posang=posang)

    # ===============================
    # APPLY MASK CONSTRAINTS
    # ===============================

    # If a mask is supplied keep only points inside the mask
    if mask != None:        
        # ... translate RA & DEC of points to x, y pix in mask
        x, y = axes.adv_to_xyz(mask, ra=ra, dec=dec)
        # ... initialize mask check
        in_mask = np.zeros(len(x),bool)
        # ... read mask
        ia.open(mask)
        mask = ia.getregion()
        ia.close()
        mask = mask >= 1.0        
        # ... loop over mosaic points
        for i in range(len(x)):    
            # ... check that the point is in the image
            if x[i] < 0 or y[i] < 0:
                continue
            shape = mask.shape
            if x[i] >= shape[0] or y[i] >= shape[1]:
                continue
            # ... check if the mask is true
            in_mask[i] = mask[x[i],y[i]]
        # ... keep only those points inside the mask
        keep = in_mask.nonzero()
        ra = ra[keep]
        dec = dec[keep]

    # ===============================
    # OUTPUT
    # ===============================

    # Output the mosaic pointings
    if outfile != None:
        output_file = open(outfile, "w")
        for i in range(len(ra)):
            source = sourceroot+str(i)
            if format == "ds9":
                ra_string = const.sixty_string(const.hms(ra[i]),hms=True)
                dec_string = const.sixty_string(const.dms(dec[i]),hms=False)
                line = "circle " + \
                    ra_string + " " + \
                    dec_string + " " + \
                    str(hpbw/2.0)+" " + \
                    "d"+tag+" " + \
                    "\n"
            elif format == "simdata":
                ra_string = const.sixty_string(const.hms(ra[i]),hms=True)
                dec_string = const.sixty_string(const.dms(dec[i]),hms=False)
                line = epoch + " " + \
                    ra_string + " " + \
                    dec_string + " " + \
                    tag+ \
                    "\n"
            elif format == "evlapst":
                ra_string = const.sixty_string(const.hms(ra[i]),colons=True)
                dec_string = const.sixty_string(const.dms(dec[i]),colons=True)
                line = \
                    source + ";" + \
                    groupname + ";" + \
                    coordsys + ";" + \
                    epoch + ";" + \
                    ra_string + ";" + \
                    dec_string + ";" + \
                    refframe + ";" + \
                    convention + ";" + \
                    velocity + ";" + \
                    "\n"
            output_file.writelines(line)
        output_file.close()
    else:
        for i in range(len(ra)):
            ra_string = const.sixty_string(const.hms(ra[i]),hms=True)
            dec_string = const.sixty_string(const.dms(dec[i]),hms=False)
            print ra_string + " " + \
                dec_string

    return
    
    

