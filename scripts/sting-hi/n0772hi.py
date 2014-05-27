#2172->2716
execfile(stinghi+'n0772b13a.py')
execfile(stinghi+'n0772b13b.py')
execfile(stinghi+'n0772b13c.py')
execfile(stinghi+'n0772bc13a.py')
execfile(stinghi+'n0772bc13b.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n0772d99a',
                          'n0772d99b',
                          'n0772bc00',
                          'n0772bc13a',
                          'n0772bc13b',
                          'n0772b13a',
                          'n0772b13b',
                          'n0772b13c']
xp['spwrgd']            ='spw'
xp['uvcs']              =True
xp['fitspw']            ='*:0~5;33~38'

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='4.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2050.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =39
xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
