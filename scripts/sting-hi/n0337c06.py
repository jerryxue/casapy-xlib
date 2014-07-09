execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      ='../n0337/AM0873_3'
xp['importspw']     ='0,1'
    
# CALIBRATION
xp['source']            ='NGC0337'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          ='0059+001'


xp['flagspw']           ="0:0~4;60~62,1:0;58~62"
xp['flagselect']        =["timerange='04:45:30~04:50:49'",
                          "timerange='04:43:20~04:44:50'",
                          "antenna='VA11&VA21'",
                          "antenna='VA06&VA21'",
                          "antenna='VA06&VA11'",
                          "antenna='VA03&VA04'",
                          "antenna='VA09' timerange='2006/11/04/04:48:20~04:56:40' field='NGC0337' spw='0:29~30'",
                          "timerange='2006/11/04/03:25:00~03:26:40' antenna='VA06&VA15'",
                          "timerange='2006/11/04/02:28:40~02:29:30' antenna='VA07&VA15'",
                          "timerange='2006/11/04/01:59:35~01:59:45'",
                          "timerange='2006/11/04/03:07:15~03:07:25'",
                          "timerange='2006/11/04/04:15:00~04:15:15'",
                          "timerange='2006/11/04/10:03:45~10:04:15'",
                          "timerange='2006/11/04/10:04:54~10:05:06'",
                          "timerange='2006/11/04/10:06:04~10:06:16'",
                          "timerange='2006/11/04/04:33:06~04:34:05'"]

execfile(stinghi+'n0337_config.py')
xp['niter']             =0
xp['fitorder']          =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
