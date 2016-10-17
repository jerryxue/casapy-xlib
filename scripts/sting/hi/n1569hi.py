
def config(xp):
    # CONSOLIDATING
    xp['spwrgd']            =''
    xp['uvcs']              =True
    xp['fitspw']            ='*:3~13;110~120'
    xp['fitorder']          =1

    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True

    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'

    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='-252km/s'
    xp['clean_width']       ='2.6km/s'
    xp['clean_nchan']       =125
    xp['phasecenter']       ='J2000 04h30m49.06 64d50m52.61'

    return xp

def b00():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AW605_F031110.xp1'

    # CALIBRATION
    xp['source']            ='NGC1569'

    xp['fluxcal']           ='0538+498'
    xp['uvrange_fluxcal']   ='<50klambda'
    xp['phasecal']          ='0404+768'
    xp['uvrange_phasecal']  =''

    xp['spw_source']        ='4,5'
    xp['spw_fluxcal']       ='0,1,2,3'
    xp['spw_phasecal']       ='0,1,2,3'
    xp['flagspw']            ='*:0~2;121~126'

    xp['flagselect']        =[    "mode='quack' quackinterval=6.0",
                    "antenna='VA26' timerange='05:54:10~05:55:10'",
                    "antenna='VA26' timerange='05:54:10~05:55:10'",
                    "antenna='VA09' timerange='11:01:40~11:05:50'",
                    "antenna='VA06' timerange='06:54:10~06:54:20'",
                    "timerange='11:00:00~11:10:00'",
                    "antenna='VA11&VA18'",
                    "timerange='05:09:40~05:10:15' field='0538+498'",
                    "timerange='12:16:40~12:19:20' field='0538+498'"
                    ]

    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def c00():
    xp=xu.init()

    # IMPORT
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AW325_C930629.xp1',st['hi_raw']+'AW325_C930629.xp2']
    xp['importfield']   ='0,1,2'
#     #xp=xu.ximport(xp)
#     #xp['prefix']        ='tmp2'
#     #xp['rawfiles']      =st['hi_raw']+'AW325_7'
#     #xp['importfield']   ='0,2'
#     #xp=xu.ximport(xp)
#     
#     #os.system("rm -rf "+xp['prefix']+'.ms')
#     #concat(vis=['tmp1.ms','tmp2.ms'],concatvis=xp['prefix']+'.ms',freqtol='50kHz')
#     os.system("rm -rf tmp?.ms")

    # TRACK INFORMATION
    xp['source']             = 'NGC1569'

    xp['fluxcal']             = '0137+331'
    xp['fluxcal_uvrange']    ='<40klambda'
    xp['phasecal']             = '0614+607_0'
    xp['phasecal_uvrange']    =''

    xp['spw_source']         = '4,5'
    xp['spw_fluxcal']         = '0,1'
    xp['spw_phasecal']         = '0,1,2,3'
    xp['flagspw']            ='*:0~2;121~126'

    # CALIBRATION & OPTIONS
    xp['flagselect']         =[
                    "mode='quack' quackinterval=6.0",
                    "timerange='13:46:40~13:47:20'",
                    "timerange='13:49:50~13:50:10'",
                    "timerange='17:33:20~17:47:30.0'",
                    "timerange='12:23:15.0~13:05:30.0'",
                    "antenna='VA23&VA25'","antenna='VA03&VA23'",
                    "antenna='VA11&VA12'",
                    "antenna='VA19&VA25'",
                    "antenna='VA19&VA23'",
                    "antenna='VA06&VA19'",
                    "antenna='VA04&VA25'",
                    "antenna='VA18&VA23'",
                    "antenna='VA17&VA24'",
                    "antenna='VA12&VA20'",
                    "antenna='VA05&VA20'",
                    "antenna='VA05&VA18'",
                    "antenna='VA04&VA23'",
                    "antenna='VA04&VA18'",
                    "antenna='VA03&VA04'",
                    "antenna='VA11'",
                    "antenna='VA02&VA23'",
                    "antenna='VA04&VA05'",
                    "antenna='VA04&VA19'",
                    "antenna='VA03&VA25'",
                    "antenna='VA02&VA03'",
                    "antenna='VA03&VA19'",
                    "scan='2'",
                    "scan='4'"
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

def d00():
    xp=xu.init()

    # IMPORT 
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AW325_A920906.xp1',
                          st['hi_raw']+'AW325_A920906.xp2']

    # TRACK INFORMATION
    xp['source']            = 'NGC1569'

    xp['fluxcal']           = '0137+331'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          = '0614+607'
    xp['phasecal_uvrange']  =''

    xp['spw_source']         = '4,5'
    xp['spw_fluxcal']         = '0,1,2,3'
    xp['spw_phasecal']         = '0,1,2,3'
    xp['flagspw']            ='*:0~2;121~126'

    # CALIBRATION & OPTIONS
    xp['flagselect'] =     [
                    "mode='quack' quackinterval=3.0",
                    "antenna='VA16'",
                    "timerange='1992/09/06/08:17:45~1992/09/06/08:19:45' antenna='VA28'",
                    "timerange='1992/09/06/09:16:30~1992/09/06/09:18:30' antenna='VA28'",
                    "timerange='1992/09/06/09:21:30~1992/09/06/09:23:30' antenna='VA28'",
                    "timerange='1992/09/06/11:42:30~1992/09/06/11:44:30' antenna='VA28'",
                    "timerange='1992/09/06/12:05:15~1992/09/06/12:07:15' antenna='VA28'",
                    "timerange='1992/09/06/11:02:30~1992/09/06/11:04:15' antenna='VA28'",
                    "antenna='VA10&VA28' timerange='1992/09/06/08:31:00~1992/09/06/08:31:40'",
                    "antenna='VA12' timerange='08:29:10~08:35:30' field='0137+331'",
                    "mode='tfcrop' freqcutoff=2.7 flagdimension='freq' field='NGC1569' maxnpieces=3" #spw='*:20~100'
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




#


def comb():
    # -170->5

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            ='../n1569/comb/'+os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['../n1569/b00/b00',
                              '../n1569/c00/c00',
                              '../n1569/d00/d00']

    xp=config(xp)
    
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['mosweight']         =True
    xp['scalewt']           =True
    
    xp['imsize']            =2**6*10*3
    xp['cell']              ='2.0arcsec'
    
    xp['clean_mask']        =0.1
    xp['minpb']             =0.01
    xp['clean_mask_cont']   =0.01
    
    xp['clean_start']       ='-231km/s'
    xp['clean_width']       ='2.6km/s'
    xp['clean_nchan']       =113

    xp['multiscale']        =[int(x*(13/2.0)) for x in [0.,1.,3.]]
    
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    
    xp['usescratch']        =False
    xp['fitspw']            ='*:3~13;110~120'
    
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


if  __name__=="__main__":
    
    #b00()
    #c00()
    #d00()
    comb()
   