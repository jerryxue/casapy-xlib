#########################################################################################
#
#   VLA-HI CASA Reduction Scripts - Step 3      (Rui Xue, Univeristy of Illinois)
#
#   PURPOSE
#       Imaging the calibrated data.
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
#       [nogui|False]:      True: Switch off GUI during plotting
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
#                           IMCONTSUB (e.g.: fit_chans  = '1~7;79~85')	
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
#       [n_iter|2000]      iteration threshold for clean
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
#       [hs|False]:            Hanning smoothing
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
#                        frame set for CLEAN psf exportfits added
#                        hanning smoothing (hs) was moved from step2 to step3, implemented
#                        in cvel
#		20111125	RX	fix a bug when performing imcontsub
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
#       (17) About multi_scale setting
#               cleans with several resolutions using Hogbom clean. The
#               scale sizes are in units of cellsize.  So if
#               cell='2arcsec', a multiscale scale=10 => 20arcsec.  The
#               first scale is recommended to  be 0 (point), we suggest the
#               second be on the order of synthesized beam, the third 3-5
#               times the synthesized beam, etc..  Avoid making the largest
#               scale too large relative to the image width or the scale of
#               the lowest measured spatial frequency:
#			  http://www.vla.nrao.edu/astro/guides/vlas/current/node10.html
#				21cm: B (120arcsec) C & D (900arcsec)
#				The largest scale should be smaller than the galaxy size
#				smallest scale should be beam size~
#				largest scale should smaller than short baseline scale
#				largest scale should be smaller than primmary beam sizes
#		(18) About overlapping spw:
#			 We used the continuum source to test spw:
#				in the dirty image, sqrt(2)*I will show up in the overlapping veocity channels
#				But it will disappear in the cleaned image.
#				In the dirty image inverted, the flux was counted twice from the difficult spws:
#				But the psf was also counted twice, so the same model flux can be used
#				to substracted the sqrt(2)*I flux.
#				psf is the more or less the same!
#				flux is the same because the primary beam factor is the same!
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
#            threshold_spec=-1 # this will jump over the dirty-cealn
#
#
#	increase cycle_factor (default:1.5) will make clean use major cycle
#	more frenqectly at the cost of fft time because it will work back to visibility
#	This wil also increase the fidelity of the image because of more acurate
#	descrption of psf. the time increasing is due to fft for working
#	back to visiblities.
#	This is for VLA single tracks
#
#	for good uv coverage, you got gaussian beam. so working back to
#	fft may be not important. at the same time, a good uv coverage means 
#	fft can be expensive. so YOU MAY DECREASE cycle_factor=0.25!!!
#	This is for CARMA tracks or ALMA tracks
#	
#	increasing cycle_factor could help you on the divergnce issue
#
#	iterchan could also on divergence issue. But it could cost X5 time because
#	more often psf fft calculations
#  
#	for vla archival track combining. you wanna mweight=True
#	still spwrgd had this sensitivity issue!
#
#	clean_mask=True using min_pb for clean masking
#	sugguested multi-scale clean scale is [0,beamfwhm,3beamfwhm]
#
#########################################################################################

#----------------------------------------------------------------------------------------
#   Environment Setup
#----------------------------------------------------------------------------------------
casalog.filter('INFO')

