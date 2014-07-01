execfile(xlib+'xinit.py')
rawdir='../'
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']      =[rawdir+'n2976/AC921_17']
xp['starttime']     ='2008/05/04/21:20:45.0'
xp['stoptime']      ='2008/05/04/23:13:15.0'

# TRACK INFORMATION
xp['source']         ='NGC2976'

xp['fluxcal']             ='1331+305'
xp['phasecal']             = '0841+708'
xp['phasecal_uvrange']    ='<20klambda'

xp['spw_source']         = '0'
xp['flagspw']            ='*:0~40;117~126'

# CALIBRATION & OPTIONS
xp['flagselect'] = [
                "antenna='VA08&EA17'",
                "antenna='EA11&VA20'",
                "antenna='EA21'",
                "antenna='VA03&VA20'",
                "antenna='VA20&EA23' timerange='21:47:20.0~21:47:30.0'",
                "antenna='VA09&EA17' timerange='21:11:50.0~21:12:00.0'",
                "antenna='VA12&EA17' timerange='22:45:00.0~22:45:10.0'",
                "antenna='EA17&EA19' timerange='22:45:00.0~22:45:10.0'",
                "antenna='VA12&EA25'",
                "antenna='VA15&EA25'",
                "antenna='VA15&EA19'",
                "antenna='EA16&EA19'",
                "antenna='EA05&VA28'"
                ]

execfile(stinghi+'n2976_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



