execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../../../raw/21cm/n1569/AW605_12'

# CALIBRATION
xp['source']            ='NGC1569'
xp['spw_source']        ='4,5'

xp['fluxcal']           ='0538+498'
xp['uvrange_fluxcal']   ='<50klambda'
xp['spw_fluxcal']       ='0,1,2,3'
xp['phasecal']          ='0404+768'
xp['uvrange_phasecal']  =''

xp['flagspw']           ='*:0~10;112~126'
xp['flagselect']        =[    "mode='quack' quackinterval=6.0",
                "antenna='VA26' timerange='05:54:10~05:55:10'",
                "antenna='VA26' timerange='05:54:10~05:55:10'",
                "antenna='VA09' timerange='11:01:40~11:05:50'",
                "antenna='VA06' timerange='06:54:10~06:54:20'",
                "timerange='11:00:00~11:10:00'",
                "antenna='VA11&VA18'",
                "timerange='05:09:40~05:10:15' field='0538+498'",
                "timerange='12:16:40~12:19:20' field='0538+498'"
                ]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='4:11~20;98~111,5:11~20;98~111'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='-215km/s'
xp['clean_width']       ='5.2km/s'
xp['clean_nchan']       =50
xp['phasecenter']       ='J2000 04h30m49.06 64d50m52.61'
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')

