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
 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import xutils as xu

def xconsol(xp):
    """
    #########################################################################################
    #
    #   PURPOSE
    #
    #       prepare calibrated data for imaging
    #
    #   INPUT FILE
    #       
    #       Mesaurement Set:    <prefix>.ms,
    #                           -- calibrated source data in the "data" column
    #       for combination     <prefix_comb[0]>.src.ms, 
    #                           <prefix_comb[1]>.src.ms,
    #                           etc..
    #   OUTPUT FILE
    #
    #       Measurement Set:    <prefix>.src.ms
    #                           <prefix>.src.ms.cont
    #                           <prefix>.src.ms.contsub 
    #
    #
    #   HISTORY
    #
    #       20110916    RX  fix for r3.3
    #       20130910    RX  use the variable <xp> to wrap pipeline parameters
    #
    #   AUTHOR
    #
    #       Rui Xue, Univeristy of Illinois
    #########################################################################################
    """
    #----------------------------------------------------------------------------------------
    #   Environment Setup
    #----------------------------------------------------------------------------------------
    casalog.filter('INFO')
    
    
    startTime=time.time()
    xu.news("")
    xu.news("++")
    xu.news("------------- Begin Task: xconsol "+xp['prefix']+" -------------")
    xu.news("++")
    xu.news("")
    casa_log = open(casalog.logfile(),'r')
    startlog = casa_log.readlines()
    casa_log.close()
    
    #----------------------------------------------------------------------------------------
    #   TRACK COMBINATION
    #----------------------------------------------------------------------------------------
    if  xp['prefix_comb']==[]:
        xp['prefix_comb']=[xp['prefix']]
    xu.news("")
    xu.news("++++++++++++++++++++++")
    xu.news("")
    xu.news("Processing Track(s):")
    xu.news(xp['prefix_comb'])
    xu.news("")
    xu.news("++++++++++++++++++++++")
    xu.news("")
    
    
    #----------------------------------------------------------------------------------------
    #   split the calibrated source visibilities
    #----------------------------------------------------------------------------------------    
    if  len(xp['prefix_comb'])==1:
    
        
        xp['msfile']=xp['prefix']+'.ms' 
        xp['srcfile']=xp['prefix']+'.src.ms'
        os.system('rm -rf '+xp['srcfile'])
    
        
        xu.news("")
        xu.news("--mstransform--")
        xu.news("")
        xu.news(" Use mstransform() to:")
        xu.news(" * extract the source data")
        xu.news(" * [spectral regridding]")
        xu.news(" * [hanning smoothing]")
        xu.news("")
        
    
        tb.open(xp['msfile'])
        if  'CORRECTED_DATA' in tb.colnames():
            datacolumn='corrected'
        else:
            datacolumn='data'
        tb.close()
    
        if  xp['spwrgd']!='spw':
            if  xp['spwrgd']=='':
                spwrgd=False
            if  xp['spwrgd']=='frame':
                spwrgd=True
            mstransform(vis=xp['msfile'],
                        outputvis=xp['srcfile'],
                        createmms=False,
                        separationaxis='auto',
                        field=xp['source'],
                        spw=xp['spw_source'],
                        usewtspectrum=True,
                        datacolumn=datacolumn,
                        chanaverage=False,
                        regridms=spwrgd,
                        combinespws=False,
                        mode='channel',
                        nchan=-1,
                        start=0,
                        width=1,
                        nspw=1,
                        keepflags=False,
                        interpolation=xp['spinterpmode'],
                        outframe=xp['outframe'],
                        restfreq=xp['restfreq'],
                        phasecenter=xp['phasecenter'],
                        hanning=xp['hs'])
            """
            split(vis=xp['msfile'],
                  outputvis=xp['srcfile'],
                  spw=xp['spw_source'],
                  datacolumn='corrected',
                  keepflags=False)
            """
        else:
            """
            tb.open(xp['msfile'],nomodify=False)
            flag=tb.getcol('FLAG')
            wts=tb.getcol('WEIGHT_SPECTRUM')
            wts=wts*(1.0-flag*1.0)
            tb.putcol('WEIGHT_SPECTRUM',wts)
            tb.close()
            """
            
            if  xp['spwrgd_method']=='cvel':
                os.system("rm -rf "+xp['srcfile']+'.tmp')
                msfile=xp['msfile']
                if  datacolumn=='corrected':
                    postfix='.tmp'
                    split(vis=msfile,
                          outputvis=xp['srcfile']+'.tmp',
                          field=xp['source'],
                          spw=xp['spw_source'],
                          datacolumn=datacolumn,
                          keepflags=False)
                    msfile=xp['srcfile']+'.tmp'
                cvel(vis=msfile,
                     outputvis=xp['srcfile'],
                     passall=False,
                     field=xp['source'],
                     selectdata=True,
                     mode=xp['cleanmode'],
                     nchan=xp['clean_nchan'],
                     start=xp['clean_start'],
                     width=xp['clean_width'],
                     interpolation=xp['spinterpmode'],
                     outframe=xp['outframe'],
                     restfreq=xp['restfreq'],
                     veltype='radio',
                     phasecenter='',
                     hanning=xp['hs'])
                os.system("rm -rf "+xp['srcfile']+'.tmp')
            
            if  xp['spwrgd_method']=='mstransform':
                os.system("rm -rf "+xp['srcfile']+'.tmp')
                if  xp['chanbin']<=1:
                    chanaverage=False
                    chanbin=1
                if  xp['chanbin']>1:
                    chanaverage=True
                    chanbin=xp['chanbin']
                mstransform(vis=xp['msfile'],
                            outputvis=xp['srcfile']+'.tmp',
                            createmms=False,
                            numsubms=64,
                            separationaxis='spw',
                            field=xp['source'],
                            spw=xp['spw_source'],
                            keepflags=True,
                            usewtspectrum=True,
                            datacolumn=datacolumn,
                            chanaverage=chanaverage,
                            chanbin=chanbin,
                            regridms=True,
                            combinespws=False,
                            mode=xp['cleanmode'],
                            nchan=xp['clean_nchan'],
                            start=xp['clean_start'],
                            width=xp['clean_width'],
                            nspw=1,
                            interpolation=xp['spinterpmode'],
                            outframe=xp['outframe'],
                            restfreq=xp['restfreq'],
                            phasecenter='',
                            hanning=xp['hs'])
                mstransform(vis=xp['srcfile']+'.tmp',
                            outputvis=xp['srcfile'],
                            keepflags=False,
                            datacolumn='all',
                            combinespws=xp['combinespws'])            
                os.system("rm -rf "+xp['srcfile']+'.tmp')
                
            xu.news("")
            xu.news("checking flagging consistency among channels:")
            xu.news("")
            xu.checkchflag(xp['srcfile'])
        
        #    
        #   COPY MEAN(WEIGHT_SPECTRUM) TO WEIGHT
        #   or
        #   COPY WEIGHT TO MEAN(WEIGHT_SPECTRUM)
        #   The resulted WEIGHT/WEIGHT_SPECTRUM will be consistent with the definition in CASA>=4.2.2
        #
        #   mstransform() and cvel() will modify weights but may not be statistically  
        #   correct during spw regridding.
        #
        #
        #   MS from xu.importmir() will have WEIGHT_SPECTRUM initialized from MIRIAD. 
        #   The filled values are based on the theoretical prediction using Tsys etc. 
        #   If the pipeline detects WEIGHT_SPECTRUM, WEIGHT will be replaced with mean(WEIGHT_SPECTRUM)
        #   For CASA<4.2.2, CLEAN will use WEIGHT -> no channel-dependent dirty beam, 
        #       if flagging is consistent. 
        #   For CASA>4.2.2, CLEAN will use WEIGHT_SPECTRUM, which may lead to a channel-dependent beam,
        #       even flagging is consistent.
        #   Here we add another optional step with <MEANWT>=True:
        #       replace WEIGHT_SPECTRUM with mean(WEIGHT_SPECTRUM)
        #   This could avoid undesired small beam variations on a channel by channel basis 
        #   (e.g. spws edges, error in the original WEIGHT_SPECTRUM)
        #
        #   In any case, we HAVE maintained the CASA>=4.2.2 WEIGHT/WEIGHT_SPECTRUM convention in the 
        #   pipeline since we introduced the WEIGHT_SPECTRUM manipulation (even before CASA 4.2.2 came out).
        # 
        if  xp['unchflag']==True:
            xu.unchflag(xp['srcfile'])
        tb.open(xp['srcfile'],nomodify=False)
        wts_exist=tb.iscelldefined('WEIGHT_SPECTRUM',0)
        tb.close()
        if  wts_exist==True:
            xu.copyweight(xp['srcfile'],copyback=True)
            if  xp['meanwt']==True:
                xu.copyweight(xp['srcfile'])  
        else:
            xu.copyweight(xp['srcfile'])
        
        xu.news("")
        xu.news("--check split data & weight--")
        xu.news("")
        listobs(xp['srcfile'])
        
        if  xp['scalewt_fitspw']=='':
            xp['scalewt_fitspw']=xp['fitspw']
            
        xu.scalewt(xp['srcfile'],
                   uvrange=xp['scalewt_uvrange'],
                   fitspw=xp['scalewt_fitspw'],
                   datacolumn='data',
                   minsamp=xp['scalewt_minsamp'],
                   modify=False)
    
        # note:  below lines can help to check weight/noise in
        #        calibrated MS before split.
        #xu.scalewt(xp['srcfile'],
        #           field=xp['source'],
        #           datacolumn='corrected',
        #           fitspw=xp['scalewt_fitspw'])
        if  xp['uvcs']==True:
               
            xu.news("")
            xu.news("--uvcontsub--")
            xu.news("")
            xu.news(" fit continuum emission in uv domain using line-free channels specified")
            xu.news(" by fit_spw")
            xu.news(" ")
            xu.news(" Two new MSes will be created:") 
            xu.news(" "+xp['srcfile']+".cont")
            xu.news(" "+xp['srcfile']+".contsub")
            xu.news(" ")
            
            os.system('rm -rf '+xp['srcfile']+".cont")
            os.system('rm -rf '+xp['srcfile']+".contsub")
            """
            uvcontsub(vis=xp['srcfile'],
                      field='',
                      fitspw=xp['fitspw'],
                      fitorder=xp['fitorder'],
                      spw='',
                      combine=xp['uvcs_combine'],
                      want_cont=False,
                      solint='int')
            replace uvcontsub with uvcontsub3 to improve performance
            """
            uvcontsub3(vis=xp['srcfile'],
                      field='',
                      fitspw=xp['fitspw'],
                      fitorder=xp['fitorder'],
                      spw='',
                      combine=xp['uvcs_combine'])
    
    
    if  len(xp['prefix_comb'])!=1 or xp['prefix']!=xp['prefix_comb'][0]:
    
        xp['srcfile_comb']=['']*len(xp['prefix_comb'])
        xp['srcfile']=xp['prefix']+'.src.ms'
    
        
        xu.news("")
        xu.news("--concat--")
        xu.news("")
        xu.news("Use CONCAT to combine tracks and create a new measurement set file")
        xu.news("")
        
        if  xp['uvcs']==False:
            postfix=['']
        else:
            postfix=['.contsub','']
        
        for loop in postfix:
            
            #mincw=0
            for i in range(len(xp['prefix_comb'])): 
                xp['srcfile_comb'][i]=xp['prefix_comb'][i]+'.src.ms'+loop
                delmod(vis=xp['srcfile_comb'][i],otf=True,scr=True)
            #    tb.open(xp['srcfile_comb'][i]+'/SPECTRAL_WINDOW')
            #    mincw=[mincw]+tb.getcol('CHAN_WIDTH')
            #    tb.close()
            #    mincw=np.min(mincw)
            
            os.system('rm -rf '+xp['srcfile']+loop)
            
            #freqtol=str(mincw/1.e6/4.)+'MHz'
            if  xp['freqtol']!='':
                freqtol=xp['freqtol']
            
            #    ADJUST WEIGHT SCALING
            wtscale=[1.0]*len(xp['prefix_comb'])
            if  xp['scalewt']==True:
                for isf in range(0,len(xp['prefix_comb'])):
                    tb.open(xp['prefix_comb'][isf]+'.src.ms')
                    tbk=tb.keywordnames()
                    if  'WEIGHT_SCALING' in tbk:
                        wtscale[isf]=tb.getkeyword('WEIGHT_SCALING')
                    tb.close()
                xu.news("")
                xu.news("default weight scaling factor: "+str(wtscale))
                if  xp['visweightscale']!=[]:
                    wtscale=xp['visweightscale']
                xu.news("   used weight scaling factor: "+str(wtscale))
                xu.news("")
            else:
                wtscale=[]
            if  xp['usevconcat']==False:
                concat(vis=xp['srcfile_comb'],
                       concatvis=xp['srcfile']+loop,
                       freqtol=xp['freqtol'],
                       dirtol=xp['dirtol'],
                       timesort=False,
                       visweightscale=wtscale,
                       copypointing=True)
                if  xp['meanwt']==True:
                    ##
                    # CLEAN() in v4.3 doesn't handle WEIGHT_SPECTRUM
                    # with variable shaped arrays
                    ##
                    xu.rmcolumn(xp['srcfile_comb'],column='WEIGHT_SPECTRUM')
                    
            else:
                virtualconcat(vis=xp['srcfile_comb'],
                       concatvis=xp['srcfile']+loop,
                       freqtol=xp['freqtol'],
                       dirtol=xp['dirtol'],
                       visweightscale=wtscale,
                       keepcopy=True,
                       copypointing=True)
            
    
            
                
    #----------------------------------------------------------------------------------------
    #   Obs List: List a summary of the new MS
    #----------------------------------------------------------------------------------------
    xu.news("")
    xu.news("--listobs--")
    xu.news("")
    xu.news("Use listobs to xu.news(verbose summary of the MS:")
    postfix=''
    if  xp['uvcs']==True:
        postfix='.contsub'
    xu.news(xp['srcfile']+postfix)
    xu.news("")
    listobs(vis=xp['srcfile']+postfix,verbose = True)
    xu.exporttasklog('listobs',xp['srcfile']+'.listobs.log')
    
    #----------------------------------------------------------------------------------------
    #   Vis Stat: Have a look at the visibility
    #----------------------------------------------------------------------------------------
    xu.news("")
    xu.news("--visstat--")
    xu.news("")
    xu.news("Use visstat to check the MS ready for imaging:")
    xu.news(xp['srcfile']+postfix)
    xu.news("")
    ms_stat=visstat(vis=xp['srcfile']+postfix,axis='uvrange')
    uvdist_max=ms_stat['UVRANGE']['max'] # in meter
    uvdist_min=ms_stat['UVRANGE']['min'] # in meter
    uvdist_rms=ms_stat['UVRANGE']['rms'] # in meter
    
    tb.open(xp['srcfile']+postfix+'/SPECTRAL_WINDOW',nomodify=False)
    header_para=tb.colnames()
    obs_freq = tb.getcol('REF_FREQUENCY')
    tb.close()
    obs_freq = obs_freq[0]
    obs_wavelength = 3.e8/obs_freq
    xu.news('obs_freq      : '+str(obs_freq))
    xu.news('obs_wavelength: '+str(obs_wavelength))
    
    theta_las=obs_wavelength/uvdist_min/3.1415*180.*60.*60./2.
    theta_fwhm=obs_wavelength/(uvdist_rms)/3.1415*180.*60.*60./2.
    xu.news("")
    xu.news("")
    xu.news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    xu.news("predicted sythesized beamwidth:  "+str(theta_fwhm)+' arcsec')
    xu.news("predicted largest angular scale: "+str(theta_las)+' arcsec')
    xu.news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    xu.news("")
    xu.news("")
    
    
    #----------------------------------------------------------------------------------------
    #   End Statement
    #----------------------------------------------------------------------------------------
    subima2time=time.time()
    xu.news("")
    xu.news("Total Continuum-subtraction and Merging Time: %10.1f" %(subima2time-startTime))
    xu.news("")
    xu.news("++")
    xu.news("------------- End Task: xconsol "+xp['prefix']+" -------------")
    xu.news("++")
    xu.news("")
    casa_log = open(casalog.logfile(),'r')
    stoplog = casa_log.readlines()
    casa_log.close()
    xu.exportcasalog(startlog,stoplog, xp['prefix']+'.xconsol.reduc.log')
    
    if  xp['email']!='':
        emailsender(xp['email'],\
                    "RUN xconsol End: "+xp['prefix'],\
                    "This email was generated automatically by your successful \
                    reduction run.\nThe log files are attached",\
                    [xp['prefix']+'.xconsol.reduc.log',xp['srcfile']+'.listobs.log'])

    return xp    
if  __name__=="__main__":
    xp=xconsol(xp) 

