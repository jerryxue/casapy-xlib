execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n5713/AP225_1']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     =''


# TRACK INFORMATION
xp['source']        = 'NGC5713'
xp['spw_source']    ='0'

xp['fluxcal']           = '1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          = '1445+099'
xp['phasecal_uvrange']  =''

xp['flagspw']           ="*:0~4;56~62"
xp['flagselect']        =["timerange='12:33:40.0~12:36:30.0'"]

execfile(stinghi+'n5713_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