startTime=time.time()
news("")
news("++")
news("------------- Begin Task: xclean "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
startlog = casa_log.readlines()
casa_log.close()

#----------------------------------------------------------------------------------------
#   Default Values for Optional Inputs
#----------------------------------------------------------------------------------------

try:
    allow_chunk
except NameError:
    allow_chunk=False

try:
    threshold_spec
except NameError:
    threshold_spec='0.0mJy'

try:
    threshold_cont
except NameError:
    threshold_cont='0.0mJy'

try:
    noplot
except NameError:
    noplot=True

try:
    fit_order
except NameError:
    fit_order=0

try:
    fit_order_imcs
except NameError:
    fit_order_imcs=fit_order

try:
    plotformat
except NameError:
    plotformat='png'

try:
    uvcs
except NameError:
    uvcs=False

try:
    imcs
except NameError:
    imcs=False

try:
    im_size
except NameError:
    im_size=512

try:
    clean_mask
except NameError:
    clean_mask=0.3333

try:
    cell_size
except NameError:
    cell_size='4.0arcsec'

try:
    n_iter
except NameError:
    n_iter=10000

try:
    sigcutoff_spec
except NameError:
    sigcutoff_spec=2.0

try:
    sigcutoff_cont
except NameError:
    sigcutoff_cont=2.0

try:
    cycle_factor
except NameError:
    cycle_factor=1.5

try:
    imstat_box_spec
except NameError:
    imstat_box_spec = str(int(im_size/4))+','+str(int(im_size/4))+','\
                +str(int(im_size*3/4))+','+str(int(im_size*3/4))        
    if  imcs==True:
        imstat_box_spec =   \
        str(0)+','+str(0)+','\
        +str(int(im_size*1/4))+','+str(int(im_size*1/4))+','\
        +str(0)+','+str(int(im_size*3/4))+','\
        +str(int(im_size*1/4))+','+str(int(im_size-1))+','\
        +str(int(im_size*3/4))+','+str(0)+','\
        +str(int(im_size-1))+','+str(int(im_size*1/4))+','\
        +str(int(im_size*3/4))+','+str(int(im_size*3/4))+','\
        +str(int(im_size-1))+','+str(int(im_size-1))    
        
try:
    imstat_rg_spec
except NameError:
    imstat_rg_spec =''
try:
    imstat_chan
except NameError:
    imstat_chan='0,1,'+str(clean_nchan-2)+','+str(clean_nchan-1)

try:
    imstat_box_cont
except NameError:
    imstat_box_cont = \
        str(0)+','+str(0)+','\
        +str(int(im_size*1/4))+','+str(int(im_size*1/4))+','\
        +str(0)+','+str(int(im_size*3/4))+','\
        +str(int(im_size*1/4))+','+str(int(im_size-1))+','\
        +str(int(im_size*3/4))+','+str(0)+','\
        +str(int(im_size-1))+','+str(int(im_size*1/4))+','\
        +str(int(im_size*3/4))+','+str(int(im_size*3/4))+','\
        +str(int(im_size-1))+','+str(int(im_size-1))    
try:
    imstat_rg_cont
except NameError:
    imstat_rg_cont =''

try:
    srcfile
except NameError:
    srcfile=prefix+'.src.ms'

try:
    ft_machine
except NameError:
    ft_machine='ft'
    
try:
    imager_mode
except NameError:
    imager_mode='csclean'
    
    prepvis=srcfile
    if  uvcs == True:
        prepvis=srcfile+'.contsub'
    
    tb.open(prepvis+'/FIELD')
    nfield=len(tb.getcol('NAME'))
    tb.close()
    if  nfield>1:
        imager_mode = 'mosaic'    
    hetero=False
    news("")
    news("nfield: "+str(nfield))
    
    tb.open(prepvis+"/OBSERVATION")
    obsnamelist=tb.getcol("TELESCOPE_NAME")
    news("obsname_list:"+str(obsnamelist))
    news("")
    for obsname in obsnamelist:
        if  obsname=='ALMA' or obsname=='CARMA':
            imager_mode = 'mosaic'
            ft_machine='mosaic'
    tb.close()
    news("imager_mode -> "+imager_mode)
    news("ft_machine  -> "+ft_machine)
    news("")
        
try:
    multi_scale
except NameError:
    multi_scale=[]

try:
    clean_field
except NameError:
    clean_field=''

try:
    cleanweight
except NameError:
    cleanweight='briggs'

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
    outer_taper
except NameError:
    outer_taper=[]

try:
    min_pb
except NameError:
    min_pb=0.1

try:
    restor_beam
except NameError:
    restor_beam=['']

try:
    cleanspec
except NameError:
    cleanspec=True

try:
    clean_gain
except NameError:
    clean_gain=0.1

try:
    wrobust
except NameError:
    wrobust=0.5
    
try:
    grid_mode
except NameError:
    grid_mode='aprojection'

try:
    mweight
except NameError:
    mweight=False

try:
    hs
except NameError:
    hs=False 
    
try:
    uvcs_combine
except NameError:
    uvcs_combine='spw'

try:
    psf_mode
except NameError:
    psf_mode='clark'

try:
    fitpsf
except NameError:
    fitpsf=False

sending=True
try:
    myemail
except NameError:
    sending=False

logflist=[]

try:
    peclean
except NameError:
    peclean=False

try:
	neg_component
except NameError:
	neg_component=-1

try:
    cleancont
except NameError:
    cleancont=False
    if  uvcs==True:
        cleancont=True

try:
	fit_chans
except NameError:
	fit_chans=''
	
try:
	save_vismodel
except NameError:
	save_vismodel=False

cleanup(prefix+'.line_d')
cleanup(prefix+'.line')
cleanup(prefix+'.coli_d')
cleanup(prefix+'.coli')
cleanup(prefix+'.cont_d')
cleanup(prefix+'.cont')
default_restor_beam=['']

#----------------------------------------------------------------------------------------
#   Make a dirty spectral cube, and determine the cube sigma level
#----------------------------------------------------------------------------------------
if  cleanspec==True:

    if  (threshold_spec=='0.0mJy' and n_iter!=0):
    
        news("")
        news("--clean--")
        news("")
        news("Make a dirty line cube (pb uncorreted)")
        news("")
        
        outname = prefix+'.line_d'
        if 	imcs==True:
        	outname = prefix+'.coli_d'
        cleanup(outname)        
        inpvis=srcfile
        if 	type(inpvis)==type(' '):
        	inpvis=[inpvis]
        if	uvcs==True:
        	for i in range(0,len(inpvis)):
				inpvis[i]=inpvis[i]+'.contsub'
	
        clean(
		vis       = inpvis,
 		imagename = outname,
    	field     = clean_field,
     	spw       = clean_spw,
      	mode      = clean_mode,
       	nchan     = clean_nchan,
    	start     = clean_start,
     	width     = clean_width,
      	niter     = 0,
       	multiscale = multi_scale,
    	negcomponent=neg_component,
        interpolation = spinterpmode,
        psfmode   = psf_mode,
        mask      = clean_mask,
        imsize    = im_size,
        cell      = cell_size,
        weighting = cleanweight,
        robust    = wrobust,
        imagermode=imager_mode,
        phasecenter=phase_center,
        ftmachine=ft_machine,
        outframe=out_frame,
        restfreq=rest_freq,
        scaletype='SAULT',
        mosweight=mweight,
        minpb=min_pb,
        pbcor=False,
        uvtaper=True,
        outertaper=outer_taper,
        cyclefactor=cycle_factor,
        restoringbeam=restor_beam,
        gain=clean_gain,
        stokes='I',
        chaniter=iterchan,
        allowchunk=allow_chunk,
        usescratch=save_vismodel,
        selectdata=True)
        modelconv(outname)
        news("")
		
        news("")   
        news("--imstat--")
        news("")
        news(" Determine the dirty cube sigma level (pb uncorreted)")
        news("")
        
        default('imstat')
        imagename = outname+'.image'
        box       = imstat_box_spec
        chans     = "" #imstat_chan
        axes=[0,1]
        region    = imstat_rg_spec
        ds_stat     = imstat()
        sigjy     = np.median(ds_stat['sigma'])
        sigmjy    = 1000 * sigjy
        news("")
        news("-------------------------------------------------------------------------")
        news(" Found the normalized sigma = "+str(sigmjy)+"mJy/beam")
        news("-------------------------------------------------------------------------")
        news("")
        
        threshold_spec=str(sigmjy*sigcutoff_spec)+'mJy'
        
        default_restor_beam=checkbeam(outname,method='maximum')

#----------------------------------------------------------------------------------------
#   Make a clean spectral cube
#----------------------------------------------------------------------------------------

    spec_restor_beam=['']
    if  restor_beam==['']:
        spec_restor_beam=default_restor_beam
    else:
        spec_restor_beam=restor_beam
        
    news("")
    news("--clean--")
    news("")
    news("Make a clean spectral cube (pb uncorrected)")
    news("Threshold value: "+threshold_spec)    
    news("")
    
    outname = prefix+'.line'
    if 	imcs==True:
		outname = prefix+'.coli'
    cleanup(outname)
    inpvis=srcfile
    if 	type(inpvis)==type(' '):
    	inpvis=[inpvis]
	if	uvcs==True:
		for i in range(0,len(inpvis)):
			inpvis[i]=inpvis[i]+'.contsub'
						    
    clean(
    vis       = inpvis,
    imagename = outname,
    field     = clean_field,
    spw       = clean_spw,
    mode      = clean_mode,
    nchan     = clean_nchan,
    start     = clean_start,
    width     = clean_width,
    niter     = n_iter,
    multiscale = multi_scale,
    negcomponent=neg_component,
    interpolation      =  spinterpmode,
    threshold = threshold_spec,
    psfmode   = psf_mode,
    mask      = clean_mask,
    imsize    = im_size,
    cell      = cell_size,
    weighting = cleanweight,
    robust    = wrobust,
    phasecenter = phase_center,
    imagermode=imager_mode,
    ftmachine=ft_machine,
    restfreq = rest_freq,
    outframe=out_frame,
    scaletype='SAULT',
    mosweight=mweight,
    minpb=min_pb,
    pbcor=False,
    uvtaper=True,
    outertaper=outer_taper,
    cyclefactor=cycle_factor,
    restoringbeam=spec_restor_beam,
    gain=clean_gain,
    stokes='I',
    chaniter=iterchan,    
    allowchunk=allow_chunk,
    usescratch=save_vismodel,
    selectdata=True)
    modelconv(outname)

    
    if  fitpsf==True:
        news("")
        news("--imfit--")
        news("")
        news("Check the PSF consistancy")
        news("")
        psf_restor_beam=checkpsf(outname)
        news("")
        news("+++")
        news("beam size from imfit:")
        news(str(psf_restor_beam))
        news("beam size used for restor:")
        news(str(restor_beam))
        news("+++")
        news("")

    news("")
    news("--immath--")
    news("")
    news("Make a pb corrected clean spectral cube")
    news("")

    immath(imagename=[outname+'.image',outname+'.flux'], expr='IM0/IM1',
        outfile=outname+'.cm')
    
    
#----------------------------------------------------------------------------------------
#   Determine the cube sigma level and produce the noise cube
#----------------------------------------------------------------------------------------
    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean cube sigma level (pb uncorreted)")
    news("")
        
    default('imstat')
    imagename = outname+'.image'
    box = imstat_box_spec 
    chans = imstat_chan
    region    = imstat_rg_spec
    cs_stat = imstat()
    sigjy     = cs_stat['sigma'][0]
    sigmjy    = 1000 * sigjy        
    

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the final normalized sigma = "+str(sigmjy)+"mJy/beam"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")

    immath(imagename=[outname+'.flux'],expr=str(sigjy)+'/IM0',outfile=outname+'.sen')
    default('imhead')
    imagename=outname+'.cm'
    mode='get'
    hdkey='beammajor'
    bmaj=imhead()
    hdkey='beamminor'
    bmin=imhead()
    hdkey='beampa'
    bpa=imhead()
    hdkey='bunit'
    bunit=imhead()
    bunit=bunit['value']
    imhead(imagename=outname+'.sen',mode='put',hdkey='beammajor',hdvalue=bmaj)
    imhead(imagename=outname+'.sen',mode='put',hdkey='beamminor',hdvalue=bmin)
    imhead(imagename=outname+'.sen',mode='put',hdkey='beampa',hdvalue=bpa)
    imhead(imagename=outname+'.sen',mode='put',hdkey='bunit',hdvalue=bunit)

