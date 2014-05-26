#########################################################################################
#
#    PURPOSE
#
#        Import visibility data into a CASA Measurement Set
#
#    INPUT FILES
#
#        VLA HI archival files, or
#        One EVLA ASDM file, or
#        One MIRIAD file, or
#        One UVFITS file written out by AIPS, MIRIAD, or other packages
#
#   OUTPUT FILES
#
#        Measurement Set (MS)       <prefix>.ms
#        Observation Summary Log    <prefix>.listobs.log
#
#   INPUT KEYWORD [ OPTIONAL | 'DEFAULT VALUE' ]
#       
#        prefix|'test'         Name of the Measurement Set
#        rawfiles|''           Name(s) of the data file(s) to be imported
#       
#        importmode|'vla'      Importing Mode      
#                              'vla':    import data in the VLA archive format
#                              'uvfits': import data from a uvfits file
#                              'evla':   import data from a EVLA ASDM file
#                              'mir':    import data in the MIRIAD format
#                              'miriad': import data in the MIRAID format (CARMAFILLER)
#                                        experimental
#                              'ms':     copy/split data from a MS file
#
#        starttime|''              start time to search for data
#        stoptime|''               end time to search for data
#        importspw|''              spectral windows to be imported
#                                  note: spw starts with 1 in miriad
#                                  examples: '1,2,7'
#        importscan|''             select the scans to be imported
#        importtimerange|''        select the timerange to be imported
#        importfield|''            select the fields to be imported
#        importband|''             band to be imported
#        importchanbin|''            channel averaging during splitting 
#        importcorr|''             import correlation
#       

#        importmirarray|'CARMA'    telescope name, CARMA, BIMA, SMA,
#                                  only for importmode='mir'
#
#   HISTORY
#
#       20100414    RX  use SPLIT to extract the wanted data based on 
#                       scan/spw/timerange/field selection rules. This option is helpful
#                       if several science targets exsit in one track.
#       20110528    RX  add email notification function
#       20110916    RX  minor fixes for v3.3
#                       add importmode 'evla' to import elva data from a ASDM file
#                       switchedpower=True will bring caldevice/syspower tables into
#                       MS files                      
#       20111120    RX  mir2ms has been merged into this script
#       20130213    RX  add into Git
#       20130910    RX  use global dict variable <xp> to wrap pipeline parameters

#    AUTHOR
#       
#       Rui Xue, University of Illinois
#
#########################################################################################

#----------------------------------------------------------------------------------------
#   Environment Setup
#----------------------------------------------------------------------------------------
casalog.filter('INFO')

startTime=time.time()
xu.news("")
xu.news("++")
xu.news("------------- Begin Task: ximport "+xp['prefix']+" -------------")
xu.news("++")
xu.news("")
casa_log = open(casalog.logfile(),'r')
startlog = casa_log.readlines()
casa_log.close()

xp['msfile'] = xp['prefix']+'.ms'
os.system('rm -rf '+xp['msfile']+'*')


#----------------------------------------------------------------------------------------
#   Data Import: Import data from VLA archive files
#----------------------------------------------------------------------------------------
if  xp['importmode']=='vla':

    xu.news("")
    xu.news("--importvla--")
    xu.news("")
    xu.news("Use importvla() to import data in the VLA archive files:")
    xu.news(xp['rawfiles'])
    xu.news("Write the data into the Measurement Set (MS):")
    xu.news(xp['msfile'])
    xu.news("")

    importvla(archivefiles=xp['rawfiles'],
              vis=xp['msfile'],
              starttime=xp['starttime'],
              stoptime=xp['stoptime'],
              bandname=xp['importband'],
              frequencytol='150000.0Hz')

#----------------------------------------------------------------------------------------
#   Data Import: Import data from VLA UVFITS files
#----------------------------------------------------------------------------------------
if     xp['importmode']=='uvfits':

    xu.news("")
    xu.news("--importuvfits--")
    xu.news("")
    xu.news("Use importuvfits() to import data in the UVFITS file:")
    xu.news(xp['rawfiles'])
    xu.news("Write the data into the Measurement Set (MS):")
    xu.news(xp['msfile'])
    xu.news("")

    importuvfits(fitsfile=xp['rawfiles'],
                 vis=xp['msfile'])

#----------------------------------------------------------------------------------------
#   Data Import: Import data from EVLA ASDM files
#----------------------------------------------------------------------------------------
if     xp['importmode']=='evla':

    xu.news("")
    xu.news("--importevla--")
    xu.news("")
    xu.news("Use importevla() to import data in the EVLA ASDM file:")
    xu.news(xp['rawfiles'])
    xu.news("Write the data into the Measurement Set (MS):")
    xu.news(xp['msfile'])
    xu.news("")

    importevla(asdm=xp['rawfiles'],
               vis=xp['msfile'],
               applyflags=True,
               switchedpower=True)
    
#----------------------------------------------------------------------------------------
#   Data Export/Import: MIRIAD->UVFITS->CASA MS
#----------------------------------------------------------------------------------------
if  xp['importmode']=='mir':
    
    xu.news("")
    xu.news("--importmir--")
    xu.news("")
    xu.news("Use importmir() to import data in the MIRIAD file:")
    xu.news(xp['rawfiles'])
    xu.news("Write the data into the Measurement Set (MS):")
    xu.news(xp['msfile'])
    xu.news("")
    xu.importmir(mirfile=xp['rawfiles'],
                 vis=xp['msfile'],
                 telescope=xp['importmirarray'],
                 nocal=xp['importmirnocal'],
                 win_list=xp['importmirspw'],
                 line=xp['importmirline'],
                 mirbin=mir_path)

