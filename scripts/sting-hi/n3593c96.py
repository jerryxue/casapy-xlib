execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n3593/AC459_2','../n3593/AC459_3','../n3593/AC459_4']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     =''


# TRACK INFORMATION
xp['source'] = 'NGC3593'

xp['fluxcal'] = '1328+307'
xp['fluxcal_uvrange']=''
xp['phasecal'] = '1117+146'
xp['phasecal_uvrange']=''

xp['spw_source'] = '0,1'
xp['flagspw'] = '*:0~4;57~62'

# CALIBRATION & OPTIONS
xp['flagselect'] = [  " mode='quack' quackinterval=8.0 ",
                " timerange='03:42:30~03:43:00' ",
                " timerange='06:51:10~06:51:20' ",
                " timerange='05:02:30~05:02:50' ",
                " timerange='07:11:14~07:11:16' ",
                " timerange='07:53:40~07:53:50' ",
                " timerange='08:02:10~08:02:20' "
                ]
execfile(stinghi+'n3593_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')


