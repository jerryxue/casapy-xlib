
def config(xp):
    
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['imcs']              =True
    xp['fitchans']          ='0~2,39~42'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']         = 'velocity'
    xp['clean_start']        ='360.00km/s'
    xp['clean_width']        ='5.2km/s'
    xp['clean_nchan']        =int((960.-360.)/5.2)
    xp['phasecenter']        ='J2000 10h19m54.92 +45d32m59.0'

    return xp

def b05():
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AW605_14',st['hi_raw']+'AW605_15']
    xp['starttime']     ='2005/04/26/23:21:25.0'
    xp['stoptime']      ='2005/04/27/08:00:00.0'
    
    # TRACK INFORMATION
    xp['source']         = 'NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '1331+305'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']             = '1035+564'
    xp['phasecal_uvrange']    =''
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect']    = [  "timerange='2005/04/26/23:30:13.0~2005/04/26/23:30:18' field='0542+498'",
                    "timerange='2005/04/27/06:00:45.0~2005/04/27/06:01:02' field='1035+564'",
                    #"clipexpr(ABS I)++clipminmax(0,10)++field(1035+564)",
                    #"antenna='VA09' corr(LL)++spw(0)",
                    #"ant(VA18)++corr(LL)++spw(0)",
                    #"ant(VA22)++corr(RR)++spw(1)",
                    "timerange='2005/04/27/04:08:24.0~2005/04/27/04:08:26' field='NGC3198'",
                    "timerange='2005/04/27/06:31:30.0~2005/04/27/06:31:40' field='NGC3198'",
                    "timerange='2005/04/27/04:19:00.0~2005/04/27/04:20:00' field='NGC3198'",
                    "timerange='2005/04/27/01:54:05.0~2005/04/27/01:54:25' field='NGC3198'",
                    "timerange='2005/04/27/07:14:15~07:14:40' field='1331+305'",
                    "antenna='VA04'","antenna='VA21&VA22'","antenna='VA12&VA28'",
                    "timerange='2005/04/27/07:16:40~07:16:50' field='1331+305' antenna='VA28'",
                    "mode='quack' quackinterval=20.0",
                    "antenna='VA22'"
                ]
    
    xp=config(xp)
    xp['niter']        =0
    
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def c02a():
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AT285_4'
    xp['starttime']     ='2002/11/16/12:34:50.0'
    xp['stoptime']      ='2002/11/16/12:57:10.0'
    
    
    
    # TRACK INFORMATION
    xp['source']         = 'NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']         = '1331+305'
    xp['fluxcal_uvrange']=''
    xp['phasecal']         = '1006+349'
    xp['phasecal_uvrange']='<30klambda'
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect']     = [
                "timerange='2002/11/16/12:55:41~2002/11/16/12:56:00' field='1006+349'",
                "uvrange='<600lambda' field='1006+349'"
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


def c02b():
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AT285_5'
    xp['starttime']     ='2002/11/19/11:23:30'
    xp['stoptime']      ='2002/11/19/12:47:50'
    
    
    # TRACK INFORMATION
    xp['source']        ='NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '1331+305'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']             = '1006+349'
    xp['phasecal_uvrange']    ='<30klambda'
    
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect'] = [
                    "mode='quack' quackinterval=20.0 field='1006+349'",
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
    

def c02c():
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AT285_8'
    xp['starttime']     ='2002/11/26/11:25:50'
    xp['stoptime']      ='2002/11/26/12:19:50'
    
    
    # TRACK INFORMATION
    xp['source']        ='NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '1331+305'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']             = '1006+349'
    xp['phasecal_uvrange']    ='<30klambda'
    spw_edge =6
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect'] = [    "timerange='2002/11/26/11:40:09~2002/11/26/11:40:10'",
                    "timerange='2002/11/26/11:45:46~2002/11/26/11:45:53'",
                    "timerange='2002/11/26/11:51:48~2002/11/26/11:51:54'",
                    "timerange='2002/11/26/11:22:30~11:24:30'",
                    "mode='quack' quackinterval=20.0 field='1006+349'",
                    "antenna='VA09&VA14'",
                    "antenna='VA07&VA08' timerange='11:40:00~11:40:20'"
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
    xp['rawfiles']      =[st['hi_raw']+'AT285_9',st['hi_raw']+'AT285_10']
    xp['starttime']     ='2003/01/07/10:39:10.0'
    xp['stoptime']      ='2003/01/07/23:00:00.0'
    
    
    # TRACK INFORMATION
    xp['source']        ='NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '1331+305'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']             = '1006+349'
    xp['phasecal_uvrange']    ='<30klambda'
    
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect'] =  [    "timerange='2003/01/07/13:12:09~2003/01/07/13:12:10'",
                    "mode='quack' quackinterval=20.0 field='1006+349'",
                    "mode='quack' quackinterval=30.0 field='1331+305'",
                    "timerange='2003/01/07/10:36:50.0~10:37:10.0'",
                    "uvrange='<1300lambda' field='1006+349'",
                    "timerange='13:12:00~13:12:20' field='1006+349'"
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
    

