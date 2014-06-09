execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n4605b',
                          'n4605c',
                          'n4605d']

execfile(stinghi+'n4605_config')

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


