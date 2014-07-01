execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4151/AP251_9','../n4151/AP251_10']
xp['starttime']     ='1993/04/23/22:58:15.0'
xp['stoptime']      ='1993/04/24/10:31:15.0'
xp['importscan']    =''
xp['importspw']     =''

# TRACK INFORMATION
xp['source']         = 'NGC4151'
xp['spw_source']    ='0'

xp['fluxcal']        = '1328+307'
xp['fluxcal_uvrange']=''
xp['spw_fluxcal']    ='0'

xp['phasecal']         = '1225+368' 
xp['phasecal_uvrange']=''



# CALIBRATION & OPTIONS
xp['flagspw']        ='*:0;60~62'
xp['flagselect']     = [     "antenna='VA11'",
                "mode='quack' quackinterval=4.0",
                "timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA21&VA22'",
                "timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA14&VA21'",
                "timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA14&VA22'"
                ]

execfile(stinghi+'n4151_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



