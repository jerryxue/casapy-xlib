import time
import os
import string
import math
import casac
from tasks import *
from taskinit import *
import socket
import numpy as np
import subprocess
import smtplib
import scipy.constants as sci_const
import matplotlib.pyplot as plt

def checkchflag(msfile):
    #
    #    check flag consistancy across channels
    #    only useful in the case with a single spw
    #    
    #    note: miriad/invert slop=1,zero could include
    #          partionally flagged records into imaging
    #          We can run xutils.unchflag() and zero-out such data
    #          to implement a similar treatment:
    #          http://www.atnf.csiro.au/computing/software/miriad/userguide/node145.html 
    #  
    tb.open(msfile)
    flag=tb.getcol('FLAG')
    shape=flag.shape
    news(msfile+' '+str(shape))
    for i in range(0,shape[0]):
        
        flag0=flag[[i],:,:] # this will make a copy 
        flag0=flag0[0,:,:]  # otehrwise .view will not work
                            # flag0.strides
        flag0=flag0.view(','.join(shape[1]* ['i1']))
        unique_vals,indicies=np.unique(flag0, return_inverse=True)
        counts = np.bincount(indicies)
        news("poln: "+str(i)+' type: '+str(len(counts)))
        for j in range(0,len(counts)):
            u=str(unique_vals[j])
            u=u.translate(None, '(), ')
            news(u+' '+str(counts[j])+'/'+str(shape[-1]))
    news("")
    tb.close()
    
def news(msg,origin='++++++'):
    #
    #    print out information to casalog
    #
    msg=str(msg)
    casalog.origin(origin)
    casalog.post(msg)