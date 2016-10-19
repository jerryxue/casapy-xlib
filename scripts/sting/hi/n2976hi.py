#-124->95
# execfile(stinghi+'n2976b02.py')
# execfile(stinghi+'n2976c02a.py')
# execfile(stinghi+'n2976c02b.py')
# execfile(stinghi+'n2976c03.py')
# execfile(stinghi+'n2976c08a.py')
# execfile(stinghi+'n2976c08b.py')
# execfile(stinghi+'n2976d03.py')

def config(xp):
    
    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~11;53~60'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='-150km/s'
    xp['clean_width']       ='5.2km/s'
    xp['clean_nchan']       =int((170.+150.)/5.2)
    xp['phasecenter']       ='J2000 09h47m15.40 67d54m59.00'

    return xp

def b02():
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AB1038_2_n2976',
                          st['hi_raw']+'AB1038_3',
                          st['hi_raw']+'AB1038_4_n2976',
                          st['hi_raw']+'AB1038_5_n2976',
                          st['hi_raw']+'AB1038_6_n2976',
                          st['hi_raw']+'AB1038_7_n2976',
                          st['hi_raw']+'AB1038_8_n2976']
    xp['importspw']     ='0'
    
    # TRACK INFORMATION
    xp['source']        = 'NGC2976'
    
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '0921+622'
    
    xp['spw_source']    = '0'
    xp['flagspw']       = '*:0;60~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    =[
                        "antenna='VA08&VA12'",
                        "timerange='24:55:50~25:40:00'",
                        "timerange='17:11:40~17:36:40'",
                        "antenna='VA02&VA06'",
                        "antenna='VA06&VA22'"
                        ] 
    xp=config(xp)    
    xp['niter']     =0  
    
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

