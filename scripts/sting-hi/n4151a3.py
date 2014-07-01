execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4151/AM591_14','../n4151/AM591_15']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='21~28'
xp['importspw']     ='3'

# TRACK INFORMATION
xp['source']         = 'NGC4151'
xp['spw_source']    ='0'

xp['fluxcal']         = '1328+307'
xp['fluxcal_uvrange']=''
xp['phasecal']         = '1223+395' 
xp['phasecal_uvrange']=''


xp['flagspw']    ='*:0;59~62'

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

