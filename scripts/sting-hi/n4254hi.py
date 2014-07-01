#execfile(stinghi+'n4254b1.py')
#execfile(stinghi+'n4254b2.py')
#execfile(stinghi+'n4254b3.py')
#execfile(stinghi+'n4254b13a.py')
#execfile(stinghi+'n4254b13b.py')
#execfile(stinghi+'n4254c.py')
#execfile(stinghi+'n4254d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n4254c','n4254d',
                          'n4254b1','n4254b2',
                          'n4254b3','n4254b13a',
                          'n4254b13b']

execfile(stinghi+'n4254_config.py')
xp['imsize']            =2**6*10
xp['cell']              ='2.0arcsec'
xp['clean_start']       ='2214.8km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =36

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['mosweight']         =True

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
