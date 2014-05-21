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

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders



def immask(imfile,maskfile):
    #
    #    use an masking image to mask a cube, avoid edge channel missing effect
    #
    os.system('rm -rf '+imfile+'.tmp')
    immath(imagename=[imfile,maskfile],expr='IM0*IM1',outfile=imfile+'.tmp') 
    os.system('rm -rf '+imfile)
    os.system('mv '+imfile+'.tmp '+imfile)


def plconfig(msfile,plotformat='png',source='',spw_source=''):
    #
    #   plot source u-v coverage and track antenna positions (not tested)
    #
    news("")
    news("--plotxy--")
    news("")
    news("plot the source uv coverage and antenna positions")
    
    plotuv(vis=msfile,field=source,\
        figfile=msfile+'.sou.uvcoverage.'+plotformat,\
        spw=spw_source,interactive=True)
    plotants(vis=msfile,figfile=msfile+'.plotants.'+plotformat,interative=True)    


def pl_amp_time(msfile,inp_field='',inp_spw='',plotformat='png',intflag=False):
    #
    #    plot source visibilities (amp vs. time) (with interactive flagging) (not tested)
    #
    news("")
    news("--plotxy--")
    news("")
    news("plots calibrator visibilities: amp vs. time")
    # inp_spw=spw_phasecal+','+spw_fluxcal+','+spw_passcal
    # inp_field=fluxcal+','+phasecal+','+passcal
    plotxy(
    vis=msfile,
    spw=inp_spw,
    field=inp_field,
    averagemode='vector',
    timebin='0',
    width='all',
    plotsymbol='b,',
    markersize=0.1,
    fontsize=6.0,
    figfile=msfile+'.plotxy.cal.time_amp.beforecal.'+plotformat,
    interactive = True)
    if  intflag==True:
        user_check=raw_input('Interactive Flagging -- Hit Return to continue script\n')
    news("")


def pl_amp_uvdist(msfile,inp_field='',inp_spw='',plotformat='png',intflag=False):
    #
    #    plot source visibilities (amp vs. uvdist) (not tested)
    #
    #spw=spw_phasecal+','+spw_fluxcal+','+spw_passcal
    #field=fluxcal+','+phasecal+','+passcal
    news("")
    news("--plotxy--")
    news("")
    news("plots calibrator visibilities: amp vs. uvdist")
    
    plotxy(
    vis=msfile,
    spw=inp_spw,
    field=inp_field,
    averagemode='vector',
    timebin='0',
    width='all',
    xaxis='uvdist',
    yaxis='amp',
    plotsymbol='b,',
    markersize=0.1,
    fontsize=6.0,
    figfile=msfile+'.plotxy.cal.uvdist_amp.beforecal.'+plotformat,
    interactive = True)
    if  intflag==True:
        user_check=raw_input('Interactive Flagging -- Hit Return to continue script\n')
    news("")


def pl_sou_amp(msfile,source='',spw_source='',plotformat='png'):
    #
    #    Plot the source visibilities (amp vs. time, amp vs. uvdist) (not tested)
    #
    plotxy(
    vis=msfile,
    spw=spw_source,
    field=source,
    averagemode ='vector',
    width='all',
    timebin='0',
    plotsymbol='b,',
    markersize=0.1,
    fontsize=6.0,
    figfile=msfile+'.plotxy.sou.time_amp.beforecal.' +plotformat,
    interactive = True)
    if  intflag==True:
        user_check=raw_input('Interactive Flagging -- Hit Return to continue script\n')
    news("")
    news("") 
    news("--plotxy--")
    news("")
    news("plots source visibilities: amp vs. uvdist")
    
    plotxy(
    vis=msfile,
    spw=spw_source,
    field=source,
    averagemode='vector',
    width='all',
    timebin='0',
    xaxis='uvdist',
    yaxis='amp',
    plotsymbol='b,',
    markersize=0.1,
    fontsize=6.0,
    figfile=msfile+'.plotxy.sou.uvdist_amp.beforecal.' +plotformat,
    interactive = True)
    if     intflag==True:
        user_check=raw_input('Interactive Flagging -- Hit Return to continue script\n')
    news("")



