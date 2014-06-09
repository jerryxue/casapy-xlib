execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      = ['../n4605/AB1038_8',
                       '../n4605/AB1038_9',
                       '../n4605/AB1038_10']
xp['starttime']     ='2002/12/19/07:54:45'
xp['stoptime']      ='2002/12/19/11:45:15'
xp['importscan']    =''
xp['importspw']     ='0'


# TRACK INFORMATION
xp['source']        ='NGC4605'
xp['fluxcal']       = '1331+305'
xp['phasecal']      = '1313+675'

xp['spw_source']    ='0'
xp['spw_edge']      ='*:0~4;57~62'

# CALIBRATION & OPTION
xp['flagselect'] = ["antenna='VA20'",
            "antenna='VA07&VA08'",
            "antenna='VA08&VA10'",
            "antenna='VA15&VA28'",
            "antenna='VA14&VA16'"]

execfile(stinghi+'n4605_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



