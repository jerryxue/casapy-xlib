execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            ='n4536hi'
xp['prefix_comb']       =['n4536d87',
                          'n4536c04',
                          'n4536d09',
                          'n4536b09a',
                          'n4536b09b',
                          'n4536b13a',
                          'n4536b13b',
                          'n4536b13c']

execfile(stinghi+'n4536/n4536_config.py')

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['mosweight']         =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')