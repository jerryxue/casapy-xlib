execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n6951/AS750_3',
                      '../n6951/AS750_4',
                      '../n6951/AS750_5']
xp['starttime']     ="2003/04/24/08:33:55.0"
xp['stoptime']      ="2003/04/24/12:01:25.0"
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
xp['flagselect']    =    [    "mode='quack' quackinterval=20.0", 
                "timerange='08:39:10~08:39:20'",
                "timerange='11:56:20~11:56:30'",
                "antenna='VA04&VA23' timerange='08:46:40~08:53:20' field='2022+616'",
                "antenna='VA04&VA23'",
                "antenna='VA28' timerange='10:00:35.0~10:00:55.0'",
                "field='1331+305' timerange='11:20:00~12:26:40'",
                "antenna='VA20&VA24'","antenna='VA20&VA12'"
            ]

execfile(stinghi+'n6951_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


