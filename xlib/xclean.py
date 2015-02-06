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

def xclean(xp):
        
    """
    #########################################################################################
    #
    #   PURPOSE
    #       
    #       imaging the calibrated data
    #
    #   INPUT FILE
    #       
    #       Mesaurement Set:    <prefix>.src.ms
    #                           <prefix>.src.ms.contsub 
    #
    #
    #   HISTORY
    #
    #       20130910    RX  use the variable <xp> to wrap pipeline parameters
    #
    #   AUTHOR
    #
    #       Rui Xue, University of Illinois
    #
    #########################################################################################
    """
    #----------------------------------------------------------------------------------------
    #   Environment Setup
    #----------------------------------------------------------------------------------------
    casalog.filter('INFO')
    
    startTime=time.time()
    xu.news("")
    xu.news("++")
    xu.news("------------- Begin Task: xclean "+xp['prefix']+" -------------")
    xu.news("++")
    xu.news("")
    casa_log = open(casalog.logfile(),'r')
    startlog = casa_log.readlines()
    casa_log.close()
    
    #----------------------------------------------------------------------------------------
    #   Default Values for Optional Inputs
    #----------------------------------------------------------------------------------------
    if  type(xp['imsize'])==type(0):
        imsize=[xp['imsize'],xp['imsize']]
    if  type(xp['imsize'])==type([]):
        imsize=xp['imsize']
    
    
    innerquarter=str(int(imsize[0]/4))+','+str(int(imsize[1]/4))+','\
                +str(int(imsize[0]*3/4))+','+str(int(imsize[1]*3/4))
    outerquarter=str(0)+','+str(0)+','\
                +str(int(imsize[0]*1/4))+','+str(int(imsize[1]*1/4))+','\
                +str(0)+','+str(int(imsize[1]*3/4))+','\
                +str(int(imsize[0]*1/4))+','+str(int(imsize[1]-1))+','\
                +str(int(imsize[0]*3/4))+','+str(0)+','\
                +str(int(imsize[0]-1))+','+str(int(imsize[1]*1/4))+','\
                +str(int(imsize[0]*3/4))+','+str(int(imsize[1]*3/4))+','\
                +str(int(imsize[0]-1))+','+str(int(imsize[1]-1))    
    if  xp['imstat_box_spec']=='':
        xp['imstat_box_spec']=innerquarter    
        if  xp['imcs']==True:
            xp['imstat_box_spec']=outerquarter
    if  xp['imstat_box_cont']=='':
        xp['imstat_box_cont']=outerquarter
    
    
    xp['srcfile']=xp['prefix']+'.src.ms'
    if  xp['imagermode']==None:
        xp['imagermode']='csclean'
        
        prepvis=xp['srcfile']
        if  xp['uvcs']==True:
            prepvis=xp['srcfile']+'.contsub'
        
        tb.open(prepvis+'/FIELD')
        nfield=len(tb.getcol('NAME'))
        tb.close()
        if  nfield>1:
            xp['imagermode']='mosaic'
        hetero=False
        xu.news("")
        xu.news("nfield: "+str(nfield))
        
        tb.open(prepvis+"/OBSERVATION")
        obsnamelist=tb.getcol("TELESCOPE_NAME")
        xu.news("obsname_list:"+str(obsnamelist))
        xu.news("")
        for obsname in obsnamelist:
            if  obsname=='ALMA' or obsname=='CARMA':
                xp['imagermode']='mosaic'
                xp['ftmachine']='mosaic'
        tb.close()
        xu.news("imagermode -> "+xp['imagermode'])
        xu.news("ftmachine  -> "+xp['ftmachine'])
        xu.news("")
    
    """
    if  xp['uvcs']==True:
        xp['cleancont']=True
    """
    
    #----------------------------------------------------------------------------------------
    #   Make a dirty spectral cube, and determine the cube sigma level
    #----------------------------------------------------------------------------------------
    
    vis_loop=[]
    outname_loop=[]
    niter_loop=[]
    threshold_loop=[]
    cleanmode_loop=[]
    cleanspw_loop=[]
    restorbeam_loop=[]
    resmooth_loop=[]
    multiscale_loop=[]
    cleanmask_loop=[]
    
    if  xp['cleanspec']==True:
        
        if  xp['uvcs']==True:
            vis=xp['srcfile']+'.contsub'
        else:
            vis=xp['srcfile']
        if  xp['imcs']==True:
            outname=xp['prefix']+'.coli'
        else:
            outname=xp['prefix']+'.line'
        
        if  xp['threshold_spec']=='0.0mJy' and xp['niter']!=0:
            vis_loop+=[vis]
            outname_loop+=[outname+'_d']
            niter_loop+=[0]
            threshold_loop+=['0.0mJy']
            cleanmode_loop+=[xp['cleanmode']]
            cleanspw_loop+=[xp['cleanspw']]
            restorbeam_loop+=[xp['restorbeam']]
            resmooth_loop+=[False]
            multiscale_loop+=[[]]
            cleanmask_loop+=[xp['clean_mask']]
    
        vis_loop+=[vis]
        outname_loop+=[outname]
        niter_loop+=[xp['niter']]
        threshold_loop+=[xp['threshold_spec']]
        cleanmode_loop+=[xp['cleanmode']]
        cleanspw_loop+=[xp['cleanspw']]
        restorbeam_loop+=[xp['restorbeam']]
        resmooth_loop+=[xp['resmooth']]
        multiscale_loop+=[xp['multiscale']]
        cleanmask_loop+=[xp['clean_mask']]
        
    if  xp['cleancont']==True:
        
        vis=xp['srcfile']
        outname=xp['prefix']+'.cont'
        if  xp['uvcs']==True:
            spw=xp['fitspw']
        else:
            spw=''
        if  xp['threshold_cont']=='0.0mJy' and xp['niter']!=0:
            vis_loop+=[vis]
            outname_loop+=[outname+'_d']
            niter_loop+=[0]
            threshold_loop+=['0.0mJy']
            cleanmode_loop+=['mfs']
            cleanspw_loop+=[spw]
            restorbeam_loop+=[xp['restorbeam']]
            resmooth_loop+=[False]
            multiscale_loop+=[[]]
            cleanmask_loop+=[xp['clean_mask_cont']]
    
        vis_loop+=[vis]
        outname_loop+=[outname]
        niter_loop+=[xp['niter']]
        threshold_loop+=[xp['threshold_cont']]
        cleanmode_loop+=['mfs']
        cleanspw_loop+=[spw]
        restorbeam_loop+=[xp['restorbeam']]
        resmooth_loop+=[False]
        multiscale_loop+=[xp['multiscale']]
        cleanmask_loop+=[xp['clean_mask_cont']]
    
    for i in range(0,len(vis_loop)):
        
        xu.news("")
        xu.news("--clean--")
        xu.news("")
        
        xu.cleanup(outname_loop[i])        
    
        start=xp['clean_start']
        width=xp['clean_width']
        if  cleanmode_loop[i]=='mfs':
            start=0
            width=1 
        if  xp['spwrgd']=='spw':
            #
            # if the MS already has the desired channel setup, we will
            # turn off CLEAN interpolation and dump SUM(weight) for each plane
            # 
            interpolation='nearest'
            xu.sumwt(vis_loop[i],oldstyle=True)
            xu.checkchflag(vis_loop[i])  
        else:
            interpolation=xp['spinterpmode']
        clean(vis=vis_loop[i],
              imagename=outname_loop[i],
              field=xp['clean_field'],
              spw=cleanspw_loop[i],
              mode=cleanmode_loop[i],
              nchan=xp['clean_nchan'],
              start=start,
              width=width,
              niter=niter_loop[i],
              intent="",
              resmooth=resmooth_loop[i],
              multiscale=multiscale_loop[i],
              negcomponent=xp['negcomponent'],
              interpolation=interpolation,
              threshold=threshold_loop[i],
              psfmode=xp['psfmode'],
              mask=cleanmask_loop[i],
              imsize=xp['imsize'],
              cell=xp['cell'],
              weighting=xp['cleanweight'],
              robust =xp['wrobust'],
              imagermode=xp['imagermode'],
              phasecenter=xp['phasecenter'],
              ftmachine=xp['ftmachine'],
              outframe=xp['outframe'],
              restfreq=xp['restfreq'],
              scaletype='SAULT',
              mosweight=xp['mosweight'],
              minpb=xp['minpb'],
              pbcor=False,
              uvtaper=True,
              innertaper=[],
              outertaper=xp['outertaper'],
              cyclefactor=xp['cyclefactor'],
              restoringbeam=restorbeam_loop[i],
              gain=xp['clean_gain'],
              stokes='I',
              chaniter=xp['iterchan'],
              allowchunk=xp['allowchunk'],
              usescratch=xp['usescratch'],
              selectdata=True)
        xu.modelconv(outname_loop[i])
    
        xu.news("")
        xu.news("")   
        xu.news("--imstat--")
        xu.news("")
        xu.news(" Determine the line cube sigma level (pb uncorreted)")
        xu.news("")
        
        if  cleanmode_loop[i]!='mfs':
            ds_stat=imstat(imagename=outname_loop[i]+'.image',
                           box=xp['imstat_box_spec'],
                           chans=xp['imstat_chan'],
                           axes=[0,1],
                           region=xp['imstat_rg_spec'])
            if  xp['imstat_sigcalc']=='min':
                sigmjy=np.nanmin(ds_stat['sigma'])*1000.
            else:
                sigmjy=np.median(ds_stat['sigma'])*1000.
            if  outname_loop[i][-2:]=='_d':
                if  threshold_loop[i+1]=='0.0mJy':
                    threshold_loop[i+1]=str(sigmjy*xp['sigcutoff_spec'])+'mJy'
                #    resmooth='common' might be better than hacking <restorbeam> on 
                #    maching flux scales in model & residual
                #
                #if  restorbeam_loop[i+1]==['']:
                #    restorbeam_loop[i+1]=\
                #        xu.checkbeam(outname_loop[i],method=xp['restorbeam_method'])
        else:
            dc_stat=imstat(imagename=outname_loop[i]+'.image',
                           box=xp['imstat_box_cont'],
                           region=xp['imstat_rg_cont'])
            sigmjy=dc_stat['sigma'][0]*1000.
            if  outname_loop[i][-2:]=='_d':
                if  threshold_loop[i+1]=='0.0mJy':
                    threshold_loop[i+1]=str(sigmjy*xp['sigcutoff_cont'])+'mJy'
        
        xu.news("")
        xu.news("-------------------------------------------------------------------------")
        xu.news(" Found the normalized sigma = "+str(sigmjy)+"mJy/beam")
        xu.news("-------------------------------------------------------------------------")
        xu.news("")
        
        imhead(imagename=outname_loop[i]+'.image')
        """
        immath(imagename=[outname_loop[i]+'.image',outname_loop[i]+'.flux'],
               expr='IM0/IM1',
               outfile=outname_loop[i]+'.cm')
        """
        impbcor(imagename=outname_loop[i]+'.image',\
                pbimage=outname_loop[i]+'.flux',\
                outfile=outname_loop[i]+'.cm',\
                cutoff=-1.0)
        
        xu.exporttasklog('imhead',outname_loop[i]+'.image.imhead.log')
        xu.exporttasklog('imstat',outname_loop[i]+'.image.imstat.log')
        xu.exporttasklog('clean',outname_loop[i]+'.image.iteration.log')
        os.system("cp -rf clean.last "+outname_loop[i]+'.image.clean.log')
    
    #----------------------------------------------------------------------------------------
    #   image-domain continuum substraction
    #----------------------------------------------------------------------------------------
    if  xp['imcs']==True:   
    
        xu.news("")
        xu.news("--imcontsub--")
        xu.news("")
        xu.news("Continumm substraction in the cube")
        xu.news("")
    
        outname = xp['prefix']
        os.system('rm -rf '+outname+'.cont.* ')
        os.system('rm -rf '+outname+'.line.* ')
     
        mask0=outname+'.coli.flux'
        xu.genmask0(mask0)
        xu.mask0clean(outname+'.coli',mask0+'.mask0')
        
        imcontsub(imagename=outname+'.coli.cm',
                  linefile=outname+'.line.cm',
                  contfile=outname+'.cont.cm.cube',
                  fitorder=xp['fitorder'],
                  chans=xp['fitchans'])
        xu.news("")
        
        immoments(imagename=outname+'.coli.cm',
                  outfile=outname+'.cont.cm',
                  chans=xp['fitchans'],
                  moments=-1)
        
        os.system('rm -rf '+outname+'.line.flux ')
        os.system('cp -rf '+outname+'.coli.flux '+outname+'.line.flux')
        immath(imagename=[outname+'.line.cm',outname+'.line.flux'],
               expr='IM0*IM1',
               outfile=outname+'.line.image')
        
        os.system('rm -rf '+outname+'.cont.flux ')        
        immath(imagename=[outname+'.cont.cm.cube',outname+'.coli.flux'],
               expr='IM0*IM1',
               outfile=outname+'.cont.image.cube')
        
        os.system('rm -rf flux.tmp?')
        immath(imagename=[outname+'.line.flux'],
               expr='1/(IM0^2)',
               outfile='flux.tmp0')
        immoments(imagename='flux.tmp0',
                  outfile='flux.tmp1',
                  chans=xp['fitchans'],
                  moments=-1)
        immath(imagename=['flux.tmp1'],
               outfile='flux.tmp2',
               expr='1/(IM0^0.5)')
        pbstat=imstat('flux.tmp2')
        pbmax=pbstat['max'][0]
        immath(imagename=['flux.tmp2'],
               outfile=outname+'.cont.flux',
               expr='IM0/'+str(pbmax))
        os.system('rm -rf flux.tmp?')   
        
        immath(imagename=[outname+'.cont.cm',outname+'.cont.flux'],expr='IM0*IM1',\
               outfile=outname+'.cont.image')
    
    
        xu.news("")
        xu.news("")   
        xu.news("--imstat--")
        xu.news("")
        xu.news(" Determine the line cube sigma level (pb uncorreted)")
        xu.news("")
        
    
        ds_stat=imstat(imagename=outname+'.line.image',
                       box=xp['imstat_box_spec'],
                       chans=xp['imstat_chan'],
                       axes=[0,1],
                       region=xp['imstat_rg_spec'])
        sigmjy=np.median(ds_stat['sigma'])*1000.
        xu.news("")
        xu.news("-------------------------------------------------------------------------")
        xu.news(" Found the normalized sigma = "+str(sigmjy)+"mJy/beam")
        xu.news("-------------------------------------------------------------------------")
        xu.news("")
    
        imhead(imagename=outname+'.line.image')
        xu.exporttasklog('imhead',outname+'.line.image.imhead.log')
        xu.exporttasklog('imstat',outname+'.line.image.imstat.log')
     
    
        
        dc_stat=imstat(imagename=outname+'.cont.image',
                       box=xp['imstat_box_cont'],
                       region=xp['imstat_rg_cont'])
        sigmjy=dc_stat['sigma'][0]*1000.
        xu.news("")
        xu.news("-------------------------------------------------------------------------")
        xu.news(" Found the normalized sigma = "+str(sigmjy)+"mJy/beam")
        xu.news("-------------------------------------------------------------------------")
        xu.news("")
        
        imhead(imagename=outname+'.cont.image')
        xu.exporttasklog('imhead',outname+'.cont.image.imhead.log')
        xu.exporttasklog('imstat',outname+'.cont.image.imstat.log')
    
    
    xu.news("")
    xu.news("--exportfits--")
    xu.news("")
    xu.news("Export all images to FITS format")
    xu.news("")
    xu.exportclean(xp['prefix']+'.line_d',keepcasaimage=xp['keepcasaimage'])
    xu.exportclean(xp['prefix']+'.line',keepcasaimage=xp['keepcasaimage'])
    xu.exportclean(xp['prefix']+'.cont_d',keepcasaimage=xp['keepcasaimage'])
    xu.exportclean(xp['prefix']+'.cont',keepcasaimage=xp['keepcasaimage'])
    xu.exportclean(xp['prefix']+'.coli_d',keepcasaimage=xp['keepcasaimage'])
    xu.exportclean(xp['prefix']+'.coli',keepcasaimage=xp['keepcasaimage'])
    xu.news("")
    
    #----------------------------------------------------------------------------------------
    #   End Statement
    #----------------------------------------------------------------------------------------
    subima2time=time.time()
    xu.news("")
    xu.news("Total Imaging Time: %10.1f" %(subima2time-startTime))
    xu.news("")
    xu.news("++")
    xu.news("------------- End Task: xclean "+xp['prefix']+" -------------")
    xu.news("++")
    xu.news("")
    casa_log=open(casalog.logfile(),'r')
    stoplog=casa_log.readlines()
    casa_log.close()
    xu.exportcasalog(startlog,stoplog,xp['prefix']+'.xclean.reduc.log')
    
    if  xp['email']!='':
        emailsender(xp['email'],\
                    "RUN xclean End: "+xp['prefix'],\
                    "This email was generated automatically \
                    by your successful reduction run.\nThe log files are attached",\
                    [xp['prefix']+'.xclean.reduc.log'])


    return xp    
if  __name__=="__main__":
    xp=clean(xp)    
    