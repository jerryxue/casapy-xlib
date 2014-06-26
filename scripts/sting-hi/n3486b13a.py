execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../n3486/13B-363.sb24635611.eb28558623.56626.60561628472.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~13'
xp['importmode']        ='ms'
xp['importchanbin']     =6


# CALIBRATION
xp['source']            ='NGC3486'
xp['spw_source']        ='0,1'

xp['fluxcal']           = '1331+305=3C286'
xp['uvrange_fluxcal']   =''
xp['phasecal']          = 'J1120+1420'
xp['uvrange_phasecal']  =''

xp['flagselect']        =[]
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
execfile(stinghi+'n3486_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
