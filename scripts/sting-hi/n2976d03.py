execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']      =[rawdir+'n2976/AB1038_15',rawdir+'n2976/AB1038_16']
xp['starttime']     ='2003/05/10/02:46:15.0'
xp['stoptime']      ='2003/05/10/04:21:55.0'
xp['importspw']     ='0'
xp['importfield']   =['NGC2976','1331+305','0921+622']

# TRACK INFORMATION
xp['source']         = 'NGC2976'

xp['fluxcal'] = '1331+305'
xp['phasecal'] = '0921+622'

xp['spw_source'] = '0'
xp['flagspw']='0:0~4;57~62'

# CALIBRATION & OPTIONS
xp['flagselect'] =    [
                    "mode='quack' quackinterval=5.0 ",
                    "antenna='VA20' timerange='03:20:14~03:20:16'",
                    "antenna='VA20&VA28' timerange='02:40:40~02:50:50'",
                    "timerange='04:14:00~04:14:10' field='1331+305'"
                    "antenna='VA03&VA09'",
                    "antenna='VA02&VA17'",
                    "antenna='VA09&VA19'",
                    "antenna='VA15&VA27'",
                    "antenna='VA03&VA10'",
                    "antenna='VA03&VA27'",
                    "antenna='VA16&VA26'",
                    "antenna='VA14&VA27'",
                    "antenna='VA08&VA11'",
                    "antenna='VA11&VA20'",
                    "antenna='VA10&VA15'",
                    "antenna='VA05&VA16'",    
                    "antenna='VA14&VA15'",    
                    "antenna='VA01&VA05'",    
                    "antenna='VA09&VA18'",    
                    "antenna='VA09&VA27'",
                    "antenna='VA03&VA15'",
                    "antenna='VA03&VA17'",
                    "antenna='VA10&VA27'",
                    "antenna='VA03&VA19'",
                    "antenna='VA08&VA14'",
                    "antenna='VA09&VA27'",
                    "antenna='VA10&VA14'",
                    "antenna='VA02&VA07'",
                    "antenna='VA18&VA19'"]

execfile(stinghi+'n2976_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')




