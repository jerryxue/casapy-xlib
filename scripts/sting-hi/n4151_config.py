xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='0:12~20;35~40'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**5*10
xp['cell']              ='8.0arcsec'

xp['cleanmode']            ='velocity'
xp['clean_start']        ='456km/s'
xp['clean_width']        ='20.8km/s'
xp['clean_nchan']        =int((1520-456)/20.8+1)
xp['phasecenter']        ='J2000 12h10m32.6 +39d24m21.0'


