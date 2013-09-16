# Note:
#    1) casapy --help for more CASA run options
#    2) casapy -c test.py mode

# Reduction Checking Note:
#    1) ensure checking right channels for continuum substraction
#    2) cell_size >1/2 Beam
#    3) casaviewer & casaplotms for flagging checks
#    5) uvcs_order=0 for spectra combined from different spws
#       uvcs_combine='spw' is also something you can tune.
#    6) no regrdding smaller than intrinsic channle sizes
#
# Current Known Bugs:
#    1) imcontsub bug
#    2) frame regridding bug in clean or cvel
#
# extra tips:
#    1) import pyfits lib:
#        >sys.path=["/Library/Frameworks/Python.framework/Versions/7.0/lib/python2.7/site-packages/"]+sys.path
#        >import pyfits
#    2) ms vis history check:
#        >listhistory
#
# Batch Run:
#     `casapy -c testscript.inp` &
#     or
#     nohup `casapy -c testscript.inp` &

# EVLA reduction
#    ---
#    importmode='evla'  # using importevla() to import data from sdm (default: 'vla')
#    evlacal=True           # using gencal()+applycal() to add proper weights (estimated from syspower/caldevice tables) into MS
#                   # (default: False)
#    calwt=False           # turn off weight re-calculating from sigma+gaincaltable when applying
#                   # gain/bandpass tables (default: True)
#    ---

# ToDo:
#        optimze file handling
#        cvel for single-track reduction
#
#       Reference:
#           http://casaguides.nrao.edu/index.php?title=CARMA_spectral_line_mosaic_M99
#           http://casaguides.nrao.edu/index.php?title=Extracting_data_from_MIRIAD
#           http://casaguides.nrao.edu/index.php?title=SMA_CO_Line_Data
#       Adapted from the NGC2403 tutorial scripts in the CASA trainning materials
#           http://casa.nrao.edu/Tutorial/20081007/
#           http://casa.nrao.edu/casatraining.shtml

#    AS to 3.3,     cleaning/cvel a file having multiple frames are not supported.
#                so cvel each one -> concat -> clean
#                
#                spws with the same config but different corrs are considered
#                as one spw. but uvcontsub & split will have trouble with it.
#                so contsub in each one -> concat 
#
#    timesort=True was added into importmir:
#        This will largly speed up cvel!!!
#

"""
box= '0,0,50,50'
region = 'circle[ [18h12m24s, -23d11m00s], 2.3arcsec]'
region = 'rotbox[ [18h12m24s, -23d11m00s], [10pix,5pix], 45deg]'

"""


"""

if  flagselect!='':
    news(""
    news("  ----------------------- "
    news("  Flagging Selection Used "
    news("  ----------------------- "
    news(""
    if  type(flagselect)==type('abc'):
        flagselect=[flagselect]

    for i in range(0, len(flagselect)):
        flagcomall=flagselect[i]

        if  flagcomall.find('quack')==-1 and flagcomall.find('rfi')==-1:
            default('flagdata')
            flagbackup=False
            vis=prefix+'.ms'
            flagcom=flagcomall.split('++')
            selectdata=True         
            for j in range(0,len(flagcom)):
                if  flagcom[j].find('time')!=-1:
                    timerange=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('ant')!=-1:
                    antenna=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]     
                if  flagcom[j].find('clipminmax')!=-1:
                    cliptext=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                    cliptext=cliptext.split(',')
                    clipminmax=[float(cliptext[0]),float(cliptext[1])]
                if  flagcom[j].find('clipexpr')!=-1:
                    clipexpr=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('field')!=-1:
                    field=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('corr')!=-1:
                    correlation=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('spw')!=-1:
                    spw=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('uvrange')!=-1:
                    uvrange=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
            news("--"
            news(flagcom
            news(" -Flagging Selection (Manualflag Mode)-"
            news(" field: "+str(field)
            news(" timerange: "+str(timerange)
            news(" correlation: "+str(correlation)
            news(" antenna: "+str(antenna)
            news(" spw:"+str(spw)
            news(" uvrange:"+str(uvrange)
            if  clipminmax!=[]:
                news(" clipminmax: "+str(clipminmax)
                news(" clipexpr: "+str(clipexpr)        
            news("--"
            flagdata()

        if  flagcomall.find('quack')!=-1:
            flagcom=flagcomall.split('++')
            default('flagdata')
            vis=prefix+'.ms'
            mode='quack'
            selectdata=True
            flagbackup=False
            
            for j in range(0,len(flagcom)):
                if  flagcom[j].find('int')!=-1:
                    quackinterval=\
                        float(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('mode')!=-1:
                    quackmode=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]     
                if  flagcom[j].find('time')!=-1:
                    timerange=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('field')!=-1:
                    field=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('ant')!=-1:
                    antenna=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('corr')!=-1:
                    correlation=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('spw')!=-1:
                    spw=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('scan')!=-1:
                    scan=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
            news("--"
            news(flagcom
            news(" -Flagging Selection (Quack Mode)-"
            news(" field: "+str(field)
            news(" timerange: "+str(timerange)
            news(" correlation: "+str(correlation)
            news(" antenna: "+str(antenna)
            news(" spw: "+str(spw)
            news(" scan: "+str(scan)
            news(" quackinterval: "+str(quackinterval)
            news(" quackmode: "+str(quackmode)     
            news("--"
            flagdata()      

        if  flagcomall.find('rfi')!=-1:
            flagcom=flagcomall.split('++')
            default('flagdata')
            flagbackup=False
            vis=prefix+'.ms'
            mode='rfi'
            selectdata=True
            
            for j in range(0,len(flagcom)):
                if  flagcom[j].find('time')==1:
                    timerange=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('ant')!=-1:
                    antenna=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]     
                if  flagcom[j].find('timeampcutoff')!=-1:
                    time_amp_cutoff=float(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('freqampcutoff')!=-1:
                    freq_amp_cutoff=float(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('bscutoff')!=-1:
                    bs_cutoff=float(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('antcutoff')!=-1:
                    ant_cutoff=float(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('clipexpr')!=-1:
                    clipexpr=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('field')!=-1:
                    field=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('corr')!=-1:
                    correlation=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('spw')!=-1:
                    spw=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('uvrange')!=-1:
                    uvrange=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('scan')!=-1:
                    scan=flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")]
                if  flagcom[j].find('bpfit')!=-1:
                    freqlinefit=True
                if  flagcom[j].find('starchan')!=-1:
                    start_chan=int(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('endchan')!=-1:
                    end_chan=int(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('numtime')!=-1:
                    num_time=int(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
                if  flagcom[j].find('flaglevel')!=-1:
                    flag_level=int(flagcom[j][flagcom[j].find("(")+1:flagcom[j].find(")")])
            news("--"
            inp(flagdata)
            news("--"
            news(flagcom
            news(" -Flagging Selection (Manualflag Mode)-"
            news(" field: "+str(field)
            news(" timerange: "+str(timerange)
            news(" correlation: "+str(correlation)
            news(" antenna: "+str(antenna)
            news(" spw:"+str(spw)
            news(" uvrange:"+str(uvrange)
            news(" time_amp_cutoff:"+str(time_amp_cutoff)
            news(" freq_amp_cutoff:"+str(freq_amp_cutoff)
            news(" bs_cutoff:"+str(bs_cutoff)
            news(" ant_cutoff:"+str(ant_cutoff)
            news(" num_time:"+str(num_time)
            
            if  clipminmax!=[]:
                news(" clipminmax: "+str(clipminmax)
                news(" clipexpr: "+str(clipexpr)        
            news("--"
            flagdata()
            
        del flagcom
        del flagcomall
"""


