execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4654/AP206_2']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     =''

# TRACK INFORMATION
xp['source']        = 'NGC4654'

xp['fluxcal']       = '1331+305'
xp['phasecal']      = '1221+282'

xp['spw_source']    = '0'
xp['flagspw']       = '*:0;60~62'

# CALIBRATION & OPTIONS
xp['flagselect']    =["timerange='1992/03/12/04:03:20~1992/03/12/04:06:40'",
                      "timerange='1992/03/12/10:16:25.0~1992/03/12/10:16:35.0'"
                      ]

execfile(stinghi+'n4654_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
