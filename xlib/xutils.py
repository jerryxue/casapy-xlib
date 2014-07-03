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
import pyfits

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


def sumwt(visfile='',
          restfreq='',
          oldstyle=False):
    #    
    #    calculate sum(weight) each channel for a sensitivity analysis 
    #
    c=3.0e5
    if  restfreq=='':
        restfreq=me.spectralline('HI')['m0']['value']
    news("")

    vsfile=open(visfile+'.sumwt.log','w')
    tb.open(visfile+'/SPECTRAL_WINDOW',nomodify=False)
    num_chan = np.min(tb.getcol('NUM_CHAN'))
    chan_freq=tb.getcol('CHAN_FREQ')
    tb.close()
    tb.open(visfile+'',nomodify=False)
    swt=tb.getcol('WEIGHT_SPECTRUM')
    flg=tb.getcol('FLAG')
    flg=1.0-flg
    swt=swt*flg
    tb.close()
    cwt=np.ma.sum(swt,axis=-1)
    cwt=np.ma.sum(cwt,axis=0)
    req_freq=chan_freq[:,0]
    v=c*(restfreq-req_freq)/restfreq
    news("   channel:       velocity : sum(weight)")
    for ic in range(0,len(v)):
        news(" "+'ch'+"{0:5.0f}".format(ic)+'   :   '+"{0:>10.2f}".format(v[ic])+'km/s   :   '+"{0:15.2f}".format(cwt[ic]))
        if  oldstyle==False:
            print >>vsfile,str(" "+''+"{0:5.0f}".format(ic)+'   '+"{0:>10.2f}".format(v[ic])+'   '+"{0:15.2f}".format(cwt[ic]))
        else:
            print >>vsfile,str(cwt[ic])
    # for ic in range(1,num_chan-3):
    #     #vs=ms.statistics(useflags=True,spw='*:'+str(ic),column='WEIGHT_SPECTRUM')
    #     vs=visstat(vis=visfile,axis='weight_spectrum',useflags=True,spw='*:'+str(ic))
    #     print "chan"+' '+str(ic)+' '+str(vs['WEIGHT_SPECTRUM']['sum'])
    #     print >>vsfile,str(vs['WEIGHT_SPECTRUM']['sum'])
    
    vsfile.close()

def importmir(mirfile='',
              vis='',
              telescope='CARMA',
              fieldname='',
              win_list='',
              line='',      # miriad/fits line parameter 
              nocal=False,  # line=velocity,$nmaps,$vfirst,$delv,$delv
              rm_noise=True,
              rm_auto=True,
              mirbin='',
              extenv={}):
    #
    #    import visbility data from a MIRIAD file into a CASA MS
    #
    if  mirbin=='':
        mirbin=os.environ['MIRBIN']+os.sep
    else:
        mirbin=mirbin+os.sep
    
    news("mirbin:")
    news(mirbin)
    
    cmd='uvlist options=spec vis='+mirfile+'>'+vis+'.uvlist.log'
    tmp=os.popen(mirbin+cmd).read()
    news(tmp,origin='miriad')
    news('run miriad-uvlist',origin='miriad')
    news(' ',origin='miriad')
    
    uvlist_dict = getuvlist(vis+'.uvlist.log')
    spw_list = range(1,len(uvlist_dict['number of channels'])+1)
    if  win_list=='':
        win_list=spw_list
    else:
        win_list=win_list.split(',')
        
    news('spectral windows list:')
    news(spw_list)
    news('spectral windows to be imported:')
    news(win_list)
    
    win_combine=[]
    
    opt=' op=uvout'
    if  line!='':
        opt=opt+' line='+line
        win_list=[0]
    if  nocal==True:
        opt=opt+' options=nocal'
    addsel=[]   
    if  rm_auto==True:
        addsel=addsel+["-auto"]
    if  rm_noise==True: 
        addsel=addsel+["-source(NOISE)"] 
    addsel=",".join(addsel)
    
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
        selectwin=""
        if  str(win_list[j])!='0':
            selectwin=",win("+str(win_list[j])+")"
        if  addsel+selectwin!='':
            selectvis=" select='"+addsel+selectwin+"'"
        cmd="fits in="+mirfile+" out="+fitspre+opt+selectvis
        
        os.system('rm -rf '+fitspre)
        news('',origin='miriad')
        news(cmd,origin='miriad')
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
    concat(vis=win_combine,concatvis=vis,respectname=False,\
           freqtol='',dirtol='',timesort=True)
    
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
    if  telescope=='SMA' or telescope=='sma' :
        prefix_ant='SMA'
        obsname='SMA'               
    
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
    
    
    tb.open(vis+"/SPECTRAL_WINDOW",nomodify=True)
    ref_freq=tb.getcol('REF_FREQUENCY')
    tb.close()
    tb.open(vis+"/SOURCE",nomodify=True)
    spw_id=tb.getcol('SPECTRAL_WINDOW_ID')
    spw_id_uni,spw_id_uni_index=np.unique(spw_id,return_index=True)
    rest_freq=tb.getcol('REST_FREQUENCY')
    rest_freq=rest_freq[0][spw_id_uni_index]
    tb.close()
    
    news("")
    news("Checking SPW starting velocity")
    news("")
    news("spw starting velocity [km/s] in MS:")
    for j in range(len(ref_freq)):
        chan_velo=sci_const.c*(rest_freq[j]-ref_freq[j])/rest_freq[j]/1000.
        news(" spw"+str(j)+": "+str(chan_velo))
    news("spw starting velocity [km/s] in MIRIAD/uvlist:")
    news("...rounded numbers...")
    for j in range(len(uvlist_dict['starting velocity'])):
        news(" spw"+str(j)+": "+str(uvlist_dict['starting velocity'][j]))
    news("note: starting frequency in the uvlist log is:")
    news("      the sky frequency (sfreq) from the first vis record")
    #+
    # UVFITS doesn't have a time-dependent sky freqency
    # importuvfits() recompute the rest frequency (time-independent if doppler track)
    # using this "starting or sky frequency" in UVFITS.
    #-
    news("")    
    
    news("")
    news("++")
    news(mirfile+'-->'+vis+' done!')
    news("++")
    news("")


