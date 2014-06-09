execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../n3147/13B-363.sb24214388.eb28581165.56639.23767209491.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~13'
xp['importmode']        ='ms'
xp['importchanbin']     =6


# CALIBRATION
xp['source']            ='NGC3147'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='0542+498=3C147'
xp['uvrange_fluxcal']   =''
xp['phasecal']          ='J0841+7053'
xp['uvrange_phasecal']  =''

# rfi at the spw center
xp['flagselect_cal']    =["mode='tfcrop' freqcutoff=7.0 flagdimension='freq'"]                        
xp['flagtsys_range']    =[5.0,200.0]

execfile(stinghi+'n3147_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
