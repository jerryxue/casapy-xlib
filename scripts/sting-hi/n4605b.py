execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4605/AB1038_2',
        '../n4605/AB1038_3',
        '../n4605/AB1038_4',
        '../n4605/AB1038_5',
        '../n4605/AB1038_6',
        '../n4605/AB1038_7']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     ='0'

# TRACK INFORMATION
xp['source']        ='NGC4605'
xp['fluxcal']       = '1331+305'
xp['phasecal']      = '1313+675'

xp['spw_source']    ='0'
xp['flagspw']       ='*:0;61~62'

# CALIBRATION & OPTION
xp['flagselect'] = ["antenna='VA08&VA12'",
                    "antenna='VA20'",
                    "antenna='VA11'"
                    ]

execfile(stinghi+'n4605_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


