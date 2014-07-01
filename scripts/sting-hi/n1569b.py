execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../n1569/AW605_12'

# CALIBRATION
xp['source']            ='NGC1569'

xp['fluxcal']           ='0538+498'
xp['uvrange_fluxcal']   ='<50klambda'
xp['phasecal']          ='0404+768'
xp['uvrange_phasecal']  =''

xp['spw_source']        ='4,5'
xp['spw_fluxcal']       ='0,1,2,3'
xp['spw_phasecal']       ='0,1,2,3'
xp['flagspw']            ='*:0~2;121~126'

xp['flagselect']        =[    "mode='quack' quackinterval=6.0",
                "antenna='VA26' timerange='05:54:10~05:55:10'",
                "antenna='VA26' timerange='05:54:10~05:55:10'",
                "antenna='VA09' timerange='11:01:40~11:05:50'",
                "antenna='VA06' timerange='06:54:10~06:54:20'",
                "timerange='11:00:00~11:10:00'",
                "antenna='VA11&VA18'",
                "timerange='05:09:40~05:10:15' field='0538+498'",
                "timerange='12:16:40~12:19:20' field='0538+498'"
                ]

execfile(stinghi+'n1569_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

