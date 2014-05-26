execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['/Volumes/Scratch/raw/21cm/n4536/AY18_A870607.xp2']
xp['importspw']         ='0,1'
xp['importscan']        ='2~18'

# CALIBRATION
xp['source']            ='N4536'
xp['fluxcal']           ='3C286'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1148-001'
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'
xp['spw_fluxcal']       ='1'
xp['spw_phasecal']      ='1'

xp['flagselect']        =["timerange='1987/06/07/02:51:00~02:52:00'",
                          "timerange='1987/06/07/04:13:15~04:14:00'",
                          "timerange='1987/06/07/05:43:30~05:44:00'",
                          "timerange='1987/06/07/06:27:00~06:27:30'"]

# CONSOLIDATING & IMAGING
execfile(stinghi+'n4536_config.py')
xp['niter']             =0
xp['clean_nchan']       =25

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

