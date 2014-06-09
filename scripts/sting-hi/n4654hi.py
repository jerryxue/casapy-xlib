xp['prefix_combine']    =['n4654c','n4654d']
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS

execfile(stinghi+'n1156_config')

p['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
