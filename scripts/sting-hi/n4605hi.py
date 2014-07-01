#execfile(stinghi+'n4605b.py')
#execfile(stinghi+'n4605c.py')
#execfile(stinghi+'n4605d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n4605b',
                          'n4605c',
                          'n4605d']

execfile(stinghi+'n4605_config.py')
xp['clean_start']       ='1.6km/s'
xp['clean_nchan']       =15
xp['imsize']            =2**6*10
xp['cell']              ='2.0arcsec'

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


