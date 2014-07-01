# execfile(stinghi+'n4536d87.py')
# execfile(stinghi+'n4536c04.py')
# execfile(stinghi+'n4536d09.py')
# execfile(stinghi+'n4536b09a.py')
# execfile(stinghi+'n4536b09b.py')
# execfile(stinghi+'n4536b13a.py')
# execfile(stinghi+'n4536b13b.py')
# execfile(stinghi+'n4536b13c.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n4536d87',
                          'n4536c04',
                          'n4536d09',
                          'n4536b09a',
                          'n4536b09b',
                          'n4536b13a',
                          'n4536b13b',
                          'n4536b13c']

execfile(stinghi+'n4536_config.py')
xp['imsize']            =2**7*10
xp['cell']              ='2arcsec'
xp['clean_start']       ='1581.2km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =24

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')