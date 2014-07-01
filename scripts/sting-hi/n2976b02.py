execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n2976/AB1038_2',
                      '../n2976/AB1038_3',
                      '../n2976/AB1038_4',
                      '../n2976/AB1038_5',
                      '../n2976/AB1038_6',
                      '../n2976/AB1038_7',
                      '../n2976/AB1038_8']
xp['importspw']     ='0'

# TRACK INFORMATION
xp['source']        = 'NGC2976'

xp['fluxcal']       = '1331+305'
xp['phasecal']      = '0921+622'

xp['spw_source']    = '0'
xp['flagspw']       = '*:0;60~62'

# CALIBRATION & OPTIONS
xp['flagselect']    =[
                    " antenna='VA08&VA12' ",
                    " timerange='24:55:50~25:40:00' ",
                    " timerange='17:11:40~17:36:40' ",
                    " antenna='VA02&VA06'",
                    " antenna='VA06&VA22'"
                    ] 
execfile(stinghi+'n2976_config.py')     
xp['niter']     =0  

#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')







