execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n1637b13a',
                          'n1637c96',
                          'n1637d03']
xp['spwrgd']            ='spw'
xp['uvcs']              =True
xp['fitspw']            ='*:0~2;41~43'

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='485km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =44
xp['phasecenter']       ='J2000 04h41m28.2 -02d51m29.0'

#xp['outertaper']        =['10arcsec']
xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
