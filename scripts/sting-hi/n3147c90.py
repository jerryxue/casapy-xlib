execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n3147/AV183_2',\
                          '../n3147/AV183_3']
xp['starttime']         ="1989/12/15/05:48:45"
xp['stoptime']          ="2003/06/22/23:59:55"

# CALIBRATION
xp['source']            ='N3147'
xp['fluxcal']           ='0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='0945+664'
xp['phasecal_uvrange']  ='<15klambda'
xp['spw_source']        ='0'

xp['flagspw']           ='*:0;60~62'
xp['flagselect']        =["timerange='16:26:40~16:40:00' antenna='VA02&VA24'",
                          "timerange='16:40:20~16:41:40'",
                          "timerange='19:16:35~19:17:00'",
                          "timerange='10:25:50~10:28:20'",
                          "timerange='16:40:40~16:41:20'",
                          "timerange='10:18:10~10:18:50'",
                          "timerange='16:40:00~16:41:00' field='N3147'",
                          "antenna='VA19&VA28'",
                          "antenna='VA17&VA26'"]

execfile(stinghi+'n3147_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
