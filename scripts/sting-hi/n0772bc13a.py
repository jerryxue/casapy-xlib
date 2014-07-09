execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='../n0772/13B-363.sb24382374.eb25239554.56540.51835789352.ms'
xp['importspw']         ='2,12'
xp['importspw']         ='2'
xp['importscan']        ='2~15'
xp['importmode']        ='ms'
xp['importtimebin']     ='21s'
xp['importchanbin']     =1

# CALIBRATION
xp['source']            ='NGC0772'
xp['spw_source']        ='0'

xp['fluxcal']           = '0137+331=3C48'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = 'J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

# xp['flagselect']        =["antenna='ea08' spw='*:22'",
#                           "antenna='ea16' spw='*:22'",
#                           "antenna='ea20' spw='*:22'",
#                           "antenna='ea25' spw='*:22'",
#                           "antenna='ea26' spw='*:22'",
#                           "antenna='ea28' spw='*:22'"]
xp['flagselect']=["antenna='ea25&ea26' field='0137+331=3C48'",
 "antenna='ea08&ea16' field='0137+331=3C48'",
 "antenna='ea08&ea25' field='0137+331=3C48'",
 "antenna='ea16&ea20' field='0137+331=3C48'",
 "antenna='ea09&ea16' field='0137+331=3C48'",
 "antenna='ea08&ea26' field='0137+331=3C48'",
 "antenna='ea13&ea16' field='0137+331=3C48'",
 "antenna='ea06&ea16' field='0137+331=3C48'",
 "antenna='ea16&ea25' field='0137+331=3C48'",
 "antenna='ea06&ea08' field='0137+331=3C48'",
 "antenna='ea06&ea26' field='0137+331=3C48'",
 "antenna='ea09&ea26' field='0137+331=3C48'",
 "antenna='ea16&ea26' field='0137+331=3C48'",
 "antenna='ea26&ea28' field='0137+331=3C48'",
 "antenna='ea11&ea16' field='0137+331=3C48'",
 "antenna='ea25&ea28' field='0137+331=3C48'",
 "antenna='ea06&ea25' field='0137+331=3C48'",
 "antenna='ea08&ea11' field='0137+331=3C48'",
 "antenna='ea06&ea09' field='0137+331=3C48'",
 "antenna='ea11&ea20' field='0137+331=3C48'",
 "antenna='ea11&ea26' field='0137+331=3C48'",
 "antenna='ea05&ea16' field='0137+331=3C48'",
 "antenna='ea15&ea16' field='0137+331=3C48'",
 "antenna='ea08&ea19' field='0137+331=3C48'",
 "antenna='ea03&ea12' field='0137+331=3C48'",
 "antenna='ea03&ea28' field='0137+331=3C48'",
 "antenna='ea08&ea20' field='0137+331=3C48'",
 "antenna='ea10&ea16' field='0137+331=3C48'",
 "antenna='ea13&ea20' field='0137+331=3C48'",
 "antenna='ea16&ea28' field='0137+331=3C48'"]
xp['flagselect']=xp['flagselect']+["timerange='12:28:50~12:29:20' field='0137+331=3C48'"]
xp['flagselect']=xp['flagselect']+["antenna='ea19'"]
xp['flagselect']=xp['flagselect']+["antenna='ea05&ea09'"]
xp['flagselect']=xp['flagselect']+["spw='*:130~140' field='J0204+1514'"]
xp['flagselect']=xp['flagselect']+["antenna='ea25&ea26' spw='*:132~136' field='N*'",
                                 "antenna='ea06&ea08' spw='*:132~136' field='N*'",
                                 "antenna='ea09&ea26' spw='*:132~136' field='N*'",
                                 "antenna='ea06&ea20' spw='*:132~136' field='N*'",
                                 "antenna='ea06&ea25' spw='*:132~136' field='N*'",
                                 "antenna='ea09&ea16' spw='*:132~136' field='N*'",
                                 "antenna='ea06&ea09' spw='*:132~136' field='N*'",
                                 "antenna='ea13&ea16' spw='*:132~136' field='N*'",
                                 "antenna='ea05&ea16' spw='*:132~136' field='N*'",
                                 "antenna='ea06&ea16' spw='*:132~136' field='N*'",
                                 "antenna='ea16&ea25' spw='*:132~136' field='N*'",
                                 "antenna='ea06&ea26' spw='*:132~136' field='N*'",
                                 "antenna='ea03&ea12' spw='*:132~136' field='N*'",
                                 "antenna='ea11&ea26' spw='*:132~136' field='N*'",
                                 "antenna='ea03&ea16' spw='*:132~136' field='N*'",
                                 "antenna='ea16&ea26' spw='*:132~136' field='N*'",
                                 "antenna='ea20&ea26' spw='*:132~136' field='N*'",
                                 "antenna='ea16&ea20' spw='*:132~136' field='N*'",
                                 "antenna='ea09&ea20' spw='*:132~136' field='N*'",
                                 "antenna='ea11&ea16' spw='*:132~136' field='N*'"]
xp['flagselect']=xp['flagselect']+["spw='*:134' field='N*'"]
#xp['flagtest']=True
xp['flagtsys_range']    =[5.0,200.0]

execfile(stinghi+'n0772_config.py')
xp['spwrgd_method']     ='mstransform'
xp['niter']             =0


# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

