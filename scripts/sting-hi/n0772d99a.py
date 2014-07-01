execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../n0772/AG564_3'
xp['importspw']         ='1'

# CALIBRATION
xp['source']            ='ARP78'
xp['spw_source']        ='0'

xp['fluxcal']           = '0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = '0204+152'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagspw']           ='0:0~4;119~126'
xp['flagselect']        = [ "antenna='VA12&VA17' timerange='17:44:35~17:44:55'",
                            "timerange='01:00:00~17:44:10'", "antenna='VA05'",
                            "antenna='VA04&VA27'","antenna='VA03&VA27'",
                            "antenna='VA06&VA25'",
                            "antenna='VA12'","antenna='VA02&VA16'",
                            "antenna='VA06&VA24'","antenna='VA11&VA24'",
                            "field='0204+152' uvrange='<1klambda'",
                            "antenna='VA21'",
                            "antenna='VA14&VA24'"]
xp['flagselect']        =[  "antenna='VA12&VA17' timerange='17:44:35~17:44:55'",
                            "field='0204+152' uvrange='<1.2klambda' scan='5'",
                            "field='ARP78' uvrange='<1.2klambda' timerange='01:00:00~17:44:10'"
                            ]

execfile(stinghi+'n0772_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

