execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['../n3147/AB1069_11',\
                          '../n3147/AB1069_12']
xp['starttime']         ="1989/12/15/05:48:45"
xp['stoptime']          ="2003/06/22/23:59:55"

# CALIBRATION
xp['source']            ='NGC3147'
xp['fluxcal']           ='1328+307'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='0950+748'
xp['phasecal_uvrange']  ='>15klambda'
xp['spw_source']        ='0'

xp['flagspw']           ='*:60~62'
xp['flagselect']        =["timerange='21:53:00~21:56:00'",
                          "timerange='23:12:00~23:17:40'",
                          "timerange='23:34:00~23:35:40'",
                          "antenna='VA04'",
                          "mode='quack' quackinterval=10.0 field='0950+748'"]
xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2

execfile(stinghi+'n3147_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
