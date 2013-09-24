execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n0772bc00' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/sting-hi/msc/n0772/raw/AT237_6'
xp['importspw']         ='1'

# CALIBRATION
xp['source']            ='NGC772'
xp['spw_source']        ='0'

xp['fluxcal']           = '0134+329'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = '0202+149'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagspw']           ='0:0~2;60~62'
xp['flagselect']        = [ "antenna='VA07'","antenna='VA17'",
                            "uvrange='<1000lambda' field='0134+329'",
                            "uvrange='<1700lambda' field='0202+149'",
                            "antenna='VA16' timerange='18:38:10~18:38:20'",
                            "antenna='VA16' timerange='18:39:40~18:39:50'"]

# CONSOLIDATING
xp['uvcs']              =True
xp['fitspw']            ='0:3~14;47~55'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512
xp['cell']              ='6.0arcsec'

xp['cleanmode']        ='velocity'
xp['clean_start']       ='2050.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =39
xp['phase_center']      ='J2000 01h59m19.58 +19d00m27.10'

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
xu.checkstatwt(xp['prefix']+'.src.ms',fitspw=xp['fitspw'])
execfile(xlib+'xclean.py')

