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
#   INPUT KEYWORD [ OPTIONAL | DEFAULT VALUE ]
#
#       prefix|'test'       Name of the Measurment Set
#       prefix_comb|[]      Names of MS files to be combined 
#
#       source|''           source name
#       spw_source|''       spectral windows for source
#
#       uvcs|False          True: the script will perform UVCONTSUB 
#       uvcs_combine|'spw'  data axes to combine for the continuum estimate.
#                           example: combine='spw' --> form spw-merged continuum estimate
#                           This may have significant impacts for tracks taken with 
#                           multiple spws.
#       fitspw|''           spectral window-channel selection for line-free channels
#                           used in UVCONTSUB.
#       fitorder|0          polynomial order for fitting the continuum in UVCONTSUB
#                           high-order polynomial may work better of the continuum source
#                           is off-center (Sault 1994)

#   HISTORY
#
#       20110916    RX  minor fixing for v3.3
#       20130910    RX  use global dict variable <xp> to wrap pipeline parameters
#
#   AUTHOR
#
#       Rui Xue, Univeristy of Illinois
#########################################################################################

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

    xu.news("")
    xu.news("--mstransform--")
    xu.news("")
    xu.news(" Use mstransform() to:")
    xu.news(" * extract the source data")
    xu.news(" * [spectral regridding]")
    xu.news(" * [hanning smoothing]")
    xu.news("")
    
    xp['msfile']=xp['prefix']+'.ms' 
    xp['srcfile']=xp['prefix']+'.src.ms'
    os.system('rm -rf '+xp['srcfile'])

    if  xp['spwrgd']!='spw':
        if  xp['spwrgd']=='':
            spwrgd=False
        if  xp['spwrgd']=='frame':
            spwrgd=True
        mstransform(vis=xp['msfile'],
                    outputvis=xp['srcfile'],
                    createmms=False,
                    separationaxis='both',
                    field=xp['source'],
                    spw='',
                    useweights='flags',
                    datacolumn= "corrected",
                    regridms=spwrgd,
                    combinespws=False,
                    mode='channel',
                    nchan=-1,
                    start=0,
                    width=1,
                    nspw=1,
                    interpolation='linear',
                    outframe=xp['outframe'],
                    restfreq=xp['restfreq'],
                    hanning=xp['hs'])
    else:
        mstransform(vis=xp['msfile'],
                    outputvis=xp['srcfile'],
                    createmms=False,
                    separationaxis='both',
                    field=xp['source'],
                    spw='',
                    useweights='spectrum',
                    datacolumn= "corrected",
                    regridms=True,
                    combinespws=True,
                    mode=xp['cleanmode'],
                    nchan=xp['clean_nchan'],
                    start=xp['clean_start'],
                    width=xp['clean_width'],
                    nspw=0,
                    interpolation=xp['spinterpmode'],
                    outframe=xp['outframe'],
                    restfreq=xp['restfreq'],
                    phasecenter=xp['phasecenter'],
                    hanning=xp['hs'])
    
    xu.news("")
    xu.news("--check split--")
    xu.news("")
    listobs(xp['srcfile'])

    if  xp['wtstat']==True:
        
        #   StatWt: Recalculate the WEIGHT & SIGMA columns
        
        xu.news("+++++++++++++++++++++++++++++++++++++++++++++++")
        xu.news("+++++++++++++++++++++++++++++++++++++++++++++++")
        xu.news("")
        xu.news("--check weight column before recalculating--")
        xu.news("")
        visstat(vis=xp['srcfile'],axis='weight')
        xu.exporttasklog('visstat',xp['srcfile']+'.before-statwt.log',
                         ['\n',"Visibility weight BEFORE recalculation.",'\n','\n'])
        xu.news("")
        xu.news("")
        
        xu.news("")
        xu.news("--statwt--")
        xu.news("")
        xu.news("Use statwt to recalculate the WEIGHT & SIGMA columns:")
        xu.news("Useful for early-stage JVLA data")
        xu.news("")
        statwt(vis=xp['srcfile'],
               fitspw=xp['wtstat_fitspw'])

        xu.news("")
        xu.news("--check weight column after recalculating--")
        xu.news("")
        visstat(vis=xp['srcfile'],axis='weight')
        xu.exporttasklog('visstat',xp['srcfile']+'.after-statwt.log',
                         ['\n',"Visibility weight AFTER recalculation.",'\n','\n'])
        xu.news("")
        xu.news("")
        xu.news("+++++++++++++++++++++++++++++++++++++++++++++++")
        xu.news("+++++++++++++++++++++++++++++++++++++++++++++++")
    
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
            delmod(vis=xp['srcfile_comb'][i],otf=True,scr=False)
        #    tb.open(xp['srcfile_comb'][i]+'/SPECTRAL_WINDOW')
        #    mincw=[mincw]+tb.getcol('CHAN_WIDTH')
        #    tb.close()
        #    mincw=np.min(mincw)
        
        os.system('rm -rf '+xp['srcfile']+loop)
        
        #freqtol=str(mincw/1.e6/4.)+'MHz'
        if  xp['freqtol']!='':
            freqtol=xp['freqtol']
        if  xp['usevconcat']==False:
            concat(vis=xp['srcfile_comb'],
                   concatvis=xp['srcfile']+loop,
                   freqtol='',
                   dirtol='1.arcsec',
                   timesort=False,
                   visweightscale=xp['wtscale'],
                   copypointing=True)
        else:
            virtualconcat(vis=xp['srcfile_comb'],
                   concatvis=xp['srcfile']+loop,
                   freqtol='',
                   dirtol='1.arcsec',
                   visweightscale=xp['wtscale'],
                   keepcopy=False,
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

