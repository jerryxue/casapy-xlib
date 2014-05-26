execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['/Volumes/Scratch/raw/21cm/n4254/AL731_E090505.xp1']

# CALIBRATION
xp['source']            ='NGC4254'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1254+116'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'

xp['flagselect']        =["antenna='EA09&VA22'",
                          "antenna='EA09'",
                          "antenna='VA12&EA18'",
                          "antenna='VA20&EA24' timerange='2009/05/05/03:57:00~03:57:30'",
                          "antenna='VA20&EA11' timerange='2009/05/05/03:13:30~03:14:60'",
                          "antenna='EA02&VA20' timerange='2009/05/05/03:04:00~03:04:30'",
                          "antenna='EA13&EA17' timerange='2009/05/05/02:54:50~02:55:20'",
                          "timerange='02:50:00~02:55:50' field='1254+116'",
                          "field='1411+522'"]

# CONSOLIDATING & IMAGING
execfile(stinghi+'n4254/n4254_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

