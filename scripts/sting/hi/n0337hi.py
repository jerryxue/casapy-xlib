#    DATA REPO 
#        wget ftp://ftp.aoc.nrao.edu/e2earchive/AT285_P030216.xp1
#        wget ftp://ftp.aoc.nrao.edu/e2earchive/AM0873_E061104.xp2

def config(xp):

    xp['spwrgd']            ='spw'
    xp['uvcs']              =True
    xp['fitspw']          	='*:0~6;88~105'
    xp['fitorder']          =1

    # IMAGING
    xp['cleanspec']         =True

    xp['imsize']            =2**6*10
    xp['cell']              ='6.0arcsec'
    xp['clean_mask']        =0.1
    xp['minpb']             =0.1

    xp['imstat_box_spec']   ='401,239,545,469'

    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1360.00km/s'
    xp['clean_width']       ='5.2km/s'
    xp['clean_nchan']       =107
    xp['phasecenter']       ='J2000 00h59m50.1 -07d34m41.0'
    xp['usescratch']        =True
    
    xp['fitorder']          =0
    xp['spwrgd_method']     ='mstransform'
    return xp
    

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


    xp['flagspw']           ="0:0~4;60~62,1:0;58~62"
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
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
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

    xp['flagspw']           ="0:0~4;60~62,1:0;58~62"
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
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    #xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')
    
def comb():
    #1474->1792

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            ='../comb/n0337hi'
    xp['prefix_comb']       =['../d03/d03','../c06/c06']

    xp=config(xp)
    #xp['fitchans']          ='0~13;77~94'

    xp['clean_start']       ='1401.6km/s'
    xp['clean_width']       ='5.2km/s'
    xp['clean_nchan']       =int((1895.6-1410.6)/5.2+1.0)

    xp['multiscale']        =[0,3,9]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0

    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


if  __name__=="__main__":
    c06()
    d03()  
    comb()      

