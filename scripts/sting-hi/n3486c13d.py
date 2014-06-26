execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n3486/13A-107.sb21767248.eb24085777.56481.08748224537.ms'
xp['importspw']         ='0'
xp['importscan']        ='2~18'
xp['importmode']        ='ms'
xp['importchanbin']     =1
xp['importtimebin']     ='30s'


# CALIBRATION
xp['source']            ='NGC3486'
xp['spw_source']        ='0'

xp['fluxcal']           = '1331+305=3C286'
xp['uvrange_fluxcal']   =''
xp['phasecal']          = 'J1125+2610'
xp['uvrange_phasecal']  =''

xp['flagselect']        =[]
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
execfile(stinghi+'n3486_config.py')

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
