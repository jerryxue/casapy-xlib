#-105->95
#execfile(stinghi+'n2976b02.py')
execfile(stinghi+'n2976c02a.py')
execfile(stinghi+'n2976c02b.py')
execfile(stinghi+'n2976c03.py')
execfile(stinghi+'n2976c08a.py')
execfile(stinghi+'n2976c08b.py')
execfile(stinghi+'n2976d03.py')

execfile(xlib+'xinit.py')

xp['prefix_combine']=['n2976b02',
                    'n2976c02a',
                    'n2976c02b',
                    'n2976c03',
                    'n2976d03',
                    'n2976c08a',
                    'n2976c08b']
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

execfile(stinghi+'n2976_config')
xp['imsize']            =2**6*10
xp['cell']              ='4.0arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
