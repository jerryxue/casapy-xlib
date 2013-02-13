#########################################################################################
#
#   Script Name -- ICAL
#
#    Author
#
#        Rui Xue, Univeristy of Illinois
#
#   PURPOSE
#
#       Inspect, flag, and calibrate data
#
#   VLA CALIBRATORS INFORMATION
#
#       http://www.vla.nrao.edu/astro/calib/manual/csource.html 
# 		http://www.vla.nrao.edu/astro/calib/search/
#   DEPENDENCE
#       ghostscript (for generating multiple-page PDF plots), 
#       default path looking for GS:  /sw/bin/gs or /opt/local/bin/gs
#
#   INPUT FILE
#       Mesaurement Set:    <prefix>.ms
#
#   OUTPUT FILE
#       Measurement Set:    <prefix>.ms 
#                           -- calibrated data in the "corrected" column
#                           <prefix>.src.ms 
#                           -- calibrated (and smoothed) source data in the "data" column
#       Calibration Table:  <prefix>.bcal 
#                           -- passband solution table
#                           <prefix>.gcal
#                           -- gain solution table
#                           <prefix>.fcal
#                           -- flux scaled gain solution table
#       Figures:    
#               before calibrations:
#                   <prefix>.plotxy.sou.uvcover.<plotformat>
#                   -- uv converage plot
#                   <prefix>.plotxy.sou.xypos.<plotformat>
#                   -- antenna position plot
#                   <prefix>.plotxy.sou.time_amp.beforecal.<plotformat>
#                   -- source visibility plot before calibrations:   amp vs. time
#                   <prefix>.plotxy.sou.uvdist_amp.beforecal.<plotformat>
#                   -- source visibility plot before calibrations:   amp vs. uvdist
#                   <prefix>.plotxy.cal.time_amp.beforecal.<plotformat>
#                   -- calibrators visiblity plot before calibrations: amp vs. time 
#                   <prefix>.plotxy.cal.uvdist_amp.beforecal.<plotformat>
#                   -- calibrators visiblity plot before calibrations: amp vs. uvdist                   
#               calibration solutions:
#                   <prefix>.plotcal.bandpass.pdf
#                   -- passband solution plots (one page for one antenna)
#                   <prefix>.plotcal.gscaled.pdf
#                   -- gain solution plots (one page for one antenna)
#                   <prefix>.plotcal.allbandpass.<plotformat>
#                   -- passband solution plot (all antennas in one page)
#                   <prefix>.plotcal.allgscaled.<plotformat>
#                   -- gain solution plot (all antennas in one page)
#               before calibrations:
#                   <prefix>.plotxy.sou.amp.aftercal.<plotformat>
#                   -- source visibility plot after calibrations:
#                        amp-chan & amp-uvdist
#                   <prefix>.plotxy.phasecal.amp.aftercal.<plotformat>
#                   -- phase calibrator visibility plot after calibrations:    
#                        amp-chan & amp-uvdist
#
#   INPUT KEYWORD [ OPTIONAL | DEFAULT VALUE]
#
#       script_home:            Path of the script repository
#       prefix:                 Name of the Measurment Set
#
#       source:                 Source Name
#       phasecal:               Phase calibrator Name
#       [phasecal_uvrange|'']:  The uvrange selection for the phase calibrator
#                               please check the VLA CALIBRATOR MANUAL
#       fluxcal:                Flux calibrator Name
#       [fluxcal_uvrange|'']:   The uvrange selection for the flux calibrator
#                               please check the VLA CALIBRATOR MANUAL       
#       [passcal|fluxcal]:      Name of the passband calibrator
#                               the default value is the flux calibrator
#       [passcal_uvrange|fluxcal_uvrange]:   
#                               The uvrange selection for the passband calibrator, the 
#                               default value is the same as that of the flux calibrator
#       
#       spw_source:                 Spectral Windows for Source
#       [spw_fluxcal|spw_source]:   Spectral Windows for Fluxcal     
#       [spw_phasecal|spw_source]:  Spectral Windows for Phasecal
#       [spw_passcal|spw_fluxcal]:  Spectral Windows for Passcal
#
#       [spw_edge|0]:           The number of edge channels to be flagged
#                               It also accepts the string synatx selection: 
#                               e.g. "0:0~2;60~62"
#                               In this case, remeber to include the edge channel 
#                               selection for both source and calibrators
#       [ref_ant|'15']:         Reference Antenna Name. If you flagged out 'VA15' or 
#                               'VA15' is not at the array center, you'd like to choose 
#                               another one.
#       [gaincurvecal|True]:    Gain-elevation curve calibration; set TRUE if the data 
#                               are from VLA and were taken in or after 2001
#     
#       [noplotcal|True]:       True: don't produce multipage bandpass/gain solution 
#                               figures. But single-page solution
#                               plots will still be generated. This will reduce the 
#                               script running time.
#       [noplot|True]:          True: Don't produce any plots
#       [intflag|False]:        True: Switch on interactive flagging, ONLY valid when 
#                               noplot=False. 
#                               Interative flagging will be applied after the manual 
#                               flagging from the keyword <flagselect>
#       [iterplot|'antenna']:   iteration plotting: 'antenna' or 'baseline'
#       [plotformat|'png']:     Figure format for plots. Other options include 'eps', 
#                               'pdf', and 'svg'.
#       [interpmode|['linear','nearest']]:
#                               Interpolation mode (in time) for applying flux scaling 
#                               and gain solution tables
#       [flagreset|True]:       reset flagging, if False, the previous flagging info
#                               saved in 'flagged' will be reused
#
#       [flagselect|'']:        A string list for selecting the data to be flagged.
#                               a crazy example:
#                  [ "time(03:41:11~03:45:27)++ant(EA01)++corr(RR LL)++field(N891)",
#                    "time(03:41:11~03:49:27)++clipminmax(0,2)++clipexpr(ABS LL)",
#                    "time(03:41:11~03:49:27)++spw(1:11~23;2~1,0:1~2)++clipexpr(ABS I)",
#                    "time(03:41:11~03:45:27)++ant(EA02)++corr(RR)++field(N891)",
#                    "uvrange(<1klambda)",
#                    "quack++interval(3.0)++mode(beg)++field(N891)++ant(EA07)++\
#                    time(03:41:11~03:45:27)++corr(RR LL)++scan(1)",
#                    "rfi++clipexpr(ABS RR)++timeampcutoff(4.0)++freqampcutoff(3.0)++\
#                    bpfit++numtime(400.0)++startchan(1.0)++endchan(2048)++\
#                    bscutoff(0.0)++antcutoff(0.0)++flaglevel(1)++spw(0)++ant(EA01)++\
#                    time(03:41:11~03:45:27)++corr(RR LL)++scan(1)++uvrange(<2klambda)\
#                    ++field(N891)"]
#                               keyword available:
#                                   time, ant, corr, spw, clip, clipexpr, field, uvrange
#                                   quack
#                               NOTE: The default value for clipexpr is "ABS RR"!!
#                                     Syntax for corr setting is "RR LL" rather than 
#                                     "RR&LL" 
#
#       [flagtest|False]:       True: the script will stop after flagging
#       [wtcal|True]:           True for vla data
#                               False for evla data taken without reliable weighting info
##       The below keywords are for reductions of high-frequency data 
#
#       [bcant|'']:            Antennas for baseline correction
#       [bctype|'antposvla']:  Baseline correction type
#       [bcpara|[]]:           Baseline correction parameter
#
#       Example for Baseline Corrections:
#           bcant='VA06,VA02,VA03,VA07,VA10,VA11,VA16,VA17,VA18,VA19'
#               bcpara=[-0.0063, -0.0205,  0.0102,
#                        0.0000,  0.0003, -0.0007,
#                       -0.0011,  0.0003, -0.0005,
#                       -0.0013,  0.0000,  0.0000,
#                       -0.0013,  0.0004,  0.0000,
#                       -0.0007,  0.0000,  0.0000,
#                        0.0000, -0.0006,  0.0000,
#                       -0.0008,  0.0000,  0.0000,
#                        0.0000, -0.0004,  0.0000,
#                        0.0000, -0.0004,  0.0000]
#
#   HISTORY
#
#       Adapted from the NGC2403 tutorial scripts in the CASA trainning materials
#           http://casa.nrao.edu/Tutorial/20081007/
#           http://casa.nrao.edu/casatraining.shtml
#
#       20090213    RX  multi-page pdf for bandpass/gain solution plot
#       20090222    RX  add uvdist-amp plots for calibrators and sources
#       20090324    RX  add the keyword <refspw_map> for FLUXSCALE
#       20090825    RX  add the edge flagging
#       20091219    RX  fix troubles caused by the missing header info in data imported 
#                       from UVFITS
#       20100301    RX  automatically determine spectral window mapping in calibrations
#       20100305    RX  <flagselect>, <flagreset>, and <flagtest> were added
#                       automatically fill missing ref_frequency values of calibrators
#                       with thoes from the matching windows of your science targets.
#                       In <flagtest> mode, the script will stop after flagging
#                       and save the flag version to "flagtest"
#       20100504    RX  add amp vs. velocity plot after calibration
#       20100611    RX  default outframe for velo-amp plotting has been changed 
#                       to 'BARY'. Be careful with "TOPO" cases.
#       20100611    RX  quack and rfi flagging modes were added into <flagselect>
#       20100920    RX  fix a bug in the <flagselect> parser, split source visibilities
#                       into a seperate file, hanning smoothing added
#       20101129    RX  performance optimization for casa3.1.0
#                       scalebychan=True for SETJY (not good for using planets as 
#                       fluxcal)
#       20110528    RX  first step of modulizations: define the function exportlog in
#                       libreduc.py
#                       add email notification function
#       20110617    RX  add wtcal
#       20110916    RX  minor fixing for v3.3
#        20111006    RX    hanning smoothing was moved to step3-cvel
#                        fix a bug for dual-pol tracks
#        20111125    RX    flagdata2 & flagcmd are used to speed up flagging
#                        flagselect syntax changed
#
#   WORKING FLOW
#
#       (1) Intialize the flagging information from 'imported' version 
#           [or resue the "flagged" version stored in the MS file]
#       (2) Edge Flagging, Shadow Flagging, Auto Flagging
#       (3) Plot the visibilities for source and flux/phase/passband calibrators
#       (4) [Interactive Flagging]
#       (5) Save flagging to the version "flagged"
#       (6) Fill the model column with theoretical values for the flux calibrator
#       (7) Determine the passband solutions
#       (8) Plot the passband solutions
#       (9) Determine the gain solutions
#       (10) Plot the gain solutions
#       (11) Bootstrap flux scalling for the source and calibrators
#       (12) Apply calibrations - **results will go to the "corrected" data column**
#       (13) Use PLOTXY to check the calibrated results
#       (14) Split the source visibities
#
#   NOTES:
#       Color in Plots: Red is for the FIRST correlation (usually RR)
#       Flagging Checking Sequence:
#       1) Check the visibilities plots
#       2) Check the passband and gain solutions plots.
#       3) Check the phase for individual baselines in plotxy
#          PLOTMS & VIEWER are recommended for visibility inspection
#       4) be sure to remove short baselines for phasecal and fluxcal in cases of 
#          the solar interference
#       5) antfilter.py may be useful for the baseline inspection
#        6) http://casaguides.nrao.edu/index.php?title=Combining_Bandpasses
#
#   MORE RESOURCES:
#       Data Flagging with Viewer:
#           http://casaguides.nrao.edu/index.php?title=Data_flagging_with_viewer
#       Data Flagging with plotms:
#           http://casaguides.nrao.edu/index.php?title=Data_flagging_with_plotms
#
#   HINTS:
#       Antenna/Baseline-based flagging: VIEWER
#       Time-based flagging: PLOTMS
#       channel-based Error: PLOTMS or VIEWER
#       if you got any ms-lock issue, try CLEARSTAT
#       you're free to flag any supsect solar interference baselines in fluxcal.
#       For high frequency data, it's better to do a phase calibration in
#       the passcal scan for better passband solutions (no implemented in this script)
#
#		a simple way to check integration time:
#			listvis('n0337c06.src.ms',spw='0:0',antenna='1&2')
#		if the integration time is too small, use split to do an interagtion averging
#		for 21cm observation:
#			B 10s C 10s D 20s
#		http://evlaguides.nrao.edu/index.php?title=Observational_Status_Summary#Time_Resolution_and_Data_Rates
#
#   TO DO:
#       Have a check of the new flagging tasks:
#           flagdata2 & flagcmd
#       the slow PLOTXY is supposed to be replaced by plotms & plotants
#       flagging parser should be updated to use the new feature from casa3.1
#
#   Issues:
#           The early EVLA system didn't record the real weights in the dataset. Trying
#       to set calwt=T to calibrate them can produce nonsensical results. This may change
#       relative weighting. calwt=True means that the weights derived from Tsys 
#       measurments should also be calibrated.
#       --from casaguides:
#       "
#       In applycal we set calwt=F. It is very important to turn off this parameter which 
#       determines if the weights are calibrated along with the data. Data from antennas 
#       with better receiver performance and/or longer integration times should have 
#       higher weights, and it can be advantageous to factor this information into the 
#       calibration. During the VLA era, meaningful weights were available for each 
#       visibility. However, EVLA is not yet recording the information necessary to 
#       calculate meaningful weights. Since these data weights are used at the imaging 
#       stage you can get strange results from having calwt=T when the input weights are 
#       themselves not meaningful, especially for self-calibration on resolved sources 
#       (your flux calibrator and target for example). In a few months EVLA data will 
#       again have meaningful weights and the default calwt=T will likely again be the 
#       best option.
#       "
#
#       Wt in MS files will not be touched if calwt=False (wt will be orginal numbers!)
#       
#       tmp:
#           applying evlagain table with calwt=True seems to bring back meanful weights.
#           However, but because sigma is 1
#		uvdist default unit: m
#
#		statwt can be used to calculated thweights
#
# check the visibility after continuum substraction bcause strong continuum source 
# can hide small error on source.
#########################################################################################

