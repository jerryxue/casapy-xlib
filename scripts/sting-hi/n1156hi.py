#280->460
#execfile(stinghi+'n1156b.py')
#execfile(stinghi+'n1156c.py')
#execfile(stinghi+'n1156d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n1156b',
                          'n1156c',
                          'n1156d']

execfile(stinghi+'n1156_config.py')
xp['uvcs']              =True

xp['imsize']            =2**7*10
xp['cell']              ='2.0arcsec'

xp['clean_start']       ='301.95km/s'
xp['clean_width']       ='3.9km/s'
xp['clean_nchan']       =37

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =-1
xp['usescratch']        =True
xp['clean_mask']        ='circle[[02h59m42.2s,+25d14m14.0s],375arcsec]'


# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
