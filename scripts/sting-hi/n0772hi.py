def config(xp):
    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['scalewt_minsamp']   =12
    xp['uvcs']              =True
    xp['fitspw']            ='*:4~9;75~80'
    xp['scalewt_minsamp']   =12
    xp['fitorder']          =1
    
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =256
    xp['cell']              ='12.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2000km/s'
    xp['clean_width']       ='10.4km/s'
    xp['clean_nchan']       =84
    xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
    return xp
    
def n0772b13a():    
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3] 
    xp['rawfiles']          ='../n0772/13B-363.sb24635393.eb28190296.56594.31903280092.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC0772'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           = '0137+331=3C48'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = 'J0204+1514'
    xp['uvrange_phasecal']  ='<100klambda'
    
    xp['flagselect']        =["antenna='ea08&ea26'"]
    xp['flagtsys_range']    =[5.0,200.0]
    
    xp=config(xp)
#    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    
def n0772b13b():
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          ='../n0772/13B-363.sb24635393.eb28501581.56608.280407708335.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    # CALIBRATION
    xp['source']            ='NGC0772'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           = '0137+331=3C48'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = 'J0204+1514'
    xp['uvrange_phasecal']  ='<100klambda'
    
    xp['flagselect']        =["timerange='2013/11/12/06:49:12.5~2013/11/12/06:49:14.5'",
                              "timerange='2013/11/12/07:32:54.5~2013/11/12/07:32:56.5'",
                              "timerange='2013/11/12/08:17:03.5~2013/11/12/08:17:05.5'"]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    xp=config(xp)
#    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0
    
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')

def n0772b13c():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          ='../n0772/13B-363.sb24635393.eb28527426.56613.267213252315.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    # CALIBRATION
    xp['source']            ='NGC0772'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           = '0137+331=3C48'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = 'J0204+1514'
    xp['uvrange_phasecal']  ='<100klambda'
    
    xp['flagselect']        =["antenna='ea08&ea26'"]
    xp['flagtsys_range']    =[5.0,200.0]
    
    xp=config(xp)
#    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    
def n0772bc00():
    # short track / low velocity resolution
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          ='../n0772/AT237_6'
    xp['importspw']         ='1'
    
    # CALIBRATION
    xp['source']            ='NGC772'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '0134+329'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = '0202+149'
    xp['uvrange_phasecal']  ='<100klambda'
    
    xp['flagspw']           ='0:0~2;60~62'
    xp['flagselect']        = [ "antenna='VA07'","antenna='VA17'",
                                "uvrange='<1000lambda' field='0134+329'",
                                "uvrange='<1700lambda' field='0202+149'",
                                "antenna='VA16' timerange='18:38:10~18:38:20'",
                                "antenna='VA16' timerange='18:39:40~18:39:50'"]
    # mode='shadow' doesn't work with B1960 in v4.2
    xp['flagselect_default']=[]
    
    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['uvcs']              =True
    xp['fitspw']            ='*:2~5;37~40'
    xp['scalewt_minsamp']   =8
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =256
    xp['cell']              ='12.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2005.2km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =42
    xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    
    
def n0772bc13a():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          ='/Volumes/Expansion-Data/evla/n0772/13B-363.sb24382374.eb25239554.56540.51835789352.ms'
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
    
    xp=config(xp)
#    xp['spwrgd_method']     ='mstransform'
    #xp['spwrgd_method']     ='cvel'
    xp['niter']             =0
    
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    
def n0772bc13b():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          ='../n0772/13B-363.sb24382374.eb25241357.56541.46377263889.ms'
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
    
    xp['flagselect']        =["antenna='ea08' spw='*:22'",
                              "antenna='ea16' spw='*:22'",
                              "antenna='ea20' spw='*:22'",
                              "antenna='ea25' spw='*:22'",
                              "antenna='ea26' spw='*:22'",
                              "antenna='ea28' spw='*:22'"]
    xp['flagselect']        =["spw='*:130~140' field='J0204+1514'"]
    xp['flagselect']        +=[ "antenna='ea09&ea26' field='0137+331=3C48'",
                                "antenna='ea16&ea20' field='0137+331=3C48'",
                                "antenna='ea09&ea16' field='0137+331=3C48'",
                                "antenna='ea03&ea28' field='0137+331=3C48'",
                                "antenna='ea13&ea16' field='0137+331=3C48'",
                                "antenna='ea06&ea16' field='0137+331=3C48'",
                                "antenna='ea03&ea12' field='0137+331=3C48'",
                                "antenna='ea16&ea26' field='0137+331=3C48'",
                                "antenna='ea11&ea16' field='0137+331=3C48'"]
    xp['flagselect']        +=["antenna='ea05&ea09'"]      
    xp['flagselect']        +=["spw='*:134' field='N*'"]                      
    xp['flagselect']        +=[  "antenna='ea14&ea25' spw='*:130~140' field='N*'",
                                 "antenna='ea05&ea06' spw='*:130~140' field='N*'",
                                 "antenna='ea06&ea09' spw='*:130~140' field='N*'",
                                 "antenna='ea08&ea26' spw='*:130~140' field='N*'",
                                 "antenna='ea08&ea09' spw='*:130~140' field='N*'",
                                 "antenna='ea05&ea16' spw='*:130~140' field='N*'",
                                 "antenna='ea06&ea16' spw='*:130~140' field='N*'",
                                 "antenna='ea06&ea26' spw='*:130~140' field='N*'",
                                 "antenna='ea20&ea24' spw='*:130~140' field='N*'",
                                 "antenna='ea22&ea26' spw='*:130~140' field='N*'",
                                 "antenna='ea13&ea20' spw='*:130~140' field='N*'",
                                 "antenna='ea11&ea16' spw='*:130~140' field='N*'"]
    xp['flagselect']        +=[  "antenna='ea09&ea26'","antenna='ea05&ea09'"
                                 "antenna='ea06&ea28' spw='*:133~135' field='N*'",
                                 "antenna='ea16&ea20' spw='*:133~135' field='N*'",
                                 "antenna='ea09&ea16' spw='*:133~135' field='N*'",
                                 "antenna='ea03&ea28' spw='*:133~135' field='N*'",
                                 "antenna='ea13&ea16' spw='*:133~135' field='N*'",
                                 "antenna='ea06&ea11' spw='*:133~135' field='N*'",
                                 "antenna='ea16&ea26' spw='*:133~135' field='N*'",
                                 "antenna='ea14&ea26' spw='*:133~135' field='N*'"]                          
    xp['flagtsys_range']    =[5.0,200.0]
    
    xp=config(xp)
