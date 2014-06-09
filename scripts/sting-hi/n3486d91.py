execfile(xlib+'xinit.py')

# IMPORT

xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='../n3486/AS428_1'
xp['importscan']        ='1,12,13,15'
xp['importspw']         ='0,1,8,9'

# CALIBRATION
xp['source']            ='NGC3486'
xp['fluxcal']           ='0134+329'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='1117+146' 
xp['phasecal_uvrange']  =''
xp['spw_source']        ='2,3'
xp['spw_phasecal']      ='2,3'
xp['spw_fluxcal']       ='0,1'

xp['flagspw']           ='*:0;62'
xp['flagselect']        =["antenna='VA18'",
                          "uvrange='<1200lambda' field='0134+329'",
                          "timerange='23:40:00~23:45:00' field='0134+329'",
                          "timerange='23:55:00~23:58:20' antenna='VA10'",
                          "timerange='23:55:00~23:58:20' antenna='VA14&VA17'"]
xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2

# CONSOLIDATING
execfile(stinghi+'n3486_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