"""
old imerge_20111125:
#----------------------------------------------------------------------------------------
#   TRACK COMBINATION
#----------------------------------------------------------------------------------------
news("")
news("++++++++++++++++++++++")
news("")
news("Merge Tracks:")
news(str(prefix_combine))
news("")
news("++++++++++++++++++++++")
news("")

prefix_combine_file=copy.deepcopy(prefix_combine)
mincw=0
srcfile=prefix+'.src.ms'
prefix_srcfile=prefix+'.src'
if    spwrgd==True:
    srcfile=prefix+'.src_rgd.ms'
    prefix_srcfile=prefix+'.src_rgd'
    
for i in range(len(prefix_combine)):
    
    prefix_combine_file[i]=prefix_combine[i]+'.src_rgd.ms'
    
    if  spwrgd==True:
        news("")
        news("--cvel--")
        news("")
        news("Use CVEL to perform a channel regridding")
        news(  prefix_combine[i]+'.src.ms'+'>>>'+\
                prefix_combine_file[i])
        news("")
        
        os.system('rm -rf '+prefix_combine_file[i])
        default('cvel')
        vis=prefix_combine[i]+'.src.ms'
        outputvis=prefix_combine_file[i]
        outframe=out_frame
        mode      = clean_mode
        nchan     = clean_nchan
        start     = clean_start
        width     = clean_width    
        restfreq = rest_freq
        interpolation = spinterpmode
        hanning=hs
        cvel()
    else:
        prefix_combine_file[i]=prefix_combine[i]+'.src.ms'
        
    tb.open(prefix_combine_file[i]+'/SPECTRAL_WINDOW')
    mincw=[mincw]+tb.getcol('CHAN_WIDTH')
    tb.close
    mincw=np.min(mincw)
    
    if  uvcs==True:
           
        news("")
        news("--uvcontsub--")
        news("")
        news(" fit continuum emission in uv domain using line-free channels specified")
        news(" by fit_spw")
        news(" ")
        news(" Two new MSes will be created:") 
        news(" "+prefix_combine_file[i]+".cont")
        news(" "+prefix_combine_file[i]+".contsub")
        news(" ")
        
        os.system('rm -rf '+prefix_combine_file[i]+".cont")
        os.system('rm -rf '+prefix_combine_file[i]+".contsub")
        default('uvcontsub')
        vis      = prefix_combine_file[i]
        field    = ''
        fitspw   = fit_spw
        fitorder = fit_order
        spw      = clean_spw
        combine  = uvcs_combine
        want_cont= True
        uvcontsub()     

if  len(prefix_combine_file)>1:

    news("")
    news("--concat--")
    news("")
    news("Use CONCAT to combine tracks and creat a new measurement set file")
    news("")
    
    if  uvcs==False:
        postfix=['']
    else:
        postfix=['.contsub','.cont']
    
    for loop in postfix:
        
        prefix_combine_inp=copy.deepcopy(prefix_combine_file)
        for i in range(len(prefix_combine_file)): 
             prefix_combine_inp[i]=prefix_combine_file[i]+loop
        os.system('rm -rf '+srcfile+loop)
        default('concat')
        vis=prefix_combine_inp
        concatvis=srcfile+loop
        freqtol=str(mincw/1.e6/4.)+'MHz'
        if  freq_tol!='':
            freqtol=freq_tol #'0.1MHz'
        dirtol='1.arcsec' #'1.arcsec'
        timesort=False
        concat()

#----------------------------------------------------------------------------------------
#   Obs List: List a summary of the new MS
#----------------------------------------------------------------------------------------
news("")
news("--listobs--")
news("")
news("Use listobs to news(verbose summary of the MS:")
postfix=''
if    uvcs==True:
    postfix='.contsub'
news(srcfile+postfix)
news("")
listobs(vis=srcfile+postfix,verbose = True)
exportlog('listobs',prefix_srcfile+'.listobs.log')
logflist=logflist+[prefix_srcfile+'.listobs.log']


#the below lines need some further explanations

if evlacal==True:
    tb.open(msfile,nomodify=False)
    tweight=tb.getcol('WEIGHT')
    tb.putcol('WEIGHT',tweight*scalewt)
    tb.close
    del tweight


"""


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
from iplot_lib import *
 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

