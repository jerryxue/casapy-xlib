execfile(xlib+'xinit.py')

xp['prefix']        ='n2976c08b'
xp['rawfiles']      =['../n2976/AC921_18']
xp['starttime']     ='2008/05/24/21:31:45.0'
xp['stoptime']      ='2008/05/24/23:24:25.0'

# TRACK INFORMATION
xp['source']         ='NGC2976'

xp['fluxcal']             ='1331+305'
xp['phasecal']             = '0841+708'
xp['phasecal_uvrange']    ='<20klambda'

xp['spw_source']         = '0'
xp['flagspw']            ='*:0~40;117~126'

# CALIBRATION & OPTIONS
xp['flagselect'] = [  "antenna='VA08&EA17'",
                "antenna='EA11&VA20'",
                "antenna='EA21'",
                "antenna='VA20&EA23' timerange='21:47:10.0~21:47:40.0'",
                "antenna='VA09&EA17' timerange='21:11:45.0~21:12:00.0'",
                "antenna='VA12&EA17' timerange='22:45:00.0~22:45:20.0'",
                "antenna='EA17&EA19' timerange='22:45:00.0~22:45:20.0'",
                "antenna='VA10&EA11'",
                "antenna='VA12&EA25'",
                "antenna='VA15&EA25'",
                "antenna='EA19&EA25'",
                "antenna='EA16&EA19'"
                ]

execfile(stinghi+'n2976_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')