#----------------------------------------------------------------------------------------
#   Environment Setup
#----------------------------------------------------------------------------------------
casalog.filter('INFO')

startTime=time.time()
news("")
news("++")
news("------------- Begin Task: ICAL "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
startlog = casa_log.readlines()
casa_log.close()

msfile = prefix + '.ms'
os.system('rm -rf '+prefix+'.psf'+'*')
os.system('rm -rf '+prefix+'.flux'+'*')
os.system('rm -rf '+prefix+'.residual'+'*')
os.system('rm -rf '+prefix+'.model'+'*')
os.system('rm -rf '+prefix+'.?cal'+'*')

news("")
news(">>>>check for flagversion Original")
news("")
if	os.path.exists(prefix+'.ms.flagversions/flags.Original'):
	news("flagversion 'Original' exists ")
	news("")
else:
	news("flagversion 'Original' doesn't exist")
	news("")
	news("save it for flagversion backup")
	news("")
	default('flagmanager')
	vis = msfile
	mode='save'
	versionname='Original'
	comment='Original Flagging'
	merge='replace'
	flagmanager()

#----------------------------------------------------------------------------------------
#   Default Values for Optional Keywords
#----------------------------------------------------------------------------------------
try:
    noplot
except NameError:
    noplot=True
   
try:
    gaincurvecal
except NameError:
    gaincurvecal=True

try:
    intflag
except NameError:
    intflag=False
    
try:
    noplotcal
except NameError:
    noplotcal=True

try:
    phasecal_uvrange
except NameError:
    phasecal_uvrange=''
try:
    fluxcal_uvrange
except NameError:
    fluxcal_uvrange=''

try: 
    passcal
except NameError:
    passcal=fluxcal
try:
    passcal_uvrange
except NameError:
    passcal_uvrange=fluxcal_uvrange

try:
    spw_edge
except NameError:
    spw_edge=0

try:
    iterplot
except NameError:
    iterplot=''

try:
    interpmode
except NameError:
    interpmode=['linear','nearest']
    
try:
    ref_ant
except NameError:
    ref_ant='15'

try:
    spw_phasecal
except NameError:
    spw_phasecal=spw_source

try:
    spw_fluxcal
except NameError:
    spw_fluxcal=spw_source

try:
    spw_passcal
except NameError:
    spw_passcal=spw_fluxcal

try:
    flagreset
except NameError:
    flagreset=True

try:
    flagselect
except NameError:
    flagselect=''

try:
    rest_freq
except NameError:
    rest_freq = '1420405752.0Hz'
    
try:
    out_frame
except NameError:
    out_frame='BARY'

try:
    flagtest
except NameError:
    flagtest=False

try:
    wtcal
except NameError:
    wtcal=True

try:
    evlacal
except NameError:
    evlacal=False

sending=True
try:
    myemail
except NameError:
    sending=False


#   Baseline Correction
try:
    bcant
except NameError:
    bcant=''
try:
    bctype
except NameError:
    bctype='antposvla'
try:
    bcpara
except NameError:
    bcpara=[]

logflist=[]



#----------------------------------------------------------------------------------------
#   MS Table Correction
#----------------------------------------------------------------------------------------

# The ms files from the importuvfits task don't have the table head keyword DOPPLER_ID,
# and sometimes <REF_FREQUENCY> is '0': e.g. old data for ngc0891
# Corrections are needed

tb.open(msfile+'/SPECTRAL_WINDOW',nomodify=False)
header_para=tb.colnames()
if 'DOPPLER_ID' in header_para:
    spwid=tb.getcol('DOPPLER_ID')
else:  
    spwid='0'
num_chan = tb.getcol('NUM_CHAN')
ref_freq = tb.getcol('REF_FREQUENCY')
tb.close()

tb.open(msfile+'/DATA_DESCRIPTION',nomodify=False)
header_para=tb.colnames()
if 'SPECTRAL_WINDOW_ID' in header_para:
    spwid=tb.getcol('SPECTRAL_WINDOW_ID')
else:
    spwid='0'
tb.close()

spwid=list(spwid)
for i in range(0,len(spwid)):
	spwid[i]=int(spwid[i])


tb.open(msfile+'/ANTENNA')
num_ant=len(tb.getcol('NAME'))
tb.close
news("")
news("Number of Antenna: "+str(num_ant))
news("")

spwid_source=spw_source.split(',')
spwid_passcal=spw_passcal.split(',')
spwid_phasecal=spw_phasecal.split(',')
spwid_fluxcal=spw_fluxcal.split(',')
spwid_soucal=spwid_source+spwid_passcal+spwid_fluxcal+spwid_phasecal
spwid_soucal=sorted(list(set(spwid_soucal)))

tb.open(msfile+'/SPECTRAL_WINDOW',nomodify=False)
news("--")
news("ref_freq (before 0-correction): "+str(ref_freq))
for i in range(0, len(spwid_passcal)):
    if ref_freq[int(spwid_passcal[i])]==0 and ref_freq[int(spwid_source[i])]!=0:
        ref_freq[int(spwid_passcal[i])]=ref_freq[int(spwid_source[i])]
for i in range(0, len(spwid_phasecal)):
    if ref_freq[int(spwid_phasecal[i])]==0 and ref_freq[int(spwid_source[i])]!=0:
        ref_freq[int(spwid_phasecal[i])]=ref_freq[int(spwid_source[i])]
for i in range(0, len(spwid_fluxcal)):
    if ref_freq[int(spwid_fluxcal[i])]==0 and ref_freq[int(spwid_source[i])]!=0:
        ref_freq[int(spwid_fluxcal[i])]=ref_freq[int(spwid_source[i])]

tb.putcol('REF_FREQUENCY',ref_freq)
tb.close()
news("ref_freq (after 0-correction):  "+str(ref_freq))
news("--")

#----------------------------------------------------------------------------------------
#   Flagging Resetting (default: True)
#----------------------------------------------------------------------------------------

if flagreset==True:
    flagmanager(vis=prefix+'.ms',mode='restore',versionname='Original')
if flagreset==False:
    flagmanager(vis=prefix+'.ms',mode='restore',versionname='flagged')

#----------------------------------------------------------------------------------------
#   Edge / Shadow / Autocorr / Quack Flagging
#----------------------------------------------------------------------------------------

if spw_edge!=0:
    if  (type(spw_edge)==type(0)):
        spw_flagged1=num_chan-num_chan
        spw_flagged2=num_chan-num_chan-1+spw_edge
        spw_flagged3=num_chan-spw_edge
        spw_flagged4=num_chan-1
        spw_flagged=','.join(\
            i+':'+\
            str(spw_flagged1[int(i)])+'~'+str(spw_flagged2[int(i)])+';'\
            +str(spw_flagged3[int(i)])+'~'+str(spw_flagged4[int(i)]) for i in spwid_soucal)
    else:
        spw_flagged=spw_edge
else:
    spw_flagged=''

news("")
news("--flagcmd--")
news("")
news("Shadow Flagging")
news("Auto-correlation Flagging")    
news("")
news("Edge channels Flagging")
news(">>>spw_flagged: "+spw_flagged)
news("")
if  flagselect!='':
	news("Manual Selection Flagging")
	news(">>>flagselect: ")
	for i in range(0,len(flagselect)):
		news("   "+flagselect[i])
	news("")


#news("")
#news("--flagdata2--")
#news("")
#news("Shadow Flagging")
#news("Auto-correlation Flagging")    
#news("Edge channels flagging")
#news(">>>spw_flagged: "+spw_flagged)
#news("")
#default(flagdata2)
#vis            =    msfile
#manualflag    =    True
#mf_antenna    =    ['*&&&',     ''            ]
#mf_spw        =   ['',        spw_flagged    ]
#if	spw_flagged=='':
#	mf_antenna=['*&&&']
#	mf_spw=['']
#shadow        =    True
#flagbackup    =    False
#flagdata2()

## flagcmd doesn't work for B1950
#default(flagdata2)
#vis            =    msfile
#manualflag    =    False
#shadow        =    True
#flagbackup    =    False
#flagdata2()
#	
#default(flagcmd)
#vis=msfile
#inpmode='cmd'
#command=[	"antenna='*&&&'",	# autocorr flagging
#			"mode='shadow'",	# shadow flagging
#			]
#if	spw_flagged!='':
#	command=command+["spw='"+spw_flagged+"'"]
#if  flagselect!='':
#	if	type(flagselect)==type(''):
#		flagselect=[flagselect]
#	command=command+flagselect
#savepars=True
#os.system('rm -rf '+msfile+'.flagcmd.log')
#outfile=msfile+'.flagcmd.log'		
#flagbackup=False
#flagcmd()


flagcommand=[]
if	spw_flagged!='':
	flagcommand=flagcommand+["spw='"+spw_flagged+"'"]
if  flagselect!='':
	if	type(flagselect)==type(''):
		flagselect=[flagselect]
	flagcommand=flagcommand+flagselect
flagcommand=flagcommand+["antenna='*&&&'","mode='shadow'"]
os.system('rm -rf '+msfile+'.flagcmd.log')
default(flagcmd)
vis=msfile
inpmode='list'
inpfile=flagcommand
savepars=True
outfile=msfile+'.flagcmd.log'		
flagbackup=False
flagcmd()
del flagcommand


if  flagtest==True:
    news("---------------------")
    news("FlagTest Mode is used")
    news("---------------------")
    news("The script stopped after flagging based on the flagselect keyword")
    news("Waiting for your inspection using plotms (recommended) or plotxy")
    del flagtest
    del flagselect
    flagmanager(vis=prefix+'.ms',mode='save',versionname='flagtest',merge='replace')    
    sys.exit("Please ignore the above color Trackback error message")

#----------------------------------------------------------------------------------------
#   Save flagging information
#----------------------------------------------------------------------------------------
news("")
news("--flagmanager--")
news("")
news("save the flagging we just did")
news("")

default('flagmanager')
vis = msfile
mode='save'
versionname='FlagCMD'
comment='Flagging After FLAGCMD'
merge='replace'
flagmanager()

news("")
news("list the current flag versions")
news("")
mode='list'
flagmanager()
news("")




#----------------------------------------------------------------------------------------
#   CALIBRATION BEGIN
#   EVLA special gain!
#----------------------------------------------------------------------------------------

if  evlacal==True:

    news("")
    news("--gencal--")
    news("")
    news("Get EVLA gain/tsys calibration table using info from")
    news("the MS's CALDEVICE and SYSPOWER subtables.")
    news("")
    default('gencal')
    vis=msfile
    caltype='evlagain'
    caltable=prefix+'.tcal'
    gencal()

#----------------------------------------------------------------------------------------
#   Baseline Correction
#----------------------------------------------------------------------------------------

if  bcant!='':

    news("")
    news("--gencal--")
    news("")
    news("solve baseline correction solutions")
    news("")
    default('gencal')
    vis=msfile
    caltable=prefix+'.pcal'
    caltype=bctype
    antenna=bcant
    parameter=bcpara
    gencal()

#----------------------------------------------------------------------------------------
#   CALIBRATION BEGIN
#   Fill the model column with the model visibilities of the flux calibrator
#----------------------------------------------------------------------------------------
news("")
news("--setjy--")
news("")
news("find the model flux density of flux calibrators, Fourier transfter the model to") 
news("visibilities and write them into the MODEL_DATA column of the current MS")
news("")

default('setjy')
vis=msfile
field=fluxcal
spw=spw_fluxcal
scalebychan=True
setjy()
news("")

#----------------------------------------------------------------------------------------
#   Calculate Bandpass Solutions
#----------------------------------------------------------------------------------------
news("")
news("--gaincal--")
news("")
news("calculate passcal gain to improve bandpass solutions")
news("")

default('gaincal')
vis=msfile
caltable=prefix+'.gcal_passcal'
field=passcal
spw=spw_passcal        
solint='inf'
combine=''
refant=ref_ant
minsnr=3.0
solnorm=False
gaintable=[]
gainfield=[]
if evlacal==True:
   gaintable=gaintable+[prefix+'.tcal']
   gainfield=gainfield+['']
if bcant!='':
   gaintable=gainfield+[prefix+'.pcal']
   gainfield=gainfield+['']
###
gaincurve = gaincurvecal
gaincal()
news("")

news("")
news("--bandpass--")
news("")
news("calculate bandpass solutions for each spw in spw_passcal")
news("")
news("")

default('bandpass')
vis      = msfile
caltable = prefix+'.bcal'
field=passcal
spw=spw_passcal
solint   = 'inf'
solnorm  = True
refant = ref_ant
selectdata = False
gaincurve = gaincurvecal
bandtype = 'B'
combine='scan'
uvrange=passcal_uvrange
gaintable=[prefix+'.gcal_passcal']
gainfield=['']
if evlacal==True:
   gaintable=gaintable+[prefix+'.tcal']
   gainfield=gainfield+['']
if bcant!='':
   gaintable=gainfield+[prefix+'.pcal']
   gainfield=gainfield+['']
bandpass()
news("")

if  len(spwid_passcal)==2*len(spwid_source):
    
    news("")
    news("--bandpass--")
    news("")
    news("calculate spw-combined bandpass solutions")
    news("")
    news("")
       
    for i in range(0,len(spwid_source)):
    	
        spw_solvebandpass=str(spwid_passcal[i])+','\
        	+str(spwid_passcal[i+len(spwid_source)])
        news("")
        news('->')
        news("processing bandpass spw: "+spw_solvebandpass)
        news('for source spw: '+str(spwid_source[i]))
        news('save bandpass solution to spw: '+str(spwid_passcal[i]))
        news('->')
        news("")
        default('bandpass')
        vis      = msfile
        caltable = prefix+'.bcal_comb'
        field=passcal
        spw=spw_solvebandpass
        solint   = 'inf'
        solnorm  = True
        refant = ref_ant
        selectdata = False
        gaincurve = gaincurvecal
        bandtype = 'B'
        uvrange=passcal_uvrange
        combine='spw,scan'
        gaintable=[prefix+'.gcal_passcal']
        gainfield=['']
        if evlacal==True:
           gaintable=gaintable+[prefix+'.tcal']
           gainfield=gainfield+['']
        if bcant!='':
           gaintable=gainfield+[prefix+'.pcal']
           gainfield=gainfield+['']
        append=True
        bandpass()
        news("")



#----------------------------------------------------------------------------------------
#   Calculate Gain Solutions
#----------------------------------------------------------------------------------------
news("")
news("--gaincal--")
news("")
news("Calculate the Gain Solutions for Phase/Flux calibrators")
news("")

news("")
news("-orginal gaincal spwmap: ")
news(str(list(spwid)))
news("")

spw_map_phasecal=list(spwid)
for i in range(0, len(spwid_phasecal)):
    if	i<len(spwid_passcal):
		spw_map_phasecal[int(spwid_phasecal[i])]=int(spwid_passcal[i])
    else:
		spw_map_phasecal[int(spwid_phasecal[i])]=int(spwid_passcal[i-len(spwid_passcal)])

spw_map_fluxcal=list(spwid)
for i in range(0, len(spwid_fluxcal)):
	if	i<len(spwid_passcal):
		spw_map_fluxcal[int(spwid_fluxcal[i])]=int(spwid_passcal[i])
	else:
		spw_map_fluxcal[int(spwid_fluxcal[i])]=int(spwid_passcal[i-len(spwid_passcal)])

news('')
news('->')
news('spwmap_bcal->phasecal:'+str(spw_map_phasecal))
news('spwmap_bcal->fluxcal:'+str(spw_map_fluxcal))
news('->')
news('')

phasecal_list=phasecal.split(',')
phasecal_uvrange_list=phasecal_uvrange.split(',')

for j in range(0,len(spwid_source)):
	
	spw_solvegain_fluxcal=str(spwid_fluxcal[j])
	if  len(spwid_fluxcal)==2*len(spwid_source):
		spw_solvegain_fluxcal=spw_solvegain_fluxcal+','+str(spwid_fluxcal[j+len(spwid_source)])
	spw_solvegain_phasecal=str(spwid_phasecal[j])
	if  len(spwid_phasecal)==2*len(spwid_source):
		spw_solvegain_phasecal=spw_solvegain_phasecal+','+str(spwid_phasecal[j+len(spwid_source)])
			
	default('gaincal')
	vis        = msfile
	caltable   = prefix + '.gcal'
	gaintable  = prefix + '.bcal'
	if  2*len(spwid_fluxcal)==len(spwid_passcal):
	    gaintable = prefix + '.bcal_comb'	
	gaintable  = [prefix + '.bcal']
	gainfield  = [passcal]
	interp     = ['nearest']
	spwmap     = [spw_map_fluxcal]
	###
	if evlacal==True:
	   gaintable  = gaintable+[prefix+'.tcal']
	   gainfield  = gainfield+['']
	   interp     = interp+['nearest']
	   spwmap     = spwmap+[[]]
	if bcant!='':
	   gaintable  = gaintable+[prefix+'.pcal']
	   gainfield  = gainfield+['']
	   interp      = interp+['']
	   spwmap      = spwmap+[[]] 
	###
	selectdata = True
	solint     = 'inf'
	gaincurve=gaincurvecal
	minsnr=3.0
	minblperant = 2
	refant     = ref_ant
	field      = fluxcal
	spw        = spw_solvegain_fluxcal
	combine    = 'spw'
	uvrange    = fluxcal_uvrange
	append     = True
	gaincal()

	gaintable[0]=prefix + '.bcal'
	if  2*len(spwid_phasecal)==len(spwid_passcal):
	    gaintable[0]=prefix + '.bcal_comb'
	spwmap     = [spw_map_phasecal]
	
	for i in range(0,len(phasecal_list)):
	    field=phasecal_list[i]
	    spw = spw_solvegain_phasecal
	    uvrange=phasecal_uvrange_list[i]
	    gaincal()       
	news("")

#----------------------------------------------------------------------------------------
#   Bootstrap flux of the phasecal source
#----------------------------------------------------------------------------------------
news("")
news("--fluxscale--")
news("")
news("calculate flux scaling and get a flux-scaled gain table")
news("see Log window for flux value found")

refspw_map=list(spwid)
news("")
news("-orginal fluxscale refspwmap: ")
news(str(refspw_map))
news("")

for i in range(0, len(spwid_phasecal)):
	if  i<len(spwid_fluxcal):
		refspw_map[int(spwid_phasecal[i])]=int(spwid_fluxcal[i])
	else:
		refspw_map[int(spwid_phasecal[i])]=int(spwid_fluxcal[i-len(spwid_fluxcal)])


news("")
news("-modified fluxscale refspwmap: ")
news(str(refspw_map))
news("")

if  phasecal!=fluxcal: 
	default('fluxscale')
	vis=msfile
	caltable= prefix + '.gcal'
	transfer = phasecal
	fluxtable=prefix + '.fcal'
	reference = fluxcal
	refspwmap=refspw_map
	fluxscale()
else: 
	os.system("cp -rf "+prefix+".gcal "+prefix+".fcal")

news("")

#----------------------------------------------------------------------------------------
#   Apply Calibration Tables - Results go to the corrected_data column 
#   Using Bandpass and Gain Solutions
#----------------------------------------------------------------------------------------
news("")
news("--applycal--")
news("")
news("apply calibration tables (flux-scaled gain + bandpass) and ")
news("writes calibrated data to the CORRECTED_DATA column..")


spwmap_bcal2source=list(spwid)
spwmap_fcal2source=list(spwid)
for i in range(0, len(spwid_source)):
	spwmap_bcal2source[int(spwid_source[i])]=int(spwid_passcal[i])
	spwmap_fcal2source[int(spwid_source[i])]=int(spwid_phasecal[i])

spwmap_bcal2phasecal=list(spwid)
spwmap_fcal2phasecal=list(spwid)
for i in range(0, len(spwid_phasecal)):	
	if  i<len(spwid_passcal):
		spwmap_bcal2phasecal[int(spwid_phasecal[i])]=int(spwid_passcal[i])
	else:
		spwmap_bcal2phasecal[int(spwid_phasecal[i])]=int(spwid_passcal[i-len(spwid_passcal)])
	if  i<len(spwid_source):
		spwmap_fcal2phasecal[int(spwid_phasecal[i])]=int(spwid_phasecal[i])
	else:
		spwmap_fcal2phasecal[int(spwid_phasecal[i])]=int(spwid_phasecal[i-len(spwid_source)])

spwmap_bcal2fluxcal=list(spwid)
spwmap_fcal2fluxcal=list(spwid)
for i in range(0, len(spwid_fluxcal)):	
	if  i<len(spwid_passcal):
		spwmap_bcal2fluxcal[int(spwid_fluxcal[i])]=int(spwid_passcal[i])
	else:
		spwmap_bcal2fluxcal[int(spwid_fluxcal[i])]=int(spwid_passcal[i-len(spwid_passcal)])
	if  i<len(spwid_source):
		spwmap_fcal2fluxcal[int(spwid_fluxcal[i])]=int(spwid_fluxcal[i])
	else:
		spwmap_fcal2fluxcal[int(spwid_fluxcal[i])]=int(spwid_fluxcal[i-len(spwid_source)])


default('applycal')

vis=msfile
calwt = wtcal
gaincurve=gaincurvecal
flagbackup=False

gaintable=[prefix+'.fcal',prefix+'.bcal']
if  len(spwid_passcal)==2*len(spwid_source):
	gaintable[1]=prefix+'.bcal_comb'
interp = ['linear','nearest']
gainfield=[phasecal,passcal]
spwmap=[spwmap_fcal2source,spwmap_bcal2source]
if evlacal==True:
   gaintable=gaintable+[prefix+'.tcal']
   interp = interp+['nearest']
   gainfield=gainfield+['']
   spwmap=spwmap+[[]]
if bcant!='':
   gaintable=gaintable+[prefix+'.pcal']
   interp = interp+['']
   gainfield=gainfield+['']
   spwmap=spwmap+[[]]
field=source
spw=spw_source
news('')
news('->')
news('spwmap_fcal->source:'+str(spwmap_fcal2source))
news('spwmap_bcal->source:'+str(spwmap_bcal2source))
news('->')
news('')
applycal()

gaintable=[prefix+'.fcal',prefix+'.bcal']
if  len(spwid_passcal)==2*len(spwid_phasecal):
	gaintable[1]=prefix+'.bcal_comb'
interp = ['nearest','nearest']
gainfield=[phasecal,passcal]
spwmap=[spwmap_fcal2phasecal,spwmap_bcal2phasecal]
if evlacal==True:
   gaintable=gaintable+[prefix+'.tcal']
   interp = interp+['nearest']
   gainfield=gainfield+['']
   spwmap=spwmap+[[]]
if bcant!='':
   gaintable=gaintable+[prefix+'.pcal']
   interp = interp+['']
   gainfield=gainfield+['']
   spwmap=spwmap+[[]]
field=phasecal
spw=spw_phasecal
news('')
news('->')
news('spwmap_fcal->phasecal:'+str(spwmap_fcal2phasecal))
news('spwmap_bcal->phasecal:'+str(spwmap_bcal2phasecal))
news('->')
news('')
applycal()

gaintable=[prefix+'.fcal',prefix+'.bcal']
if  len(spwid_passcal)==2*len(spwid_fluxcal):
	gaintable[1]=prefix+'.bcal_comb'
interp = ['nearest','nearest']
gainfield=[fluxcal,passcal]
spwmap=[spwmap_fcal2fluxcal,spwmap_bcal2fluxcal]
if evlacal==True:
   gaintable=gaintable+[prefix+'.tcal']
   interp = interp+['nearest']
   gainfield=gainfield+['']
   spwmap=spwmap+[[]]
if bcant!='':
   gaintable=gaintable+[prefix+'.pcal']
   interp = interp+['']
   gainfield=gainfield+['']
   spwmap=spwmap+[[]]
field=fluxcal
spw=spw_fluxcal
news('')
news('->')
news('spwmap_fcal->fluxcal:'+str(spwmap_fcal2fluxcal))
news('spwmap_bcal->fluxcal:'+str(spwmap_bcal2fluxcal))
news('->')
news('')
applycal()
news("")


#----------------------------------------------------------------------------------------
#   Save flagging information
#----------------------------------------------------------------------------------------
news("")
news("--flagmanager--")
news("")
news("save the flagging after applying calibration tables")
news("")

default('flagmanager')
vis = msfile
mode='save'
versionname='ApplyCal'
comment='Flagging After ApplyCAL'
merge='replace'
flagmanager()

news("")
news("list the current flag versions")
news("")
mode='list'
flagmanager()
news("")

#----------------------------------------------------------------------------------------
#   check the calibrated dataset
#----------------------------------------------------------------------------------------

listobs(vis=msfile)

news("")
news(">>>check spw_name")
news("")
spw_name_list=vishead(msfile,mode='get',hdkey='spw_name')
news("")
news("++++++++++++")
for spw_name in spw_name_list[0]:
    if  spw_name.find('TOPO')!=-1:
        news("TOPO frame found!")
        news("Spectral regridding might be automatically preformed when splitting sources!")
        news("Please check the spw defination changing!")
news("++++++++++++")
news("")


#----------------------------------------------------------------------------------------
#   End Statement
#----------------------------------------------------------------------------------------

flagcal2time=time.time()
news("")
news("Total flagging and calibration time: %10.1f" %(flagcal2time-startTime))
news("")
news("++")
news("------------- End Task: ICAL "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
stoplog = casa_log.readlines()
casa_log.close()
exportcasalog(startlog,stoplog, prefix+'.ical.reduc.log')

if  sending==True:
    emailsender(myemail,\
                "RUN ICAL End: "+prefix,\
                "This email was generated automatically by your successful reduction run.\nThe log files are attached",\
                [prefix+'.ical.reduc.log']+logflist)
                
#----------------------------------------------------------------------------------------
#   Clean Global Variables
#----------------------------------------------------------------------------------------
del intflag
del phasecal_uvrange
del fluxcal_uvrange
del passcal_uvrange
del passcal
del ref_ant
if  spw_edge!=0:
    del spw_flagged
del spw_edge
del gaincurvecal
del noplotcal
del iterplot
del interpmode
del refspw_map
del spwmap_bcal2source
del spwmap_fcal2source
del spwmap_bcal2phasecal
del spwmap_fcal2phasecal
del spwmap_bcal2fluxcal
del spwmap_fcal2fluxcal
del flagreset
del flagselect
del num_chan
del spw_passcal
del spw_fluxcal
del spw_phasecal
del flagtest
del logflist
del wtcal
del evlacal
del bcant
del bctype
del bcpara