def getuvlist(logname):
    #
    #    convert a uvlist log file from 
    #    <uvlist options=spec> to a python dict
    #
    uvlist_log = open(logname,'r')
    lines = uvlist_log.readlines()
    uvlist_log.close()
    nchan=0

    uvlist_dict={   'rest frequency':         [],
                    'starting channel':        [],
                    'number of channels':    [],
                    'starting frequency':    [],
                    'frequency interval':    [],
                    'starting velocity':    [],
                    'ending velocity':        [],
                    'velocity interval':    []  }
    
    keys=uvlist_dict.keys()
    for line in lines:
        line=line.lower()
        if  line.find(':')!=-1:
            [key, value]=line.split(':')
            values=value.split()            
            #values = map(float, values)
            for tmp in keys:
                if  key.find(tmp)!=-1:
                    uvlist_dict[tmp]=uvlist_dict[tmp]+values
        if  line.find('optical velocities')!=-1:
            break
            
    return uvlist_dict


def exporttasklog(taskname,logname,extralog=[]):
    #
    #   export task log to a plain text file
    #
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


def exportcasalog(blines,elines,logname):
    #
    #   export casapy log to a plain text file
    #
    task_log = open(logname,'w')
    for i in range(len(elines)):
        if i>=len(blines):
            task_log.write(elines[i])    
    task_log.close()


def emailsender(myemail,subject,maintext,attachs,\
                smtpserver='smtp.gmail.com',\
                eusrname='yourname@gmail.com',\
                epassword='yourpassword'):
    #
    #    send out a reduction log email
    #
    msg = MIMEMultipart()
    
    msg['From'] = eusrname
    if  eusername=='yourname@gmail.com':
        msg['From']=myemail
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

def getprefixlist(prefix):
    #
    #    Read the file name(s) from a plain textfile <prefix>.list
    #
    rawfiles_list=open(prefix+'.list','r')
    lines=rawfiles_list.readlines()
    rawfiles_list.close()
    rawfiles=[]
    for line in lines:
            line=line.strip()
            rawfiles.append(line)
    
    return rawfiles

def importmiriad(mirfile='',
                vis='',
                telescope='CARMA',
                extenv=''    ):
    #
    #    import visbility data from a miriad file into a CASA MS using CARMAFILLER (experimental)
    #
    
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
    

def cleanup(outname,tag=''):
    #
    #    cleanup imaging products
    #
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

def exportclean(outname,keepcasaimage=True):
    #
    #    export imaging products into fits files
    #
    version=['mask','cm','residual','model','cmodel',
            'psf','cpsf','image','sen',
            'flux.pbcoverage','flux.pbcoverage.thresh_mask',
            'flux','flux.thresh_mask',
            'flux.mask0']
    for i in range(0,len(version)):
        if  os.path.exists(outname+'.'+version[i]):
            exportfits(outname+'.'+version[i],
                       outname+'.'+version[i]+'.fits', 
                       velocity=True,
                       overwrite=True)
            if  keepcasaimage==False:
                os.system("rm -rf "+outname+'.'+version[i])



def checkbeam(outname,method='maximum'):
    #
    #    estimate the recommndated beam size
    #
    imhdlist=imhead(imagename=outname+'.image',mode='list')
    
    if  'perplanebeams' in imhdlist.keys():

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
    
    if  'beammajor' in imhdlist.keys():
        
        bmaj=imhdlist['beammajor']
        bmin=imhdlist['beamminor']
        bpa=imhdlist['beampa']
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

