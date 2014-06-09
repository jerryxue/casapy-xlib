execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='../n0772/13B-363.sb24382374.eb25239554.56540.51835789352.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~15'
xp['importmode']        ='ms'
xp['importchanbin']     =6

# CALIBRATION
xp['source']            ='NGC0772'
xp['spw_source']        ='0,1'

xp['fluxcal']           = '0137+331=3C48'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = 'J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagselect']        =["antenna='ea08' spw='*:22'",
                          "antenna='ea16' spw='*:22'",
                          "antenna='ea20' spw='*:22'",
                          "antenna='ea25' spw='*:22'",
                          "antenna='ea26' spw='*:22'",
                          "antenna='ea28' spw='*:22'"]
xp['flagtsys_range']    =[5.0,200.0]

execfile(stinghi+'n0772_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

