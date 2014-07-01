#  [865,1120]

# execfile(stinghi+'n4151a1.py')
# execfile(stinghi+'n4151a2.py')
# execfile(stinghi+'n4151a3.py')
# execfile(stinghi+'n4151b93.py')
# execfile(stinghi+'n4151c1.py')
# execfile(stinghi+'n4151c2.py')


execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n4151a1',
                          'n4151a2',
                          'n4151a3',
                          'n4151b93',
                          'n4151c1',
                          'n4151c2']

execfile(stinghi+'n4151_config.py')
xp['imsize']            =2**7*10
xp['cell']              ='2.0arcsec'
xp['clean_start']        ='726.4km/s'
xp['clean_width']        ='20.8km/s'
xp['clean_nchan']        =int((1267.2-726.4)/20.8+1)

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
