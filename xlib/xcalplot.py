#########################################################################################
#
#   PURPOSE
#
#       Plot calibration results 
#
#   INPUT FILES
#       Mesaurement Set:    <prefix>.ms
#                           -- calibrated data in the "corrected" column
#       Calibration Table:  <prefix>.bcal 
#                           -- passband solution table
#                           <prefix>.gcal
#                           -- gain solution table
#                           <prefix>.fcal
#                           -- flux-corrected gain solution table
#
#   OUTPUT FILES
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
#                   <prefix>.plotcal.bandpass.png
#                   -- passband solution plots (one page for one antenna)
#                   <prefix>.plotcal.gscaled.png
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

#   DEPENDENCE
#       ghostscript (generating multiple-page PDF plots), 
#       default path looking for GS:  /sw/bin/gs or /opt/local/bin/gs
#
#   INPUT KEYWORD [ OPTIONAL | DEFAULT VALUE]
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

#----------------------------------------------------------------------------------------
#   Environment Setup
#----------------------------------------------------------------------------------------
casalog.filter('INFO')

startTime=time.time()
xu.news("")
xu.news("++")
xu.news("------------- Begin Task: xcalplot "+xp['prefix']+" -------------")
xu.news("++")
xu.news("")
casa_log = open(casalog.logfile(),'r')
startlog = casa_log.readlines()
casa_log.close()


xp['msfile']=xp['prefix']+'.ms'


xu.news("")
xu.news("--plotxy--")
xu.news("")
xu.news("plot the source uv coverage and antenna positions")

"""
plotxy(vis=xp['msfile'],
    xaxis='x',
    figfile=xp['msfile']+'.array_config.png',
    interactive=False)
"""
#plotants(vis=xp['msfile'],
#    figfile=xp['msfile']+'.array_config.png')
"""
plotxy(vis=xp['msfile'],field=xp['source'],spw='',
     xaxis='u',yaxis='v',
     figfile=xp['msfile']+'.sou_uvcoverage.png',
     interactive=True) 
"""
plotms(vis=xp['msfile'],
       xaxis='u',yaxis='v',
       showmajorgrid=False,
       plotfile=xp['msfile']+'.sou_uvcoverage.png',
       interactive=False,
       overwrite=True)
# alternative solution: plotuv & plotants
#sys.exit("Please ignore the above color Trackback error message")

xu.news("")
xu.news("--xplotcal--")
xu.news("")
xu.news("plot the syscal/gain/passband solutions")

if  os.path.exists(xp['prefix']+'.gcal_passcal'):
    xu.xplotcal(xp['prefix']+'.gcal_passcal',iterant=False,extenv=extenv)
if  os.path.exists(xp['prefix']+'.bcal'):
    xu.xplotcal(xp['prefix']+'.bcal',iterant=False,extenv=extenv)
if  os.path.exists(xp['prefix']+'.bcal_comb'):
    xu.xplotcal(xp['prefix']+'.bcal_comb',iterant=False,extenv=extenv)
if  os.path.exists(xp['prefix']+'.fcal'):
    xu.xplotcal(xp['prefix']+'.fcal',iterant=False,extenv=extenv)


if  os.path.exists(xp['prefix']+'.scal'):
    xu.xplotcal(xp['prefix']+'.scal',iterant=False,extenv=extenv)
if  os.path.exists(xp['prefix']+'.scal.origin'):
    xu.xplotcal(xp['prefix']+'.scal.origin',iterant=False,extenv=extenv)
if  os.path.exists(xp['prefix']+'.scal.unflagged'):
    xu.xplotcal(xp['prefix']+'.scal.unflagged',iterant=False,extenv=extenv)
        
xu.news("")
xu.news("--plotxy--")
xu.news("")
xu.news("plot weights vs. uvdist")
"""
plotxy(vis=xp['msfile'],xaxis='uvdist',yaxis='weight',
       width='all',timebin='0',
       field=xp['source'],
       figfile=xp['msfile']+'.wt_uvdist.png', multicolor='both',
       datacolumn='data',interactive=False)
"""
plotms(vis=xp['msfile'],
       xaxis='uvdist',yaxis='weight',
       xdatacolumn='data',
       showmajorgrid=False,
       plotfile=xp['msfile']+'.wt_uvdist.png',
       interactive=False,
       overwrite=True)

xu.news("")
xu.news("--plotxy--")
xu.news("")
xu.news("plot amp vs. uvdist")
"""
plotxy(vis=xp['msfile'],xaxis='uvdist',yaxis='amp',
       width='all',timebin='0',
       field=xp['source'],
       figfile=xp['msfile']+'.amp_uvdist.png', multicolor='both',
       datacolumn='corrected',interactive=False)
"""
plotms(vis=xp['msfile'],
       xaxis='uvdist',yaxis='amp',
       xdatacolumn='corrected',
       showmajorgrid=False,
       plotfile=xp['msfile']+'.amp_uvdist.png',
       interactive=False,
       overwrite=True)

xu.news("")
xu.news("--plotxy--")
xu.news("")
xu.news("plot amp vs. time")
"""
plotxy(vis=xp['msfile'],xaxis='time',yaxis='amp',
       width='all',timebin='0',
       field=xp['source'],
       figfile=xp['msfile']+'.amp_time.png', multicolor='both',
       datacolumn='corrected',interactive=False)
"""
plotms(vis=xp['msfile'],
       xaxis='time',yaxis='amp',
       xdatacolumn='corrected',
       showmajorgrid=False,
       plotfile=xp['msfile']+'.amp_time.png',
       interactive=False,
       overwrite=True)
xu.news("")
xu.news("--plotxy--")
xu.news("")
xu.news("plot amp vs. freq")
"""
plotxy(vis=xp['msfile'],xaxis='frequency',yaxis='amp',
       width='',timebin='all',crossscans=True,
       field=xp['source'],restfreq=xp['restfreq'],frame=xp['outframe'],
       figfile=xp['msfile']+'.amp_freq.png', multicolor='both',
       datacolumn='corrected',interactive=False)
"""
plotms(vis=xp['msfile'],
       xaxis='frequency',yaxis='amp',
       xdatacolumn='corrected',
       showmajorgrid=False,
       transform=True,
       field=xp['source'],restfreq=xp['restfreq'],freqframe=xp['outframe'],
       plotfile=xp['msfile']+'.amp_freq.png',
       interactive=False,
       overwrite=True)
#----------------------------------------------------------------------------------------
#   End Statement
#----------------------------------------------------------------------------------------

flagcal2time=time.time()
xu.news("")
xu.news("Total plotting time: %10.1f" %(flagcal2time-startTime))
xu.news("")
xu.news("++")
xu.news("------------- End Task: XCALPLOT "+xp['prefix']+" -------------")
xu.news("++")
xu.news("")
casa_log = open(casalog.logfile(),'r')
stoplog = casa_log.readlines()
casa_log.close()
xu.exportcasalog(startlog,stoplog, xp['prefix']+'.xcalplot.reduc.log')

if  xp['email']!='':
    emailsender(xp['email'],\
                "RUN XCAL End: "+xp['prefix'],\
                "This email was generated automatically by your successful \
                reduction run.\nThe log files are attached",\
                [xp['prefix']+'.xcalplot.reduc.log'])

