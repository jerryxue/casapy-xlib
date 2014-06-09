execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =[rawdir+'/n3198/AT285_8']
xp['starttime']     ='2002/11/26/11:25:50'
xp['stoptime']      ='2002/11/26/12:19:50'


# TRACK INFORMATION
xp['source']        ='NGC3198'
xp['spw_source']    ='0,1'

xp['fluxcal']             = '1331+305'
xp['fluxcal_uvrange']    =''
xp['phasecal']             = '1006+349'
xp['phasecal_uvrange']    ='<30klambda'
spw_edge =6

# CALIBRATION & OPTIONS
xp['flagselect'] = [    "timerange='2002/11/26/11:40:09~2002/11/26/11:40:10'",
                "timerange='2002/11/26/11:45:46~2002/11/26/11:45:53'",
                "timerange='2002/11/26/11:51:48~2002/11/26/11:51:54'",
                "timerange='2002/11/26/11:22:30~11:24:30'",
                "mode='quack' quackinterval=20.0 field='1006+349'",
                "antenna='VA09&VA14'",
                "antenna='VA07&VA08' timerange='11:40:00~11:40:20'"
                ]


execfile(stinghi+'n3198_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


