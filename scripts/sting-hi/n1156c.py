execfile(xlib+'xinit.py')

xp['prefix']   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles'] = ['../n1156/AM418_1',
                  '../n1156/AM418_2',
                  '../n1156/AM418_3']
xp['starttime'] ='1993/08/09/10:59:45.0'
xp['stoptime']  ='1993/08/09/16:28:15.0'


xp['source']            = 'NGC1156'
xp['spw_source']        = '0,1'

xp['fluxcal']           = '0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          = '0318+164' 
xp['phasecal_uvrange']  ='<100klambda'
xp['passcal']           = '0137+331'
xp['passcal_uvrange']   ='<40klambda'

xp['flagspw']   ='*:0~3;123~126'
xp['flagselect'] = [    "mode='quack' quackinterval=3.0",
                "antenna='VA23' spw='1'",
                "antenna='VA09&VA11' ",
                "antenna='VA02&VA11' ",
                "antenna='VA11&VA21' ",
                "antenna='VA11&VA21' ",
                "antenna='VA10&VA11'",
                "antenna='VA11&VA27'",
                "antenna='VA11&VA14'",
                "antenna='VA11&VA22'"
                ]

execfile(stinghi+'n1156_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

