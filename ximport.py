#########################################################################################
#
#   Author
#
#       Rui Xue, University of Illinois
#   
#   PURPOSE
#
#       Load visibility data into CASA Measurement Sets
#
#   INPUT FILES
#
#       VLA HI Archival Files, or
#       ONE EVLA ASDM Data File, or
#       MIRIAD Files, or
#       ONE UVFITS file written out by AIPS, MIRIAD, or other packages
#
#   OUTPUT FILES
#
#       Measurement Set (MS):       <prefix>.ms
#       Observation Summary Log:    <prefix>.listobs.log
#
#   INPUT KEYWORD [ OPTIONAL | 'DEFAULT VALUE' ]
#       
#       script_home:    script repository
#       prefix:         Name of the Measurement Set
#       rawfiles:       Name(s) of the data file(s) to be imported
#                       if <rawfiles> is not given, the script will read the file name list 
#                       from a plain text file <prefix>.list 
#       
#       [importmode|'vla']:    Import Mode
#                              'vla':    import VLA data in archive format
#                              'uvfits': import data from ONE uvfits file
#                              'evla':   import EVLA data from ONE ASDM file
#                              'mir':    import MIRIAD data
#       >>>vla:
#       [import_starttime|'']: Start time to search for data
#       [import_stoptime|'']:  End time to search for data
#       >>>mir:
#       [win_list|[4,5,6]:     mir spectral windows to be exported
#        [telescope|'CARMA']    telescope name, CARMA, BIMA, SMA, etc.
# 
#       Additional data selecting rules:
#   
#       [import_scan|'']:      Select the scans to be imported
#       [import_spw|'']:       Select the spectral windows to be imported
#       [import_timerange|'']: Select the timerange to be imported
#       [import_field|'']:     Select the fields to be imported
#       [import_band|'']:      Band to be imported, default: '' all bands
#       

#
#   HISTORY
#
#       20090215    RX  generate a listobs log file: 'prefix'.listobs.log
#       20090511    RX  add <importmode> for importing data in different formats
#       20100414    RX  use SPLIT to extract the wanted data based on 
#                       scan/spw/timerange/field selection rules. This option is helpful
#                       if several science targets exsit in one track.
#       20100616    RX  baseline Correction was added, only useful for high-freq data
#                       please check http://www.vla.nrao.edu/astro/archive/baselines/
#                       for baseline solutions
#       20101101    RX  script clean
#       20110528    RX  first step of modulizations: define the function exportlog in
#                       libreduc.py
#                       add email notification function
#       20110916    RX  minor fixing for v3.3
#                       add importmode 'evla' to import elva data from a ASDM file
#                       switchedpower=True will bring caldevice/syspower tables into
#                       MS files
#                       Note: for freshely imported evla data, the sigma&weight columns
#                       is 1.0; for vla data, the sigma&weight columns are NOT 1, but
#                       with weight=1/sigma^2 (weights ~200-700 for raw HI data, ~250
#                       after calibrations). Sigma is always not touched during the
#                       calibration, and weight acts like a scratch column.                      
#       20111120    RX  mir2ms was merged into this script / add timebin
#		20130213	RX	added into a git repo.
#
#   WORKING FLOW
#
#       * import raw data
#       * export the LISTOBS log file
#      [* use SPLIT to extract the data based on your additional selection setting]
#      [* baseline solution]
#
#########################################################################################

#----------------------------------------------------------------------------------------
#   Environment Setup
#----------------------------------------------------------------------------------------
casalog.filter('INFO')