def resmoothpsf(outname):
    #
    #    calculate the "ultimate" psf when resmooth=True
    #
    os.system('rm -rf cpsf.tmp')
    os.system('cp -r '+outname+'.psf cpsf.tmp')
    
    imhead(imagename='cpsf.tmp',mode='add',hdkey='bunit',hdvalue='Jy/beam')
    
    ia.open(outname+'_d.image')
    rb=ia.restoringbeam()
    ia.close()
    ia.open('cpsf.tmp')
    for i in range(0,rb['nStokes']):
        for j in range(0,rb['nChannels']):
            ia.setrestoringbeam(beam=rb['beams']['*'+str(j)]['*'+str(i)],channel=j,polarization=i)
    rb2=ia.restoringbeam()
    ia.close()
    
    hdcim=imhead(outname+'.image',mode='list')
    imsmooth(imagename='cpsf.tmp',targetres=True,
            major=str(hdcim['beammajor']['value'])+hdcim['beammajor']['unit'],
            minor=str(hdcim['beamminor']['value'])+hdcim['beamminor']['unit'],
            pa=str(hdcim['beampa']['value'])+hdcim['beampa']['unit'],
            outfile=outname+'.cpsf',
            overwrite=True)
    os.system('rm -rf cpsf.tmp')
    
    # im2=ia.convolve2d(  outfile=outname+'.cpsf',
    #                     axes=[0,1],
    #                     type='gaussian',
    #                     targetres=True,
    #                     major=str(hdcim['beammajor']['value'])+hdcim['beammajor']['unit'],
    #                     minor=str(hdcim['beamminor']['value'])+hdcim['beamminor']['unit'],
    #                     pa=str(hdcim['beampa']['value'])+hdcim['beampa']['unit'],  
    #                     overwrite=true);

def checkpsf(outname):    
    #
    #    check the psf at diffrent planes (out of date!)
    #
    imhead(imagename=outname+'.psf',mode='put',hdkey='bunit',hdvalue='Jy/pixel')
    hd=imhead(outname+'.image',mode='list')
    psf_nx=hd['shape'][0]
    psf_ny=hd['shape'][1]
    psf_nz=hd['shape'][3]
    
    # get some info for the initial guessing
    if  'perplanebeams' in hd.keys():
        nchan=psf_nz
        psf_bmaj=np.arange(float(nchan))
        psf_bmin=np.arange(float(nchan))
        psf_bpa=np.arange(float(nchan))
        psf_size=np.arange(float(nchan))
        for i in range(0,nchan):
            psf_bmaj[i]=hd['perplanebeams']['*'+str(i)]['major']['value']
            psf_bmin[i]=hd['perplanebeams']['*'+str(i)]['minor']['value']
            psf_bpa[i]=hd['perplanebeams']['*'+str(i)]['positionangle']['value']
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
        news([psf_bmaj[index_median],psf_bmin[index_median],psf_bpa[index_median]])
        news([psf_bmaj[index_max],psf_bmin[index_max],psf_bpa[index_max]])
        news("")
        index_choice=index_max
        bmaj=psf_bmaj[index_choice]
        bmin=psf_bmin[index_choice]
        bpa=psf_bpa[index_choice]
    else:
        bmaj=hd['beammajor']['value']
        bpa=hd['beampa']['value']
        bmin=hd['beamminor']['value']
    
    
    psize=abs(hd['cdelt1']/(np.pi)*180.*60.*60.)
    
    # write a file with initial guessing
    estfile=open(outname+'.psf.imfit.est.log','w')
    print >>estfile,'1.0, '+\
            str(int(psf_nx/2))+', '+\
            str(int(psf_ny/2))+', '+\
            str(bmaj)+'arcsec, '+str(bmin)+'arcsec, '+str(bpa)+'deg, f'
            # str(bmaj)+'arcsec, '+str(bmin)+'arcsec, '+str(bpa)+'deg' # without peak fixed to 1Jy/pixel
    estfile.close()
    
    # setting fitbox
    imfit_box=  str(int(psf_nx/2-3*(bmaj/psize)))+','+\
                str(int(psf_ny/2-3*(bmaj/psize)))+','+\
                str(int(psf_nx/2+3*(bmaj/psize)))+','+\
                str(int(psf_ny/2+3*(bmaj/psize))) 
    print imfit_box
    imfit_log=imfit(imagename=outname+'.psf',
                    box=imfit_box,
                    logfile=outname+'.psf.imfit.log',
                    estimates=outname+'.psf.imfit.est.log')
                    #estimates='')
    
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
    news("fitted  channels:  %i " % psf_nchan)
    
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
    #
    #    search for unique baselines from the last PLOTMS locating log
    #
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

def news(msg,origin='++++++'):
    #
    #    print out information to casalog
    #
    msg=str(msg)
    casalog.origin(origin)
    casalog.post(msg)
    
    
def genmask0(imfile):    
    #
    #     produce a mask image with unmask values=1
    #
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
    

def mask0clean(outname,mask0):
    #
    #    mask a cube using a mask image 
    #    note: used as a trimmer for masking out x-y pixels with partial coverages   
    #
    version=['mask','cm','residual','model','cmodel',
            'psf','image','sen',
            'flux.pbcoverage','flux.pbcoverage.thresh_mask',
            'flux','flux.thresh_mask']
    for i in range(0,len(version)):
        if  os.path.exists(outname+'.'+version[i]):
            os.system('rm -rf '+outname+'.'+version[i]+'.tmp')
            immath(imagename=[outname+'.'+version[i],mask0],
                   expr='IM0*IM1',outfile=outname+'.'+version[i]+'.tmp')
            os.system('rm -rf '+outname+'.'+version[i])
            os.system('mv '+outname+'.'+version[i]+'.tmp '+outname+'.'+version[i])


