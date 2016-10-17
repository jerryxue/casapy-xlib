

def config(xp):
    
    xp['spwrgd']            ='spw'
    xp['uvcs']              =True
    xp['scalewt']           =True
    xp['fitspw']            ='*:4~7;120~122'
    xp['fitorder']          =1

    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'

    xp['cleanmode'] = 'velocity'
    xp['clean_start']='291.6km/s'
    xp['clean_nchan']=126
    xp['clean_width']='1.29km/s'
    xp['phasecenter']='J2000 02h59m42.2 +25d14m14.0'

    return xp
    # no line-free chanels

def b93():
    
    xp=xu.init()

    xp['prefix']   = '../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles'] = [st['hi_raw']+'AM418_5',
                      st['hi_raw']+'AM418_6']
                  
    xp['source']            = 'NGC1156'
    xp['spw_source']        = '0,1'

    xp['fluxcal']           = '0137+331'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          = '0318+164' 
    xp['phasecal_uvrange']  ='<100klambda'
    xp['passcal']           = '0137+331'
    xp['passcal_uvrange']   ='<40klambda'

    xp['flagspw']   ='*:0~3;123~126'
    xp['flagselect'] = [    "antenna='VA20&VA26'  spw='0' timerange='09:36:35~09:36:50'",
                    "antenna='VA02&VA26'  spw='0' timerange='17:24:10~17:24:20'",
                    "antenna='VA22&VA27'  spw='1' timerange='17:10:40~17:10:50'",
                    "antenna='VA02&VA26'  spw='0' timerange='11:14:20~11:15:00'",
                    "antenna='VA02&VA26'  spw='0' timerange='12:42:10~12:42:20'",
                    "antenna='VA10&VA26'  spw='0' timerange='12:42:10~12:42:20'",
                    "antenna='VA26' spw='0' timerange='17:13:42~17:13:48'",
                    "antenna='VA17' spw='0'",
                    "antenna='VA22' timerange='09:35:20~09:36:00'",
                    "timerange='17:15:20~17:16:00' field='0137+331'",
                    "timerange='13:28:00~13:29:20'",
                    "antenna='VA27' timerange='14:59:00~14:59:40'",
                    "timerange='17:10:40~17:11:00'",
                    "timerange='09:41:40~09:41:50'",
                    "antenna='VA10&VA26'",
                    "antenna='VA26&VA28'",
                    "antenna='VA20&VA26'",
                     "antenna='VA18&VA26'",
                     "antenna='VA23&VA26'",
                     "antenna='VA08&VA26'",
                     "antenna='VA02&VA26'",
                     "antenna='VA03&VA26'"
                    ]

    xp=config(xp)
    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def c93():
    xp=xu.init()

    xp['prefix']   = '../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles'] = [st['hi_raw']+'AM418_1',
                      st['hi_raw']+'AM418_2',
                      st['hi_raw']+'AM418_3']
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

    xp=config(xp)
    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def d93():
    xp=xu.init()


    xp['prefix']   = '../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles'] = st['hi_raw']+'AM418_4'


    xp['source']            = 'NGC1156'
    xp['spw_source']        = '0,1'

    xp['fluxcal']           = '0137+331'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          = '0318+164' 
    xp['phasecal_uvrange']  ='<100klambda'
    xp['passcal']           = '0137+331'
    xp['passcal_uvrange']   ='<40klambda'

    xp['flagspw']   ='*:0~3;123~126'
    xp['flagselect'] = [    "timerange='22:00:00~24:43:20'",
                    "mode='quack' quackinterval=3.0",
                    "antenna='VA08&VA15' timerange='23:20:42~23:20:48'",
                    "antenna='VA10&VA11' timerange='25:41:42~25:41:48'",
                    "antenna='VA08&VA15' spw='0' timerange='23:46:25~23:46:35'",
                    "antenna='VA09&VA11' spw='0' timerange='24:50:20~24:50:40'",
                    "antenna='VA09&VA11' spw='0' timerange='25:03:00~25:04:00'",
                    "antenna='VA22&VA11' spw='0' timerange='25:03:00~25:04:00'",
                    "antenna='VA21&VA11' spw='0' timerange='25:18:25~25:18:35'",
                    "antenna='VA21&VA11' spw='0' timerange='25:18:25~25:18:35'",
                    "antenna='VA03&VA11' spw='0' timerange='26:50:20~26:50:40'",
                    "antenna='VA11&VA28' spw='0' timerange='26:53:40~26:54:40'",
                    "uvrange='<500lambda' field='0137+331' timerange='22:33:20~24:46:40'",
                    "uvrange='<500lambda' field='0318+164' timerange='22:33:20~24:56:40'",
                    "uvrange='<500lambda' field='0318+164' timerange='22:33:20~24:56:40'",
                    "uvrange='<500lambda' field='NGC1156' timerange='23:23:20~24:30:00'"]

    xp=config(xp)
    xp['spwrgd_method']     ='mstransform'
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def comb():
    #280->460
    #execfile(stinghi+'n1156b.py')
    #execfile(stinghi+'n1156c.py')
    #execfile(stinghi+'n1156d.py')

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            ='../n1156/comb/n1156hi'
    xp['prefix_comb']       =['../n1156/b93/b93',
                              '../n1156/c93/c93',
                              '../n1156/d93/d93']

    xp=config(xp)
    
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['mosweight']         =True
    xp['scalewt']           =True
    
    xp['imsize']            =2**6*10*3
    xp['cell']              ='2.0arcsec'

    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01

    xp['clean_start']       ='301.95km/s'
    xp['clean_width']       ='3.9km/s'
    xp['clean_nchan']       =37

    xp['multiscale']        =[int(x*(9.0/2.0)) for x in [0.,1.,3.]]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =-1

    xp['clean_mask']        ='circle[[02h59m42.2s,+25d14m14.0s],375arcsec]'
    xp['fitspw']            ='*:4~7;120~122'

    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)

    # RUN SCRIPTS:
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'
    xu.xclean(xp)
#     xu.mossen(vis=xp['prefix']+'.src.ms',
#       log=xp['prefix']+xp['ctag']+'.line.sens.log',
#       nchan=xp['clean_nchan'],ftmachine='mosaic',
#       mosweight=True,imsize=xp['imsize'],
#       weight=xp['cleanweight'])
    
    #xp['ctag']              ='_natural'
    #xp['cleanweight']       ='natural'
    #xu.xclean(xp)
#     xu.mossen(vis=xp['prefix']+'.src.ms',
#       log=xp['prefix']+xp['ctag']+'.line.sens.log',
#       nchan=xp['clean_nchan'],ftmachine='mosaic',
#       mosweight=True,imsize=xp['imsize'],
#       weight=xp['cleanweight'])

if  __name__=="__main__":
    #b93()
    #d93()
    #c93()
    comb()      