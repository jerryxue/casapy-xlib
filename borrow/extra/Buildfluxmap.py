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

from readcol import readcol

def buildfluxmap(
    ptgfile=None, # pointing file
    template=None, # template image for astrometry
    outfile=None, # output image file
    freq=None, # frequency of observations
    diam=25.0, # telescope diameter
    overwrite=True # overwrite output file
    ):
    """
    Accept a pointing file listing mosaic pointings, a telescope
    diameter, and an observing frequency. Use these to construct an
    expected noise map (arbitrary normalization) on the astrometry of
    a template image.
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

    # Checks on knowing the HPBW
    if freq == None or diam == None:
        casalog.post("Not enough information to calculate primary beam.", 
                     priority = 'ERROR')
        return
    else:
        hpbw = const.hpbw(freq_hz = freq, 
                          diam_m = diam, 
                          units=False) / \
                          const.dtor

    weight_sig = hpbw/(2.0)**0.5/2.354

    # ===============================
    # READ THE MOSAIC
    # ===============================

    # This will need updating
    trash, ra_string, dec_string, trash2 = \
        readcol(ptgfile \
                    , comment='#' \
                    , twod=False)    
    ra = np.zeros(len(ra_string))
    dec = np.zeros(len(dec_string))
    for i in range(len(ra_string)):
        ra[i] = qa.quantity(ra_string[i])['value']
        dec[i] = qa.quantity(dec_string[i])['value']
        
    print ra, dec

    # ===============================
    # INITIALIZE THE OUTPUT IMAGE
    # ===============================

    # Write the template to a new file
    ia.open(template)
    ia.subimage(outfile=outfile,overwrite=overwrite)
    ia.close()

    ra_img, dec_img = axes.make_axes(template,
                                     image=True,
                                     only_sky=True)
    
    ia.open(outfile)
    weight_image = ia.getregion()
    weight_image *= 0.0
    ia.close()

    # ===============================
    # BUILD THE SENSITIVITY MAP
    # ===============================

    # extract ra and dec images of the template
    for i in range(len(ra)):

        print "Field "+str(i)

        # get the distance
        dist = geo.ang_dist(ra_img, dec_img,ra[i],dec[i] \
                                , degrees=True)

        # build the beam for this position (only out to dist_thresh sigma)
        weight_beam = np.exp(-1.0*(dist)**2/2.0/weight_sig**2)

        # add to the running weight
        weight_image += weight_beam

    # the final sensitivity is the sqrt of the sum of weights
    weight_image = np.sqrt(weight_image)

    # ===============================
    # OUTPUT
    # ===============================

    ia.open(outfile)
    ia.putregion(weight_image)
    ia.close()

    return
    
    