if  xp['importmode']=='miriad':
    
    xu.news("")
    xu.news("--importmiriad--")
    xu.news("")
    xu.news("Use importmiriad() to import data in the MIRIAD file:")
    xu.news(xp['rawfiles'])
    xu.news("Write the data into the Measurement Set (MS):")
    xu.news(xp['msfile'])
    xu.news("")
    xu.importmiriad(mirfile=xp['rawfiles'],
                    vis=xp['msfile'],
                    telescope=xp['importmirarray'],
                    extenv=extenv)

#----------------------------------------------------------------------------------------
#   Additional Data Selection
#----------------------------------------------------------------------------------------
if  (   xp['importscan']!=''
     or xp['importspw']!=''
     or xp['importtimerange']!=''
     or xp['importfield']!=''
     or xp['importtimebin']!='0s'
     or xp['importchanbin']!=1
     or xp['importmode']=='ms') :
    
    if  xp['importmode']=='ms':
        xp['prepfile']=xp['rawfiles']
    else:
        xp['prepfile']=xp['msfile']
    
    xu.news("")
    xu.news("--listobs--")
    xu.news("")
    xu.news("Use listobs to get an observation summary:")
    xu.news(xp['prepfile'])
    xu.news("")
    
    listobs(vis=xp['prepfile'],verbose = True)    
    
    xu.news("")
    xu.news("--split--")
    xu.news("")
    xu.news("Use split to extract data based on Scan/Spw/Timerange/Field selecting and TimeBin setting:")
    xu.news(xp['prepfile'])
    xu.news("")
    """
    split(vis=xp['prepfile'],
          outputvis=xp['msfile']+'.select',
          scan=xp['importscan'],
          timerange=xp['importtimerange'],
          spw=xp['importspw'],
          field=xp['importfield'],
          timebin=xp['importtimebin'],
          datacolumn='data',
          keepflags=True,
          width=xp['importchanbin'],
          correlation=xp['importcorr'],
          combine='')
    
    """
    if  xp['importchanbin']!=1:
        chanaverage=True
    else:
        chanavarage=False
    if  xp['importtimebin']!='':
        timeaverage=True
    else:
        timeaverage=False
    mstransform(vis=xp['prepfile'],
          outputvis=xp['msfile']+'.select',
          scan=xp['importscan'],
          timerange=xp['importtimerange'],
          spw=xp['importspw'],
          field=xp['importfield'],
          datacolumn='data',
          combinespws=False,
          chanaverage=chanaverage,
          chanbin=xp['importchanbin'],
          timeaverage=timeaverage,
          timebin=xp['importtimebin'],
          useweights='flags',
          regridms=False,
          correlation=xp['importcorr'])

    os.system('rm -rf '+xp['msfile'])
    os.system('rm -rf '+xp['msfile']+'.flagversions')
    os.system('mv '+xp['msfile']+'.select '+xp['msfile'])
    os.system('mv '+xp['msfile']+'.select.flagversions '+xp['msfile']+'.flagversions')

#----------------------------------------------------------------------------------------
#   Obs List: List a summary of the MS
#----------------------------------------------------------------------------------------
xu.news("")
xu.news("--listobs--")
xu.news("")
xu.news("Use listobs to xu.news(a observation summary:")
xu.news(xp['msfile'])
xu.news("")

listobs(vis=xp['msfile'],verbose=True)

#----------------------------------------------------------------------------------------
#   Log Export: Write the LISTOBS log to a seperate file: 'prefix'.listobs.log
#----------------------------------------------------------------------------------------
xu.news("")
xu.news("--Export Logs--")
xu.news("")
xu.exporttasklog('listobs',xp['msfile']+'.listobs.log')


#----------------------------------------------------------------------------------------
#   Flagging Saving: Save the Flagging information
#----------------------------------------------------------------------------------------
xu.news("")
xu.news("--flagmanager--")
xu.news("")
xu.news("save the flagging information after importing")
xu.news("")
flagmanager(vis=xp['msfile'],
            mode='save',
            versionname='Original',
            comment='Original Flagging',
            merge='replace')

casa_log = open(casalog.logfile(),'r')
stoplog = casa_log.readlines()
casa_log.close()
xu.exportcasalog(startlog,stoplog, xp['prefix']+'.ximport.reduc.log')

#----------------------------------------------------------------------------------------
#   End Statement
#----------------------------------------------------------------------------------------
import2time=time.time()
xu.news("")
xu.news("Total importing time: %10.1f" %(import2time-startTime))
xu.news("")
xu.news("++")
xu.news("------------- End Task: ximport "+xp['prefix']+" -------------")
xu.news("++")
xu.news("")

if  xp['email']!='':
    xu.emailsender(xp['email'],\
                   "RUN <ximport> End: "+xp['prefix'],\
                   "This email was generated automatically by your successful \
                   reduction run.\nThe log files are attached",\
                   [xp['prefix']+'.ximport.reduc.log',xp['msfile']+'.listobs.log'])
