

def b06():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AH912_7']
    xp['starttime']     ="2006/07/01/08:05:05.0"
    xp['stoptime']      ="2006/07/01/18:02:25.0"
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source']        = 'NGC6951'
    
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '2022+616'
    
    xp['spw_source']    = '0,1'
    xp['flagspw']       = '*:0~6;57~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    =["mode='quack' quackinterval=25.0",
                          "timerange='08:06:20~08:06:30'",
                          "antenna='VA07'",
                          "antenna='VA22'",
                          "antenna='VA04&VA06'",
                          "timerange='15:11:40~15:12:10'",
                          "timerange='13:26:05.0~13:26:25.0' antenna='VA17'",
                          "antenna='VA06&VA25' timerange='08:55:45.0~08:56:05.0'",
                          "antenna='VA06&VA25' timerange='09:35:35.0~09:35:55.0'",
                          "timerange='17:03:35.0~17:03:55.0'",
                          "antenna='VA11&VA21' timerange='13:23:20~14:13:20'",
                          "antenna='VA06&VA28' timerange='17:02:25~17:02:45'",
                          "timerange='16:30:35.0~16:30:55.0' antenna='VA06&VA25'",
                          "timerange='11:15:15.0~11:15:35.0' antenna='VA06&VA17'",
                          "timerange='14:35:55.0~14:36:20.0' antenna='VA06&VA17'",
                          "timerange='15:37:45.0~15:38:05.0'",
                          "timerange='17:00:00.0~17:00:10.0' antenna='VA06&VA17'"
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
    
    
    
    


def c02():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AM737_1',st['hi_raw']+'AM737_2']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source']        = 'NGC6951'
    
    xp['fluxcal']       = '0542+498'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']      = '2022+616'
    xp['phasecal_uvrange']  =''
    
    xp['spw_source']    = '0,1'
    xp['flagspw']       = '0:0~10;28~30,1:0~2;21~30'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    = [  "timerange='2002/10/18/00:31:45.0~2002/10/20/00:31:45.0'",
                    "antenna='VA10'",
                    "timerange='2002/10/20/02:56:35~2002/10/20/02:56:55'",
                    "timerange='2002/10/20/04:03:35~2002/10/20/04:03:55'",
                    "timerange='27:46:20~27:47:00'",
                    "timerange='26:37:00~30:00:00' field='NGC6951'",
                    "timerange='26:37:00~30:00:00' field='2022+616'"
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
    
    
    
     
    
    
    


def c04():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AS787_6'
    xp['starttime']     ="2004/05/10/10:31:05.0"
    xp['stoptime']      ="2004/05/10/13:53:05.0"
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source']        = 'NGC6951'
    
    xp['fluxcal']       = '1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']      = '2022+616'
    xp['phasecal_uvrange']  =''
    
    xp['spw_source']    = '0,1'
    xp['flagspw']       = '*:0~6;57~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    =    [    "timerange='2004/05/10/12:51:59~2004/05/10/12:54:22'",
                    "timerange='2004/05/10/12:59:33~2004/05/10/15:59:33'",
                    #"field='1331+305' mode='clip' cliprange='10~1000' clipexpr='ABS_RR'",
                    #"field='1331+305' mode='clip' cliprange='10~1000' clipexpr='ABS_LL'",
                    "antenna='VA22' ",
                    "mode='quack' quackinterval=20.0",
                    "antenna='VA06' timerange='10:33:30~11:33:40'",
                    "timerange='12:13:20~13:03:20' field='NGC6951'",
                    "timerange='12:47:40.0~12:47:50.0' antenna='VA06&VA08'",
                    "timerange='10:38:00~10:38:10' field='2022+616'",
                    "antenna='VA06&VA12'","antenna='VA06&VA28'",
                    "antenna='VA04'",
                    "antenna='VA06'",
                    "antenna='VA18&VA25'","antenna='VA11&VA21'"
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

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AS750_3',st['hi_raw']+'AS750_4',st['hi_raw']+'AS750_5']
    xp['starttime']     ="2003/04/24/08:33:55.0"
    xp['stoptime']      ="2003/04/24/12:01:25.0"
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source']        = 'NGC6951'
    
    xp['fluxcal']       = '1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']      = '2022+616'
    xp['phasecal_uvrange']  =''
    
    xp['spw_source']    = '0,1'
    xp['flagspw']       = '*:0~6;57~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    =    [    "mode='quack' quackinterval=20.0", 
                    "timerange='08:39:10~08:39:20'",
                    "timerange='11:56:20~11:56:30'",
                    "antenna='VA04&VA23' timerange='08:46:40~08:53:20' field='2022+616'",
                    "antenna='VA04&VA23'",
                    "antenna='VA28' timerange='10:00:35.0~10:00:55.0'",
                    "field='1331+305' timerange='11:20:00~12:26:40'",
                    "antenna='VA20&VA24'","antenna='VA20&VA12'"
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
    
    
def config(xp):

    xp['spwrgd']            ='spw'
    xp['uvcs']              =True
    xp['fitspw']            ='*:2~4;23~25'
    xp['fitorder']          =1
    xp['scalewt']           =True
    xp['scalewt_minsamp']   =6
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='4.0arcsec'
    
    xp['cleanmode']     = 'velocity'
    xp['clean_start']   ='1130km/s'
    xp['clean_nchan']   =29
    xp['clean_width']   ='20.8km/s'
    xp['phasecenter']   ='J2000 20h37m14.1 +66d06m20.0'
    
    return xp
    

    
def comb():
    #    line_vrange=[1225,1607]
    #execfile(stinghi+'n6951b06.py')
    #execfile(stinghi+'n6951c02.py')
    #execfile(stinghi+'n6951c04.py')
    #execfile(stinghi+'n6951d03.py')
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            ='../n6951/comb/'+os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['../n6951/d03/d03',
                              '../n6951/c04/c04',
                              '../n6951/b06/b06',
                              '../n6951/c02/c02']
    
    xp=config(xp)
    
    xp['mosweight']         =True
    xp['scalewt']           =True
    
    xp['imsize']            =2**8*5
    xp['cell']              ='3.0arcsec'
    
    xp['clean_start']       ='1171.6km/s'
    xp['clean_nchan']       =24
    
    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01

    xp['multiscale']        =[int(x*(8./3.)) for x in [0.,1.,5.]]
    
    xp['threshold_spec']    ='0.26mJy'
    
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    
    xp['fitspw']            ='*:2~4;23~25'
    
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)

    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'    
    xp=xu.xclean(xp)

if  __name__=="__main__":
    #d03()
    #c04()
    #b06()
    #c02()
    comb()      
