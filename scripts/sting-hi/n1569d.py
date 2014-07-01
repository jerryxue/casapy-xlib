execfile(xlib+'xinit.py')

# IMPORT 
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n1569/AW325_4',
                      '../n1569/AW325_5']

# TRACK INFORMATION
xp['source']            = 'NGC1569'

xp['fluxcal']           = '0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          = '0614+607'
xp['phasecal_uvrange']  =''

xp['spw_source']         = '4,5'
xp['spw_fluxcal']         = '0,1,2,3'
xp['spw_phasecal']         = '0,1,2,3'
xp['flagspw']            ='*:0~2;121~126'

# CALIBRATION & OPTIONS
xp['flagselect'] =     [
                "mode='quack' quackinterval=3.0",
                "antenna='VA16'",
                "timerange='1992/09/06/08:17:45~1992/09/06/08:19:45' antenna='VA28'",
                "timerange='1992/09/06/09:16:30~1992/09/06/09:18:30' antenna='VA28'",
                "timerange='1992/09/06/09:21:30~1992/09/06/09:23:30' antenna='VA28'",
                "timerange='1992/09/06/11:42:30~1992/09/06/11:44:30' antenna='VA28'",
                "timerange='1992/09/06/12:05:15~1992/09/06/12:07:15' antenna='VA28'",
                "timerange='1992/09/06/11:02:30~1992/09/06/11:04:15' antenna='VA28'",
                "antenna='VA10&VA28' timerange='1992/09/06/08:31:00~1992/09/06/08:31:40'",
                "antenna='VA12' timerange='08:29:10~08:35:30' field='0137+331'",
                "mode='tfcrop' freqcutoff=2.7 flagdimension='freq' field='NGC1569' maxnpieces=3" #spw='*:20~100'
                ]

execfile(stinghi+'n1569_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