def getuvrange(msfile):
    #
    #    inspect the uv sampling
    #
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


def uvspec(msfile,restfreq='1420405752.0Hz'):
    #
    #   shortcut for a miriad-like uvspec
    #
    plotms(msfile,xaxis='velocity',yaxis='amp',avgtime='999999s',
        avgscan=True,transform=True,restfreq=restfreq,
        xdatacolumn='corrected',ydatacolumn='corrected',
        coloraxis='spw')

def uvplt(msfile):
    #
    # shortcut for a miriad-like uvplt
    #
    plotms(msfile,xaxis='time',yaxis='amp',avgchannel='99999',
        xdatacolumn='corrected',ydatacolumn='corrected',
        coloraxis='field')


def modelconv(outname,mode=''):
    #
    #    calculate a convolved model
    #
    # use *.residual *.image to get cmodel
    os.system('rm -rf '+outname+'.cmodel')
    os.system('rm -rf '+outname+'.cmodel2')
    
    # mode=''
    if  mode=="":    
        immath(imagename=[outname+'.image',outname+'.residual'],
        expr='IM0-IM1',outfile=outname+'.cmodel')
    
    # mode='conv'
    if  mode=="test":
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

def copyweight(srcfile,
               copyback=False):
    # copyback=False copy weight to weight_spectrum
    # copyback=True  copy mean(weight_spectrum) to weight if weight_spectrum exists
    
    news("")
    news("--copyweight--")
    
    if  copyback==True:
        news("  mean(weight_spectrum)->weight")
        tb.open(srcfile,nomodify=False)
        wt=tb.getcol('WEIGHT')
        header_para=tb.colnames()
        wts_exist=tb.iscelldefined('WEIGHT_SPECTRUM',0)
        if  wts_exist==True:
            wts=tb.getcol('WEIGHT_SPECTRUM')
            flag=tb.getcol('FLAG')
            wtsc=np.ma.average(wts,axis=-2,weights=1.0-flag)*1.0
            tb.putcol('WEIGHT',wtsc)
            sigma=np.where(wtsc>0.0,wtsc**0.5,-1.0)
            sigma=1.0/sigma
            tb.putcol('SIGMA',sigma)
        else:
            news("no valid WEIGHT_SPECTRUM values")
        tb.close()
    else:
        news("  weight->weight_spectrum")
        tb.open(srcfile,nomodify=False)
        wts=tb.getcol('FLAG')*1.0
        wtt=tb.getcol('WEIGHT')
        for i in range(0,wtt.shape[0]):
            wts[i,:,:]=wtt[i,:]
        tb.putcol('WEIGHT_SPECTRUM',wts)
        tb.close()
        
    news("")
    
def checkchflag(msfile):
    #
    #    check flag consistancy in channel
    #    currently only handle the case with a single spw
    #    
    #    note: miriad/invert slop=1,zero could include
    #          partionally flagged records into imaging
    #          In CASA, we can unlflag and zero-out such data
    #          to have a similar treatment:
    #          http://www.atnf.csiro.au/computing/software/miriad/userguide/node144.html)
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

def unchflag(msfile):
    #
    #  cleanup flagging glitch near spw edges from mstransform() 
    #  this will make sure a consistant flagging and psf cross different
    #  channels (only use it when you believe mstransform flags more
    #  spw edge channels than it should do during spw regridding)
    #  It will have similar effects as miriad/invert slop=1,zero
    #
    tb.open(msfile,nomodify=False)
    flag=tb.getcol('FLAG')
    shape=flag.shape
    news(msfile+' '+str(shape))
    for i in range(0,shape[0]):
        for j in range(0,shape[-1]):
            flag0=np.sum(flag[i,:,j])
            if  flag0!=0 and flag0!=shape[-1]:
                flag[i,:,j]=False
    tb.putcol('FLAG',flag)
    tb.close()
    
