# execfile(stinghi+'n3486c13a.py')
# execfile(stinghi+'n3486c13b.py')
# execfile(stinghi+'n3486c13c.py')
# execfile(stinghi+'n3486c13d.py')
# execfile(stinghi+'n3486c13e.py')
# execfile(stinghi+'n3486b13b.py')
# execfile(stinghi+'n3486b13a.py')
# execfile(stinghi+'n3486d91.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n3486d91',
                          'n3486b13a',
                          'n3486b13b',
                          'n3486c13a',
                          'n3486c13b',
                          'n3486c13c',
                          'n3486c13d',
                          'n3486c13e']

# CONSOLIDATING
execfile(stinghi+'n3486_config.py')
xp['imsize']            =2**7*10
xp['cell']              ='2.0arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
