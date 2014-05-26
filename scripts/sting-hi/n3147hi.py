execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n3147a03',
                          'n3147bc04',
                          'n3147c90',
                          'n3147d03b',
                          'n3147d89',
                          'n3147d03a',
                          'n3147b13a',
                          'n3147b13b',
                          'n3147b13c']

execfile(stinghi+'n3147/n3147_config.py')

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['mosweight']         =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
