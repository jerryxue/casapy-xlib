execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      ='../n1569/AW325_6'
xp['starttime']     ='1993/06/29/12:06:45.0'
xp['stoptime']      ='1993/06/29/17:57:15.0'

# TRACK INFORMATION
xp['source']             = 'NGC1569'

xp['fluxcal']             = '0137+331'
xp['fluxcal_uvrange']    ='<40klambda'
xp['phasecal']             = '0614+607_0'
xp['phasecal_uvrange']    =''

xp['spw_source']         = '4,5'
xp['spw_fluxcal']         = '0,1'
xp['spw_phasecal']         = '0,1,2,3'
xp['flagspw']            ='*:0~10;112~126'

# CALIBRATION & OPTIONS
xp['flagselect']         =[
                "mode='quack' quackinterval=6.0",
                "timerange='13:46:40~13:47:20'",
                "timerange='13:49:50~13:50:10'",
                "timerange='17:33:20~17:47:30.0'",
                "timerange='12:23:15.0~13:05:30.0'",
                "antenna='VA23&VA25'","antenna='VA03&VA23'",
                "antenna='VA11&VA12'",
                "antenna='VA19&VA25'",
                "antenna='VA19&VA23'",
                "antenna='VA06&VA19'",
                "antenna='VA04&VA25'",
                "antenna='VA18&VA23'",
                "antenna='VA17&VA24'",
                "antenna='VA12&VA20'",
                "antenna='VA05&VA20'",
                "antenna='VA05&VA18'",
                "antenna='VA04&VA23'",
                "antenna='VA04&VA18'",
                "antenna='VA03&VA04'",
                "antenna='VA11'",
                "antenna='VA02&VA23'",
                "antenna='VA04&VA05'",
                "antenna='VA04&VA19'",
                "antenna='VA03&VA25'",
                "antenna='VA02&VA03'",
                "antenna='VA03&VA19'",
                "scan='2'",
                "scan='4'"
                ]

execfile(stinghi+'n1569_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')