#----------------------------------------------------------------------------------------
#   Examine the pb-corrected spectral cube and noise cube
#----------------------------------------------------------------------------------------
    news("")
    news("--imhead--")
    news("")
    news(" Use imhead to inspect the cleaned image cube")
    news("")
    
    default('imhead')
    imagename = outname+'.cm'
    imhead()

    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean pb-corrected cube center sigma level")
    news("")    

    default('imstat')
    imagename = outname+'.sen'
    box = str(int(im_size/2)-1)+','+str(int(im_size/2)-1)+','\
        +str(int(im_size/2)+1)+','+str(int(im_size/2)+1)
    chans = imstat_chan
    csno_stat = imstat()

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the center sigma = "+str(1000*csno_stat['mean'][0])+" mJy/beam"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")
            
#----------------------------------------------------------------------------------------
#   Log Export: Write the result from imstate/imhead to: 
#       prefix.clean.imstat.log
#       prefix.clean.imhead.log
#       prefix.clean.iteration.log
#----------------------------------------------------------------------------------------
    exportlog('imhead',outname+'.cm.imhead.log')
    logflist=logflist+[outname+'.cm.imhead.log']
    exportlog('imstat',outname+'.cm.imstat.log',\
        [rmsprint1+'\n',rmsprint2+'\n',rmsprint3+'\n'])
    logflist=logflist+[outname+'.cm.imstat.log']    
    exportlog('clean',outname+'.cm.iteration.log',\
        ['\n',"Used threshold value: "+str(threshold_spec),'\n','\n'])
    logflist=logflist+[outname+'.cm.iteration.log']    