def pl_gain():
    #
    #    plot gain solution (not tested)
    #
    news("")
    news("--plotcal--")
    news("")
    news("Plot the amplitude/phase/SNR of flux scaled gain solutions for each antenna")

    default('plotcal')
    caltable= prefix + '.fcal'
    xaxis='time'
    selectplot=True
    showgui = True

    merge_eps='gs -sDEVICE=pdfwrite -sOutputFile='+prefix+'.plotcal.gscaled.pdf'
    merge_eps=merge_eps+' -dNOPAUSE -dBATCH'
    
    for i in range(0,num_ant-1):
    
        antenna=str(i)
        field=phasecal+','+fluxcal
        yaxis='amp'
        subplot=311
        figfile=prefix+'.plotcal.gscaled.ant'+str(i)+'.pdf'
        plotsymbol='b,'
        markersize=0.1
        fontsize=6.0
        title='Antenna '+str(i)
        plotcal()
        subtitle='Gain Solution: Antenna '+str(i)+' SpwID '+spwid_passcal[j]
        pl.title(subtitle,fontsize=6)
    
        yaxis='phase'
        subplot=312
        figfile=prefix+'.plotcal.gscaled.ant'+str(i)+'.pdf'
        plotsymbol='b,'
        markersize=0.1
        fontsize=6.0
        title='Antenna '+str(i)
        plotcal()
    
        yaxis='snr'
        subplot=313
        figfile=prefix+'.plotcal.gscaled.ant'+str(i)+'.pdf'
        plotsymbol='b,'
        markersize=0.1
        fontsize=6.0
        title='Antenna '+str(i)
        plotcal()
        
        merge_eps=merge_eps+' '+prefix+'.plotcal.gscaled.ant'+str(i)+'.pdf'
    
    tmp=os.popen(merge_eps).read()
    news(tmp,origin='ghostscript')
    os.system('rm '+prefix+'.plotcal.gscaled.ant*.pdf')
    news("")

    news("")
    news("--plotcal--")
    news("")
    news("Plot the amplitude/phase/SNR of flux scaled gain solutions for all antennae")

    default('plotcal')
    caltable= prefix + '.fcal'
    xaxis='time'
    selectplot=True
    showgui = True  
    field=phasecal+','+fluxcal
    yaxis='amp'
    subplot=311
    figfile=prefix+'.plotcal.allgscaled.'+plotformat
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    plotcal()
    subtitle='Gain Solution'
    pl.title(subtitle,fontsize=6)

    yaxis='phase'
    subplot=312
    figfile=prefix+'.plotcal.allgscaled.'+plotformat
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    plotcal()
    yaxis='snr'
    subplot=313
    figfile=prefix+'.plotcal.allgscaled.'+plotformat
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    plotcal()
    news("")

def pl_aftercal():
    #
    #    Use plotxy for source (after calibrations) (not tested)
    #
    news("")
    news("--plotxy--")
    news("")
    news("2 Panels - Upper panel: amp vs. channel")
    news("2 Panels - Lower panel: amp vs. uvdist")
    
    default('plotxy')
    vis=msfile
    selectplot=True
    spw=spw_source
    field=source
    averagemode='vector'
    crosscans= False
    datacolumn='corrected'
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    interactive = True
    
    for j in range(0,len(spwid_source)):
    
        spw=spwid_source[j]
        width='1'
        subplot = 2*100+len(spwid_source)*10+1+j
        timebin = '1e7'
        xaxis = 'chan'
        yaxis = 'amp'
        title=' SpwID '+spwid_source[j]
        figfile=prefix+'.plotxy.sou.amp.aftercal.'+plotformat
        plotxy()
        
        spw=spwid_source[j]
        width='all'
        subplot = 2*100+len(spwid_source)*10+len(spwid_source)+j+1
        timebin = '0'
        xaxis='uvdist'
        yaxis = 'amp'
        title=' SpwID '+spwid_source[j]
        figfile=prefix+'.plotxy.sou.amp.aftercal.'+plotformat
        plotxy()
        
        news("")

    news("")
    news("--plotxy--")
    news("")
    news("2 Panels - Upper panel: amp vs. channel")
    news("2 Panels - Lower panel: amp vs. uvdist")

    default('plotxy')
    vis=msfile
    selectplot=True
    spw=spw_phasecal
    field=phasecal
    uvrange=phasecal_uvrange
    averagemode='vector'
    interactive = True
    
    for j in range(0,len(spwid_phasecal)):
    
        spw=spwid_phasecal[j]
        subplot = 2*100+len(spwid_phasecal)*10+1+j
        timebin = '1e7'
        width='1'
        xaxis = 'chan'
        yaxis = 'amp'
        plotsymbol='b,'
        markersize=0.1
        fontsize=6.0
        datacolumn='corrected'
        title='Phasecal SpwID '+spwid_phasecal[j]
        figfile=prefix+'.plotxy.phasecal.amp.aftercal.'+plotformat
        plotxy()
        
        spw=spwid_phasecal[j]
        subplot = 2*100+len(spwid_phasecal)*10+len(spwid_phasecal)+j+1
        timebin='0'
        width='all'
        xaxis='uvdist'
        yaxis = 'amp'
        title='Phasecal SpwID '+spwid_phasecal[j]
        figfile=prefix+'.plotxy.phasecal.amp.aftercal.'+plotformat
        plotxy()
        
        news("")

    news("")
    news("--plotxy--")
    news("")
    news("amp vs. velocity for source")
    
    default('plotxy')
    vis=msfile
    selectplot=True
    spw=spw_source
    field=source
    averagemode='vector'
    datacolumn='corrected'
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    width='1'
    timebin = '1e9'
    xaxis = 'velocity'
    yaxis = 'amp'
    title=source+': amp vs. velocity'
    frame=out_frame
    restfreq=rest_freq
    crossscans=True
    figfile=prefix+'.plotxy.sou.velo_amp.aftercal.'+plotformat
    plotxy()
    news("")


