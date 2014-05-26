execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n4254/13B-363.sb24608405.eb28587663.56645.491426168985.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~15'
xp['importmode']        ='ms'
xp['importchanbin']     =4


# CALIBRATION
xp['source']            ='NGC4254'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='1331+305=3C286'
xp['uvrange_fluxcal']   =''
xp['phasecal']          ='J1254+1141'
xp['uvrange_phasecal']  =''

# rfi at the spw center
xp['flagselect']        =[]#["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
xp['flagtsys_range']    =[5.0,200.0]

execfile(stinghi+'n4254/n4254_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
