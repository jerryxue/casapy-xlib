execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            ='n3486hi'
xp['prefix_comb']       =['n3486d91',
                          'n3486b13a',
                          'n3486b13b']
xp['spwrgd']            ='spw'
xp['uvcs']              =True
xp['fitspw']            ="*:0~3;44~46"

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='400km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =47
xp['phasecenter']       ='J2000 11h00m23.9 +28d58m29.0'

xp['outertaper']        =['10arcsec']
xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