def pl_source_after():
    #
    #   Use plotxy for Source
    #
    news("")
    news("--plotxy--")
    news("")
    news("2 Panels - Upper panel: amp vs. channel")
    news("2 Panels - Lower panel: amp vs. uvdist")
    
    default('plotxy')
    vis=srcfile+postfix
    selectplot=True
    spw=''
    averagemode='vector'
    
    crosscans= True
    datacolumn='corrected'
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    interactive = True
    spw=''
    
    subplot = 211
    width = '1'
    xaxis = 'chan'
    yaxis = 'amp'
    timebin = '1e7'
    title=' SpwID 0'
    figfile=prefix+'.plotxy.sou.amp.rc.'+plotformat
    plotxy()
    
    subplot = 212
    timebin='0'
    xaxis='uvdist'
    yaxis = 'amp'
    width='all'
    timebine='0'
    title=' SpwID 0'
    figfile=prefix+'.plotxy.sou.amp.rc.'+plotformat
    plotxy() 
    news("")

    news("")
    news("--plotxy--")
    news("")
    news("amp vs. velocity for source visibilities")
    
    default('plotxy')
    vis=srcfile+postfix
    selectplot=True
    field=source
    averagemode='vector'
    crosscans= True
    datacolumn='corrected'
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    width='1'
    timebin = '1e7'
    xaxis = 'velocity'
    yaxis = 'amp'
    title=source+': amp vs. velocity'
    restfreq=rest_freq
    frame=out_frame
    figfile=prefix+'.plotxy.sou.velo_amp.rc.'+plotformat
    plotxy()
    news("")





 
def checkcube(prefix): 
 
    cellsize=imhead(prefix+'.line.cm',mode='get',hdkey='cdelt1')
    cellsize=abs(cellsize['value']/np.pi*180*60*60)
     
    bmaj=imhead(prefix+'.line.cm',mode='get',hdkey='beammajor')
    bmin=imhead(prefix+'.line.cm',mode='get',hdkey='beamminor')
    bmaj=bmaj['value']
    bmin=bmin['value']
     
    restfreq=imhead(prefix+'.line.cm',mode='get',hdkey='restfreq')
    cdelt4=imhead(prefix+'.line.cm',mode='get',hdkey='cdelt4')
    restfreq=restfreq['value']
    cdelt4=cdelt4['value']
    chanwidth=cdelt4/restfreq[0]*300000.0
     
    shape=imhead(prefix+'.line.cm',mode='get',hdkey='shape')
    shape=shape['value']
    imsize=shape[0]
     
    msfile=prefix+'.src.ms'
    if not os.path.exists(msfile):
         msfile=prefix+'.src.ms.contsub'
         ms_stat=visstat(vis=msfile,axis='uvrange',\
                datacolumn='corrected',\
                uvrange='>0')

    uvdist_max=ms_stat['UVRANGE']['max']    # in meter
    uvdist_min=ms_stat['UVRANGE']['min']    # in meter
    uvdist_rms=ms_stat['UVRANGE']['rms']     # in meter
    uvdist_mean=ms_stat['UVRANGE']['mean']  # in meter
    
    tb.open(msfile+'/SPECTRAL_WINDOW',nomodify=False)
    header_para=tb.colnames()
    obs_freq = tb.getcol('REF_FREQUENCY')
    tb.close()

    obs_freq = obs_freq[0]
    obs_wavelength = 3.e8/obs_freq
    news('')
    news('obs_freq      : '+str(obs_freq))
    news('obs_wavelength: '+str(obs_wavelength))

    theta_las=obs_wavelength/uvdist_min/3.1415*180.*60.*60./2.
    theta_fwhm_mean=obs_wavelength/(uvdist_mean)/3.1415*180.*60.*60./2.
    theta_fwhm_rms=obs_wavelength/(uvdist_rms)/3.1415*180.*60.*60./2.
    news("")
    news("")
    news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    news("predicted sythesized beamwidth (mean):  "+str(theta_fwhm_mean)+' arcsec')
    news("predicted sythesized beamwidth (rms) :  "+str(theta_fwhm_rms)+' arcsec')
    news("predicted largest angular scale: "+str(theta_las)+' arcsec')
    news("real sythesized beamwidth:  "+str(bmaj)+' X '+str(bmin)+' arcsec')
    news("image cell size: "+str(cellsize)+' arcsec')
    news("image size:      "+str(imsize)+' pixel')
    news("channel width:   "+str(chanwidth)+' km/s')
    news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    news("")
    news("")
    
