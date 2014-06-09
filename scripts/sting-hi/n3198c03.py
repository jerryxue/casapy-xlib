execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =[rawdir+'/n3198/AT285_9',rawdir+'/n3198/AT285_10']
xp['starttime']     ='2003/01/07/10:39:10.0'
xp['stoptime']      ='2003/01/07/23:00:00.0'


# TRACK INFORMATION
xp['source']        ='NGC3198'
xp['spw_source']    ='0,1'

xp['fluxcal']             = '1331+305'
xp['fluxcal_uvrange']    =''
xp['phasecal']             = '1006+349'
xp['phasecal_uvrange']    ='<30klambda'
spw_edge =6

# CALIBRATION & OPTIONS
xp['flagselect'] =  [    "timerange='2003/01/07/13:12:09~2003/01/07/13:12:10'",
                "mode='quack' quackinterval=20.0 field='1006+349'",
                "mode='quack' quackinterval=30.0 field='1331+305'",
                "timerange='2003/01/07/10:36:50.0~10:37:10.0'",
                "uvrange='<1300lambda' field='1006+349'",
                "timerange='13:12:00~13:12:20' field='1006+349'"
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