#    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    
    
def n0772d99a():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          ='../n0772/AG564_3'
    xp['importspw']         ='1'
    
    # CALIBRATION
    xp['source']            ='ARP78'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '0137+331'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = '0204+152'
    xp['uvrange_phasecal']  ='<100klambda'
    
    xp['flagspw']           ='0:0~4;119~126'
    xp['flagselect']        = [ "antenna='VA12&VA17' timerange='17:44:35~17:44:55'",
                                "timerange='01:00:00~17:44:10'", "antenna='VA05'",
                                "antenna='VA04&VA27'","antenna='VA03&VA27'",
                                "antenna='VA06&VA25'",
                                "antenna='VA12'","antenna='VA02&VA16'",
                                "antenna='VA06&VA24'","antenna='VA11&VA24'",
                                "field='0204+152' uvrange='<1klambda'",
                                "antenna='VA21'",
                                "antenna='VA14&VA24'"]
    xp['flagselect']        =[  "antenna='VA12&VA17' timerange='17:44:35~17:44:55'",
                                "field='0204+152' uvrange='<1.2klambda' scan='5'",
                                "field='ARP78' uvrange='<1.2klambda' timerange='01:00:00~17:44:10'"
                                ]
    
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    
def n0772d99b():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]
    xp['rawfiles']          =['/Volumes/Scratch/raw/21cm/n0772/AG564_4',
                              '/Volumes/Scratch/raw/21cm/n0772/AG564_5']
    xp['importspw']         ='1'
    
    # CALIBRATION
    xp['source']            ='ARP78'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '0137+331'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = '0204+152'
    xp['uvrange_phasecal']  ='<100klambda'
    
    xp['flagspw']           ='0:0~4;122~126'
    xp['flagselect']        = [ #"timerange='16:06:40~17:29:15'", 
                                "timerange='19:57:25~19:57:35'", 
                                "timerange='17:38:00~17:40:00'",
                                "field='0137+331' uvrange='<800lambda'",
                                "field='0204+152' uvrange='<800lambda'",
                                "timerange='19:51:20~19:54:00' antenna='VA05'",
                                "antenna='VA14&VA24'",
                                "antenna='VA14&VA28'",
                                "antenna='VA14&VA12'",
                                "antenna='VA19&VA26'"]
    xp['flagselect']        = [ "timerange='16:06:40~17:29:15' field='ARP78' uvrange='<800lambda'", 
                                "timerange='19:57:25~19:57:35'", 
                                "timerange='17:38:00~17:40:00'",
                                "field='0137+331' uvrange='<800lambda'",
                                "field='0204+152' uvrange='<800lambda'",
                                "timerange='19:51:20~19:54:00' antenna='VA05'",
                                ]
    
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    au.timeOnSource(xp['prefix']+'.src.ms')
    


def n0772hi():
    #2172->2716

    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n0772d99a',
                              'n0772d99b',
                              'n0772bc13a',
                              'n0772bc13b',
                              'n0772b13a',
                              'n0772b13b',
                              'n0772b13c']
    
    xp=config(xp)
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**7*10
    xp['cell']              ='2.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2031.2km/s'
    xp['clean_width']       ='10.4km/s'
    xp['clean_nchan']       =80
    
    xp['multiscale']        =[0,4,12]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    xp['clean_mask']        ='circle[[01h59m25.7s,+18d59m14.0s],750arcsec]'
    
    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

if  __name__=="__main__":
    #n0772d99a()
    #n0772d99b()
    #n0772bc13a()
    #n0772bc13b()
    #n0772b13a()
    #n0772b13b()
    #n0772b13c()
    n0772hi()      

# # CONSOLIDATING
# xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
# xp['prefix_comb']       =['n0772d99a',
#                           'n0772d99b',
# #                          'n0772bc00',
#                           'n0772bc13a',
#                           'n0772bc13b',
#                           'n0772b13a',
#                           'n0772b13b',
#                           'n0772b13c']
# xp['scalewt']           =True
# xp['spwrgd']            ='spw'
# xp['uvcs']              =True
# xp['fitspw']            ='0:2~5;37~40,1:4~9;75~80'
# 
# # IMAGING
# xp['cleanspec']         =True
# xp['cleancont']         =True
# 
# xp['imsize']            =2**7*10
# xp['cell']              ='2.0arcsec'
# 
# xp['imsize']            =2**5*10
# xp['cell']              ='4.0arcsec'
# 
# xp['cleanmode']         ='velocity'
# xp['clean_start']       ='2036.4km/s'
# xp['clean_width']       ='20.8km/s'
# xp['clean_nchan']       =39
# xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
# 
# xp['multiscale']        =[0,4,12]
# xp['clean_gain']        =0.3
# xp['cyclefactor']       =5.0
# xp['negcomponent']      =0
# xp['usescratch']        =True
# 
# # RUN SCRIPTS:
# xp=xu.xconsol(xp)
# xp=xu.xclean(xp)