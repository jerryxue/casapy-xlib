# [1760,2060]
execfile(stinghi+'n5713c12a.py')
execfile(stinghi+'n5713c12b.py')
execfile(stinghi+'n5713c92.py')
execfile(stinghi+'n5713d99.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n5713c12a',
                          'n5713c12b',
                          'n5713c92',
                          'n5713d99']

execfile(stinghi+'n5713_config')

xp['imsize']            =2**7*10
xp['cell']              ='4.0arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

