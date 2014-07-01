# -170->5
#execfile(stinghi+'n1569b.py')
#execfile(stinghi+'n1569c.py')
#execfile(stinghi+'n1569d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n1569b',
                          'n1569c',
                          'n1569d']

execfile(stinghi+'n1569_config.py')
xp['scalewt']           =True
xp['imsize']            =2**6*10
xp['cell']              ='2.0arcsec'
xp['clean_start']       ='-231km/s'
xp['clean_width']       ='2.6km/s'
xp['clean_nchan']       =113

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
