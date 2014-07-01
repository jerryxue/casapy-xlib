execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n4536/AL735_3']
xp['importspw']         ='0'
xp['importscan']        ='34~43'

# CALIBRATION
xp['source']            ='NGC4536'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1254+116'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagspw']           ='*:0~1;120~126'
xp['flagselect']        =["antenna='VA04' timerange='2004/02/22/09:41:40~09:53:30.6'",
                          "antenna='VA06' timerange='2004/02/22/09:41:40~09:53:30.6'",
                          "antenna='VA08' timerange='2004/02/22/11:28:00~11:35:25.0'",
                          "antenna='VA10' timerange='2004/02/22/10:16:00~10:39:00.0'",
                          "antenna='VA11' timerange='2004/02/22/10:16:00~10:39:00.0'",
                          "antenna='VA22' ",
                          "timerange='2004/02/22/08:28:49~08:28:59.5' field='1'",
                          "timerange='2004/02/22/11:50:53~11:51:00.0' field='1'",
                          "timerange='2004/02/22/08:21:20~08:21:40.0' field='0'",
                          "antenna='VA02&VA04'",
                          "antenna='VA08&VA14'",
                          "antenna='VA18&VA04'",
                          "antenna='VA18&VA25'",
                          "timerange='10:59:15~10:59:25'",
                          "mode='quack' quackinterval=5.0 field='NGC3147'",
                          "timerange='11:29:30~11:30:00' field='NGC3147'"]

# CONSOLIDATING & IMAGING
execfile(stinghi+'n4536_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

