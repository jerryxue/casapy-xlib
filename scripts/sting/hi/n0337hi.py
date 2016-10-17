#    DATA REPO 
#        wget ftp://ftp.aoc.nrao.edu/e2earchive/AT285_P030216.xp1
#        wget ftp://ftp.aoc.nrao.edu/e2earchive/AM0873_E061104.xp2

def c06():

    xp=xu.init()

    # IMPORT
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AM0873_E061104.xp2'
    xp['importspw']     ='0,1'
    
    # CALIBRATION
    xp['source']            ='NGC0337'
    xp['spw_source']        ='0,1'

    xp['fluxcal']           ='0137+331'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          ='0059+001'


    xp['flagspw']           ="0:0~2;58~62,1:0~2;58~62"
    xp['flagselect']        =["timerange='04:45:30~04:50:49'",
                              "timerange='04:43:20~04:44:50'",
                              "antenna='VA11&VA21'",
                              "antenna='VA06&VA21'",
                              "antenna='VA06&VA11'",
                              "antenna='VA03&VA04'",
                              "antenna='VA09' timerange='2006/11/04/04:48:20~04:56:40' field='NGC0337' spw='0:29~30'",
                              "timerange='2006/11/04/03:25:00~03:26:40' antenna='VA06&VA15'",
                              "timerange='2006/11/04/02:28:40~02:29:30' antenna='VA07&VA15'",
                              "timerange='2006/11/04/01:59:35~01:59:45'",
                              "timerange='2006/11/04/03:07:15~03:07:25'",
                              "timerange='2006/11/04/04:15:00~04:15:15'",
                              "timerange='2006/11/04/10:03:45~10:04:15'",
                              "timerange='2006/11/04/10:04:54~10:05:06'",
                              "timerange='2006/11/04/10:06:04~10:06:16'",
                              "timerange='2006/11/04/04:33:06~04:34:05'"]
    xp=config(xp)
    
    xp['imsize']            =2**5*10*4
    xp['cell']              ='3.0arcsec'
    xp['imsize']            =2**5*10*2
    xp['cell']              ='6.0arcsec'    
    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01
    
    xp['cleanspec']         =True
    xp['cleancont']         =False

    xp['fitspw']            ='0:1~10;92~101'
    xp['fitorder']          =0
    
    xp['uvcs']      =False
    xp['imcs']      =False
    xp['fitchans']  ='8~21;86~101'
    xp['fitorder']          =0


    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xp=xu.xcal(xp)
    #xp=xu.xconsol(xp)
    #xp=xu.xclean(xp)
    #xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')

def d03():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    print inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AT285_P030216.xp1'
    xp['importspw']     ='0,1'

    # CALIBRATION
    xp['source']            ='NGC0337'
    xp['spw_source']        ='0,1'

    xp['fluxcal']           ='0137+331'
    xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          ='0059+001'
    
    xp['flagspw']           ="0:0~2;58~62,1:0~2;58~62"
    xp['flagselect']        =[  "timerange='2003/02/16/22:06:02~22:06:30' field='0137+331'",
                                "antenna='VA08&VA11'",
                                "antenna='VA20&VA11'",
                                "antenna='VA03&VA08'",
                                "antenna='VA03&VA09'",
                                "antenna='VA03&VA10'",
                                "antenna='VA14&VA27'",
                                "antenna='VA08&VA14'",
                                "antenna='VA08&VA10'",
                                "antenna='VA04&VA20'",
                                "antenna='VA10&VA15'",
                                "antenna='VA09&VA19'",
                                "antenna='VA02&VA03'"]
    addselect=["antenna='VA12&VA28'",
               "antenna='VA03&VA27'",
               "antenna='VA21&VA24'",
               "antenna='VA10&VA14'",
               "antenna='VA07&VA24'",
               "antenna='VA03&VA17'",
               "antenna='VA12&VA21'",
               "antenna='VA07&VA17'"]
    xp['flagselect']=xp['flagselect']+addselect
    
    xp=config(xp)
    xp['imsize']            =2**4*10*3
    xp['cell']              ='8.0arcsec'
    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01
    #xp['niter']             =0
    
    xp['cleanspec']         =False
    xp['cleancont']         =True

    xp['fitspw']            ='0:4~10;92~97'
    xp['fitorder']          =0
    xp['combinespws']       =True
    xp['uvcs_combine']      ='spw'
    
    xp['uvcs']      =True
    xp['imcs']      =False
    xp['fitchans']  ='8~21;86~101'
    xp['fitorder']          =1

    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xp=xu.xcal(xp)
    #xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    #xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')


def config(xp):

    xp['spwrgd']            ='spw'
    xp['spwrgd_method']     ='mstransform'
    xp['uvcs']              =True
    xp['fitspw']              ='0:0~6;88~105'
    xp['fitorder']          =0

    # IMAGING
    xp['cleanspec']         =False
    xp['cleancont']         =True
    
    xp['imsize']            =2**6*10
    xp['cell']              ='6.0arcsec'
    xp['clean_mask']        =0.1
    xp['minpb']             =0.1

    #xp['imstat_box_spec']   ='401,239,545,469'

    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1360.00km/s'
    xp['clean_width']       ='5.2km/s'
    xp['clean_nchan']       =107
    xp['phasecenter']       ='J2000 00h59m50.1 -07d34m41.0'
    xp['usescratch']        =False
    
    return xp
    
    
def comb():
    #1474->1792

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            ='../n0337/comb/n0337hi'
    xp['prefix_comb']       =['../n0337/d03/d03','../n0337/c06/c06']

    xp=config(xp)
    #xp['fitchans']          ='0~13;77~94'

    xp['clean_start']       ='1406.8km/s'
    xp['clean_width']       ='5.2km/s'
    xp['clean_nchan']       =int((1890.40-1406.8)/5.2+1.0)

    xp['multiscale']        =[int(x*(18/4.0)) for x in [0.,1.,3.]]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    
    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01
    
    xp['imsize']            =2**8*5
    xp['cell']              ='3.0arcsec'
    
    xp['fitspw']            ='0:4~10;92~97'
    
    xp['cleanspec']         =True
    xp['cleancont']         =True
    xp['scalewt']           =True

    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'
    xp=xu.xclean(xp)
    
    #xu.mossen(vis=xp['prefix']+'.src.ms',
    #  log=xp['prefix']+xp['ctag']+'.line.sens.log',
    #  nchan=xp['clean_nchan'],ftmachine='mosaic',
    #  mosweight=True,imsize=xp['imsize'],
    #  weight=xp['cleanweight'])


if  __name__=="__main__":
    #c06()
    #d03()  
    comb()      

