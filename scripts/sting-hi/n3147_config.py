# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~16;40~56'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**5*10
xp['cell']              ='8.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2200.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =int((3400-2200)/20.8)
xp['phasecenter']       ='J2000 10h16m53.6 +73d24m03.0'
