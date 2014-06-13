execfile(xlib+'xinit.py')

xp['prefix']        ='n2976c02b'
xp['rawfiles']      =['../n2976/AB1038_11',
                      '../n2976/AB1038_12']
xp['importspw']     ='0'


# TRACK INFORMATION
xp['source']        = 'NGC2976'

xp['fluxcal']       = '1331+305'
xp['phasecal']      = '0921+622'

xp['spw_source']    = '0'
xp['flagspw']       ='*:0~3;57~62'

# CALIBRATION & OPTIONS

xp['flagselect']    =    [
                    "antenna='VA07&VA08'",
                    "mode='quack' quackinterval=3.0",
                    "antenna='VA20' timerange='10:45:40.0~10:45:50.0'",
                    "timerange='11:02:00.0~11:02:10.0'",
                    "antenna='VA15'",
                    "antenna='VA09&VA18'",
                    "antenna='VA11&VA14'",
                    "antenna='VA03&VA14'",
                    "antenna='VA02&VA03'",
                    "antenna='VA09&VA14'"
                ]

execfile(stinghi+'n2976_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')