def d03a():
    
    
    xp=xu.init()

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AT285_11'
    xp['starttime']     ='2003/03/27/06:16:50.0'
    xp['stoptime']      ='2003/03/27/06:45:30.0'
    
    # TRACK INFORMATION
    xp['source']        ='NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '1331+305'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']             = '1006+349'
    xp['phasecal_uvrange']    ='<30klambda'
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect'] =  [    "timerange='2003/03/27/06:04:10~06:25:25' field='1331+305'",
                    "mode='quack' quackinterval=20.0 field='1006+349'"]

    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
def d03b():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AT285_12'
    xp['starttime']     ='2003/04/28/04:10:50.0'
    xp['stoptime']      ='2003/04/28/04:36:50.0'
    
    # TRACK INFORMATION
    xp['source']        ='NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '1331+305'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']             = '1006+349'
    xp['phasecal_uvrange']    ='<30klambda'
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect'] = [    "timerange='2003/04/28/04:18:20~04:19:25' field='1331+305'"
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
    
    
def d04():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AW605_13'
    xp['starttime']     ='2004/07/09/19:12:05.0'
    xp['stoptime']      ='2004/07/09/23:09:05.0'
    xp['importscan']    ='1,18~25'
    xp['importspw']     ='0,1'
    
    # TRACK INFORMATION
    xp['source']         = 'NGC3198'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']             = '0542+498'
    xp['fluxcal_uvrange']    ='<50klambda'
    xp['phasecal']             = '1035+564'
    xp['phasecal_uvrange']    =''
    
    # CALIBRATION & OPTIONS
    xp['flagspw']       ='*:0;60~62'
    xp['flagselect']    = [  "timerange='2004/07/09/22:03:28.0~22:04:32' field='NGC3198'",
                    "timerange='2004/07/09/22:26:56.0~22:27:45' field='NGC3198'",
                    "timerange='2004/07/09/21:33:44.0~21:34:34' field='NGC3198'",
                    "timerange='2004/07/09/21:41:03.0~21:41:06' field='NGC3198'",
                    "timerange='2004/07/09/21:52:07.0~21:55:31' field='NGC3198'",
                    "timerange='2004/07/09/22:57:18.0~22:57:30' field='NGC3198'",
                    "timerange='2004/07/09/22:58:11.0~23:03:05' field='NGC3198'",
                    "timerange='2004/07/09/22:29:23.5~22:29:28.3' field='NGC3198'",
                    "timerange='2004/07/09/22:57:57.9~22:58:48.4' field='NGC3198'",
                    "timerange='2004/07/09/21:48:54~21:49:58' field='1035+564'",
                    "timerange='2004/07/09/21:48:03~21:48:10' field='1035+564'",
                    "timerange='2004/07/09/21:48:03~21:48:10' field='1035+564'",
                    "timerange='2004/07/09/22:13:33~22:13:38' field='1035+564'",
                    "timerange='2004/07/09/22:06:38.3~22:06:48' field='1035+564'",
                    "timerange='2004/07/09/19:12:29~19:12:43' field='0542+498'",
                    "timerange='2004/07/09/19:12:00~19:12:11' field='0542+498'",
                    "timerange='2004/07/09/19:16:28~19:16:43' field='0542+498'",
                    "timerange='2004/07/09/19:17:39~19:17:53' field='0542+498'",
                    "mode='clip' clipminmax=[0,10] field='NGC3198'",
                    "antenna='VA22'",
                    "antenna='VA26'",
                    "mode='clip' clipminmax=[0,10] field='1035+564'",
                    "uvrange='<600lambda' field='1035+564'",
                    "mode='quack' quackinterval=15.0 field='1035+564'",
                    "antenna='VA06&VA27' field='NGC3198' timerange='2004/07/09/22:08:00~2004/07/09/22:08:10'"
                    ]
    
    xp=config(xp)
    xp['niter']        =0
    
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

def comb():
    #[470,830]
    xp=xu.init()
    
    xp['prefix']            ='../n3198/comb/n3198hi'
    xp['prefix_comb']       =[  '../n3198/d04/d04',
                                '../n3198/d03b/d03b',
                                '../n3198/d03a/d03a',
                                '../n3198/c03/c03',
                                '../n3198/c02c/c02c',
                                '../n3198/c02b/c02b',
                                '../n3198/c02a/c02a',
                                '../n3198/b05/b05']
    
    xp=config(xp)
    
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['mosweight']         =True
    xp['scalewt']           =True
    
    xp['fitchans']           ='0~13,85~100'
    xp['clean_start']        ='406.8km/s'
    xp['clean_width']        ='5.2km/s'
    xp['clean_nchan']        =101
    
    xp['imsize']            =2**8*5
    xp['cell']              ='3.0arcsec'
    
    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01
    
    xp['multiscale']        =[int(x*(7.0/3.0)) for x in [0.,2.,5.]]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    xp['threshold_spec']    ='0.6mJy'
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'
    xp=xu.xclean(xp)

if  __name__=="__main__":
    
    #d04()
    #d03b()
    #d03a()
    #c03()
    #c02c()
    #c02b()
    #c02a()
    #b05()
    comb()

