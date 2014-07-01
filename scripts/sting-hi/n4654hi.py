#execfile(stinghi+'n4654d.py')
#execfile(stinghi+'n4654c.py')

execfile(xlib+'xinit.py')

xp['prefix_comb']       =['n4654c','n4654d']
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS

execfile(stinghi+'n4654_config.py')
xp['clean_start']    ='810.6km/s'
xp['clean_nchan']    = 54

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
