execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']      =['../n3198/AT285_11']
xp['starttime']     ='2003/03/27/06:16:50.0'
xp['stoptime']      ='2003/03/27/06:45:30.0'

# TRACK INFORMATION
xp['source']        ='NGC3198'
xp['spw_source']    ='0,1'

xp['fluxcal']             = '1331+305'
xp['fluxcal_uvrange']    =''
xp['phasecal']             = '1006+349'
xp['phasecal_uvrange']    ='<30klambda'

# CALIBRATION & OPTIONS
xp['flagspw']       ='*:0;60~62'
xp['flagselect'] =  [    "timerange='2003/03/27/06:04:10~06:25:25' field='1331+305'",
                "mode='quack' quackinterval=20.0 field='1006+349'"]



execfile(stinghi+'n3198_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')