#----------------------------------------------------------------------------------------
#   Make a dirty cont image, and determine the image sigma level
#----------------------------------------------------------------------------------------
if  cleancont==True:

    if  (threshold_cont=='0.0mJy' and n_iter!=0):

        news("")
        news("--clean--")
        news("")
        news("Make a dirty cont image (pb uncorreted)")
        news("")
        
        outname = prefix+'.cont_d'
        cleanup(outname)
        inpvis=srcfile
        if 	type(inpvis)==type(' '):
        	inpvis=[inpvis]
		if	uvcs==True:
			for i in range(0,len(inpvis)):
				inpvis[i]=inpvis[i]+'.cont'  
        
        clean(
        vis       = inpvis,
        imagename = outname,
        field     = clean_field,
        mode      = 'mfs',
        niter     = 0,
        multiscale = multi_scale,
        negcomponent=neg_component,
        psfmode   = psf_mode,
        imsize    = im_size,
        cell      = cell_size,
        mask      = clean_mask,
        weighting = cleanweight,
        robust    = wrobust,
        imagermode=imager_mode,
        phasecenter=phase_center,
        ftmachine=ft_machine,
        outframe=out_frame,
        restfreq=rest_freq,
        scaletype='SAULT',
        mosweight=mweight,
        minpb=min_pb,
        pbcor=False,
        uvtaper=True,
        outertaper=outer_taper,
        cyclefactor=cycle_factor,
        restoringbeam=restor_beam,
        gain=clean_gain,
        stokes='I',
        allowchunk=allow_chunk,
        usescratch=save_vismodel,
        selectdata=True)
        modelconv(outname)
        news("")
    
        news("")   
        news("--imstat--")
        news("")
        news(" Determine the dirty image sigma level (pb uncorreted)")
        news("")
        
        default('imstat')
        imagename = outname+'.image'
        box       = imstat_box_cont
        region    = imstat_rg_cont
        dc_stat     = imstat()
        sigjy     = dc_stat['sigma'][0]
        sigmjy    = 1000 * sigjy
        news("")
        news("-------------------------------------------------------------------------")
        news(" Found the normalized sigma = "+str(sigmjy)+"mJy/beam")
        news("-------------------------------------------------------------------------")
        news("")
        
        threshold_cont=str(sigmjy*sigcutoff_cont)+'mJy'
		
