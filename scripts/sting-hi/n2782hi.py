#2390,2725

#execfile(stinghi+'n2782ab.py')
execfile(stinghi+'n2782c.py')
execfile(stinghi+'n2782d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n2782ab',
                          'n2782c',
                          'n2782d']

execfile(stinghi+'n2782_config.py')
xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
