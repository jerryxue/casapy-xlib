xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['imcs']              =True
xp['fitchans']          ='0~2,39~42'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**5*10
xp['cell']              ='8.0arcsec'

xp['cleanmode']         = 'velocity'
xp['clean_start']        ='360.00km/s'
xp['clean_width']        ='5.2km/s'
xp['clean_nchan']        =int((960.-360.)/5.2)
xp['phasecenter']        ='J2000 10h19m54.92 +45d32m59.0'



