execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4151/AB658_7','../n4151/AB658_8']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='17~22'
xp['importspw']     ='8~9'



# TRACK INFORMATION
xp['source']         = 'NGC4151'
xp['spw_source']    ='0,1'

xp['fluxcal']         = '1328+307'
xp['fluxcal_uvrange']='0,1'
xp['phasecal']         = '1225+368' 
xp['phasecal_uvrange']='0,1'

xp['flagspw']    ='*:30'

# CALIBRATION & OPTIONS
xp['flagselect'] =     []

execfile(stinghi+'n4151_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

