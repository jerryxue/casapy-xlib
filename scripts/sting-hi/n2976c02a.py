execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =[rawdir+'n2976/AT285_9',
                      rawdir+'n2976/AT285_10']
xp['importfield']   =['NGC2976','0841+708','0542+498']
xp['importscan']    ='2~20'
xp['importspw']     ='0~5'


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
xp['flagselect'] =    [
                    " antenna='VA07&VA08' timerange='13:36:30~13:37:00' ",
                    " antenna='VA03&VA15' timerange='13:38:20~13:45:00' ",
                    " antenna='VA03&VA15' timerange='13:40:00~14:46:40' ",
                    " antenna='VA14&VA15' ",
                    " antenna='VA02&VA24' ",
                    " antenna='VA03&VA15' ",
                    " antenna='VA02&VA15' ",
                    " antenna='VA02&VA03' ",
                    " antenna='VA02&VA03' timerange='13:40:00~14:46:40' ",
                    " mode='quack' quackinterval=10. ",
                    " antenna='VA02&VA14;VA02&VA15;VA02&VA24;VA06&VA08;VA06&VA24;VA03&VA24' \
                        timerange='13:38:20~13:45:00' ",
                    " antenna='VA02&VA14;VA02&VA15;VA02&VA24;VA06&VA08;VA06&VA24;VA03&VA24' \
                        timerange='14:00:00~14:13:20' ",
                    " antenna='VA03&VA14' timerange='13:38:20~15:00:00' "    
                ]

execfile(stinghi+'n2976_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')







