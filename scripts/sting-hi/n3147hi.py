execfile(xlib+'xinit.py')

xp['prefix_comb']       =['n3147a03',
                          'n3147bc04',
                          'n3147c90',
                          'n3147d03b',
                          'n3147d89',
                          'n3147d03a',
                          'n3147b13a',
                          'n3147b13b',
                          'n3147b13c']
# for one in xp['prefix_comb']:
#     execfile(stinghi+one+'.py')     
    
# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n3147a03',
                          'n3147bc04',
                          'n3147c90',
                          'n3147d03b',
                          'n3147d89',
                          'n3147d03a',
                          'n3147b13a',
                          'n3147b13b',
                          'n3147b13c']

execfile(stinghi+'n3147_config.py')

xp['imsize']            =2**7*10
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2532.8km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =int((3052.8-2532.8)/20.8)+1

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
