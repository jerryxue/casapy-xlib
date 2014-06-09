execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n3486d91',
                          'n3486b13a',
                          'n3486b13b']

# CONSOLIDATING
execfile(stinghi+'n3486_config.py')

xp['outertaper']        =['10arcsec']
xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
