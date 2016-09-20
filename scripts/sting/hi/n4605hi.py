def config(xp):

    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~4;16~19'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']     = 'velocity'
    xp['clean_start']   ='-40km/s'
    xp['clean_nchan']   =20
    xp['clean_width']   ='20.8km/s'
    xp['phasecenter']   ='J2000 12h40m00.0 +61d36m31.01'
    
    return xp
    
    
def b00():
    
    
    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AB1038_2',
            st['hi_raw']+'AB1038_3',
            st['hi_raw']+'AB1038_4',
            st['hi_raw']+'AB1038_5',
            st['hi_raw']+'AB1038_6',
            st['hi_raw']+'AB1038_7']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    =''
    xp['importspw']     ='0'
    
    # TRACK INFORMATION
    xp['source']        ='NGC4605'
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '1313+675'
    
    xp['spw_source']    ='0'
    xp['flagspw']       ='*:0;61~62'
    
    # CALIBRATION & OPTION
    xp['flagselect'] = ["antenna='VA08&VA12'",
                        "antenna='VA20'",
                        "antenna='VA11'"
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
    
    
    
    
def c00():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      = [st['hi_raw']+'AB1038_8',
                           st['hi_raw']+'AB1038_9',
                           st['hi_raw']+'AB1038_10']
    xp['starttime']     ='2002/12/19/07:54:45'
    xp['stoptime']      ='2002/12/19/11:45:15'
    xp['importscan']    =''
    xp['importspw']     ='0'
    
    
    # TRACK INFORMATION
    xp['source']        ='NGC4605'
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '1313+675'
    
    xp['spw_source']    ='0'
    xp['flagspw']       ='*:0;61~62'
    
    # CALIBRATION & OPTION
    xp['flagselect'] = ["antenna='VA20'",
                "antenna='VA07&VA08'",
                "antenna='VA08&VA10'",
                "antenna='VA15&VA28'",
                "antenna='VA14&VA16'"]
    
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

    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AC168_1',st['hi_raw']+'AC168_2',st['hi_raw']+'AC168_3']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importfield']   ='N4605,1203+645,3C286'
    xp['importscan']    ='32,34,35,36,37,38,57'
    xp['importspw']     ='3,8'
    
    # TRACK INFORMATION
    xp['source']         = 'N4605'
    xp['fluxcal']        = '3C286'
    xp['phasecal']       = '1203+645'
    
    xp['spw_source']     = '1'
    xp['spw_fluxcal']    = '1'
    xp['spw_phasecal']   = '0'
    
    xp['flagspw']        ='' #'0:0~3;58~63'
    xp['flagselect']    =[]
    
    
    xp=config(xp)
    xp['spwrgd_method']     ='mstransform'
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def comb():
    
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            ='../comb/n4605hi'
    xp['prefix_comb']       =['../b00/b00',
                              '../c00/c00',
                              '../d00/d00']
    
    xp=config(xp)
    xp['clean_start']       ='1.6km/s'
    xp['clean_nchan']       =15
    xp['imsize']            =2**6*10
    xp['cell']              ='2.0arcsec'
    
    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

if  __name__=="__main__":
    
    #b00()
    #c00()
    #d00()
    comb()      

