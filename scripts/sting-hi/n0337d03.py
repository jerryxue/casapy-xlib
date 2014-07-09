execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      ='../n0337/AT285_1'
xp['importspw']     ='0,1'

# CALIBRATION
xp['source']            ='NGC0337'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          ='0059+001'

xp['flagspw']           ="0:0~4;60~62,1:0;58~62"
xp['flagselect']        =[  "timerange='2003/02/16/22:06:02~22:06:30' field='0137+331'",
                            "antenna='VA08&VA11'",
                            "antenna='VA20&VA11'",
                            "antenna='VA03&VA08'",
                            "antenna='VA03&VA09'",
                            "antenna='VA03&VA10'",
                            "antenna='VA14&VA27'",
                            "antenna='VA08&VA14'",
                            "antenna='VA08&VA10'",
                            "antenna='VA04&VA20'",
                            "antenna='VA10&VA15'",
                            "antenna='VA09&VA19'",
                            "antenna='VA02&VA03'"]
addselect=["antenna='VA12&VA28'",
 "antenna='VA03&VA27'",
 "antenna='VA21&VA24'",
 "antenna='VA10&VA14'",
 "antenna='VA07&VA24'",
 "antenna='VA03&VA17'",
 "antenna='VA12&VA21'",
 "antenna='VA07&VA17'"]
xp['flagselect']=xp['flagselect']+addselect
execfile(stinghi+'n0337_config.py')
xp['fitorder']          =0

xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