def scalewt(srcfile,
            field='',
            uvrange='',
            fitspw='',
            datacolumn='corrected',
            minsamp=2,
            modify=False):
    #
    # statwt() modifies weight/sigma for each vis record using an emperical
    # noise estimation from the data itself.
    #
    # this function will only scale weight/sigma by a constant factor (derived by
    # comparing weight before&after statwt() results) for all records in a single track
    # This might be better than statwt() because:
    #    *  weights in the raw data are usually correct in the relative sense in a single track 
    #       (e.g. theoretical prediction using tsys+gain+int+freq etc.), just at 
    #       a wrong absolute scale (which is required when combing tracks).
    #    *  statwt() requires line-free data for noise evaluation. but still the vis "noise" will be
    #       amplified for the records with strong continuum emissions (see wt=1/sig^2.0 vs. uvdist from statwt results).
    #       In addition, statwt() could introduce small-scale weight value "noise" 
    #       for individual records if the statistical sampling selection is not well done.
    #
    # modify=False: WEIGHT/SIGMA is not touched, so you could run a test
    #               and check if the scaling factor is reasonable.
    # uvrange:      ideally, the uvrange doesn't show strong signal (either cont or line)
    #
    # 
    # BACKUP OLD WEIGHT & SIGMA & WEIGHT_SPECTRUM
    # 
    # clean will use WEIGHT rather than WEIGHT_SPECTRUM (as for r4.2.1)
    # 
    news("")
    news("--running scalewt from xutils--")
    news("")
    
    #    SAVE OLD WEIGHT/SIGMA/WEIGHT_SPECTRUM VALUES
    ms.open(srcfile,nomodify=True)
    tbwt_old=ms.getdata(['weight','sigma'])
    ms.close()
    tb.open(srcfile,nomodify=True)
    wts_exist=tb.iscelldefined('WEIGHT_SPECTRUM',0)
    if  wts_exist==True:
        tswt_old=tb.getcol('WEIGHT_SPECTRUM')
    tb.close()
    
    #####
    # NOTE (as for r4.2.1):
    #    visstat(axis='weight') doesn't use the FLAG column correctly
    #    we copy WEIGHT to WEIGHT_SPECTRUM for visstat calculations
    #    statwt doesn't really touch WEIGHT_SPECTRUM
    #####
    news("")
    news(">"*60)
    news(">"*60)
    news("")
    news("--check weight column before recalculating--")
    copyweight(srcfile)
    """
    stwt_old=visstat(vis=srcfile,
                     field=field,
                     axis='weight_spectrum',
                     uvrange=uvrange,
                     useflags=True,
                     spw='')
    """
    tb.open(srcfile,nomodify=True)
    swt_before=tb.getcol('WEIGHT_SPECTRUM')
    flg_before=tb.getcol('FLAG')
    flg_before=1.0-flg_before
    tb.close()
    news("Use statwt to recalculate the WEIGHT & SIGMA columns:")
    statwt(vis=srcfile,
           fitspw=fitspw,
           spw=fitspw,
           field=field,
           minsamp=minsamp,
           combine='',
           datacolumn=datacolumn,
           dorms=False)
    news("")
    news("--check weight column after recalculating--")
    copyweight(srcfile)
    """
    stwt_new=visstat(vis=srcfile,
                     field=field,
                     axis='weight_spectrum',
                     uvrange=uvrange,
                     useflags=True,
                     spw='')
    """
    tb.open(srcfile,nomodify=True)
    swt_after=tb.getcol('WEIGHT_SPECTRUM')
    flg_after=tb.getcol('FLAG')
    flg_after=1.0-flg_after
    tb.close()
    news("<"*60)
    news("<"*60)
    
    a=np.ravel(swt_before*flg_before)
    b=np.ravel(swt_after*flg_after)
    tag=np.where((a!=0) & (b!=0))[0]
    
    if  len(tag.flat)!=0: 
    
        a1=1./np.sqrt(a[tag])
        b1=1./np.sqrt(b[tag])
        a2=a[tag]
        b2=b[tag]
        
        news("")
        news("1/WEIGHT^0.5")
        news("Median,Min,Max (before): "+str([np.median(a1),np.min(a1),np.max(a1)]))
        news("Median,Min,Max (after) : "+str([np.median(b1),np.min(b1),np.max(b1)]))
        news("WEIGHT")
        news("Median,Min,Max (before): "+str([np.median(a2),np.min(a2),np.max(a2)]))
        news("Median,Min,Max (after) : "+str([np.median(b2),np.min(b2),np.max(b2)]))
        news("")
        
        plt.close()
        plt.ioff()
        
        plt.figure(figsize=(5,8))
        plt.subplot(2,1,1)
        plt.xlabel("1/wt$^{0.5}$ before")
        plt.ylabel("1/wt$^{0.5}$ after")
        H, xedges, yedges = np.histogram2d(a1, b1, bins=(40,40))
        H = np.rot90(H)
        H = np.flipud(H)
        Hmasked = np.ma.masked_where(H==0,H) 
        plt.axis([0, xedges.max(), 0, yedges.max()])
        plt.pcolormesh(xedges,yedges,Hmasked)
        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Counts')
        xrange=np.array([0, xedges.max()])
        plt.plot(xrange,xrange*(np.median(b1/a1)),label="sf="+str((1/np.median(b1/a1))**2.0))
        plt.legend()
        
        plt.subplot(2,1,2)
        plt.xlabel("wt before")
        plt.ylabel("wt after")
        H, xedges, yedges = np.histogram2d(a2, b2, bins=(40,40))
        H = np.rot90(H)
        H = np.flipud(H)
        Hmasked = np.ma.masked_where(H==0,H) 
        plt.axis([0, xedges.max(), 0, yedges.max()])
        plt.pcolormesh(xedges,yedges,Hmasked)
        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Counts')
        xrange=np.array([0, xedges.max()])
        plt.plot(xrange,xrange*(np.median(b2/a2)),label="sf="+str(np.median(b2/a2)))
        plt.legend()
        
        #plt.show()
        plt.savefig(srcfile+".scalewt.pdf")
        plt.close()
        news("")
        news("save scatter plot for the WEIGHT change to:")
        news(srcfile+".scalewt.pdf")
        news("")
        """
        print "weight scaling factor: "+str((1/np.median(b1/a1))**2.0)
        print "weight scaling factor: "+str(np.median(b2/a2))
        print ""
        """
        """
        medianwt_old=stwt_old['WEIGHT_SPECTRUM']['median']
        medianwt_new=stwt_new['WEIGHT_SPECTRUM']['median']
        sf=medianwt_new/medianwt_old
        """
        medianwt_old=np.median(a2)
        medianwt_new=np.median(b2)
        sf=np.median(b2/a2)
        news("")
        news("*"*60)
        news("median(wt) before statwt():  "+str(medianwt_old))
        news("median(wt) after  statwt():  "+str(medianwt_new))
        news("scaling factor:              "+str(sf))
        news("*"*60)
        news("based on fitspw :            "+str(fitspw))
        news("         minsamp:            "+str(minsamp))
        news("note: only correct if enough unflagged line-free channels left")
        news("      minsamp <= channel number in fitspw")
        news("*"*60)
        news("")
    
    else:
        
        sf=1.0
        news("")
        news("*"*60)
        news("no enough unflagged line-free channels left for statwt()")
        news("*"*60)
        news("based on fitspw :            "+str(fitspw))
        news("         minsamp:            "+str(minsamp))
        news("note: only correct if enough unflagged line-free channels left")
        news("      minsamp <= channel number in fitspw")
        news("*"*60)
        news("")
            
    # SCALE THE OLD WEIGHT/SIGMA & LOAD THE NEW VALUES
    if  modify==True:
        news("WEIGHT/SIGMA are modified")
        tbwt_old['weight']=tbwt_old['weight']*sf
        tswt_old=tswt_old*sf
        if  sf>0.0:
            tbwt_old['sigma']=tbwt_old['sigma']/(sf**0.5)
        if  sf==0.0:
            tbwt_old['sigma']=tbwt_old['sigma']*0.0-1.0
    else:
        news("WEIGHT/SIGMA are not modified")
    
    ms.open(srcfile,nomodify=False)
    tbwt_new=ms.getdata(['weight','sigma'])
    ms.putdata(tbwt_old)
    ms.close()
    tb.open(srcfile,nomodify=False)
    if  wts_exist==True:
        tb.putcol('WEIGHT_SPECTRUM',tswt_old)
    else:
        copyweight(srcfile)
    tb.close()
    
    if  len(tag.flat)!=0:
        news("")
        news("add table keyword WEIGHT_SCALING="+str(sf)+" to "+srcfile)
        news("")
        tb.open(srcfile,nomodify=False)
        tb.putkeyword('WEIGHT_SCALING',sf)
        tb.close()
    
    return sf

