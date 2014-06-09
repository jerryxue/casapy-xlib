execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n6951/AH912_7']
xp['starttime']     ="2006/07/01/08:05:05.0"
xp['stoptime']      ="2006/07/01/18:02:25.0"
xp['importscan']    =''
xp['importspw']     =''

# TRACK INFORMATION
xp['source']        = 'NGC6951'

xp['fluxcal']       = '1331+305'
xp['phasecal']      = '2022+616'

xp['spw_source']    = '0,1'
xp['spw_edge']      = '*:0~6;57~62'

# CALIBRATION & OPTIONS
xp['flagselect']    =["mode='quack' quackinterval=25.0",
                      "timerange='08:06:20~08:06:30'",
                      "antenna='VA07'",
                      "antenna='VA22'",
                      "antenna='VA04&VA06'",
                      "timerange='15:11:40~15:12:10'",
                      "timerange='13:26:05.0~13:26:25.0' antenna='VA17'",
                      "antenna='VA06&VA25' timerange='08:55:45.0~08:56:05.0'",
                      "antenna='VA06&VA25' timerange='09:35:35.0~09:35:55.0'",
                      "timerange='17:03:35.0~17:03:55.0'",
                      "antenna='VA11&VA21' timerange='13:23:20~14:13:20'",
                      "antenna='VA06&VA28' timerange='17:02:25~17:02:45'",
                      "timerange='16:30:35.0~16:30:55.0' antenna='VA06&VA25'",
                      "timerange='11:15:15.0~11:15:35.0' antenna='VA06&VA17'",
                      "timerange='14:35:55.0~14:36:20.0' antenna='VA06&VA17'",
                      "timerange='15:37:45.0~15:38:05.0'",
                      "timerange='17:00:00.0~17:00:10.0' antenna='VA06&VA17'"
                      ]

execfile(stinghi+'n6951_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')