#----------------------------------------------------------------------------------------
#   Make a clean cont image
#----------------------------------------------------------------------------------------

    news("")
    news("--clean--")
    news("")
    news("Make a clean cont image using MFS (pb uncorrected)")
    news("Threshold value: "+threshold_cont)
    news("")
    
    outname = prefix+'.cont'
    cleanup(outname)
    inpvis=srcfile
    if 	type(inpvis)==type(' '):
    	inpvis=[inpvis]
    if	uvcs==True:
		for i in range(0,len(inpvis)):
			inpvis[i]=inpvis[i]+'.cont'  
    
    clean(
    vis       = inpvis,
    imagename = outname,
    field     = clean_field,
    mode      = 'mfs',
    niter     = n_iter,
    multiscale = multi_scale,
    negcomponent=neg_component,
    threshold = threshold_cont, 
    psfmode   = psf_mode,
    mask      = clean_mask,
    imsize    = im_size,
    cell      = cell_size,
    weighting = cleanweight,
    robust    = wrobust,
    phasecenter = phase_center,
    imagermode=imager_mode,
    ftmachine=ft_machine,
    restfreq = rest_freq,
    outframe=out_frame,
    scaletype='SAULT',
    mosweight=mweight,
    minpb=min_pb,
    pbcor=False,
    uvtaper=True,
    outertaper=outer_taper,
    cyclefactor=cycle_factor,
    restoringbeam=restor_beam,
    gain=clean_gain,
    stokes='I',
    allowchunk=allow_chunk,
    usescratch=save_vismodel,
    selectdata=True)
    modelconv(outname)

    if  fitpsf==True:
        news("")
        news("--imfit--")
        news("")
        news("Check the PSF consistancy")
        news("")
        psf_restor_beam=checkpsf(outname)
        news("")
        news("+++")
        news("beam size from imfit:")
        news(str(psf_restor_beam))
        news("beam size used for restor:")
        news(str(restor_beam))
        news("+++")
        news("")
        
    news("")
    news("--immath--")
    news("")
    news("Make a pb corrected clean cont image")
    news("")

    immath(imagename=[outname+'.image',outname+'.flux'],expr='IM0/IM1',\
        outfile=outname+'.cm')

