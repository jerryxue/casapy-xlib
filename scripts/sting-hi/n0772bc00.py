execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
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
xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2

# CONSOLIDATING
xp['spwrgd']            =''
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='0:3~14;47~55'
xp['fitorder']          =1
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~5;33~38'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512
xp['cell']              ='6.0arcsec'

xp['cleanmode']        ='velocity'
xp['clean_start']       ='2050.0km/s'
xp['clean_width']       ='20.8km/s'
# evla tracks have nchan=39 to avoid spws with different corrs merging into one.
xp['clean_nchan']       =40
xp['phasecenter']      ='J2000 01h59m19.58 +19d00m27.10'

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')

