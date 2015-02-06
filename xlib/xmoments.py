import time
import os
import string
import math
import casac
import glob
from tasks import *
from taskinit import *
import numpy as np
import subprocess
import scipy.constants as sci_const
from scipy.ndimage.measurements import label as sci_label


def xmoments(   imagename,
                error='',
                smfac=[3.0,3.0],
                clip=4.0,
                grow=2.0,
                smooth=True,
                dilated=True,
                box='',
                chans='',
                region=''):
    """
    a function supposed to replace the idl-moments
    
    Inputs:
        imagename    spectral cube file (in CASA/MIRIAD/FITS)
        error        error cube
        smfac        smoothing factor
        clip         sigma clipping
        grow         grow level for dilated masking
        smooth       smoothing for signal identification
        dialated     mask expanding
    
    history:
        20130720    RX  introduced with "smooth-masking" implemented 
        20140720    RX  add "dilate-masking"
        20150205    RX  stripped from xtest.py
                        add examples/documents

    To Do:
        error propagation
        better treatment for masking
         
    """

    if  type(smfac)!=type([]):
        smfac=[smfac,0.0]
    
    
    ia.fromimage(infile=imagename,dropdeg=False)
    im_array=ia.getregion(dropdeg=True)
    #np.isnan(im_array.any())
    ia.close()
    ia.fromimage(infile=error,dropdeg=False)
    err_array=ia.getregion(dropdeg=True)
    ia.close()
    
    snr_array=im_array/err_array    
    
    if  smooth==True:        
        hd=imhead(imagename,mode='list')
        ia.fromimage(infile=imagename,dropdeg=False)
        sm=ia.convolve2d(axes=[0,1],
                         type='gaussian',
                         targetres=True,
                         major=str(hd['beammajor']['value']*smfac[0])+hd['beammajor']['unit'],
                         minor=str(hd['beamminor']['value']*smfac[0])+hd['beamminor']['unit'],
                         pa=str(hd['beampa']['value'])+hd['beampa']['unit'],  
                         overwrite=True)
        
        if  smfac[1]!=0.0:
            sm3d=sm.sepconvolve(axes=[2],
                           types=['gaussian'],
                           widths=[smfac[1]],stretch=True,overwrite=True)
            sm.done()
            sm3d.getregion()
            sm=sm3d
    
    
        sm.putregion((sm.getregion(dropdeg=True))/err_array)
        os.system("rm -rf _tmp.fits")
        sm.tofits("_tmp.fits")
        #stat=sm.statistics(robust=True,region=region,axes=[0,1])
        stat=imstat(imagename='_tmp.fits',chans=chans,axes=[0,1],region=region,box=box)
        os.system("rm -rf _tmp.fits")
        
        sfc=np.median(stat['sigma'])
        snr_array=sm.getregion()*sfc
        print sfc
        sm.close()
        snr_array=im_array/err_array
    
    snr_array_clip=snr_array>clip
    detcore=np.where(snr_array_clip,1.,0.)
    mask=detcore
    
    if  dilated==True:
        print "++"
        snr_array_grow=snr_array>grow
        snr_array_expand=np.pad(snr_array_grow,((1,1),(1,1),(1,1)),mode='constant')
        det=np.logical_or(snr_array_expand[1:-1,1:-1,:-2],snr_array_expand[1:-1,1:-1,2::])
        det=np.logical_and(det,snr_array_grow)
        
        det=np.where(det,1.,0.)
        label,nlabel=sci_label(det)
        mask=label*0.0
        for i in range(1,nlabel+1):
            if  (np.sum(detcore[label==i]))>0.0:
                mask[label==i]=1.0
    
    ia.fromarray(outfile=imagename+'.mask',pixels=mask,overwrite=True)
    ia.close()
        
    os.system("rm -rf "+imagename+'.mom0')    
    for mom in ['0','1']:
        os.system("rm -rf "+imagename+'.mom'+mom)
        os.system("rm -rf "+imagename+'.mom'+mom+'.fits') 
        immoments(imagename,
              axis="spec",
              mask=imagename+'.mask>0',
              stretch=True,
              moments=[int(mom)],
              outfile=imagename+'.mom'+mom)
        exportfits(imagename+'.mom'+mom,
               imagename+'.mom'+mom+'.fits', 
               velocity=True,
               overwrite=True) 
        viewer(infile=imagename+'.mom'+mom,gui=False,\
               outfile=imagename+'.mom'+mom+'.jpg')

if  __name__=="__main__":
    xmoments('n4254co.line.cm.fits',
             error='n4254co.line.err.fits')


          
    