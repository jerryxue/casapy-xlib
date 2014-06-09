execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n4536/AL731_2']

# CALIBRATION
xp['source']            ='NGC4536'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1150-003'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagselect']        =["antenna='EA08'",
                          "timerange='00:00:01~01:10:20' field='1150-003'",
                          "timerange='02:26:45.0~02:27:05.0' antenna='EA14&EA23'",
                          "timerange='01:30:45.0' antenna='VA20&EA24'",
                          "timerange='2009/05/17/01:32:05.0~2009/05/17/01:32:25.0' antenna='EA15&VA20'",
                          "timerange='2009/05/17/02:13:15.0~2009/05/17/02:13:35.0' antenna='EA11&VA20'",
                          "timerange='2009/05/17/02:36:25.0~2009/05/17/02:36:45.0' antenna='EA14&VA20'",
                          "timerange='2009/05/17/05:27:55.0~2009/05/17/05:28:15.0' antenna='EA01&VA20'",
                          "timerange='2009/05/17/06:02:35.0~2009/05/17/06:02:55.0' antenna='EA16&VA20'",
                          "timerange='2009/05/17/06:23:05.0~2009/05/17/06:23:25.0' antenna='EA04&EA17'",
                          "timerange='06:16:40~06:17:10'",
                          "timerange='06:42:55~06:43:10'",
                          "field='1411+522'"]

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

