
def config(xp):

    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~11;48~61'
    xp['fitorder']          =1

    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True

    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'

    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2090.0km/s'
    xp['clean_width']       ='10.4km/s'
    xp['clean_nchan']       =62
    xp['phasecenter']       ='J2000 12h18m49.56 +14d24m58.50'
    
    return xp

def b1():

    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AL731_E090505.xp1'

    # CALIBRATION
    xp['source']            ='NGC4254'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1254+116'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'

    xp['flagspw']           ='*:0;122~126'
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
    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')


def b2():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =[st['hi_raw']+'AL731_4']
    xp['importspw']         ='2'

    # CALIBRATION
    xp['source']            ='NGC4254'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1254+116'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'

    xp['flagspw']           ='*:0;122~126'
    xp['flagselect']        =["timerange='2009/05/10/06:40:45.0~2009/05/10/06:41:05.0' antenna='EA16&VA20'",
                              "timerange='2009/05/10/07:49:55.0~2009/05/10/07:50:15.0' antenna='EA01&VA20'",
                              "timerange='2009/05/10/06:34:25.0~2009/05/10/06:34:45.0'",
                              "timerange='2009/05/10/06:59:25.0~2009/05/10/06:59:45.0'",
                              "timerange='2009/05/10/07:13:35.0~2009/05/10/07:13:55.0'",
                              "timerange='2009/05/10/07:07:45.0~2009/05/10/07:08:05.0'",
                              "timerange='2009/05/10/07:29:05.0~2009/05/10/07:29:25.0'",
                              "field='1411+522'"]

    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')

def b3():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =[st['hi_raw']+'AL731_5',
                              st['hi_raw']+'AL731_6']
    xp['importspw']         ='0'

    # CALIBRATION
    xp['source']            ='NGC4254'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1254+116'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'

    xp['flagspw']           ='*:0;122~126'
    xp['flagselect']        =["timerange='2009/05/16/03:45:46~2009/05/16/03:46:06'",
                              "timerange='2009/05/16/05:25:00~2009/05/16/05:26:00'",
                              "timerange='2009/05/16/04:40:30~2009/05/16/04:40:48'",
                              "timerange='2009/05/16/01:27:04~2009/05/16/01:27:06'",
                              "timerange='2009/05/16/05:27:24~2009/05/16/05:27:26'",
                              "timerange='2009/05/15/23:54:55~2009/05/15/23:55:10'",
                              "timerange='2009/05/15/23:54:55~2009/05/15/23:55:10'",
                              "timerange='2009/05/15/24:30:30~2009/05/15/24:30:40'",
                              "timerange='2009/05/15/24:39:30~2009/05/15/24:39:40'",
                              "timerange='2009/05/15/25:02:14~2009/05/15/25:02:16'",
                              "timerange='2009/05/15/25:16:40~2009/05/15/25:16:50'",
                              "timerange='2009/05/15/25:21:24~2009/05/15/25:21:26'",
                              "timerange='2009/05/15/24:28:00~2009/05/15/24:28:10'",
                              "timerange='2009/05/15/23:48:04~2009/05/15/23:48:06'",
                              "scan='7' timerange='2009/05/16/00:51:40~2009/05/16/00:55:00'",
                              "timerange='23:39:10~23:42:30' field='1254+116'",
                              "field='1411+522'",
                              "antenna='EA09' timerange='22:00:00~24:53:20'",
                              "antenna='EA02&EA18'"]

    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')

def b13a():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'13B-363.sb24608405.eb28587663.56645.491426168985.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~15'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6


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

    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')

def b13b():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'13B-363.sb24608405.eb28593304.56652.43071001158.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~15'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6


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

    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')


def c00():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =[st['hi_raw']+'AP206_B920305.xp1']
    xp['importspw']         ='0'

    # CALIBRATION
    xp['source']            ='NGC4254'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1221+282'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'

    xp['flagspw']           ='*:60~62'
    xp['flagselect']        =["antenna='VA27'"]

    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')

def d00():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =[st['hi_raw']+'AP206_1']
    xp['importspw']         ='0'

    # CALIBRATION
    xp['source']            ='NGC4254'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1221+282'
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'

    xp['flagspw']           ='*:60~62'
    xp['flagselect']        =["timerange='10:29:30~10:30:00'"]

    # CONSOLIDATING & IMAGING
    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')



def comb():

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            ='../n4254/comb/n4254hi'
    xp['prefix_comb']       =['../n4254/c00/c00','../n4254/d00/d00',
                              '../n4254/b1/b1','../n4254/b2/b2',
                              '../n4254/b3/b3','../n4254/b13a/b13a','../n4254/b13b/b13b']

    xp=config(xp)
    
    xp['cleanspec']         =True
    xp['cleancont']         =True

    xp['mosweight']         =True
    xp['scalewt']           =True

    xp['imsize']            =2**8*5
    xp['cell']              ='3.0arcsec'
    
    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01

    xp['clean_start']       ='2214.8km/s'
    xp['clean_width']       ='10.4km/s'
    xp['clean_nchan']       =36

    xp['multiscale']        =[int(x*(9/3.0)) for x in [0.,1.,5.]]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0

    xp['fitspw']            ='*:0~11;48~61'
    
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'    
    xp=xu.xclean(xp)
    
#     xu.mossen(vis=xp['prefix']+'.src.ms',
#           log=xp['prefix']+xp['ctag']+'.line.sens.log',
#           nchan=xp['clean_nchan'],ftmachine='mosaic',
#           mosweight=True,imsize=xp['imsize'],
#           weight=xp['cleanweight'])
    
if  __name__=="__main__":
    #c00()
    #d00()
    #b1()
    #b2()
    #b3()
    #b13a()
    #b13b()
    comb()        
