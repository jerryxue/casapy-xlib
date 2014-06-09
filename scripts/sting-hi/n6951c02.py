execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n6951/AM737_1','../n6951/AM737_2']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     =''

# TRACK INFORMATION
xp['source']        = 'NGC6951'

xp['fluxcal']       = '0542+498'
xp['fluxcal_uvrange']   =''
xp['phasecal']      = '2022+616'
xp['phasecal_uvrange']  =''

xp['spw_source']    = '0,1'
xp['flagspw']       = '0:0~10;28~30,1:0~2;21~30'

# CALIBRATION & OPTIONS
xp['flagselect']    = [  "timerange='2002/10/18/00:31:45.0~2002/10/20/00:31:45.0'",
                "antenna='VA10'",
                "timerange='2002/10/20/02:56:35~2002/10/20/02:56:55'",
                "timerange='2002/10/20/04:03:35~2002/10/20/04:03:55'",
                "timerange='27:46:20~27:47:00'",
                "timerange='26:37:00~30:00:00' field='NGC6951'",
                "timerange='26:37:00~30:00:00' field='2022+616'"
                 ]

execfile(stinghi+'n6951_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



 



