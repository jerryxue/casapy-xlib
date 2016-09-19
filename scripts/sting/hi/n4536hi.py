def config(xp):

    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~10;30~39'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1394.0km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =40
    xp['phasecenter']       ='J2000 12h34m27.1 +02d11m16.0'

    return xp

def b09a():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AL731_2'
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1150-003'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:0~1:120~126'
    xp['flagselect']        =["antenna='EA08'",
                              "timerange='00:00:01~01:10:20' field='1150-003'",
                              "timerange='02:26:45.0~02:27:05.0' antenna='EA14&EA23'",
                              "timerange='01:30:45.0' antenna='VA20&EA24'",
                              "timerange='2009/05/17/01:32:05.0~2009/05/17/01:32:25.0' antenna='EA15&VA20'",
                              "timerange='2009/05/17/02:13:15.0~2009/05/17/02:13:35.0' antenna='EA11&VA20'",
                              "timerange='2009/05/17/02:36:25.0~2009/05/17/02:36:45.0' antenna='EA14&VA20'",
                              "timerange='2009/05/17/05:27:55.0~2009/05/17/05:28:15.0' antenna='EA01&VA20'",
                              "timerange='2009/05/17/06:02:35.0~2009/05/17/06:02:55.0' antenna='EA16&VA20'",
                              "timerange='2009/05/17/06:23:05.0~2009/05/17/06:23:25.0' antenna='EA04&EA17'",
                              "timerange='06:16:40~06:17:10'",
                              "timerange='06:42:55~06:43:10'",
                              "field='1411+522'"]
    
    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

    
def b09b():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AL731_L090518.xp1'
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1150-003'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:0~1:120~126'
    xp['flagselect']        =["field='1411+522'",    "timerange='01:28:20~01:33:20'","timerange='05:20:20~05:20:30'",
                              "antenna='EA23&EA25' timerange='2009/05/18/05:14:50.0~2009/05/18/05:15:10.0'",
                              "timerange='2009/05/18/01:40:35.0~2009/05/18/01:40:55.0' antenna='EA02&VA20'",
                              "timerange='2009/05/18/01:49:25.0~2009/05/18/01:49:45.0' antenna='EA03&VA20'",
                              "timerange='2009/05/18/02:04:05.0~2009/05/18/02:04:25.0' antenna='EA19&VA20'",
                              "timerange='2009/05/18/02:55:45.0~2009/05/18/02:56:05.0' antenna='EA16&VA20'",
                              "timerange='2009/05/18/03:05:45.0~2009/05/18/03:06:05.0' antenna='EA17&VA20'",
                              "timerange='2009/05/18/05:05:45.0~2009/05/18/05:06:05.0' antenna='VA10&EA17'",
                              "timerange='2009/05/18/05:10:15.0~2009/05/18/05:10:35.0' antenna='EA02&VA20'",
                              "timerange='2009/05/18/05:05:45.0~2009/05/18/05:06:05.0' antenna='EA02&EA17'"]
    
    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def b13a():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'13B-363.sb24635609.eb28587662.56645.42906541667.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~15'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           ='1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J1254+1141'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =[]#["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def b13b():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'13B-363.sb24635609.eb28593305.56652.4930632176.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~15'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           ='1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J1254+1141'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def b13c():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
    xp['rawfiles']          =st['hi_raw']+'13B-363.sb24635609.eb28595273.56653.44875773148.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~15'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           ='1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J1254+1141'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def c04():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AN119_1'
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1254+116'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:0;60~62'
    xp['flagselect']        =["antenna='VA08&VA14'","antenna='VA06&VA14'","antenna='VA02&VA04'",
                              "antenna='VA06' timerange='2004/03/22/09:53:00~2004/03/22/09:53:40'",
                              "antenna='VA06&VA08' timerange='2004/03/22/03:53:20~04:06:40' field='NGC4536'",
                              "field='1331+305' timerange='07:38:50~07:39:00'",
                              "field='1331+305' timerange='07:38:50~07:39:00'",
                              "field='1331+305' timerange='10:32:20~10:32:30'",
                              "field='1331+305' timerange='10:33:50~10:34:00'",
                              "mode='quack' quackinterval=20.0",
                              "timerange='10:33:45.0~10:34:05.0' antenna='VA07'",
                              "antenna='VA04'",
                              "timerange='08:23:05.0~08:23:25.0' antenna='VA18&VA25'",
                              "timerange='2004/03/22/10:18:35.0~2004/03/22/10:18:55.0'",
                              "timerange='2004/03/22/11:12:05.0~2004/03/22/11:12:25.0'",
                              "timerange='2004/03/22/11:31:35.0~2004/03/22/11:31:55.0'",
                              "antenna='VA12&VA14'","antenna='VA14&VA16'"]
    
    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    


def d09():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AL735_3'
    xp['importspw']         ='0'
    xp['importscan']        ='34~43'
    
    # CALIBRATION
    xp['source']            ='NGC4536'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1254+116'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:0~1;120~126'
    xp['flagselect']        =["antenna='VA04' timerange='2004/02/22/09:41:40~09:53:30.6'",
                              "antenna='VA06' timerange='2004/02/22/09:41:40~09:53:30.6'",
                              "antenna='VA08' timerange='2004/02/22/11:28:00~11:35:25.0'",
                              "antenna='VA10' timerange='2004/02/22/10:16:00~10:39:00.0'",
                              "antenna='VA11' timerange='2004/02/22/10:16:00~10:39:00.0'",
                              "antenna='VA22' ",
                              "timerange='2004/02/22/08:28:49~08:28:59.5' field='1'",
                              "timerange='2004/02/22/11:50:53~11:51:00.0' field='1'",
                              "timerange='2004/02/22/08:21:20~08:21:40.0' field='0'",
                              "antenna='VA02&VA04'",
                              "antenna='VA08&VA14'",
                              "antenna='VA18&VA04'",
                              "antenna='VA18&VA25'",
                              "timerange='10:59:15~10:59:25'",
                              "mode='quack' quackinterval=5.0 field='NGC3147'",
                              "timerange='11:29:30~11:30:00' field='NGC3147'"]
    
    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    


def d87():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AY18_A870607.xp2'
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
    xp=config(xp)
    xp['niter']             =0
    
    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    


def comb():


    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            ='../comb/n4536hi'
    xp['prefix_comb']       =['../d87/d87',
                              '../c04/c04',
                              '../d09/d09',
                              '../b09a/b09a',
                              '../b09b/b09b',
                              '../b13a/b13a',
                              '../b13b/b13b',
                              '../b13c/b13c']
    
    xp=config(xp)
    
    xp['imsize']            =2**7*10
    xp['cell']              ='2arcsec'
    xp['clean_start']       ='1581.2km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =24
    
    xp['multiscale']        =[0,3,9]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    
    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
if  __name__=="__main__":

    d87()
    c04()
    d09()
    b09a()
    b09b()
    b13a()
    b13b()
    b13c()
    comb()