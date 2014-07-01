execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n4254/AL731_5',
                          '../n4254/AL731_6']
xp['importspw']         ='0'

# CALIBRATION
xp['source']            ='NGC4254'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1254+116'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagspw']           ='*:0;122~126'
xp['flagselect']        =["timerange='2009/05/16/03:45:46~2009/05/16/03:46:06'",
                          "timerange='2009/05/16/05:25:00~2009/05/16/05:26:00'",
                          "timerange='2009/05/16/04:40:30~2009/05/16/04:40:48'",
                          "timerange='2009/05/16/01:27:04~2009/05/16/01:27:06'",
                          "timerange='2009/05/16/05:27:24~2009/05/16/05:27:26'",
                          "timerange='2009/05/15/23:54:55~2009/05/15/23:55:10'",
                          "timerange='2009/05/15/23:54:55~2009/05/15/23:55:10'",
                          "timerange='2009/05/15/24:30:30~2009/05/15/24:30:40'",
                          "timerange='2009/05/15/24:39:30~2009/05/15/24:39:40'",
                          "timerange='2009/05/15/25:02:14~2009/05/15/25:02:16'",
                          "timerange='2009/05/15/25:16:40~2009/05/15/25:16:50'",
                          "timerange='2009/05/15/25:21:24~2009/05/15/25:21:26'",
                          "timerange='2009/05/15/24:28:00~2009/05/15/24:28:10'",
                          "timerange='2009/05/15/23:48:04~2009/05/15/23:48:06'",
                          "scan='7' timerange='2009/05/16/00:51:40~2009/05/16/00:55:00'",
                          "timerange='23:39:10~23:42:30' field='1254+116'",
                          "field='1411+522'",
                          "antenna='EA09' timerange='22:00:00~24:53:20'",
                          "antenna='EA02&EA18'"]

# CONSOLIDATING & IMAGING
execfile(stinghi+'n4254_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