def xmoments(imagename,
               smfac=[3.0,3.0],
               th=3.0,
               errfile='',
               box='',
               chans='',
               region=''):
    #
    #    a function which will replace the idl-moments
    #    currely only "smooth-masking" is implemented
    #
    #    imagename: root name of clean products
    #    
    if  errfile=='':
        errfile=imagename+'.flux'
    
    if  type(smfac)!=type([]):
        smfac=[smfac,0]
    
    
    hd=imhead(imagename+'.image',mode='list')
    ia.open(imagename+'.image') 
    sm2d=ia.convolve2d(outfile='__sm2d',axes=[0,1],
                  type='gaussian',
                  targetres=True,
                  major=str(hd['beammajor']['value']*smfac[0])+hd['beammajor']['unit'],
                  minor=str(hd['beamminor']['value']*smfac[0])+hd['beamminor']['unit'],
                  pa=str(hd['beampa']['value'])+hd['beampa']['unit'],  
                  overwrite=True)
    sm2d.done()
    ia.close()
    sfile='__sm2d'
    
    if  smfac[1]!=0.0:
        ia.open('__sm2d')
        sm3d=ia.sepconvolve(outfile='__sm3d',axes=[0,1,3],
                       types=['gaussian']*3,
                       widths=[1,1,smfac[1]],stretch=True,overwrite=True)
        sm3d.done()
        ia.close()
        sfile='__sm3d'
    
    exportfits(imagename=sfile,fitsimage='test.fits',velocity=True,overwrite=True)
    stat=imstat(imagename=sfile,box=box,chans=chans,axes=[0,1],region=region)
    sigma=np.median(stat['sigma'])
    
    os.system("rm -rf "+imagename+'.cm_masked')
    os.system("rm -rf "+imagename+'.cm.moms*')
    immath(imagename=[imagename+'.cm',sfile],
           expr="iif(IM1>="+str(th*sigma)+",IM0,0.0)",
           outfile=imagename+'.cm_masked')
    os.system("rm -rf __sm3d __sm2d")
    
    immoments(imagename+'.cm_masked',
              axis="spec",
              moments=[0],
              outfile=imagename+'.cm.moms0')
    
    immoments(imagename+'.cm_masked',
              axis="spec",
              moments=[1],
              outfile=imagename+'.cm.moms1')
    
def getevladata(url,user='',password='',extenv={}):
    #
    #    a shortcut to download VLA data
    #
    cmd="wget -r -w 2 -nH -c --cut-dirs=2 --no-check-certificate --user="+\
        user+" --password="+password+" -e robots=off "+url
    
    p=subprocess.Popen(cmd,shell=True,env=extenv,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline,''):
        news(line,origin='wget')