def immask2(im,region): 
     # region='box[[243pix,305pix].[702pix,714pix]]'
     # do masking based on region using ia.putregion
     
     ia.open(im)
     cs=ia.coordsys()
     
     rgi=rg.fromtext(text=region,
                    shape=list(np.shape(ia.getregion())),
                    csys=cs.torecord())
     region_val=ia.getregion(region=rgi)
     print region_val
     np.shape(region_val)
     ia.close()



def calc_db_area(outname,ichan=''):
    
    psf_stat=imstat(imagename=outname+'.psf',chans=ichan)
    
    bmaj=imhead(    imagename=outname+'.image',
                    mode='get',
                    hdkey='beammajor')
    bmin=imhead(    imagename=outname+'.image',
                    mode='get',        
                    hdkey='beamminor')
    bpa=imhead(        imagename=outname+'.image',
                    mode='get',        
                    hdkey='beampa')
    psf_psize=imhead(    imagename=outname+'.image',
                        mode='get',        
                        hdkey='cdelt1')
    bmaj=bmaj['value']
    bpa=bpa['value']
    bmin=bmin['value']
    psf_psize=abs(psf_psize['value']/(np.pi)*180*60*60)
    
    dbeam_area=psf_stat['sum'][0]*psf_psize**2/psf_stat['max'][0]
    
    print dbeam_area
    print 1.133*bmaj*bmin
    
def calcscale(outname):
    #
    # calculate the scaling factor for the residual map
    #
    shape=imhead(outname+'.image',mode='get',hdkey='shape')
    shape=shape['value']
    nchan=shape[-1]
    #print nchan
    
    cmodel_flux=np.arange(float(nchan))
    dmap_flux=np.arange(float(nchan))
    rmap_flux=np.arange(float(nchan))
    res_scale=np.arange(float(nchan))
    
    for i in range(0,nchan):
            
       rmap_stat=imstat(imagename=outname+'.residual',chans=str(i))
       dmap_stat=imstat(imagename=outname+'_d.residual',chans=str(i))
       cmodel_stat=imstat(imagename=outname+'.cmodel',chans=str(i))
       eff=cmodel_stat['sum'][0]/(dmap_stat['sum'][0]-rmap_stat['sum'][0])
       
       res_scale[i]=eff
       cmodel_flux[i]=cmodel_stat['sum'][0]
       dmap_flux[i]=dmap_stat['sum'][0]
       rmap_flux[i]=rmap_stat['sum'][0]
    
       
       for i in range(0,nchan):
           print "---"
           print res_scale[i]
           print 'model flux: '+str(cmodel_flux[i])
           print 'dmap flux:  '+str(dmap_flux[i])
           print 'res flux:   '+str(rmap_flux[i])



def testmask(imfile):
    
    os.system('rm -rf '+imfile+'.masked')
    immath(imagename=imfile,expr='IM0',outfile=imfile+'.masked')
    

#######################
    ipl_statwt(oldsrcfile,srcfile)

def wtplt(msfile):
    plotms(msfile,xaxis='uvdist',yaxis='wt',
        coloraxis='field',showmajorgrid=True,
        plotfile=msfile+'.wt_uvdist.png',overwrite=True) 




#
#   tested with
#       casapy: r22208
#       UVLIST: Revision 2012/03/29
#       FITS:   Revision 2012/06/27 
#
#   install carmafiller from the developer version CASA
#       https://safe.nrao.edu/wiki/bin/view/Main/ScottRankinCasaBuildNotes
#   
#   regarding the frequency/frame issue
#       https://safe.nrao.edu/wiki/bin/view/Software/ChannelFrequencies
#       http://www.jb.man.ac.uk/ALMA/ATCAfixes.html
#       * carmafiller yields different restfreq/reffreq information... (needs checking)
#       * my carma data seem to be okay after going through importmir.py
#
#
