execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../n0772/13B-363.sb24635393.eb28501581.56608.280407708335.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~13'
xp['importmode']        ='ms'
xp['importchanbin']     =6

# CALIBRATION
xp['source']            ='NGC0772'
xp['spw_source']        ='0,1'

xp['fluxcal']           = '0137+331=3C48'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = 'J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagselect']        =["timerange='2013/11/12/06:49:12.5~2013/11/12/06:49:14.5'",
                          "timerange='2013/11/12/07:32:54.5~2013/11/12/07:32:56.5'",
                          "timerange='2013/11/12/08:17:03.5~2013/11/12/08:17:05.5'"]
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
execfile(stinghi+'n0772_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
