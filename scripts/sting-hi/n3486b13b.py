execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='../n3486/13B-363.sb24635611.eb28563417.56632.4332934375.ms'
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
xp['syscal']            =''

# CONSOLIDATING
execfile(stinghi+'n3486_config.py')

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
