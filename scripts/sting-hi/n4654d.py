execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4654/AP206_1']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     ='1'


# TRACK INFORMATION
xp['source']        = 'NGC4654'

xp['fluxcal']       = '1331+305'
xp['phasecal']      = '1221+282'

xp['spw_source']    = '0'
xp['spw_edge']      = '*:0~5;58~62'

# CALIBRATION & OPTIONS
xp['flagselect']    =["antenna='VA10'"]

execfile(stinghi+'n4654_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


