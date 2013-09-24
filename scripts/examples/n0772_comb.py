execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            ='n0772hi'
xp['prefix_comn']       =['n0772d99a',
                          'n0772d99b',
                          'n0772bc00',
                          'n0772bc13a',
                          'n0772bc13b']
xp['uvcs']              =True

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512
xp['cell']              ='6.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2050.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =39
xp['phase_center']      ='J2000 01h59m19.58 +19d00m27.10'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
