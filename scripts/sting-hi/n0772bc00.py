execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='../n0772/AT237_6'
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
# mode='shadow' doesn't work with B1960 in v4.2
xp['flagselect_default']=[]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['uvcs']              =True
xp['fitspw']            ='*:2~5;37~40'
xp['scalewt_minsamp']   =8
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =256
xp['cell']              ='12.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2005.2km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =42
xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')



