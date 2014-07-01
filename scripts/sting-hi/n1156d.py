execfile(xlib+'xinit.py')


xp['prefix']   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles'] = '../n1156/AM418_4'


xp['source']            = 'NGC1156'
xp['spw_source']        = '0,1'

xp['fluxcal']           = '0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          = '0318+164' 
xp['phasecal_uvrange']  ='<100klambda'
xp['passcal']           = '0137+331'
xp['passcal_uvrange']   ='<40klambda'

xp['flagspw']   ='*:0~3;123~126'
xp['flagselect'] = [    "timerange='22:00:00~24:43:20'",
                "mode='quack' quackinterval=3.0",
                "antenna='VA08&VA15' timerange='23:20:42~23:20:48'",
                "antenna='VA10&VA11' timerange='25:41:42~25:41:48'",
                "antenna='VA08&VA15' spw='0' timerange='23:46:25~23:46:35'",
                "antenna='VA09&VA11' spw='0' timerange='24:50:20~24:50:40'",
                "antenna='VA09&VA11' spw='0' timerange='25:03:00~25:04:00'",
                "antenna='VA22&VA11' spw='0' timerange='25:03:00~25:04:00'",
                "antenna='VA21&VA11' spw='0' timerange='25:18:25~25:18:35'",
                "antenna='VA21&VA11' spw='0' timerange='25:18:25~25:18:35'",
                "antenna='VA03&VA11' spw='0' timerange='26:50:20~26:50:40'",
                "antenna='VA11&VA28' spw='0' timerange='26:53:40~26:54:40'",
                "uvrange='<500lambda' field='0137+331' timerange='22:33:20~24:46:40'",
                "uvrange='<500lambda' field='0318+164' timerange='22:33:20~24:56:40'",
                "uvrange='<500lambda' field='0318+164' timerange='22:33:20~24:56:40'",
                "uvrange='<500lambda' field='NGC1156' timerange='23:23:20~24:30:00'"]

execfile(stinghi+'n1156_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