def c02a():
    
    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AT285_9_n2976',
                          st['hi_raw']+'AT285_10_n2976']
    xp['importfield']   ='NGC2976,0841+708,0542+498'
    xp['importscan']    ='2~20'
    xp['importspw']     ='0~5'
    
    
    # TRACK INFORMATION
    xp['source']            ='NGC2976'
    
    xp['fluxcal']           ='0542+498'
    xp['fluxcal_uvrange']   ='<50klambda'
    xp['phasecal']          = '0841+708'
    xp['phasecal_uvrange']  ='<20klambda'
    
    xp['spw_source']        = '0,1'
    xp['spw_fluxcal']       ='2,3,4,5'
    xp['spw_phasecal']      ='2,3,4,5'
    xp['flagspw']           ='*:0~2;120~126'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] =    [
                        "antenna='VA07&VA08' timerange='13:36:30~13:37:00'",
                        "antenna='VA03&VA15' timerange='13:38:20~13:45:00'",
                        "antenna='VA03&VA15' timerange='13:40:00~14:46:40'",
                        "antenna='VA14&VA15'",
                        "antenna='VA02&VA24'",
                        "antenna='VA03&VA15'",
                        "antenna='VA02&VA15'",
                        "antenna='VA02&VA03'",
                        "antenna='VA02&VA03' timerange='13:40:00~14:46:40'",
                        "mode='quack' quackinterval=10",
                        "antenna='VA02&VA14;VA02&VA15;VA02&VA24;VA06&VA08;VA06&VA24;VA03&VA24' timerange='13:38:20~13:45:00'",
                        "antenna='VA02&VA14;VA02&VA15;VA02&VA24;VA06&VA08;VA06&VA24;VA03&VA24' timerange='14:00:00~14:13:20'",
                        "antenna='VA03&VA14' timerange='13:38:20~15:00:00'"    
                    ]
    
    xp=config(xp)
    xp['niter']        =0
    xp['spwrgd_method'] ='mstransform'
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
def c02b():
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AB1038_11',
                          st['hi_raw']+'AB1038_12']
    xp['importspw']     ='0'
    
    
    # TRACK INFORMATION
    xp['source']        = 'NGC2976'
    
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '0921+622'
    
    xp['spw_source']    = '0'
    xp['flagspw']       ='*:0;60~62'
    
    # CALIBRATION & OPTIONS
    
    xp['flagselect']    =    [
                        "antenna='VA07&VA08'",
                        "mode='quack' quackinterval=3.0",
                        "antenna='VA20' timerange='10:45:40.0~10:45:50.0'",
                        "timerange='11:02:00.0~11:02:10.0'",
                        "antenna='VA15'",
                        "antenna='VA09&VA18'",
                        "antenna='VA11&VA14'",
                        "antenna='VA03&VA14'",
                        "antenna='VA02&VA03'",
                        "antenna='VA09&VA14'"
                    ]
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def c03():
    
    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AT285_13',st['hi_raw']+'AT285_14']
    xp['importfield']   ='NGC2976,0841+708,0542+498'
    xp['importscan']    ='2~20'
    xp['importspw']    ='0~5'
    
    # TRACK INFORMATION
    xp['source']            ='NGC2976'
    
    xp['fluxcal']           ='0542+498'
    xp['fluxcal_uvrange']   ='<50klambda'
    xp['phasecal']          = '0841+708'
    xp['phasecal_uvrange']  ='<20klambda'
    
    xp['spw_source']        = '0,1'
    xp['spw_fluxcal']       ='2,3,4,5'
    xp['spw_phasecal']      ='2,3,4,5'
    xp['flagspw']           ='*:0~2;120~126'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']     =    [
                        "mode='quack' quackinterval=3.0",
                        "timerange='07:06:40~07:40:00' field='0542+498'",
                        "antenna='VA07&VA08' timerange='07:32:08~07:32:12'",
                        "antenna='VA14&VA15'",
                        "antenna='VA09&VA15'",
                        "antenna='VA03&VA15'",
                        "antenna='VA02&VA03'",
                        "antenna='VA03&VA14'",
                        "antenna='VA09&VA18'",
                        "antenna='VA11&VA14'",
                        "antenna='VA02&VA09'",
                        "antenna='VA07&VA08'"
                    ]
    
    xp=config(xp)
    xp['spwrgd_method'] ='mstransform'
    xp['niter']        =0
    
    
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    
def c08a():
    
    xp=xu.init()
    rawdir='../'
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3] 
    xp['rawfiles']      =st['hi_raw']+'AC921_17'
    xp['starttime']     ='2008/05/04/21:20:45.0'
    xp['stoptime']      ='2008/05/04/23:13:15.0'
    
    # TRACK INFORMATION
    xp['source']         ='NGC2976'
    
    xp['fluxcal']             ='1331+305'
    xp['phasecal']             = '0841+708'
    xp['phasecal_uvrange']    ='<20klambda'
    
    xp['spw_source']         = '0'
    xp['flagspw']            ='*:0~40;117~126'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] = [
                    "antenna='VA08&EA17'",
                    "antenna='EA11&VA20'",
                    "antenna='EA21'",
                    "antenna='VA03&VA20'",
                    "antenna='VA20&EA23' timerange='21:47:20.0~21:47:30.0'",
                    "antenna='VA09&EA17' timerange='21:11:50.0~21:12:00.0'",
                    "antenna='VA12&EA17' timerange='22:45:00.0~22:45:10.0'",
                    "antenna='EA17&EA19' timerange='22:45:00.0~22:45:10.0'",
                    "antenna='VA12&EA25'",
                    "antenna='VA15&EA25'",
                    "antenna='VA15&EA19'",
                    "antenna='EA16&EA19'",
                    "antenna='EA05&VA28'"
                    ]
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def c08b():
    
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AC921_18']
    xp['starttime']     ='2008/05/24/21:31:45.0'
    xp['stoptime']      ='2008/05/24/23:24:25.0'
    
    # TRACK INFORMATION
    xp['source']         ='NGC2976'
    
    xp['fluxcal']             ='1331+305'
    xp['phasecal']             = '0841+708'
    xp['phasecal_uvrange']    ='<20klambda'
    
    xp['spw_source']         = '0'
    xp['flagspw']            ='*:0~40;117~126'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] = [  "antenna='VA08&EA17'",
                    "antenna='EA11&VA20'",
                    "antenna='EA21'",
                    "antenna='VA20&EA23' timerange='21:47:10.0~21:47:40.0'",
                    "antenna='VA09&EA17' timerange='21:11:45.0~21:12:00.0'",
                    "antenna='VA12&EA17' timerange='22:45:00.0~22:45:20.0'",
                    "antenna='EA17&EA19' timerange='22:45:00.0~22:45:20.0'",
                    "antenna='VA10&EA11'",
                    "antenna='VA12&EA25'",
                    "antenna='VA15&EA25'",
                    "antenna='EA19&EA25'",
                    "antenna='EA16&EA19'"
                    ]
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    
def d03():
    
    xp=xu.init()

    rawdir='../'
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AB1038_15',st['hi_raw']+'AB1038_16']
    xp['starttime']     ='2003/05/10/02:46:15.0'
    xp['stoptime']      ='2003/05/10/04:21:55.0'
    xp['importspw']     ='0'
    xp['importfield']   ='NGC2976,1331+305,0921+622'
    
    # TRACK INFORMATION
    xp['source']         = 'NGC2976'
    
    xp['fluxcal'] = '1331+305'
    xp['phasecal'] = '0921+622'
    
    xp['spw_source'] = '0'
    xp['flagspw']='0:0;60~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] =    [
                        "mode='quack' quackinterval=5.0 ",
                        "antenna='VA20' timerange='03:20:14~03:20:16'",
                        "antenna='VA20&VA28' timerange='02:40:40~02:50:50'",
                        "timerange='04:14:00~04:14:10' field='1331+305'"
                        "antenna='VA03&VA09'",
                        "antenna='VA02&VA17'",
                        "antenna='VA09&VA19'",
                        "antenna='VA15&VA27'",
                        "antenna='VA03&VA10'",
                        "antenna='VA03&VA27'",
                        "antenna='VA16&VA26'",
                        "antenna='VA14&VA27'",
                        "antenna='VA08&VA11'",
                        "antenna='VA11&VA20'",
                        "antenna='VA10&VA15'",
                        "antenna='VA05&VA16'",    
                        "antenna='VA14&VA15'",    
                        "antenna='VA01&VA05'",    
                        "antenna='VA09&VA18'",    
                        "antenna='VA09&VA27'",
                        "antenna='VA03&VA15'",
                        "antenna='VA03&VA17'",
                        "antenna='VA10&VA27'",
                        "antenna='VA03&VA19'",
                        "antenna='VA08&VA14'",
                        "antenna='VA09&VA27'",
                        "antenna='VA10&VA14'",
                        "antenna='VA02&VA07'",
                        "antenna='VA18&VA19'"]
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    
def comb():
    
    xp=xu.init()
    
    xp['prefix_comb']=['../n2976/b02/b02',
                        '../n2976/c02a/c02a',
                        '../n2976/c02b/c02b',
                        '../n2976/c03/c03',
                        '../n2976/d03/d03',
                        '../n2976/c08a/c08a',
                        '../n2976/c08b/c08b']
    xp['prefix']        ='../n2976/comb/n2976hi'
    
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

    xp['clean_start']       ='-134.4km/s'
    xp['clean_width']       ='5.2km/s'
    xp['clean_nchan']       =int((170.+150.)/5.2)-4
    
    xp['multiscale']        =[int(x*(7.0/3.0)) for x in [0.,1.,3.]]
    
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    
    xp['fitspw']            ='*:0~11;53~60'
    
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'
    xp=xu.xclean(xp)
    
if  __name__=="__main__":
    #c02a()
    #c02b()
    #c03()
    #d03()
    #c08a()
    #c08b()
    #b02()
    comb()

