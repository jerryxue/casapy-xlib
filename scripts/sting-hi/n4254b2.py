execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n4254/AL731_4']
xp['importspw']         ='2'

# CALIBRATION
xp['source']            ='NGC4254'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1254+116'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagselect']        =["timerange='2009/05/10/06:40:45.0~2009/05/10/06:41:05.0' antenna='EA16&VA20'",
                          "timerange='2009/05/10/07:49:55.0~2009/05/10/07:50:15.0' antenna='EA01&VA20'",
                          "timerange='2009/05/10/06:34:25.0~2009/05/10/06:34:45.0'",
                          "timerange='2009/05/10/06:59:25.0~2009/05/10/06:59:45.0'",
                          "timerange='2009/05/10/07:13:35.0~2009/05/10/07:13:55.0'",
                          "timerange='2009/05/10/07:07:45.0~2009/05/10/07:08:05.0'",
                          "timerange='2009/05/10/07:29:05.0~2009/05/10/07:29:25.0'",
                          "field='1411+522'"]

# CONSOLIDATING & IMAGING
execfile(stinghi+'n4254_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')

