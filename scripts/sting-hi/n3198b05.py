execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n3198/AW605_14','../n3198/AW605_15']
xp['starttime']     ='2005/04/26/23:21:25.0'
xp['stoptime']      ='2005/04/27/08:00:00.0'

# TRACK INFORMATION
xp['source']         = 'NGC3198'
xp['spw_source']    ='0,1'

xp['fluxcal']             = '1331+305'
xp['fluxcal_uvrange']    =''
xp['phasecal']             = '1035+564'
xp['phasecal_uvrange']    =''

# CALIBRATION & OPTIONS
xp['flagselect']    = [  "timerange='2005/04/26/23:30:13.0~2005/04/26/23:30:18' field='0542+498'",
                "timerange='2005/04/27/06:00:45.0~2005/04/27/06:01:02' field='1035+564'",
                #"clipexpr(ABS I)++clipminmax(0,10)++field(1035+564)",
                #"antenna='VA09' corr(LL)++spw(0)",
                #"ant(VA18)++corr(LL)++spw(0)",
                #"ant(VA22)++corr(RR)++spw(1)",
                "timerange='2005/04/27/04:08:24.0~2005/04/27/04:08:26' field='NGC3198'",
                "timerange='2005/04/27/06:31:30.0~2005/04/27/06:31:40' field='NGC3198'",
                "timerange='2005/04/27/04:19:00.0~2005/04/27/04:20:00' field='NGC3198'",
                "timerange='2005/04/27/01:54:05.0~2005/04/27/01:54:25' field='NGC3198'",
                "timerange='2005/04/27/07:14:15~07:14:40' field='1331+305'",
                "antenna='VA04'","antenna='VA21&VA22'","antenna='VA12&VA28'",
                "timerange='2005/04/27/07:16:40~07:16:50' field='1331+305' antenna='VA28'",
                "mode='quack' quackinterval=20.0",
                "antenna='VA22'"
            ]

execfile(stinghi+'n3198_config.py')
xp['niter']        =0

execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
