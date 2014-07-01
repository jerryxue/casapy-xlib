
execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4151/AP104_2',
                      '../n4151/AP104_3',
                      '../n4151/AP104_4',
                      '../n4151/AP104_5']
xp['importband']    ='L'
xp['starttime']     ='1985/09/14/17:02:15.0'
xp['stoptime']      ='1985/09/15/03:19:15.0'
xp['importscan']    =''
xp['importspw']     =''

# TRACK INFORMATION
xp['source'] = 'N4151'

xp['fluxcal'] = '3C286'
xp['fluxcal_uvrange']=''
xp['phasecal'] = '1216+487' 
xp['phasecal_uvrange']=''
xp['passcal']= '3C286'
xp['passcal_uvrange']=''
xp['spw_source'] = '0'

# CALIBRATION & OPTIONS

xp['flagselect']=   [  "antenna='VA20' timerange='24:55:00~24:56:40'",
                "antenna='VA18&VA27'",
                "antenna='VA11&VA27'",
                "antenna='VA06&VA19'",
                "antenna='VA08' timerange='17:08:00~17:16:40'",
                "timerange='19:15:00~19:15:50'",
                "antenna='VA11&VA18'",
                "antenna='VA21&VA27'",
                "antenna='VA21&VA25'",
                "antenna='VA25&VA27'",
                "antenna='VA06&VA18'",
                "antenna='VA18&VA21'",
                "scan='17~36'"
            ]
xp['ref_ant']    ='16'

execfile(stinghi+'n4151_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


