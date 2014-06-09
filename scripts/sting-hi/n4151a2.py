execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4151/AB658_7','../n4151/AB658_8']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='17~22'
xp['importspw']     ='8~9'



# TRACK INFORMATION
xp['source']         = 'NGC4151'
xp['spw_source']    ='0'

xp['fluxcal']         = '1328+307'
xp['fluxcal_uvrange']=''
xp['phasecal']         = '1223+395' 
xp['phasecal_uvrange']='>20klambda'

xp['flagspw']    ='*:0~4;58~62'

# CALIBRATION & OPTIONS
xp['flagselect'] =     [
                "mode='quack' quackinterval=6.0",
                "timerange='02:09:10~02:09:20' antenna='VA23&VA26'",
                "timerange='03:14:20~03:14:30' antenna='VA23&VA26'",
                "timerange='02:19:40~02:19:50' antenna='VA01&VA26'",
                "timerange='02:34:50~02:34:58'",
                "timerange='02:39:40~02:39:50' antenna='VA01&VA28'",
                "mode='quack' quackinterval=30.0 field='1328+307'",
                "timerange='02:35:00~02:35:20' field='1328+307'",
                #"uvrange(<40000lambda' field(1328+307)",
                "antenna='VA14'",
                "antenna='VA15&VA27' field='1223+395'"
                ]

execfile(stinghi+'n4151_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

