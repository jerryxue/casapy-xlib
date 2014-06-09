execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n3593/AC459_5','../n3593/AC459_6']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='2~9'
xp['importspw']     =''



# TRACK INFORMATION
xp['source'] = 'NGC3593'

xp['fluxcal'] = '1328+307'
xp['fluxcal_uvrange']=''
xp['phasecal'] = '1117+146'
xp['phasecal_uvrange']=''

xp['spw_source'] = '0,1'
xp['flagspw'] = '*:0~4;57~62'

# CALIBRATION & OPTIONS
xp['flagselect'] =  [  "mode='quack' quackinterval=8.0 ",
                "timerange='23:25:40~23:26:20'",
                "timerange='23:32:40~23:50:00'",
                "antenna='VA17' timerange='23:30:00~23:31:00'",
                "antenna='VA16' timerange='22:13:00~22:13:30'",
                "antenna='VA16' timerange='22:32:30~22:33:00'",
                "antenna='VA16' timerange='23:01:30~23:02:00'",
                "antenna='VA01' timerange='22:44:00~22:44:30'",
                "timerange='22:48:00~22:48:30'",
                "antenna='VA28' timerange='22:58:30~22:59:00'"
                "uvrange='900lambda'",
                "timerange='23:26:30~23:27:00' field='1328+307' antenna='VA16'",
                "antenna='VA12' timerange='22:07:30~22:08:00'",
                "antenna='VA12' timerange='23:16:30~23:17:00'"
                ]
execfile(stinghi+'n3593_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