#----------------------------------------------------------------------------------------
#   Determine the image sigma level and produce the noise image
#----------------------------------------------------------------------------------------
    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean image sigma level (pb uncorreted)")
    news("")
        
    default('imstat')
    imagename = outname+'.image'
    box       = imstat_box_cont
    region    = imstat_rg_cont
    cc_stat   = imstat()
    sigjy     = cc_stat['sigma'][0]
    sigmjy    = 1000 * sigjy        
    

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the final normalized sigma = "+str(sigmjy)+"mJy/beam"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")

    immath(imagename=[outname+'.flux'],expr=str(sigjy)+'/IM0',outfile=outname+'.sen')
    default('imhead')
    imagename=outname+'.cm'
    mode='get'
    hdkey='beammajor'
    bmaj=imhead()
    hdkey='beamminor'
    bmin=imhead()
    hdkey='beampa'
    bpa=imhead()
    hdkey='bunit'
    bunit=imhead()
    bunit=bunit['value']
    imhead(imagename=outname+'.sen',mode='put',hdkey='beammajor',hdvalue=bmaj)
    imhead(imagename=outname+'.sen',mode='put',hdkey='beamminor',hdvalue=bmin)
    imhead(imagename=outname+'.sen',mode='put',hdkey='beampa',hdvalue=bpa)
    imhead(imagename=outname+'.sen',mode='put',hdkey='bunit',hdvalue=bunit)

#----------------------------------------------------------------------------------------
#   Examine the pb-corrected cont image and noise image
#----------------------------------------------------------------------------------------
    news("")
    news("--imhead--")
    news("")
    news(" Use imhead to inspect the clean image")
    news("")
    
    default('imhead')
    imagename = outname+'.cm'
    imhead()

    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean pb-corrected image center sigma level")
    news("")

    default('imstat')
    imagename = outname+'.sen'
    box = str(int(im_size/2)-1)+','+str(int(im_size/2)-1)+','\
        +str(int(im_size/2)+1)+','+str(int(im_size/2)+1)
    ccno_stat = imstat()

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the center sigma = "+str(1000*ccno_stat['mean'][0])+"mJy/beam"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")
            
#----------------------------------------------------------------------------------------
#   Log Export: Write the result from imstate/imhead to: 
#       prefix.clean.imstat.log
#       prefix.clean.imhead.log
#       prefix.clean.iteration.log
#----------------------------------------------------------------------------------------
    exportlog('imhead',outname+'.cm.imhead.log')
    logflist=logflist+[outname+'.cm.imhead.log']
    exportlog('imstat',outname+'.cm.imstat.log',\
        [rmsprint1+'\n',rmsprint2+'\n',rmsprint3+'\n'])
    logflist=logflist+[outname+'.cm.imstat.log']    
    exportlog('clean',outname+'.cm.iteration.log',\
        ['\n',"Used threshold value: "+str(threshold_cont),'\n','\n'])
    logflist=logflist+[outname+'.cm.iteration.log'] 
       


#----------------------------------------------------------------------------------------
#   image-domain continuum substraction
#----------------------------------------------------------------------------------------
if  imcs == True:   

    news("")
    news("--imcontsub--")
    news("")
    news("Continumm substraction in the cube")
    news("")

    outname = prefix
    os.system('rm -rf '+outname+'.cont.* ')
    os.system('rm -rf '+outname+'.line.* ')
    
    default('imcontsub')
    imagename = outname+'.coli.cm'
    linefile  = outname+'.line.cm'
    contfile  = outname+'.cont.cm.cube'
    fitorder  = fit_order_imcs
    chans     = fit_chans
    imcontsub()
    news("")
    
    immoments(moments=-1,imagename=outname+'.cont.cm.cube', \
        outfile=outname+'.cont.cm')
    
    os.system('rm -rf '+outname+'.line.flux ')
    os.system('cp -rf '+outname+'.coli.flux '+outname+'.line.flux')	
    immath(imagename=[outname+'.line.cm',outname+'.line.flux'],expr='IM0*IM1',\
        outfile=outname+'.line.image')
    
    os.system('rm -rf '+outname+'.cont.flux ')
    #os.system('cp -rf '+outname+'.coli.flux '+outname+'.cont.flux')	        
    immath(imagename=[outname+'.cont.cm.cube',outname+'.coli.flux'],expr='IM0*IM1',\
        outfile=outname+'.cont.image.cube')
    
    os.system('rm -rf flux.tmp?')
    immath(imagename=[outname+'.line.flux'],expr='1/(IM0^2)',outfile='flux.tmp0')
    immoments(moments=-1,imagename='flux.tmp0', outfile='flux.tmp1')
    immath(imagename=['flux.tmp1'],expr='1/(IM0^0.5)',outfile='flux.tmp2')
    pbstat=imstat('flux.tmp2')
    pbmax=pbstat['max'][0]
    immath(imagename=['flux.tmp2'],expr='IM0/'+str(pbmax),outfile=outname+'.cont.flux')
    os.system('rm -rf flux.tmp?')   
    
    immath(imagename=[outname+'.cont.cm',outname+'.cont.flux'],expr='IM0*IM1',\
		outfile=outname+'.cont.image')
	