def findoutliers(data,
                 m=2.,
                 range=[-1,-1]):
    # find outliers in the data
    # *  clip in a range
    # *  median filtering.
    if  range!=[-1,-1]:
        outliers=np.logical_or(data<range[0],data>range[1])
    else:
        outliers=(data!=data)
    inrange=(np.where(outliers==False))[0]
    if  inrange.size!=0:
        subdata=data[inrange]
        med=np.median(subdata)
        d=np.abs(subdata-med)
        mdev=np.median(d)
        s=d/mdev if mdev else 0
        news("median,medabsdevmed,threshold:"+str([med,mdev,m]))
        flag=np.where(s>m)[0]
        if  flag.size!=0:
            outliers[inrange[flag]]=True
    news("outliers percent: "+str(np.mean(outliers)*100.0)+" %")
    return outliers


def flagtsys(caltable='',
            tsysrange=[5.0,1000.0]):
    #
    # flag bad tsys records in the swpow caltable.
    #
    news("")
    news("--flagtsys--")
    news("")
    news("Flag bad TSYS")
    news("caltable:  "+str(caltable))
    news("tsysrange: "+str(tsysrange))
    
    # READ FLAG/SPW/ANTENA/TSYS/SWPOW
    tb.open(caltable,nomodify=False)
    var=tb.getcol('FPARAM')
    flag=tb.getcol('FLAG')
    spwids=tb.getcol('SPECTRAL_WINDOW_ID')
    spwid=np.unique(spwids)
    antids=tb.getcol('ANTENNA1')
    antid=np.unique(antids)
    
    for ant in antid:
        for spw in spwid:
            list=np.where(np.logical_and(spwids==spw,antids==ant))[0]
            nc=var.shape[0]/2
            for pick in range(nc):
                news("antenna,spw,corr"+str([ant,spw,pick]))
                tsys=var[pick*2+1,0,list]
                tag=np.where(findoutliers(tsys,m=10,range=tsysrange)==True)
                flag[:,:,list[tag]]=True
                
    tb.putcol('FLAG',flag)
    tb.close

    news("")
    
