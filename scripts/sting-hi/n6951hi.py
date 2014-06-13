#    line_vrange=[1225,1607]
#execfile(stinghi+'n6951b06.py')
#execfile(stinghi+'n6951c02.py')
#execfile(stinghi+'n6951c04.py')
#execfile(stinghi+'n6951d03.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n6951d03',
                          'n6951c04',
                          'n6951b06',
                          'n6951c02']

execfile(stinghi+'n6951_config.py')


xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

