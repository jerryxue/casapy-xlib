execfile(xlib+'xinit.py')

xp['prefix']        ='n2976c03'
xp['rawfiles']      =['../n2976/AT285_13','../n2976/AT285_14']
xp['importfield']   =['NGC2976','0841+708','0542+498']
xp['importscan']    ='2~20'
xp['importspw']    ='0~5'

# TRACK INFORMATION
xp['source']            ='NGC2976'

xp['fluxcal']           ='0542+498'
xp['fluxcal_uvrange']   ='<50klambda'
xp['phasecal']          = '0841+708'
xp['phasecal_uvrange']  ='<20klambda'

xp['spw_source']        = '0,1'
xp['spw_fluxcal']       ='2,3,4,5'
xp['spw_phasecal']      ='2,3,4,5'
xp['flagspw']           ='*:0~5;116~126'

# CALIBRATION & OPTIONS
xp['flagselect']     =    [
                    "mode='quack' quackinterval=3.0",
                    "timerange='07:06:40~07:40:00' field='0542+498'",
                    "antenna='VA07&VA08' timerange='07:32:08~07:32:12'",
                    "antenna='VA14&VA15'",
                    "antenna='VA09&VA15'",
                    "antenna='VA03&VA15'",
                    "antenna='VA02&VA03'",
                    "antenna='VA03&VA14'",
                    "antenna='VA09&VA18'",
                    "antenna='VA11&VA14'",
                    "antenna='VA02&VA09'",
                    "antenna='VA07&VA08'"
                ]
execfile(stinghi+'n2976_config.py')
xp['niter']        =0


execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')




