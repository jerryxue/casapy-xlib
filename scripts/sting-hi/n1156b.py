
#
execfile(xlib+'xinit.py')


xp['prefix']   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles'] = ['../../../raw/21cm/n1156/AM418_5',
                  '../../../raw/21cm/n1156/AM418_6']


xp['source']            = 'NGC1156'
xp['spw_source']        = '0,1'

xp['fluxcal']           = '0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          = '0318+164' 
xp['phasecal_uvrange']  ='<100klambda'
xp['passcal']           = '0137+331'
xp['passcal_uvrange']   ='<40klambda'

xp['flagspw']   ='*:0~3;123~126'
xp['flagselect'] = [    "antenna='VA20&VA26'  spw='0' timerange='09:36:35~09:36:50'",
                "antenna='VA02&VA26'  spw='0' timerange='17:24:10~17:24:20'",
                "antenna='VA22&VA27'  spw='1' timerange='17:10:40~17:10:50'",
                "antenna='VA02&VA26'  spw='0' timerange='11:14:20~11:15:00'",
                "antenna='VA02&VA26'  spw='0' timerange='12:42:10~12:42:20'",
                "antenna='VA10&VA26'  spw='0' timerange='12:42:10~12:42:20'",
                "antenna='VA26' spw='0' timerange='17:13:42~17:13:48'",
                "antenna='VA17' spw='0'",
                "antenna='VA22' timerange='09:35:20~09:36:00'",
                "timerange='17:15:20~17:16:00' field='0137+331'",
                "timerange='13:28:00~13:29:20'",
                "antenna='VA27' timerange='14:59:00~14:59:40'",
                "timerange='17:10:40~17:11:00'",
                "timerange='09:41:40~09:41:50'",
                "antenna='VA10&VA26'",
                "antenna='VA26&VA28'",
                "antenna='VA20&VA26'",
                 "antenna='VA18&VA26'",
                 "antenna='VA23&VA26'",
                 "antenna='VA08&VA26'",
                 "antenna='VA02&VA26'",
                 "antenna='VA03&VA26'"
                ]

xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='0:4~7;119~122,1:4~7;119~122'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True
xp['imsize']            =512+256
xp['cell']              ='2.0arcsec'

xp['cleanmode'] = 'velocity'
xp['clean_start']='300km/s'
xp['clean_nchan']=58
xp['clean_width']='2.6km/s'
xp['phasecenter']='J2000 02h59m42.2 +25d14m14.0'



line_vrange=[280,460]

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
