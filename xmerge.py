#########################################################################################
#
#   Script Name - IMERGE
#
#   Author
#
#       Rui Xue, Univeristy of Illinois
#
#   PURPOSE
#
#       Prepare Calibrated data for Imaging
#
#   INPUT FILE
#       
#       Mesaurement Set:    <prefix>.src.ms,
#                           -- calibrated source data in the "data" column
#       for combination     <prefix1>.src.ms, 
#                           <prefix2>.src.ms,
#                           etc..
#   OUTPUT FILE
#       Measurement Set:    <prefix>.src.ms
#                           -- spectral line vis in the "corrected" column
#                           <prefix>.src.ms.cont
#                           -- continuum vis in the "data" column
#                           <prefix_combine>.src.ms
#                           -- combined vis
#                           <prefix_combine>.src.ms.cont
#                           -- combined cont vis
#                           Note: CLEAN will only work on the 'corrected' column,
#                                 and also modify the 'model' column.
#                                 be careful of the underhood changing
#
#       Figures:            <prefix>.plotxy.sou.amp.aftersub.<plotformat>
#                           <prefix>.plotxy.sou.velo_amp.aftersub.<plotformat>
#                           <prefix>.plotxy.sou.uvdist_amp.aftercomb.<plotformat>
#
#       FITS:               <prefix>.clean[.uvline][.imline].im.fits
#                           <prefix>.clean[.uvcont][.imcont].im.fits
#                                                          *.no.fits
#                                                          *.flux.fits
#                                                          *.res.fits
#                           <prefix>.cleanmfs[.uvcont].fits
#
#   INPUT KEYWORD [ OPTIONAL | DEFAULT VALUE ]
#
#       script_home:        path of the script repository
#       prefix:             Name of the Measurment Set
#       [prefix_combine]:   perfix tags of the MS files to be combined 
#                           if it is setted, <combine> will be changed to True
#
#       [source]:           Source Name (only for single-track imaging)
#       [spw_source]:       Spectral Windows for Source (only for single-track imaging)
#
#       [noplot|False]:     True: Don't produce any plots
#       [cleanonly|False]   this mode will help you tune clean without starting from
#                           concat or continuum substraction
#       
#       ---- Continuum Substraction ----
#
#       [uvcs|True]:        True: the script will perform UVCONTSUB 
#                           Note: for multi-track imaging, it is still required.
#       [uvcs_combine|'spw']:
#                           Data axes to combine for the continuum estimate.
#                           example: combine='spw' --> form spw-merged continuum estimate
#                           This may have significant impacts for tracks taken with 
#                           multiple spws.
#       fit_spw:            Spectral window-channel selection for fitting continuum
#                           in UVCONTSUB.
#       fit_order:          Polynomial order for fitting the continuum in UVCONTSUB
#                           High-order polynomial may work better of the continuum source
#                           is off-center (Sault 1994)
#       
#       [imcs|False]:       True: the script will perform IMCONTSUB. 
#                           You may do IMCONTSUB even after UVCONTSUB2.
#                           Note: for multi-track imaging, it is still required.
#       fit_chans:          Image cube channel selection for fitting the continuum in 
#                           IMCONTSUB (e.g.: fit_chans  = '1~7;79~85').
#       [fit_order_imcs|fit_order]: 
#                           Polynomial order for fitting the continuum in IMCONTSUB
#
#       NOTE:   
#           - the CONTSUB methords (imcs or uvcs) should be identical for all tracks
#   
#       ---- Imaging xy Setting ----
#       [im_size|400]:      Imaging size (numbers of pixels)
#       [cell_size|'4.0arcsec']:    
#                           Imaging pixel size.
#                           Note:   the default value of <cell_size> may be too large 
#                                   for the VLA-B array
#       [clean_mask|[0,0,im_size-1,im_size-1]]:  
#
#                           if True: using minpb to set the cleaning box
#
#                           Region to be cleaned  
#                           It can be the coordinates of the BL/TR corner pixel of the
#                           box, or a string pointing to the name of a cleanbox file
#                           see help->clean
#
#       [imstat_box_spec|]: Box for the <sig> calculation default: inner quarters
#       [imstat_box_cont|]: Box for the <sig> calculation default: four corners
#
#       [imstat_chan|'0,1,num_chan-2,num_chan-1']      
#                           Channels for the <sig> calculation
#
#       [imstat_rg_spec|'']     region for the <sig> calculation
#       [imatst_rg_cont|'']     region for the <sig> calculation
#
#       [sigcutoff_spec|2.5]    <sigcutoff_spec>*<sig> is the default threshold value for
#                               Spectral Cube CLEAN 
#                               <sig> is calculated from the dirty cube using line-free 
#                               channels&region.
#       [sigcutoff_cont|2.5]    <sigcutoff_cont>*<sig> is the default threshold value for
#                               continuum MSF CLEAN 
#                               <sig> is calculated from the dirty image using line-free 
#                               region
#
#       -- Imaging z Setting --
#       clean_mode:         "channel" or "velocity"
#       clean_start:        First channel/velocity to clean
#       clean_nchan:        Number of planes in the output image
#       clean_width:        Number of input channels to average 
#                           or the velocity width for each image plane
#       [rest_freq|'1420405752.0Hz']    
#                           rest freqency for imaging. The restfreq info may be missing 
#                           in CASA ms files during importing or concatenation. Resetting 
#                           rest_freq may fix it.
#       [out_frame|'BARY']  Frame of the output image
#       [spinterpmode|'linear'] 
#                           spectral gridding interpolation mode in CLEAN                         
#
#       ---- Clean Setting ----
#       [phase_center|'']   phasecenter for clean 
#                           The syntax should be 'J2000 12h18m49.6 14d24m59.01'
#                           Or you may use the fieldid number: e.g. '2'
#
#       [threshold_spec|<sigcutoff_spec>*<sig>/ units-mJy]:  
#                           Threshold for spec cleaning. <sig> from dirty CLEAN
#       [threshold_cont|<sigcutoff_cont>*<sig>/ units-mJy]:  
#                           Threshold for mfs cleaning. <sig> from dirty CLEAN
#
#       [n_iter|20000]      iteration threshold for clean
#       [imager_mode| 'csclean'(if combine==False) / 'mosaic'(if combine==True) ]
#                           imagermode for clean, options include: 'csclean', 'mosaic', 
#                           ''. 'mosaic' must be be used if your science target is in 
#                           multiple fields or it's heterogeneous-array observation.
#                           'csclean' for single point+homogeneous array data. 
#       [ft_machine|'ft']   Options: 'mosaic' or 'ft'
#                           ft_machine controls how clean produces the mosaic 
#                           (cookbook $5.3.15). 
#                           For ftmachine='ft', clean will perform a weighted combination 
#                           of the images produced by transforming each mosaic pointing 
#                           separately. This may be slow if we are really doing "MOSAIC" 
#                           (e.g. CARMA STING), as the individual sub-images must be 
#                           recombined in the image plane. But it is preferred for data 
#                           taken with sub-optimal mosaic sampling (e.g. fields too far 
#                           apart, on a irregular pattern, etc.)
#                           The VLA HI tracl combination is more like the SECOND CASE.
#                           CAUSTION!!!!: 
#                               ftmachine='mosaic' may be buggy for track combination 
#                               right now. For CARMA, you must always use 
#                               ftmachine='mosaic', because it is a heterogeneous array.
#       [cleanweight|'briggs']  
#                           default: briggs, robust=0.5
#                           Other options: 'briggs', 'uniform' or 'natural'
#       [wrobust|0.5]       briggs robust weight R parameter
#       [outer_taper|[]]    taper function for weighting
#       [multi_scale|[]]    Using multi-scale clean is not the default setting
#                           CAUSTION: multi_scale is under development in CASA.
#                           multi_scale=[0,1,3,10,30] is recommened, and units is pixel
#       [clean_gain|0.1]    gain factor for clean, 
#                           for multi-scale clean, clean_gain=0.7 is recommended
#
#       -- Restore Setting --
#       [restor_beam|['']]  force a restor beam for imaging
#                           default values are calculated from IMFIT of the psf
#                           at the first image plane
#       [min_pb|0.25]        cutoff for pb correction
#       [gride_mode|'aprojection']
#
#       [cleancont|True]    True: MFS Imaging for the continuum data
#       [cleanspec|True]    True: Channel by channel imaging for the spectral line data
#       [mweight]           True: mosweight=True to better deal with few fields+ different
#                                 nosie level case in the archival data
#       [spwrgd|True]      True: regrid frame. set it True if multiple frames 
#                                 in one MS file.
#                                 otherwise, CLEAN will fail
#       [hs|False]:         Hanning smoothing
#
#   HISTORY
#
#       Adapted from the NGC2403 tutorial scripts in the online CASA Trainning Materials
#           http://casa.nrao.edu/Tutorial/20081007/
#           http://casa.nrao.edu/casatraining.shtml
#
#       20090213    RX  track combination added as an option
#       20090213    RX  dirtymap processing as an option
#       20090512    RX  add options for continuum substraction in uv/image domain
#       20100130    RX  add rest_freq to reset the rest frequency if it is missing.
#       20100228    RX  multiscale clean was added
#       20100305    RX  clean_spw added. 
#       20100309    RX  imhead and imstat results are exported into log files
#       20100504    RX  add amp vs. velocity plot after contsub
#                       the sequence of the spwids in spw_source won't affect the
#                       channel mode clean now. The script will make the best choice
#                       automatically in the "channel" model clean.
#       20100611    RX  default outframe for clean and velo-amp plotting has been changed 
#                       to 'BARY'. Be careful of the "topo" case.
#       20100901    RX  noise, residual, and noise-normilized cubes will be produced
#                       CLEAN iteration log will be exported to prefix.clean.iteration.log                      
#       20101101    RX  source SPLIT and HANNINGSMOOTH moved to step2
#                       robust moment map derivations are moved to step3
#                       sophisticated algorithms are available.                 
#       20101129    RX  ensure it working in casa3.1
#       20110528    RX  ensure it working in casa3.2
#                       imcs now works in the dirty map
#       20110528    RX  first step of modulizations: define the function exportlog in
#                       libreduc.py
#       20110617    RX  uvcontsub2 used; ms file naming convention changed
#                       spw_source will not be kept in step2 source vis splitting
#                       for the version > 20110617. So source spw will be reset to
#                       0,1,2. The change was caused by the difficulty of clean/cvel
#                       regridding on vis with different frames. Even calibrators in
#                       different frames were removed, the spw strcutures were still 
#                       in the vis file.
#                       Currently, imcontsub has a bug... submitted to the helpdesk
#                       add <uvcs_combine>
#                       add email notification function
#       20110916    RX  minor fixing for v3.3
#       20111005    RX  when combining tracks, cvel now will regrid MS to the same 
#                       frame set for CLEAN psf exportfits added
#                       hanning smoothing (hs) was moved from step2 to step3, implemented
#                       in cvel
#
#
#   REDUCTION FLOW
#   
#       (1) Continuum subtraction in the UV domain [ Or perform merging ]
#       (2) [Image dirty maps & Determine the rms from line-free edge channels]
#       (3) Image spectral cube
#       (4) Image continuum 
#       (5) [Continuum subtraction in the image domain]
#       (6) Statistics on cleaned image cube 
#
#   NOTES:
#       (1) the source spwids may change during combination.
#           the spwid sequence can affect the result from the channel mode CLEAN
#           After 20100504, spwid will be perserved after source/calibrator splitting.
#           The sequence of spwid in the channel mode clean will be automatically 
#           detrmined by the script.
#       (2) if there are two spectral windows with different channel numbers or 
#           polarization settings, then the channel gridding and averaging modules in 
#           CLEAN will not work. In such case, one may try FEATHER in data combination.
#       (3) the rms calculation may not produce the real values if UVCS is 
#           not performed and there are strong continuum sources in the imstate region of 
#           the dirty map. Then the wrong value will affect the thereohold setting 
#           in the final tuned clean.
#           A correct therehold value should be set via threshold_value, and an
#           image domain continuum substraction can be followed.
#       (4) bad patterns in edge image planes may indicate wrong contsub,
#           because the uneven rms there break down CLEAN (which has the same threshold 
#           at differnet planes)
#       (5) adjusting robust parameter is necessary for the STING VLA-HI work because 
#           individual tracks are not configed to optimze combinations.
#           or the observations are not designed to produce white noise in combined cube.
#       (6) use the low-resolution | high senstivity map to identify line-free
#           velocity range; use PLOTMS to identify the channel range according to
#           the line-free velocity range.
#           CHOOSE the narrowest "commom" velocity range when combing different tracks
#           before combination; MAKE SURE the contsub for individual track is okay.
#       (7) for order=1 contsub, you'd better choose line-free channles 
#           as many as possible; it will reduce the uncertainties in CONTSUB
#       (8) <clean_gain> can be increased if you're using multisale clean
#       (9) threshold values can be estimated from Viewer using the polygon drawing
#           tools
#       (10) imstat_rg_spec/cont can be useful for an acuurate threshold value
#            estimation.
#       (11) check if the clean converged succesfully
#       (12) mosweight=True to adjust weighting of each pointing via per baseline bais
#       (13) <multi_scale> is supposed to set to the typical length scales for your clean
#            structures. 0 means point source. 
#            Warning: If you set the largest scale in <multi_scale> unresaonablly large,
#            you may see some extend artificial strcutures because msc could found some 
#            wrong extended components.
#       (14) casa 3.2.1 can't regrid one ms file containing data in multiple frames.
#            what one can do is regridding in files with only one frames, and then 
#            combining them. Note: clean can be fed with multiple ms files in 3.2.1 now
#       (15) in 3.2.1, you have to set your channel width >= intrinsic channel width
#            to ensure "safe" regrdding
#       (16) the fits image from casa now use the new wcslib convention. 
#            so some keyword in the fits header may be not recognized by MIRIAD or KVIS
#       (17) cvel become default
#
#   Template for different clean mode:
#
#       "deep" cleaning
#           clean_mode = 'velocity'
#           clean_start='296km/s'
#           clean_nchan=120
#           clean_width='1.3km/s'
#
#       "dirty" testing 
#           (it actually will break the script. but the dirty maps wil stil be generated)
#           clean_mode = 'channel'
#           clean_nchan=-1
#           clean_width=1
#           clean_start=''
#           n_iter=0          # this will stop the cleaning without iterations
#           threshold_spec=-1 # this will jump over the dirty-cealn
#
#   It's better for you to sort the prefix_combine by time!!!!
#
#
#   stories about spwrgd
#
#   if there is no spw rigridding, for each final output channel, 
#   the weighting of each vis record is from the filled-in channel weights.
#   The final SNR in that channel was optimzed. However, due to weights  
#   changes (a weight for one spw in each vis record ) for the same vis 
#   record, the final psf changes although SNR optimzed in each channel 
#
#   if there is a spw rigridding, for each vis in each output channel, they
#   have the same weights, the final psf is a constant!
#
#   retoring is the from the fieldID near the phasecenter!!! not the real
#   psf which varies at diffrent positions.
#   in summary, replace a weight for a regrided windows (orginal from multi-windows)
#   will increase the noise. for noise oprimzed, please avoid spwrgd on multi-spw data.
#
#   regid in clean / cvel doesn't matter for single spw data! (test showed same result)
#   anyprceossing trying to replace weights for different spw with one weight will
#   be losing information
#########################################################################################

