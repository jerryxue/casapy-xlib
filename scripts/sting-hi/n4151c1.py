execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      ='../n4151/AP104_1'
xp['importband']    ='L'
xp['starttime']     ='1985/09/12/15:10:15.0'
xp['stoptime']      ='1985/09/12/19:43:15.0'
xp['importscan']    =''
xp['importspw']     ='0'


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

xp['flagselect']=        [    "antenna='VA20'",
                    "antenna='VA18&VA27' timerange='1985/09/12/16:14:10.0~1985/09/12/16:14:20.0'",
                    "uvrange='<500lambda' field='1216+487'",
                    "timerange='1985/09/12/18:45:00.0~1985/09/12/18:45:30.0'"
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