#----------------------------------------------------------------------------------------
#     this function will export task log to a plain text file
#----------------------------------------------------------------------------------------
def    exportlog(taskname,logname,extralog=[]):

    casa_log = open(casalog.logfile(),'r')
    lines = casa_log.readlines()
    casa_log.close()
    
    iswrite=False
    task_log = open(logname,'w')
    for line in lines:
        if line.find('Begin Task: '+taskname) != -1 or iswrite==True:
                if line.find('Begin Task: '+taskname) != -1:
                    task_log = open(logname,'w')
                task_log.write(line)
                iswrite=True
        if line.find('End Task: '+taskname)!=-1:
            if extralog!=[]:
                for tmp in extralog:
                    task_log.write(tmp)
            iswrite=False
            task_log.close()
    task_log.close()

def exportcasalog(blines, elines,logname):
    
    task_log = open(logname,'w')
    for i in range(len(elines)):
        if i>=len(blines):
            task_log.write(elines[i])    
    task_log.close()

#----------------------------------------------------------------------------------------
#   plot source u-v coverage and track antenna positions (not tested)
#----------------------------------------------------------------------------------------
def plconfig(msfile,plotformat='png',source='',spw_source=''):

    news("")
    news("--plotxy--")
    news("")
    news("plot the source uv coverage and antenna positions")
    
    plotuv(vis=msfile,field=source,\
        figfile=msfile+'.sou.uvcoverage.'+plotformat,\
        spw=spw_source,interactive=True)
    plotants(vis=msfile,figfile=msfile+'.plotants.'+plotformat,interative=True)    

#----------------------------------------------------------------------------------------
#   plot source visibilities (amp vs. time) (with interactive flagging) (not tested)
#----------------------------------------------------------------------------------------
def pl_amp_time(msfile,inp_field='',inp_spw='',plotformat='png',intflag=False):
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

#----------------------------------------------------------------------------------------
#   plot source visibilities (amp vs. uvdist) (not tested)
#----------------------------------------------------------------------------------------
def pl_amp_uvdist(msfile,inp_field='',inp_spw='',plotformat='png',intflag=False):

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


#----------------------------------------------------------------------------------------
#   Plot the source visibilities (amp vs. time, amp vs. uvdist) (not tested)
#----------------------------------------------------------------------------------------
def pl_sou_amp(msfile,source='',spw_source='',plotformat='png'):

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

#----------------------------------------------------------------------------------------
#   plot bandpass solutions (not tested)
#----------------------------------------------------------------------------------------
def pl_bandpass(tbfile,passcal=''):
    # msfile
    # tbfile=prefix+'.bcal'
    plotformat='png'
    news("")
    news("--plotcal--")
    news("")
    news("Plot banpass solutions for each antenna")
    
    merge_eps='gs -sDEVICE=pdfwrite -sOutputFile='+tbfile+'.bandpass.pdf'
    merge_eps=merge_eps+' -dNOPAUSE -dBATCH'
        
    default('plotcal')
    caltable = tbfile
    field = passcal
    selectplot=True
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    showgui = False
    
    tb.open(tbfile+'/ANTENNA')
    num_ant=len(tb.getcol('NAME'))
    tb.close
    news("")
    news("Number of Antenna: "+str(num_ant))
    news("")
    tb.open(tbfile)
    spwid_passcal=np.unique(tb.getcol('SPECTRAL_WINDOW'))
    spwid_passcal=sorted(list(set(spwid_passcal)))
    tb.close
    news("")
    news("spwid: "+str(spwid_passcal))
    news("")
        
    for i in range(0,num_ant-1):
        antenna=str(i)
        for j in range(0,len(spwid_passcal)):
            spw=spwid_passcal[j]
            plotrange = [-1, -1, 0.6, 1.4]
            subplot = 2*100+len(spwid_passcal)*10+1+j
            xaxis = 'chan'
            yaxis = 'amp'
            figfile=tbfile+'.bandpass.ant'+str(i)+'.pdf'
            plotcal()
            subtitle='Bandpass Solution: Antenna '+str(i)+' SpwID '+spwid_passcal[j]
            pl.title(subtitle,fontsize=6)        
           
            spw=spwid_passcal[j]
            plotrange = [-1, -1, -45, 45]
            subplot = 2*100+len(spwid_passcal)*10+len(spwid_passcal)+j+1
            xaxis=  'chan'
            yaxis = 'phase'
            figfile=tbfile+'.bandpass.ant'+str(i)+'.pdf'
            title='Passband Solution, Antenna '+str(i)+ 'SpwID '+spwid_passcal[j]
            plotcal()
        
        merge_eps=merge_eps+' '+tbfile+'.bandpass.ant'+str(i)+'.pdf'
    
    tmp=os.popen(merge_eps).read()
    news(tmp,origin='ghostscript')
    
    os.system('rm '+tbfile+'.bandpass.ant*.pdf')
    news("")
    
    news("")
    news("--plotcal--")
    news("")
    news("Plot banpass solutions for all antennae")
    
    default('plotcal')
    caltable = tbfile
    field = passcal
    selectplot=True
    plotsymbol='b,'
    markersize=0.1
    fontsize=6.0
    showgui = False      
    for j in range(0,len(spwid_passcal)):
        spw=spwid_passcal[j]
        plotrange = [-1, -1, 0.6, 1.4]
        subplot = 2*100+len(spwid_passcal)*10+1+j
        xaxis = 'chan'
        yaxis = 'amp'
        figfile=tbfile+'.plotcal.allbandpass.'+plotformat
        plotcal()
        subtitle='Bandpass Solution'
        pl.title(subtitle,fontsize=6)       
        spw=spwid_passcal[j]
        plotrange = [-1, -1, -90, 90]
        subplot = 2*100+len(spwid_passcal)*10+len(spwid_passcal)+j+1
        xaxis = 'chan'
        yaxis = 'phase'
        figfile=tbfile+'.plotcal.allbandpass.'+plotformat
        title='Passband Solution'
        plotcal()
    news("")


#----------------------------------------------------------------------------------------
#   plot gain solution (not tested)
#----------------------------------------------------------------------------------------
def pl_gain():

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

#----------------------------------------------------------------------------------------
#   Use plotxy for source (after calibrations) (not tested)
#----------------------------------------------------------------------------------------
def pl_aftercal():
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
#----------------------------------------------------------------------------------------
#   Use plotxy for calibrators (after calibrations)
#----------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------
#   Use plotxy for source (after calibrations)
#----------------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------------
#   Use plotxy for Source
#----------------------------------------------------------------------------------------    
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












