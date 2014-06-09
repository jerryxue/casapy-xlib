execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n4536/AN119_1']

# CALIBRATION
xp['source']            ='NGC4536'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1254+116'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagselect']        =["antenna='VA08&VA14'","antenna='VA06&VA14'","antenna='VA02&VA04'",
                          "antenna='VA06' timerange='2004/03/22/09:53:00~2004/03/22/09:53:40'",
                          "antenna='VA06&VA08' timerange='2004/03/22/03:53:20~04:06:40' field='NGC4536'",
                          "field='1331+305' timerange='07:38:50~07:39:00'",
                          "field='1331+305' timerange='07:38:50~07:39:00'",
                          "field='1331+305' timerange='10:32:20~10:32:30'",
                          "field='1331+305' timerange='10:33:50~10:34:00'",
                          "mode='quack' quackinterval=20.0",
                          "timerange='10:33:45.0~10:34:05.0' antenna='VA07'",
                          "antenna='VA04'",
                          "timerange='08:23:05.0~08:23:25.0' antenna='VA18&VA25'",
                          "timerange='2004/03/22/10:18:35.0~2004/03/22/10:18:55.0'",
                          "timerange='2004/03/22/11:12:05.0~2004/03/22/11:12:25.0'",
                          "timerange='2004/03/22/11:31:35.0~2004/03/22/11:31:55.0'",
                          "antenna='VA12&VA14'","antenna='VA14&VA16'"]

# CONSOLIDATING & IMAGING
execfile(stinghi+'n4536_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')

