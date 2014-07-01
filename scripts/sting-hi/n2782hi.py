#2390,2725

execfile(stinghi+'n2782ab.py')
execfile(stinghi+'n2782c.py')
execfile(stinghi+'n2782d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n2782ab',
                          'n2782c',
                          'n2782d']

execfile(stinghi+'n2782_config.py')
xp['imsize']            =2**6*10
xp['cell']              ='4.0arcsec'
xp['clean_start']    ='2252km/s'
xp['clean_nchan']    =int((2824-2252.)/10.4)

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