#----------------------------------------------------------------------------------------
#   Determine the cube sigma level and produce the noise image
#----------------------------------------------------------------------------------------
    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean cube sigma level (pb uncorreted)")
    news("")
        
    default('imstat')
    imagename = outname+'.line.image'
    box = imstat_box_spec 
    chans = imstat_chan
    region    = imstat_rg_spec
    cs_stat = imstat()
    sigjy     = cs_stat['sigma'][0]
    sigmjy    = 1000 * sigjy        
    

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the final normalized sigma = ", sigmjy, "mJy"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")

    os.system('rm -rf '+outname+'.line.sen')
    immath(imagename=[outname+'.line.flux'],expr=str(sigjy)+'/IM0',outfile=outname+'.line.sen')
    default('imhead')
    imagename=outname+'.line.cm'
    mode='get'
    hdkey='beammajor'
    bmaj=imhead()
    hdkey='beamminor'
    bmin=imhead()
    hdkey='beampa'
    bpa=imhead()
    hdkey='bunit'
    bunit=imhead()
    bunit=bunit['value']
    imhead(imagename=outname+'.line.sen',mode='put',hdkey='beammajor',hdvalue=bmaj)
    imhead(imagename=outname+'.line.sen',mode='put',hdkey='beamminor',hdvalue=bmin)
    imhead(imagename=outname+'.line.sen',mode='put',hdkey='beampa',hdvalue=bpa)
    imhead(imagename=outname+'.line.sen',mode='put',hdkey='bunit',hdvalue=bunit)

#----------------------------------------------------------------------------------------
#   Examine the pb-corrected spectral cube and noise cube
#----------------------------------------------------------------------------------------
    
    news("")
    news("--imhead--")
    news("")
    news(" Use imhead to inspect the cleaned image cube")
    news("")
    default('imhead')
    imagename = outname+'.line.cm'
    imhead()
    
    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean pb-corrected cube center sigma level")
    news("")
            
    
    default('imstat')
    imagename = outname+'.line.sen'
    box = str(int(im_size/2)-1)+','+str(int(im_size/2)-1)+','\
        +str(int(im_size/2)+1)+','+str(int(im_size/2)+1)
    chans = imstat_chan
    csno_stat = imstat()

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the center rms = "+str(1000*csno_stat['mean'][0])+"mJy/beam"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")

    
#----------------------------------------------------------------------------------------
#   Log Export: Write the result from imstate/imhead to: 
#       'prefix'.clean.imline.imstat.log
#       'prefix'.clean.imline.imhead.log
#----------------------------------------------------------------------------------------
    exportlog('imhead',outname+'.line.imhead.log')
    logflist=logflist+[outname+'.line.imhead.log']
    exportlog('imstat',outname+'.line.imstat.log',[rmsprint1+'\n',rmsprint2+'\n',rmsprint3+'\n'])
    logflist=logflist+[outname+'.line.imstat.log']



#----------------------------------------------------------------------------------------
#   Determine the image sigma level and produce the noise image
#----------------------------------------------------------------------------------------
    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean image sigma level (pb uncorreted)")
    news("")
        
    default('imstat')
    imagename = outname+'.cont.image'
    box       = imstat_box_cont
    region    = imstat_rg_cont
    cc_stat   = imstat()
    sigjy     = cc_stat['sigma'][0]
    sigmjy    = 1000 * sigjy        
    

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the final normalized sigma = ", sigmjy, "mJy"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")

    immath(imagename=[outname+'.cont.flux'],expr=str(sigjy)+'/IM0',outfile=outname+'.cont.sen')
    default('imhead')
    imagename=outname+'.cont.cm'
    mode='get'
    hdkey='beammajor'
    bmaj=imhead()
    hdkey='beamminor'
    bmin=imhead()
    hdkey='beampa'
    bpa=imhead()
    hdkey='bunit'
    bunit=imhead()
    bunit=bunit['value']
    imhead(imagename=outname+'.cont.sen',mode='put',hdkey='beammajor',hdvalue=bmaj)
    imhead(imagename=outname+'.cont.sen',mode='put',hdkey='beamminor',hdvalue=bmin)
    imhead(imagename=outname+'.cont.sen',mode='put',hdkey='beampa',hdvalue=bpa)
    imhead(imagename=outname+'.cont.sen',mode='put',hdkey='bunit',hdvalue=bunit)