def xplotcal(tbfile,iterant=False,
             amprange=[],pharange=[],
             tsysrange=[],spgrange=[],
             extenv=''):

    news("")
    news("--xplotcal--")
    news("")
    news("Plot Gain Tables")
    
    tb.open(tbfile)
    tbtype=tb.getkeyword('VisCal')
    tb.close()
    
    
    if  tbtype=='B Jones' or \
        tbtype=='G Jones' or \
        tbtype=='G EVLASWPOW' :
        if  amprange=='':
            if  tbtype=='B Jones':
                amprange=[-1,-1,0.2,1.4]
            if  tbtype=='G Jones':
                amprange=[-1,-1,-1,-1]
        if  pharange=='':
            if  tbtype=='B Jones':
                pharange=[-1,-1,-20,20]
            if  tbtype=='G Jones':
                pharange=[-1,-1,-180,180]
        if  tsysrange==[]:
            if  tbtype=='G EVLASWPOW':
                tsysrange=[]
        if  spgrange==[]:
            if  tbtype=='G EVLASWPOW':
                spgrange=[]
        
        tb.open(tbfile+'/ANTENNA')
        ant_name=tb.getcol('NAME')
        ant_stat=tb.getcol('STATION')
        ant_code=range(0,len(tb.getcol('NAME')))
        tb.close()
        
        tb.open(tbfile)
        spw_name=np.unique(tb.getcol('SPECTRAL_WINDOW_ID'))
        spw_name=sorted(list(set(spw_name)))
        spw_name=[str(i) for i in spw_name]
        tb.close()
        
        news("")
        news("Antenna Name:   "+str(ant_name))
        news("SPW     Name:   "+str(spw_name))
        news("")
        
        if  iterant==False:
            ant_name=['']
            ant_stat=['all']
            ant_code=['all']
        
        merge_pdf='gs -sDEVICE=pdfwrite -sOutputFile='+tbfile+'.antall.pdf'
        merge_pdf=merge_pdf+' -dNOPAUSE -dBATCH'
        all_pdf=''
        
        for i in range(0,len(ant_name)):
            one_pdf=tbfile+'.ant'+str(ant_code[i])+'.pdf'
            if  len(ant_name)==1:
                one_pdf=tbfile+'.ant'+str(ant_code[i])+'.png'
            ant_str='Ant'+str(ant_code[i])+'/'+ant_name[i]+'/'+ant_stat[i]
            if  iterant==False:
                ant_str='All Ants'
            for j in range(0,len(spw_name)):
                for k in range(0,2):
                    figfile_loop=['','']
                    if  j==len(spw_name)-1 and k==1:
                        figfile_loop[1]=one_pdf
                    if  tbtype=='G Jones' or tbtype=='B Jones':
                        yaxis_loop=['amp','phase']
                        plotrange_loop=[amprange,pharange]
                    if  tbtype=='G EVLASWPOW':
                        yaxis_loop=['tsys','spgain']
                        plotrange_loop=[tsysrange,spgrange]
                    plotcal(caltable=tbfile,
                        antenna=ant_name[i],
                        field='',
                        plotsymbol='o',
                        plotcolor='blue',
                        markersize=5.0,
                        fontsize=10.0,
                        showgui = False,
                        spw=spw_name[j],
                        plotrange=plotrange_loop[k],
                        subplot=2*100+len(spw_name)*10+1+j+k*len(spw_name),
                        yaxis=yaxis_loop[k],
                        figfile=figfile_loop[k])
                    if  k==0:
                        subtitle='Solution: '+ant_str+' SpwID '+str(spw_name[j])
                        plt.title(subtitle,fontsize=10)
            merge_pdf=merge_pdf+' '+one_pdf
            all_pdf=all_pdf+' '+one_pdf
            
        if  iterant==True:
            p=subprocess.Popen(merge_pdf,shell=True,env=extenv,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = p.stdout.read()
            os.system('rm '+all_pdf)
    
    else:
        news("not supported .scal table")


def checkvrange(srcfile='',
                outframe='',
                restfreq=''):
    #
    #    check the velocity coverage of a spectral line observation
    #
    """
    me.list()
    me.spectralline('CO_1_0')['m0']['value']
    me.spectralline('HI')['m0']['value']
    examples:
        srcfile='n3147bc04.ms'
        outframe='LSRK'
        restfreq=me.spectralline('HI')['m0']['value']
        start='2515.0km/s'
        width='20.8km/s'
        nchan=26
        field=2
    with limited functions (no frame conversion)
    """
    c=3e5
    if  restfreq=='':
        restfreq=me.spectralline('HI')['m0']['value']
    news("")
    tb.open(srcfile+'/SPECTRAL_WINDOW')
    news("available range (Hz) in orginal frame:")
    chan_freq=tb.getcol('CHAN_FREQ')
    header_para=tb.colnames()
    if 'MEAS_FREQ_REF' in header_para:
        frame=tb.getcol('MEAS_FREQ_REF')
        spwids=range(0,len(tb.getcol('MEAS_FREQ_REF')))
    else:  
        spwids=0
    
    chan_del_freq=np.average(np.abs(chan_freq[0]-chan_freq[1]))
    chan_low_freq=np.min(chan_freq)-chan_del_freq/2.0
    chan_hig_freq=np.max(chan_freq)+chan_del_freq/2.0
    news([chan_low_freq,chan_del_freq,chan_hig_freq])
    v=c*(restfreq-np.array([np.max(chan_freq),np.min(chan_freq)]))/restfreq
    news(v)
    
    ms.open(srcfile)
    for spwid in spwids:
        req_freq=chan_freq[:,spwid]
        v=c*(restfreq-req_freq)/restfreq
        news(['spwid: '+str(spwid),'frame: '+str(frame[spwid]),np.min(np.sort(v)),np.max(np.sort(v)),np.abs(v[0]-v[1])])
    ms.close()
    
    tb.close()
    
    news("0 REST 1 LSRK2 LSRD 3 BARY 4 GEO 5 TOPO 6 GALACTO 7 LGROUP")
    news("")

def bpcopy(table,
           reference='0',
           transfer='1',
           replace=False):
    ###
    #    transfer bandpass from one spw to another spw
    #    note: different from spwmap+frequency-wise interpolation across spws
    #
    #    bpcopy will not performe if:
    #    * reference and transfer (target) spw are the same
    #    * transfer (target) spw bandpass already exists
    #
    #    replace=False: results will be saved in table"_bpcopy"
    #
    # example:
    #    reference='0,0'
    #    transfer='1,2'
    #    use the bandpass from spw=0 to spw=1,2
    #
    #   table='n5371hi.bcal'
    #   reference='1,1'
    #   transfer='2,2'
    #   xu.bpcopy(table,reference=reference,transfer=transfer,replace=True)
    #
    ###
    idr=reference.split(',')
    idt=transfer.split(',')

    if  replace==False:
        
        os.system("rm -rf "+table+"_bpcopy")
        os.system("cp -rf "+table+" "+table+"_bpcopy")
        table=table+"_bpcopy"
        
    for k in range(len(idr)):

        os.system("rm -rf tmp.bcal")
        
        tb.open(table,nomodify=False)
        subtb=tb.query('SPECTRAL_WINDOW_ID=='+str(idr[k]))
        subtb1=tb.query('SPECTRAL_WINDOW_ID=='+str(idt[k]))
        docopy=(subtb1.nrows()==0 and subtb.nrows()!=0)
        news(" reference: "+str(idr[k])+" transfer: "+str(idt[k])+" copy: "+str(docopy))
        if  docopy:
            copytb=subtb.copy('tmp.bcal',deep=True,valuecopy=True,memorytable=True,returnobject=True)
        subtb.close()
        subtb1.close()
        tb.close()
        if  docopy:
            spws=copytb.getcol("SPECTRAL_WINDOW_ID").tolist()
            for i in range(len(spws)):
                spws[i]=int(idt[k])
            copytb.putcol("SPECTRAL_WINDOW_ID",spws)
            copytb.copyrows(table)
            copytb.close()
            
        os.system("rm -rf tmp.bcal")
    