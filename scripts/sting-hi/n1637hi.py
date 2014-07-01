#588->838
#execfile(stinghi+'n1637b.py')
#execfile(stinghi+'n1637c.py')
#execfile(stinghi+'n1637d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n1637b',
                          'n1637c',
                          'n1637d']

execfile(stinghi+'n1637_config.py')

#xp['outertaper']        =['10arcsec']
xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