#----------------------------------------------------------------------------------------
#   Examine the pb-corrected cont image and noise image
#----------------------------------------------------------------------------------------
    news("")
    news("--imhead--")
    news("")
    news(" Use imhead to inspect the clean image")
    news("")
    
    default('imhead')
    imagename = outname+'.cont.cm'
    imhead()

    news("")
    news("--imstate--")
    news("")
    news(" Determine the clean pb-corrected image center sigma level")
    news("")    

    default('imstat')
    imagename = outname+'.cont.sen'
    box = str(int(im_size/2)-1)+','+str(int(im_size/2)-1)+','\
        +str(int(im_size/2)+1)+','+str(int(im_size/2)+1)
    ccno_stat = imstat()

    rmsprint1="-------------------------------------------------------------------------"
    rmsprint2=" Found the center sigma = "+str(1000*ccno_stat['mean'][0])+" mJy"
    rmsprint3="-------------------------------------------------------------------------"
    news("")
    news(rmsprint1)
    news(rmsprint2)
    news(rmsprint3)
    news("")
            
#----------------------------------------------------------------------------------------
#   Log Export: Write the result from imstate/imhead to: 
#       prefix.clean.imstat.log
#       prefix.clean.imhead.log
#----------------------------------------------------------------------------------------
    exportlog('imhead',outname+'.cont.imhead.log')
    logflist=logflist+[outname+'.cont.imhead.log']
    exportlog('imstat',outname+'.cont.imstat.log',[rmsprint1+'\n',rmsprint2+'\n',rmsprint3+'\n'])
    logflist=logflist+[outname+'.cont.imstat.log']


#----------------------------------------------------------------------------------------
#   Export to FITS file
#----------------------------------------------------------------------------------------
#genmask(outname+'.flux')
#immask(outname+'.image',outname+'.flux.mask')
#immask(outname+'.flux',outname+'.flux.mask')

news("")
news("--exportmask--")
news("")
news("do masking for all images")
news("")

#mask0=prefix+'.line.flux'
#if 	imcs==True:
#	mask0=prefix+'.coli.flux'
#if	os.path.exists(mask0):
#	genmask0(mask0)
#	mask0clean(prefix+'.line_d',mask0+'.mask0')
#	mask0clean(prefix+'.line',mask0+'.mask0')
#	mask0clean(prefix+'.cont_d',mask0+'.mask0')
#	mask0clean(prefix+'.cont',mask0+'.mask0')
#	mask0clean(prefix+'.coli_d',mask0+'.mask0')
#	mask0clean(prefix+'.coli',mask0+'.mask0')
#	news("")

news("")
news("--exportfits--")
news("")
news("Export all images to FITS format")
news("")
exportclean(prefix+'.line_d')
exportclean(prefix+'.line')
exportclean(prefix+'.cont_d')
exportclean(prefix+'.cont')
exportclean(prefix+'.coli_d')
exportclean(prefix+'.coli')
news("")

#----------------------------------------------------------------------------------------
#   End Statement
#----------------------------------------------------------------------------------------
subima2time=time.time()
news("")
news("Total Imaging Time: %10.1f" %(subima2time-startTime))
news("")
news("++")
news("------------- End Task: xclean "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
stoplog = casa_log.readlines()
casa_log.close()
exportcasalog(startlog,stoplog, prefix+'.xclean.reduc.log')

if 	sending==True:
    emailsender(myemail,\
                "RUN xclean End: "+prefix,\
                "This email was generated automatically by your successful reduction run.\nThe log files are attached",\
                [prefix+'.xclean.reduc.log']+logflist)
                
#----------------------------------------------------------------------------------------
#   Clean Global Variables
#----------------------------------------------------------------------------------------
del cycle_factor
del allow_chunk
del threshold_spec
del threshold_cont
del plotformat
del noplot
del cell_size
del im_size
del clean_mask
del imager_mode
del rest_freq
del ft_machine
del sigcutoff_spec
del sigcutoff_cont
del multi_scale
del cleanweight
del n_iter
del clean_spw
del phase_center
del spinterpmode
del out_frame
del freq_tol
del outer_taper
del min_pb
del restor_beam
del clean_gain
del wrobust
del cleancont
del cleanspec
del imstat_box_spec
del imstat_box_cont
del imstat_rg_spec
del imstat_rg_cont
del imstat_chan
del mweight
del uvcs_combine
del logflist
del psf_mode
del hs
del clean_field
del fitpsf
del iterchan
del srcfile
del peclean
del neg_component
del fit_chans
del save_vismodel