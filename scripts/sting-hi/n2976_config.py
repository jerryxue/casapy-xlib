# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~11;53~60'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**5*10
xp['cell']              ='8.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='-150km/s'
xp['clean_width']       ='5.2km/s'
xp['clean_nchan']       =int((170.+150.)/5.2)
xp['phasecenter']       ='J2000 09h47m15.40 67d54m59.00'




