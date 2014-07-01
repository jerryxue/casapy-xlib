#-124->95
# execfile(stinghi+'n2976b02.py')
# execfile(stinghi+'n2976c02a.py')
# execfile(stinghi+'n2976c02b.py')
# execfile(stinghi+'n2976c03.py')
# execfile(stinghi+'n2976c08a.py')
# execfile(stinghi+'n2976c08b.py')
# execfile(stinghi+'n2976d03.py')

execfile(xlib+'xinit.py')

xp['prefix_comb']=['n2976b02',
                    'n2976c02a',
                    'n2976c02b',
                    'n2976c03',
                    'n2976d03',
                    'n2976c08a',
                    'n2976c08b']
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

execfile(stinghi+'n2976_config.py')
xp['imsize']            =2**7*10
xp['cell']              ='2.0arcsec'
xp['clean_start']       ='-134.4km/s'
xp['clean_width']       ='5.2km/s'
xp['clean_nchan']       =int((170.+150.)/5.2)-4

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