startTime=time.time()
news("")
news("++")
news("------------- Begin Task: ximport "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
startlog = casa_log.readlines()
casa_log.close()

msfile = prefix + '.ms'
os.system('rm -rf '+msfile+'*')


#----------------------------------------------------------------------------------------
#   Default Values for Optional Keywords
#----------------------------------------------------------------------------------------

#   Time Interval for Data Searching
try:
    import_starttime
except NameError:
    import_starttime=''
try:
    import_stoptime
except NameError:
    import_stoptime=''

#   Names of the Data Files to be Imported
try:
    rawfiles
except NameError:
    rawfiles=None
    
#   Data Import Mode
try:
    importmode
except  NameError:
    importmode='vla'

#   Additional Data Selection
try:
    import_scan
except NameError:
    import_scan=''
try:
    import_spw
except NameError:
    import_spw=''
try:
    import_timerange
except NameError:
    import_timerange=''
try:
    import_field
except NameError:
    import_field=''
try:
    import_band
except NameError:
    import_band=''

try:
    import_win
except NameError:
    import_win=[]

try:
    telescope
except NameError:
    telescope='CARMA'

try:
    nocal
except NameError:
    nocal=False

try:
	time_bin
except NameError:
	time_bin='0s'

try:
    mirbin
except NameError:
    mirbin=''

sending=True
try:
    myemail
except NameError:
    sending=False

logflist=[]

#----------------------------------------------------------------------------------------
#   Data Import: Import data from VLA archive files
#----------------------------------------------------------------------------------------
if  importmode=='vla':

    news("")
    news("--importvla--")
    news("")
    news("Use importvla() to import data in the VLA archive files:")
    news(str(rawfiles))
    news("Write the data into the Measurement Set (MS):")
    news(str(msfile))
    news("")

    default('importvla')
    archivefiles=rawfiles
    vis = msfile
    starttime = import_starttime
    stoptime = import_stoptime
    bandname=import_band
    frequencytol='150000.0Hz'
    importvla()

#----------------------------------------------------------------------------------------
#   Data Import: Import data from VLA UVFITS files
#----------------------------------------------------------------------------------------
if 	importmode=='uvfits':

    news("")
    news("--importuvfits--")
    news("")
    news("Use importuvfits() to import data in the UVFITS file:")
    news(str(rawfiles))
    news("Write the data into the Measurement Set (MS):")
    news(str(msfile))
    news("")

    default('importuvfits')
    fitsfile = rawfiles
    vis = msfile
    importuvfits()

#----------------------------------------------------------------------------------------
#   Data Import: Import data from EVLA ASDM files
#----------------------------------------------------------------------------------------
if 	importmode=='evla':

    news("")
    news("--importevla--")
    news("")
    news("Use importevla() to import data in the EVLA ASDM file:")
    news(str(rawfiles))
    news("Write the data into the Measurement Set (MS):")
    news(str(msfile))
    news("")

    default('importevla')
    asdm = rawfiles
    vis = msfile
    applyflags=True
    switchedpower=True
    importevla()
    
#----------------------------------------------------------------------------------------
#   Data Export/Import: MIRIAD->UVFITS->CASA MS
#----------------------------------------------------------------------------------------
if  importmode=='mir':
    
    news("")
    news("--importmir--")
    news("")
    news("Use importmir() to import data in the MIRIAD file:")
    news(str(rawfiles))
    news("Write the data into the Measurement Set (MS):")
    news(str(msfile))
    news("")
    importmir(  mirfile=rawfiles,
                vis=msfile,
                telescope=telescope,
                nocal=nocal,
                win_list=import_win,
                mirbin=mirbin)

#----------------------------------------------------------------------------------------
#   Additional Data Selection
#----------------------------------------------------------------------------------------
if  (import_scan!='' or import_spw!='' or import_timerange!='' \
    or import_field!='' or time_bin!='0s' or importmode=='ms') :
    
    if  importmode=='ms':
    	prepfile=rawfiles
    else:
    	prepfile=msfile
    
    news("")
    news("--listobs--")
    news("")
    news("Use listobs to get an observation summary:")
    news(str(prepfile))
    news("")
    
    listobs(vis=prepfile,verbose = True)    
    
    news("")
    news("--split--")
    news("")
    news("Use split to extract data based on Scan/Spw/Timerange/Field selecting and TimeBin setting:")
    news(str(prepfile))
    news("")
    
    default('split')
    vis       = prepfile
    outputvis = msfile+'.select'
    scan = import_scan
    timerange = import_timerange
    spw = import_spw
    field = import_field
    timebin=time_bin
    datacolumn='data'
    keepflags=True
    combine=''
    split()
    os.system('rm -rf '+msfile)
    os.system('rm -rf '+msfile+'.flagversions')
    os.system('mv '+msfile+'.select '+msfile)
    os.system('mv '+msfile+'.select.flagversions '+msfile+'.flagversions')

#----------------------------------------------------------------------------------------
#   Obs List: List a summary of the MS
#----------------------------------------------------------------------------------------
news("")
news("--listobs--")
news("")
news("Use listobs to news(a observation summary:")
news(str(msfile))
news("")

verbose = True
listobs(vis=msfile)

#----------------------------------------------------------------------------------------
#   Log Export: Write the LISTOBS log to a seperate file: 'prefix'.listobs.log
#----------------------------------------------------------------------------------------
news("")
news("--Export Logs--")
news("")
exportlog('listobs',prefix+'.listobs.log')
logflist=logflist+[prefix+'.listobs.log']


#----------------------------------------------------------------------------------------
#   Flagging Saving: Save the Flagging information
#----------------------------------------------------------------------------------------
news("")
news("--flagmanager--")
news("")
news("save the flagging information after importing")
news("")
default('flagmanager')
vis = msfile
mode='save'
versionname='Original'
comment='Original Flagging'
merge='replace'
flagmanager()


#----------------------------------------------------------------------------------------
#   End Statement
#----------------------------------------------------------------------------------------
import2time=time.time()
news("")
news("Total importing time: %10.1f" %(import2time-startTime))
news("")
news("++")
news("------------- End Task: ximport "+prefix+" -------------")
news("++")
news("")
casa_log = open(casalog.logfile(),'r')
stoplog = casa_log.readlines()
casa_log.close()
exportcasalog(startlog,stoplog, prefix+'.ximport.reduc.log')

if  sending==True:
    emailsender(myemail,\
                "RUN <ximport> End: "+prefix,\
                "This email was generated automatically by your successful reduction run.\nThe log files are attached",\
                [prefix+'.ximport.reduc.log']+logflist)
                
#----------------------------------------------------------------------------------------
#   Clean Global Variables
#----------------------------------------------------------------------------------------
del import_starttime
del import_stoptime
del rawfiles
del import_scan
del import_spw
del import_timerange
del import_field
del import_band
del importmode
del import_win
del telescope
del nocal
del logflist
del time_bin