#----------------------------------------------------------------------------------------
#   Environment Setup
#----------------------------------------------------------------------------------------
casalog.filter('INFO')


startTime=time.time()
news("")
news("++")
news("------------- Begin Task: IMERGE "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
startlog = casa_log.readlines()
casa_log.close()

#----------------------------------------------------------------------------------------
#   Default Values for Optional Inputs
#----------------------------------------------------------------------------------------

try:
    prefix_combine
except NameError:
    prefix_combine=[prefix]

try:
    noplot
except NameError:
    noplot=True

try:
    fit_order
except NameError:
    fit_order=0

try:
    uvcs
except NameError:
    uvcs=False

try:
    imcs
except NameError:
    imcs=False

try:
    clean_spw
except NameError:
    clean_spw=''

try:
    iterchan
except NameError:
    iterchan=False

try:
    phase_center
except NameError:
    phase_center=''
    
try:
    spinterpmode
except NameError:
    spinterpmode='linear'
    
try:
    rest_freq
except NameError:
    rest_freq = '1420405752.0Hz'
    
try:
    out_frame
except NameError:
    out_frame='BARY'

try:
    freq_tol
except NameError:
    freq_tol=''
    
try:
    uvcs_combine
except NameError:
    uvcs_combine='spw'
    
try:
    wt_scale
except NameError:
    wt_scale=[]   

try:
    wtstat
except NameError:
    wtstat=False

try:
    wtstat_fitspw 
except NameError:
    wtstat_fitspw=''
        
try:
    concat_mms
except NameError:
    concat_mms=False

sending=True
try:
    myemail
except NameError:
    sending=False



try:
    hs
except NameError:
    hs=False 
    
logflist=[]


#----------------------------------------------------------------------------------------
#   Get optimized CLEAN_SPW
#----------------------------------------------------------------------------------------
# if  combine!=True and cleanonly==False:  
# 
#     spwid_source=spw_source.split(',')
#     tb.open(srcfile+'/SPECTRAL_WINDOW',nomodify=False)
#     header_para=tb.colnames()
#     if 'DOPPLER_ID' in header_para:
#         spwid=tb.getcol('DOPPLER_ID')
#     else:
#         spwid='0'
#     ref_freq = tb.getcol('REF_FREQUENCY')
#     tb.close()
#     tb.open(srcfile+'/DATA_DESCRIPTION',nomodify=False)
#     header_para=tb.colnames()
#     if 'SPECTRAL_WINDOW_ID' in header_para:
#         spwid=tb.getcol('SPECTRAL_WINDOW_ID')
#     else:
#         spwid='0'
#     tb.close()

#     if  clean_spw=='':
#         ref_freq_table=[]
#         for i in spwid_source:
#             ref_freq_table.append([i,ref_freq[int(i)]])
#         ref_freq_table=sorted(ref_freq_table, key=lambda \
#             ref_freq_table:ref_freq_table[1])
#         for i in range(0, len(spwid_source)):
#             tmp=ref_freq_table[i]
#             spwid_source[i]=tmp[0]
#             del tmp
#         clean_spw=','.join(str(spwid_source[i]) for i in range(len(spwid_source)))
#         del ref_freq_table
#         news(""
#         news("--"
#         news("optimized clean_spw: "+str(clean_spw)
#         news("--"
#         news(""

#----------------------------------------------------------------------------------------
#   TRACK COMBINATION
#----------------------------------------------------------------------------------------
news("")
news("++++++++++++++++++++++")
news("")
news("Processing Track(s):")
news(str(prefix_combine))
news("")
news("++++++++++++++++++++++")
news("")


#----------------------------------------------------------------------------------------
#   split the calibrated source visibilities
#----------------------------------------------------------------------------------------    
if  len(prefix_combine)==1:

    news("")
    news("--split--")
    news("")
    news(" Use split to extract the source data.")
    news("")
    
    srcfile = prefix+'.src.ms'
    msfile=prefix+'.ms'
    os.system('rm -rf '+srcfile)
    default('split')
    vis       = msfile
    outputvis = srcfile
    field     = source
    #spw       = spw_source
    keepflags=False
    datacolumn= "corrected"
    split()
    
#----------------------------------------------------------------------------------------
#   gridding the calibrated source visibilities
#----------------------------------------------------------------------------------------
    news("")
    news(">>>check spw_name")
    news("")
    spw_name_list=vishead(srcfile,mode='get',hdkey='spw_name')
    news("")
    try:
        spwrgd
    except NameError:
        spwrgd=False
        for spw_name in spw_name_list[0]:
            if  spw_name.find('TOPO')!=-1:
                spwrgd=True
        news("")
    

    if  spwrgd==True:
        news("")
        news("")
        news("TOPO frame: Spectral Regridding Performed Automatically") 
        news("")
        news("")
        news("--cvel--")
        news("")
        news(" Use cvel to perform a spectral regridding.")
        if  hs==True:
            news(" to perform a hanning smoothing to remove Gibbs ringing")    
        news("")
        
        os.system('rm -rf tmp.ms')
        default('cvel')
        vis       = srcfile
        outputvis = 'tmp.ms'
        field      = ''
        passall      = False
        spw       = ''
        mode      = 'channel'
        restfreq  = rest_freq
        outframe  = out_frame
        if    hs==True:
            hanning=True
        cvel()
        os.system('rm -rf '+srcfile)
        os.system('mv tmp.ms '+srcfile)
    
    else:
#----------------------------------------------------------------------------------------
#   HANNNING SMOOTHING
#----------------------------------------------------------------------------------------
        if  hs==True:
        
            news("")
            news("--Hanning Smooth--")
            news("")
            news(" Use HANNINGSMOOTH to remove Gibbs ringing")
            news("")
            default('hanningsmooth')
            vis       = srcfile
            hanningsmooth()
#---    
    news("")
    news("--check split--")
    news("")
    listobs(srcfile)
#---    
#----------------------------------------------------------------------------------------
#   StatWt: Recalculate the WEIGHT & SIGMA columns
#----------------------------------------------------------------------------------------
    if  wtstat==True:
        
        news("+++++++++++++++++++++++++++++++++++++++++++++++")
        news("+++++++++++++++++++++++++++++++++++++++++++++++")
        news("")
        news("--check weight column before recalculating--")
        news("")
        visstat(vis=srcfile,axis='weight')
        exportlog('visstat',srcfile+'.before-statwt.log',
            ['\n',"Visibility weight BEFORE recalculation.",'\n','\n'])
        news("")
        news("")
        
        news("")
        news("--statwt--")
        news("")
        news("Use statwt to recalculate the WEIGHT & SIGMA columns:")
        news("Useful for early-stage JVLA data")
        news("")
        default('statwt')
        vis=srcfile
        fitspw=wtstat_fitspw
        statwt()
        
        news("")
        news("--check weight column after recalculating--")
        news("")
        visstat(vis=srcfile,axis='weight')
        exportlog('visstat',srcfile+'.after-statwt.log',
            ['\n',"Visibility weight AFTER recalculation.",'\n','\n'])
        news("")
        news("")
        news("+++++++++++++++++++++++++++++++++++++++++++++++")
        news("+++++++++++++++++++++++++++++++++++++++++++++++")


prefix_combine_file=copy.deepcopy(prefix_combine)
srcfile=prefix+'.src.ms'
try:
	spwrgd
except NameError:
	spwrgd=False
mincw=0
for i in range(len(prefix_combine)):

    prefix_combine_file[i]=prefix_combine[i]+'.src.ms'
    tb.open(prefix_combine_file[i]+'/SPECTRAL_WINDOW')
    if  uvcs==True and len(prefix_combine_file)!=1:
        tb.open(prefix_combine_file[i]+'.contsub/SPECTRAL_WINDOW')
    mincw=[mincw]+tb.getcol('CHAN_WIDTH')
    tb.close
    mincw=np.min(mincw)
    
    if  uvcs==True and len(prefix_combine_file)==1:
           
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
        solint='int'
        uvcontsub()
        #os.system('rm -rf '+prefix_combine_file[i])     

if  len(prefix_combine_file)!=1 or prefix!=prefix_combine[0]:

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
            delmod(vis=prefix_combine_inp[i],otf=True,scr=False)
        os.system('rm -rf '+srcfile+loop)
       
        default('concat')
        vis=prefix_combine_inp
        concatvis=srcfile+loop
        freqtol=str(mincw/1.e6/4.)+'MHz'
        if  freq_tol!='':
            freqtol=freq_tol #'0.1MHz'
        dirtol='1.arcsec' #'1.arcsec'
        timesort=False
        visweightscale=wt_scale
        createmms=concat_mms
        concat()

    

#----------------------------------------------------------------------------------------
#   Obs List: List a summary of the new MS
#----------------------------------------------------------------------------------------
news("")
news("--listobs--")
news("")
news("Use listobs to news(verbose summary of the MS:")
postfix=''
if  uvcs==True:
    postfix='.contsub'
news(srcfile+postfix)
news("")
listobs(vis=srcfile+postfix,verbose = True)
exportlog('listobs',srcfile+'.listobs.log')
logflist=logflist+[srcfile+'.listobs.log']

#----------------------------------------------------------------------------------------
#   Vis Stat: Have a look at the visibility
#----------------------------------------------------------------------------------------
news("")
news("--visstat--")
news("")
news("Use visstat to check the MS ready for imaging:")
postfix=''
if  uvcs==True:
    postfix='.contsub'
news(srcfile+postfix)
news("")
ms_stat=visstat(vis=srcfile+postfix,axis='uvrange')

uvdist_max=ms_stat['UVRANGE']['max'] # in meter
uvdist_min=ms_stat['UVRANGE']['min'] # in meter
uvdist_rms=ms_stat['UVRANGE']['rms'] # in meter

tb.open(srcfile+postfix+'/SPECTRAL_WINDOW',nomodify=False)
header_para=tb.colnames()
obs_freq = tb.getcol('REF_FREQUENCY')
tb.close()

obs_freq = obs_freq[0]
obs_wavelength = 3.e8/obs_freq
news('obs_freq      : '+str(obs_freq))
news('obs_wavelength: '+str(obs_wavelength))

theta_las=obs_wavelength/uvdist_min/3.1415*180.*60.*60./2.
theta_fwhm=obs_wavelength/(uvdist_rms)/3.1415*180.*60.*60./2.
news("")
news("")
news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
news("predicted sythesized beamwidth:  "+str(theta_fwhm)+' arcsec')
news("predicted largest angular scale: "+str(theta_las)+' arcsec')
news("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
news("")
news("")


#----------------------------------------------------------------------------------------
#   End Statement
#----------------------------------------------------------------------------------------
subima2time=time.time()
news("")
news("Total Continuum-subtraction and Merging Time: %10.1f" %(subima2time-startTime))
news("")
news("++")
news("------------- End Task: IMERGE "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
stoplog = casa_log.readlines()
casa_log.close()
exportcasalog(startlog,stoplog, prefix+'.imerge.reduc.log')

if  sending==True:
    emailsender(myemail,\
                "RUN IMERGE End: "+prefix,\
                "This email was generated automatically by your successful reduction run.\nThe log files are attached",\
                [prefix+'.imerge.reduc.log']+logflist)
                
#----------------------------------------------------------------------------------------
#   Clean Global Variables
#----------------------------------------------------------------------------------------
del noplot
del clean_spw
del freq_tol
del uvcs_combine
del logflist
del srcfile
del prefix_combine
del concat_mms
del wt_scale
del wtstat
del wtstat_fitspw
del spwrgd
del hs
