execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n3198/AW605_13']
xp['starttime']     ='2004/07/09/19:12:05.0'
xp['stoptime']      ='2004/07/09/23:09:05.0'
xp['importscan']    ='1,18~25'
xp['importspw']     ='0,1'

# TRACK INFORMATION
xp['source']         = 'NGC3198'
xp['spw_source']    ='0,1'

xp['fluxcal']             = '0542+498'
xp['fluxcal_uvrange']    ='<50klambda'
xp['phasecal']             = '1035+564'
xp['phasecal_uvrange']    =''

# CALIBRATION & OPTIONS
xp['flagspw']       ='*:0;60~62'
xp['flagselect']    = [  "timerange='2004/07/09/22:03:28.0~22:04:32' field='NGC3198'",
                "timerange='2004/07/09/22:26:56.0~22:27:45' field='NGC3198'",
                "timerange='2004/07/09/21:33:44.0~21:34:34' field='NGC3198'",
                "timerange='2004/07/09/21:41:03.0~21:41:06' field='NGC3198'",
                "timerange='2004/07/09/21:52:07.0~21:55:31' field='NGC3198'",
                "timerange='2004/07/09/22:57:18.0~22:57:30' field='NGC3198'",
                "timerange='2004/07/09/22:58:11.0~23:03:05' field='NGC3198'",
                "timerange='2004/07/09/22:29:23.5~22:29:28.3' field='NGC3198'",
                "timerange='2004/07/09/22:57:57.9~22:58:48.4' field='NGC3198'",
                "timerange='2004/07/09/21:48:54~21:49:58' field='1035+564'",
                "timerange='2004/07/09/21:48:03~21:48:10' field='1035+564'",
                "timerange='2004/07/09/21:48:03~21:48:10' field='1035+564'",
                "timerange='2004/07/09/22:13:33~22:13:38' field='1035+564'",
                "timerange='2004/07/09/22:06:38.3~22:06:48' field='1035+564'",
                "timerange='2004/07/09/19:12:29~19:12:43' field='0542+498'",
                "timerange='2004/07/09/19:12:00~19:12:11' field='0542+498'",
                "timerange='2004/07/09/19:16:28~19:16:43' field='0542+498'",
                "timerange='2004/07/09/19:17:39~19:17:53' field='0542+498'",
                "mode='clip' clipminmax=[0,10] field='NGC3198'",
                "antenna='VA22'",
                "antenna='VA26'",
                "mode='clip' clipminmax=[0,10] field='1035+564'",
                "uvrange='<600lambda' field='1035+564'",
                "mode='quack' quackinterval=15.0 field='1035+564'",
                "antenna='VA06&VA27' field='NGC3198' timerange='2004/07/09/22:08:00~2004/07/09/22:08:10'"
                ]

execfile(stinghi+'n3198_config.py')
xp['niter']        =0

#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


