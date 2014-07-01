execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n4536/AL731_L090518.xp1']

# CALIBRATION
xp['source']            ='NGC4536'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1150-003'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagspw']           ='*:0~1:120~126'
xp['flagselect']        =["field='1411+522'",    "timerange='01:28:20~01:33:20'","timerange='05:20:20~05:20:30'",
                          "antenna='EA23&EA25' timerange='2009/05/18/05:14:50.0~2009/05/18/05:15:10.0'",
                          "timerange='2009/05/18/01:40:35.0~2009/05/18/01:40:55.0' antenna='EA02&VA20'",
                          "timerange='2009/05/18/01:49:25.0~2009/05/18/01:49:45.0' antenna='EA03&VA20'",
                          "timerange='2009/05/18/02:04:05.0~2009/05/18/02:04:25.0' antenna='EA19&VA20'",
                          "timerange='2009/05/18/02:55:45.0~2009/05/18/02:56:05.0' antenna='EA16&VA20'",
                          "timerange='2009/05/18/03:05:45.0~2009/05/18/03:06:05.0' antenna='EA17&VA20'",
                          "timerange='2009/05/18/05:05:45.0~2009/05/18/05:06:05.0' antenna='VA10&EA17'",
                          "timerange='2009/05/18/05:10:15.0~2009/05/18/05:10:35.0' antenna='EA02&VA20'",
                          "timerange='2009/05/18/05:05:45.0~2009/05/18/05:06:05.0' antenna='EA02&EA17'"]

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