# This function can convert the information in the log file of 
# /uvlist options=spec/ to a python dictonary
#     updated for the old amiriad uvlist log style
def getuvlist(logname):
    
    uvlist_log = open(logname,'r')
    lines = uvlist_log.readlines()
    uvlist_log.close()
    
    nchan=0

    uvlist_dict={    'rest frequency':         [],
                    'starting channel':        [],
                    'number of channels':    [],
                    'starting frequency':    [],
                    'frequency interval':    [],
                    'starting velocity':    [],
                    'ending velocity':        [],
                    'velocity interval':    [],
    }
    keys=uvlist_dict.keys()
    for line in lines:
        line = line.lower()
        if    line.find(':') != -1:
            [key, value] = line.split(':')
            values=value.split()            
            #values = map(float, values)
            for tmp in keys:
                if    key.find(tmp) != -1:
                    uvlist_dict[tmp]=uvlist_dict[tmp]+values
        if  line.find('optical velocities') !=-1:
            break
            
    return uvlist_dict


# This function can send an reduction run log email back to you
#
def emailsender(myemail,subject,maintext,attachs,\
                smtpserver='smtp.gmail.com',\
                eusrname='casareduc@gmail.com',\
                epassword='astrouiuc'):

   msg = MIMEMultipart()

   msg['From'] = eusrname
   msg['To'] = myemail
   msg['Subject'] = subject

   msg.attach(MIMEText(maintext))

   if  type(attachs)==type('abc'):
          attachs=[attachs]
   for attach in attachs:
       part = MIMEBase('application', 'octet-stream')
       part.set_payload(open(attach, 'rb').read())
       Encoders.encode_base64(part)
       postfix=attach.split('.')
       postfix=postfix[-1]
       if postfix=='log' or postfix=='py' :
             attach=attach+'.txt'
       part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach))
       msg.attach(part)

   mailServer = smtplib.SMTP(smtpserver,587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(eusrname, epassword)
   mailServer.sendmail(eusrname, myemail, msg.as_string())
   mailServer.close()

#----------------------------------------------------------------------------------------
#   File List: Read the data file name(s) from 'prefix'.list, if 'rawfiles' not defined
#----------------------------------------------------------------------------------------
def getprefixlist(prefix):
    
    rawfiles_list=open(prefix+'.list','r')
    lines=rawfiles_list.readlines()
    rawfiles_list.close()
    rawfiles=[]
    for line in lines:
            line=line.strip()
            rawfiles.append(line)
    
    return rawfiles


# This function will import the data in a mir file into a CASA MS
#
def importmir(    mirfile='',
                vis='',
                telescope='CARMA',
                win_list=[],
                nocal=False,
                mirbin=''    ):

    machinename=socket.gethostname()
    news('machinename:')
    news(machinename)
    if mirbin=='':
        mirbin='/usr/local/miriad/bin/darwin/'
        if machinename=='carma-data.astro.illinois.edu':
            mirbin='/usr/local/miriad/miriad/bin/darwin/'
        if machinename=='rui-macbookpro.local':
            mirbin='/usr/local/miriad-carma/bin/darwin/'
        if machinename=='mmwave.astro.illinois.edu':
            mirbin='/usr/local/miriad/bin/darwin/'
        if machinename=='neon.astro.illinois.edu':
            mirbin='/usr/local/miriad-carma/bin/darwin/'            
    news('mirpath:')
    news(mirbin)
    
    cmd='uvlist options=spec vis='+mirfile+'>'+vis+'.uvlist.log'
    tmp=os.popen(mirbin+cmd).read()
    news(tmp,origin='miriad')
    news('run miriad-uvlist',origin='miriad')
    news(' ',origin='miriad')
    
    uvlist_dict = getuvlist(vis+'.uvlist.log')
    spw_list = range(1,len(uvlist_dict['number of channels'])+1)
    if win_list==[]:
        win_list=spw_list
    news('spectral windows list:')
    news(str(win_list))
        
    win_combine=[]
    for j in range(0,len(win_list)):

        fitspre=vis+'.win'+str(win_list[j])+'.fits'
        mspre=vis+'.win'+str(win_list[j])
        
        news("")
        news(">>>miriad-fits")
        news("")
        news("Use miriad-fits to export data from:")
        news(mirfile)
        news("to UVFITS:")
        news(fitspre)
        cmd=''
        if nocal==True:
            cmd=' options=nocal'
        cmd="fits in="+mirfile+" op=uvout select='win("+str(win_list[j])+\
            ")' out="+fitspre+cmd
        os.system('rm -rf '+fitspre)
        tmp=os.popen(mirbin+cmd).read()
        news(tmp,origin='miriad')
        
        news("")
        news(">>>importuvfits")
        news("")
        news("Use importuvfits() to import data in the UVFITS file:")
        news(fitspre)
        news("Write the data into the Measurement Set (MS):")
        news(mspre)
        news("")
        os.system('rm -rf '+mspre)
        importuvfits(fitsfile=fitspre,vis=mspre)
        win_combine.append(mspre)
        os.system('rm -rf '+fitspre)

    news("")
    news(">>>concat")
    news("")
    news("Use concat to glue windows and create a new measurement set file:")
    news(vis)
    news("")
    
    os.system('rm -rf '+vis)
    concat(vis=win_combine,concatvis=vis,freqtol='',dirtol='',timesort=True)
    for tmp in win_combine:
        os.system('rm -rf '+tmp+'*')
    
    news("")
    news("Changing Antenna Names")
    prefix_ant=''
    if telescope=='CARMA' or telescope=='carma' :
        prefix_ant='CA'
        obsname='CARMA'
    if telescope=='BIMA' or telescope=='bima' :
        prefix_ant='BA'
        obsname='BIMA'            
    
    tb.open(vis+"/ANTENNA",nomodify=False)
    namelist=tb.getcol("NAME").tolist()
    for k in range(len(namelist)):
        name = prefix_ant+namelist[k]
        news(' Changing '+namelist[k]+' to '+name)
        namelist[k]=name
    tb.putcol("NAME",namelist)
    tb.close()
    
    tb.open(vis+"/OBSERVATION",nomodify=False)
    namelist=tb.getcol("TELESCOPE_NAME").tolist()
    for k in range(len(namelist)):
        namelist[k]=obsname
    tb.putcol("TELESCOPE_NAME",namelist)
    tb.close()
    
    news("")
    news("++")
    news(mirfile+'-->'+vis+' done!')
    news("++")
    news("")

# This function will import the data in a miriad file into a CASA MS
def importmiriad(mirfile='',
                vis='',
                telescope='CARMA',
                extenv=''    ):

    if  extenv=='':
        extenv={"PATH":"/usr/local/miriad-carma/bin/darwin:/usr/local/miriad-carma/opt/casa/bin:",
                "DYLD_LIBRARY_PATH":"/usr/local/miriad-carma/opt/casa/lib",
                "HOME":"~/"}

    # FIX UV HEADR FOR BIMA DATA
    if  telescope=='BIMA' or telescope=='bima' :
        
        news(' ',origin='miriad')
        news('##########################################',origin='miriad')
        news('##### Begin Task: UVPUTH             #####',origin='miriad')
        os.system("rm -rf "+vis+'.bima')
        cmd='uvputhd type=a varval=s hdvar=purpose vis='+mirfile+' out='+vis+'.bima'
        p=subprocess.Popen(cmd,shell=True,env=extenv,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.stdout.read()
        news(output,origin='miriad')
        cmd='fix4bima '+vis+'.bima'
        p=subprocess.Popen(cmd,shell=True,env=extenv,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.stdout.read()
        news(output,origin='miriad')
        news('##### END Task: UVPUTH               #####',origin='miriad')
        news(' ',origin='miriad')
        news('##########################################',origin='miriad')  
        mirfile=vis+'.bima'
    
    # RECREAT WIDEBAND DATA
    news(' ',origin='miriad')
    news('##########################################',origin='miriad')
    news('##### Begin Task: UVCAL              #####',origin='miriad')
    os.system("rm -rf "+vis+'.mir')
    cmd='uvcal options=avechan,nowide,unflagged vis='+mirfile+' out='+vis+'.mir'
    p=subprocess.Popen(cmd,shell=True,env=extenv,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.read()
    news(output,origin='miriad')
    news('##### END Task: UVCAL                #####',origin='miriad')
    news(' ',origin='miriad')
    news('##########################################',origin='miriad')
    
    # RUN CARMAFILLER
    news(' ',origin='miriad')
    news('##########################################',origin='miriad')
    news('##### Begin Task: CARMAFILLER        #####',origin='miriad')
    os.system("rm -rf "+vis)
    cmd='carmafiller tsys=True vis='+vis+'.mir'+' ms='+vis
    p=subprocess.Popen(cmd,shell=True,env=extenv,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.read()
    news(output,origin='miriad')
    news('##### END Task: CARMAFILLER          #####',origin='miriad')
    news('##########################################',origin='miriad')
    
    # FIX ANTENNA NAME & DISH SIZE
    news("")
    news("Changing Antenna Names")
    prefix_ant=''
    if  telescope=='CARMA' or telescope=='carma' :
        prefix_ant='CA'
        obsname='CARMA'
    if  telescope=='BIMA' or telescope=='bima' :
        prefix_ant='BA'
        obsname='BIMA'            
    tb.open(vis+"/ANTENNA",nomodify=False)
    namelist=tb.getcol("NAME").tolist()
    dialist=tb.getcol("DISH_DIAMETER").tolist()
    for k in range(len(namelist)):
        name = namelist[k].replace("C", prefix_ant)
        news(' Changing '+namelist[k]+' to '+name)
        namelist[k]=name
        if  telescope=='BIMA' or telescope=='bima' :
            dialist[k]=6.1
    tb.putcol("NAME",namelist)
    tb.putcol("DISH_DIAMETER",dialist)
    tb.close()
    
    # UPDATE SCAN NUMBER TO START FROM 1
    tb.open(vis+"",nomodify=False)
    scanlist=tb.getcol("SCAN_NUMBER")
    for k in range(len(scanlist)):
        scan=scanlist[k]+1
        scanlist[k]=str(scan)
    tb.putcol("SCAN_NUMBER",scanlist)
    tb.close()
    
    # FIX TELESCOPE NAME
    tb.open(vis+"/OBSERVATION",nomodify=False)
    namelist=tb.getcol("TELESCOPE_NAME").tolist()
    for k in range(len(namelist)):
        namelist[k]=obsname
    tb.putcol("TELESCOPE_NAME",namelist)
    tb.close()
    
    # FIX PROJECT 
    tb.open(vis+"/OBSERVATION",nomodify=False)
    prolist=tb.getcol("PROJECT").tolist()
    for k in range(len(prolist)):
        prolist[k]=vis
    tb.putcol("PROJECT",prolist)
    tb.close()
    
    # FIX TIMERANGE (zero number will cause troubles when concating MSs) 
    ms_stat=visstat(vis=vis,axis='time')
    timerange_max=ms_stat['TIME']['max']    # in s
    timerange_min=ms_stat['TIME']['min']
    timerange_mean=ms_stat['TIME']['mean']    # in s
    tb.open(vis+"/OBSERVATION",nomodify=False)
    prolist=tb.getcol("TIME_RANGE").tolist()
    for k in range(len(prolist)/2):
        prolist[0][k]=timerange_min
        prolist[1][k]=timerange_max
    tb.putcol("TIME_RANGE",prolist)
    prolist=tb.getcol("RELEASE_DATE").tolist()
    for k in range(len(prolist)):
        prolist[k]=timerange_mean
    tb.putcol("RELEASE_DATE",prolist) 
    tb.close()
    
    
    
# This function will clean image products
#
def cleanup(outname,tag=''):
    version=['mask','cm','residual','model','cmodel',
            'psf','image','sen',
            'flux.pbcoverage','flux.pbcoverage.thresh_mask',
            'flux','flux.thresh_mask',
            'flux.mask0']
    for i in range(0,len(version)):
        if    os.path.exists(outname+'.'+version[i]):
            if     tag=='':
                os.system('rm -rf '+outname+'.'+version[i])
            else:
                os.system('rm -rf '+outname+'.'+tag+'.'+version[i])
                os.system('mv '+outname+'.'+version[i]+' '\
                        +outname+'.'+tag+'.'+version[i])

def exportclean(outname):
    version=['mask','cm','residual','model','cmodel',
            'psf','image','sen',
            'flux.pbcoverage','flux.pbcoverage.thresh_mask',
            'flux','flux.thresh_mask',
            'flux.mask0']
    for i in range(0,len(version)):
        if    os.path.exists(outname+'.'+version[i]):
            exportfits(outname+'.'+version[i],
                    outname+'.'+version[i]+'.fits', 
                    velocity=True,
                    overwrite=True)


def mask0clean(outname,mask0):
    version=['mask','cm','residual','model','cmodel',
            'psf','image','sen',
            'flux.pbcoverage','flux.pbcoverage.thresh_mask',
            'flux','flux.thresh_mask']
    for i in range(0,len(version)):
        if    os.path.exists(outname+'.'+version[i]):
            immask(outname+'.'+version[i],mask0)


def checkbeam(outname,method='maximum'):

    outnamelist=imhead(imagename=outname+'.image',mode='list')
    
    if  'perplanebeams' in outnamelist.keys():
    
        imhdlist=imhead(outname+'.image',mode='list')
        nchan=imhdlist['perplanebeams']['nChannels']
        
        psf_bmaj=np.arange(float(nchan))
        psf_bmin=np.arange(float(nchan))
        psf_bpa=np.arange(float(nchan))
        psf_size=np.arange(float(nchan))
            
        for i in range(0,nchan):
            
            news("")
            news('FRAME: %i' % i)
            news("")
            psf_bmaj[i]=imhdlist['perplanebeams']['*'+str(i)]['major']['value']
            psf_bmin[i]=imhdlist['perplanebeams']['*'+str(i)]['minor']['value']
            psf_bpa[i]=imhdlist['perplanebeams']['*'+str(i)]['positionangle']['value']
            psf_size[i]=psf_bmaj[i]*psf_bmin[i]
            news('BMAJ       %7.2f arcsec' % psf_bmaj[i])
            news('BMIN       %7.2f arcsec' % psf_bmin[i])
            news('BPA        %7.2f deg' % psf_bpa[i])
            news('BMAJXBMIN  %7.2f arcsec^2' % psf_size[i])
        
        
        psf_size_median=np.median(psf_size)
        sortindex=sorted(range(len(psf_size)),key=lambda x:psf_size[x])
        index_median=sortindex[nchan/2]
        index_max=max(enumerate(psf_size),key=lambda x: x[1])[0]
        news("")
        news([psf_size[index_median],psf_bmaj[index_median],psf_bmin[index_median],psf_bpa[index_median]])
        news([psf_size[index_max],psf_bmaj[index_max],psf_bmin[index_max],psf_bpa[index_max]])
        news("")
        if  method=='maximum':
            index_choice=index_max
        if  method=='median':
            index_choice=index_median
            
        rbmaj= '%.2f' % psf_bmaj[index_choice]
        rbmin= '%.2f' % psf_bmin[index_choice]
        rbpa= '%.2f' % psf_bpa[index_choice]
    
    if  'beammajor' in outnamelist.keys():
        
        bmaj=imhead(imagename=outname+'.image',mode='get',hdkey='beammajor')
        bmin=imhead(imagename=outname+'.image',mode='get',hdkey='beamminor')
        bpa=imhead(imagename=outname+'.image',mode='get',hdkey='beampa')
        rbmaj= '%.2f' % bmaj['value']
        rbmin= '%.2f' % bmin['value']
        rbpa= '%.2f' % bpa['value']

    rbmaj=rbmaj+'arcsec'
    rbmin=rbmin+'arcsec'
    rbpa=rbpa+'deg'
    psf_restor_beam=[rbmaj,rbmin,rbpa]
    news("return restoring beam:")
    news(str(psf_restor_beam))
    return psf_restor_beam


# This function can check the psf at diffrent 
#
# parameter:
#
#     outname
#    execfile('/Users/ruixue1/Worklib/casapy/checkpsf.py')

    

def checkpsf(outname):    
    
    imhead(imagename=outname+'.psf',mode='put',hdkey='bunit',hdvalue='Jy/pixel')
    psf_shape=imhead(outname+'.psf',mode='get',hdkey='shape')
    psf_nx=psf_shape['value'][0]
    psf_ny=psf_shape['value'][1]
    psf_nz=psf_shape['value'][3]
    
    # get some info for the initial guessing
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
    
    # write a file with initial guessing
    estfile=open(outname+'.psf.imfit.est.log','w')
    print >>estfile,'1.0, '+\
            str(int(psf_nx/2))+', '+\
            str(int(psf_ny/2))+', '+\
            str(bmaj)+'arcsec, '+str(bmin)+'arcsec, '+str(bpa)+'deg, f'
            # str(bmaj)+'arcsec, '+str(bmin)+'arcsec, '+str(bpa)+'deg' # without peak fixed to 1Jy/pixel
    estfile.close()
    
    # setting fitbox
    imfit_box=str(int(psf_nx/2-3*(bmaj/psf_psize)))+','+str(int(psf_ny/2-3*(bmaj/psf_psize)))+','\
            +str(int(psf_nx/2+3*(bmaj/psf_psize)))+','+str(int(psf_ny/2+3*(bmaj/psf_psize))) 
    print imfit_box
    imfit_log=imfit(imagename=outname+'.psf',box=imfit_box,\
        logfile=outname+'.psf.imfit.log',\
        #estimates=outname+'.psf.imfit.est.log')
        estimates='')
    
    psf_nchan=imfit_log['results']['nelements']    
    psf_bmaj=np.arange(float(psf_nchan))
    psf_bmin=np.arange(float(psf_nchan))
    psf_bpa=np.arange(float(psf_nchan))
    
    for i in range(0,psf_nchan):
        news("")
        news('FRAME: %i' % i)
        news("")
        psf_bmaj[i]=imfit_log['results']['component'+str(i)]['shape']['majoraxis']['value']
        psf_bmin[i]=imfit_log['results']['component'+str(i)]['shape']['minoraxis']['value']
        psf_bpa[i]=imfit_log['results']['component'+str(i)]['shape']['positionangle']['value']
        news('BMAJ %5.2f arcsec' % psf_bmaj[i])
        news('BMIN %5.2f arcsec' % psf_bmin[i])
        news('BPA  %5.2f deg' % psf_bpa[i])
    
    news("")
    news("Initial Guessing")
    news("")
    news('BMAJ %5.2f arcsec' % bmaj)
    news('BMIN %5.2f arcsec' % bmin)
    news('BPA  %5.2f deg' % bpa)
    news("")
    news("--")
    news("Beam Area Error: abs(barea/MEAN(barea)-1)")
    psf_area=psf_bmaj*psf_bmin
    mpsf_area=np.mean(psf_area)
    dist=np.abs(psf_area/mpsf_area-1)
    news(str(dist))
    dist= np.where( dist >0.1, dist, 0)
    
    news("")
    news("pass the psf consistancy test?")
    news(str(np.sum(dist)==0))
    news("")
    news("How many frame has been fitted succesfully?")
    news("orginal channels: %i " % psf_nz)
    news("fitted channels:  %i " % psf_nchan)
    
    rbmaj= '%.2f' % np.mean(psf_bmaj)
    rbmin= '%.2f' % np.mean(psf_bmin)
    rbpa= '%.2f' % np.mean(psf_bpa)
    rbmaj=rbmaj+'arcsec'
    rbmin=rbmin+'arcsec'
    rbpa=rbpa+'deg'
    psf_restor_beam=[rbmaj,rbmin,rbpa]
    news(str(psf_restor_beam))
    
    return psf_restor_beam

def blsearch(logname=casalog.logfile()):
    
    news("")
    news("----------- antfilter Begin: -----------")
    news("")
    
    casa_log = open(logname,'r')
    lines = casa_log.readlines()
    casa_log.close()
    lines.reverse()
    
    antlist=[]
    lastfind=False
    for line in lines:
        if     line.find('BL=')!=-1 and \
            line.find("PlotMS::locate")!=-1 :
            logline=line.split("PlotMS::locate+")
            news(string.strip(logline[1]))
            ant=line.split(' ')
            for j in range(0,len(ant)):
                if  ant[j]=='&':
                    ant1=ant[j-1]
                    ant1=ant1[3:]
                    ant2=ant[j+1]
                    ant2=ant2.split('[')
                    left=ant2[1]
                    ant2=ant2[0]
                    news(ant1+'&'+ant2+' ['+left)
                    news("")
                    ant1=ant1.split('@')
                    ant1=ant1[0]
                    ant2=ant2.split('@')
                    ant2=ant2[0]
                    antlist.append("antenna='"+ant1+'&'+ant2+"'") 
                    lastfind=True
        else:
            if    lastfind==True:
                break    

    
    antlist=list(set(antlist))
    news("")
    news("flagging command: "+str(len(antlist)))
    news(str(antlist))
    news("")
    
    return antlist
    news("")
    news("----------- antfilter End: -----------")
    news("")

# write out information to casalog

def news(msg,origin='++++++'):
    
    msg=str(msg)
    casalog.origin(origin)
    casalog.post(msg)
    
    
def pbmask(imfile):    
    
    rmtables(imfile+'.mask')
    rmtables(imfile+'.mask1')
    rmtables(imfile+'.mask2')
    rmtables(imfile+'.mask3')
    rmtables(imfile+'.mask4')
    
    immath(imagename=[imfile,imfile],\
        expr='IM0/IM1',\
        outfile=imfile+'.mask0',\
        mask=imfile+'!=0')
    immoments(imagename=imfile+'.mask0',moments=0,outfile=imfile+'.mask1')
    stat=imstat(imfile+'.mask1')
    cutoff=stat['max'][0]
    print 'IM0/'+str(cutoff)
    immath(imagename=imfile+'.mask1',expr='IM0/'+str(cutoff),outfile=imfile+'.mask2')
    
    immath(imagename=imfile+'.mask2',expr='IM0',outfile=imfile+'.mask3',mask='"'+imfile+'.mask2">=1.0')
    #immath(imagename=[imfile,imfile+'.mask3',imfile+'.mask3'],expr='IM0*IM1*IM2',outfile=imfile+'.mask4')
    immath(imagename=[imfile,imfile+'.mask3'],expr='IM0*IM1',outfile=imfile+'.mask4')
    rmtables(imfile+'.mask0')
    rmtables(imfile+'.mask1')
    rmtables(imfile+'.mask2')
    rmtables(imfile+'.mask3')
    rmtables(imfile)
    os.system('mv '+imfile+'.mask4 '+imfile)
        
def genmask0(imfile):    
    # produce a mask image with unmask values=1
    os.system('rm -rf '+imfile+'.mask0')
    os.system('rm -rf tmp0')
    os.system('rm -rf tmp1')
    os.system('rm -rf tmp2')
    os.system('rm -rf tmp3')
    
    os.system('cp -rf '+imfile+' tmp0')
    immath(imagename=['tmp0','tmp0'],\
        expr='IM0/IM1',\
        outfile='tmp1',\
        mask='"tmp0"!=0')
    immoments(imagename='tmp1',moments=0,outfile='tmp2')
    stat=imstat('tmp2')
    cutoff=stat['max'][0]
    immath(imagename='tmp2',expr='IM0/'+str(cutoff),
        outfile='tmp3')
    immath(imagename='tmp3',expr='IM0',outfile=imfile+'.mask0',
        mask='"tmp3">=1.0')
    
    os.system('rm -rf tmp0')
    os.system('rm -rf tmp1')
    os.system('rm -rf tmp2')
    os.system('rm -rf tmp3')
    
    
def immask(imfile,maskfile):
    # use an masking image to mask a cube, avoid edge channel missing effect
    os.system('rm -rf '+imfile+'.tmp')
    immath(imagename=[imfile,maskfile],expr='IM0*IM1',outfile=imfile+'.tmp') 
    os.system('rm -rf '+imfile)
    os.system('mv '+imfile+'.tmp '+imfile)

def getuvrange(msfile):

    news("")
    news("--visstat--")
    news("")
    news("Use visstat to check the MS ready for imaging:")
    news(msfile)
    news("")
    ms_stat=visstat(vis=msfile,axis='uvrange',
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
    news('obs_freq      : '+str(obs_freq))
    news('obs_wavelength: '+str(obs_wavelength))

    # Synthesis Image in Radio Astronomy II P137
    theta_las=obs_wavelength/uvdist_min/3.1415*180.*60.*60*0.77/2.0
    theta_fwhm=obs_wavelength/(uvdist_rms)/3.1415*180.*60.*60*0.77/2.0
    news("")
    news("")
    news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    news("predicted beamwidth (uniform weighted)  : "+str(theta_fwhm)+' arcsec')
    news("predicted largest senstive angular scale: "+str(theta_las)+' arcsec')
    news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    news("")
    news("")


def uvspec(msfile,rest_freq='1420405752.0Hz'):
    # just like miriad uvspec to plot an "integrated" spectrum.
     plotms(msfile,xaxis='velocity',yaxis='amp',avgtime='999999s',
        avgscan=True,transform=True,restfreq=rest_freq,
        xdatacolumn='corrected',ydatacolumn='corrected',
        coloraxis='spw')

def uvplt(msfile):
    plotms(msfile,xaxis='time',yaxis='amp',avgchannel='99999',
        xdatacolumn='corrected',ydatacolumn='corrected',
        coloraxis='field')


 
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
     
#def dbscale(outname):
    
def modelconv(outname,mode=''):    

    # use *.residual *.image to get cmodel
    os.system('rm -rf '+outname+'.cmodel')
    os.system('rm -rf '+outname+'.cmodel2')
    
    # mode=''
    if     mode=="":    
        immath(imagename=[outname+'.image',outname+'.residual'],
        expr='IM0-IM1',outfile=outname+'.cmodel')
    
    # mode='conv'
    if     mode=="conv":
        bmaj=imhead(imagename=outname+'.image',mode='get',hdkey='beammajor')
        bmin=imhead(imagename=outname+'.image',mode='get',hdkey='beamminor')
        bpa=imhead(imagename=outname+'.image',mode='get',hdkey='beampa')
        print np.float(bmaj['value'])
        print np.float(bmin['value'])
        print np.float(bpa['value'])
        imsmooth(imagename=outname+'.model', kernel='gauss', \
                major=str(bmaj['value'])+'arcsec', \
                minor=str(bmin['value'])+'arcsec',\
                pa=str(bpa['value'])+'deg',\
                outfile=outname+'.cmodel2')
        immath(imagename=[outname+'.cmodel2',outname+'.image'],\
        expr='IM0+IM1-IM1',outfile=outname+'.cmodel')
        os.system('rm -rf '+outname+'.cmodel2')    

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
    # calculate the scaling factor for the residual map

    #os.system('rm -rf '+outname+'.cmodel')
    #immath(imagename=[outname+'.image',outname+'.residual'],
    #    expr='IM0-IM1',outfile=outname+'.cmodel')
    
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
        #mask='"'+imfile+'">=1.0')    
    


def checkstatwt(srcfile,statwt_fitspw=''):
    
    #srcfile='n0337d03.src.ms'
    #statwt_fitspw='1:7~17,0:46~56'

    oldsrcfile=srcfile
    srcfile=srcfile+'.rewt'
    
    os.system("rm -rf "+srcfile)
    os.system("cp -rf "+oldsrcfile+" "+srcfile)
    
    news("+++++++++++++++++++++++++++++++++++++++++++++++")
    news("+++++++++++++++++++++++++++++++++++++++++++++++")
    news("")
    news("--check weight column before recalculating--")
    news("")
    wt_before=visstat(vis=oldsrcfile,axis='weight')
    news("")
    news("")
    
    news("")
    news("--statwt--")
    news("")
    news("Use statwt to recalculate the WEIGHT & SIGMA columns:")
    news("Useful for early-stage JVLA data")
    news("")
    statwt(vis=srcfile,fitspw=statwt_fitspw)
    
    news("")
    news("--check weight column after recalculating--")
    news("")
    wt_after=visstat(vis=srcfile,axis='weight')
    news("")
    news("")
    news("+++++++++++++++++++++++++++++++++++++++++++++++")
    news("+++++++++++++++++++++++++++++++++++++++++++++++")

        
    ipl_statwt(oldsrcfile,srcfile)

def wtplt(msfile):
    plotms(msfile,xaxis='uvdist',yaxis='wt',
        coloraxis='field',showmajorgrid=True,
        plotfile=msfile+'.wt_uvdist.png',overwrite=True) 
    
    #    plotms(vis=oldsrcfile,xaxis='uvdist',yaxis='wt',
#        showmajorgrid=True,coloraxis='field',
#        plotfile=oldsrcfile+'.statwt.wt_uvdist.png',overwrite=True)
#else:
    
#    iplotxy(vis=oldsrcfile,xaxis='uvdist',yaxis='amp',
#        figfile=oldsrcfile+'.statwt.wt_uvdist.png',interactive=False,
#        title='Calibrated Visibility',ylabels='Amp',
#        selectplot=True,subplot=311,width='all')
#    iplotxy(vis=oldsrcfile,xaxis='uvdist',yaxis='weight',
#        figfile=oldsrcfile+'.statwt.wt_uvdist.png',interactive=False,
#        title='Before STATWT',ylabels='Weights',
#        selectplot=True,subplot=312)
#    iplotxy(vis=srcfile,xaxis='uvdist',yaxis='weight',
#        figfile=oldsrcfile+'.statwt.wt_uvdist.png',interactive=False,
#        title='After STATWT',ylabels='Weights',
#        selectplot=True,subplot=313)    
    