execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n6951/AS787_6']
xp['starttime']     ="2004/05/10/10:31:05.0"
xp['stoptime']      ="2004/05/10/13:53:05.0"
xp['importscan']    =''
xp['importspw']     =''

# TRACK INFORMATION
xp['source']        = 'NGC6951'

xp['fluxcal']       = '1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']      = '2022+616'
xp['phasecal_uvrange']  =''

xp['spw_source']    = '0,1'
xp['flagspw']       = '*:0~6;57~62'

# CALIBRATION & OPTIONS
xp['flagselect']    =    [    "timerange='2004/05/10/12:51:59~2004/05/10/12:54:22'",
                "timerange='2004/05/10/12:59:33~2004/05/10/15:59:33'",
                #"field='1331+305' mode='clip' cliprange='10~1000' clipexpr='ABS_RR'",
                #"field='1331+305' mode='clip' cliprange='10~1000' clipexpr='ABS_LL'",
                "antenna='VA22' ",
                "mode='quack' quackinterval=20.0",
                "antenna='VA06' timerange='10:33:30~11:33:40'",
                "timerange='12:13:20~13:03:20' field='NGC6951'",
                "timerange='12:47:40.0~12:47:50.0' antenna='VA06&VA08'",
                "timerange='10:38:00~10:38:10' field='2022+616'",
                "antenna='VA06&VA12'","antenna='VA06&VA28'",
                "antenna='VA04'",
                "antenna='VA06'",
                "antenna='VA18&VA25'","antenna='VA11&VA21'"
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







