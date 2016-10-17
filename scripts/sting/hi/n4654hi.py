def c92():

    xp=xu.init()
    
    xp['prefix']        =inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AP206_2'
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source']        = 'NGC4654'
    
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '1221+282'
    
    xp['spw_source']    = '0'
    xp['flagspw']       = '*:0;60~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    =["timerange='1992/03/12/04:03:20~1992/03/12/04:06:40'",
                          "timerange='1992/03/12/10:16:25.0~1992/03/12/10:16:35.0'"
                          ]
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def d92():

    xp=xu.init()
    
    xp['prefix']        =inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AP206_1'
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    =''
    xp['importspw']     ='1'
    
    
    # TRACK INFORMATION
    xp['source']        = 'NGC4654'
    
    xp['fluxcal']       = '1331+305'
    xp['phasecal']      = '1221+282'
    
    xp['spw_source']    = '0'
    xp['flagspw']       = '*:0;60~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']    =["antenna='VA10'"]
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def d14():
    #   KS
    #
    xp=xu.init()

    # IMPORT
    xp['prefix']            =inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'14A-468.sb29385635.eb29466750.56849.87760721065.ms'
    xp['importspw']         ='8'
    xp['importmode']        ='ms'
    xp['importchanbin']     =8


    # CALIBRATION
    xp['source']            ='NGC4654'
    xp['spw_source']        ='0'

    xp['fluxcal']           ='1331+305=3C286'
    #xp['uvrange_fluxcal']   ='<40klambda'
    xp['phasecal']          = 'J1254+1141'
    #xp['uvrange_phasecal']  ='<100klambda'

    #xp['flagselect']        =["antenna='ea08&ea26'"]
    xp['flagspw']           ='0:0~25;485~511'
    xp['flagtsys_range']    =[5.0,200.0]

    xp=config(xp)
    xp['niter']             =0
    xp['fitspw']            ='0:1~15;56~59'
    xp['imsize']            =2**6*5
    xp['cell']              ='12arcsec'

    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    #xu.checkvrange(xp['prefix']+'.src.ms')
    #au.timeOnSource(xp['prefix']+'.src.ms')

def config(xp):

    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='0:1~15;56~59'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**6*10
    xp['cell']              ='4.0arcsec'
    
    xp['cleanmode']     = 'velocity'
    xp['clean_start']    ='769km/s'
    xp['clean_nchan']    = 62
    xp['clean_width']    ='10.4km/s'
    xp['phasecenter']    ='J2000 12h43m56.6 +13d07m36.0'
    
    return xp
    
    
def comb():

    
    xp=xu.init()
    
    xp['prefix_comb']       =['../n4654/c92/c92','../n4654/d92/d92','../n4654/d14/d14']
    xp['prefix']            ='../n4654/comb/n4654hi'
    
    # CLEANING, IMAGING, & ANALYSIS
    
    xp=config(xp)
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['mosweight']         =True
    xp['scalewt']           =True
    
    xp['imsize']            =2**8*5
    xp['cell']              ='3arcsec'

    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01

    xp['clean_start']    ='810.6km/s'
    xp['clean_nchan']    = 54
    
    xp['multiscale']        =[int(x*(19.0/3.0)) for x in [0.,1.,3.]]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    
    xp['fitspw']            ='*:1~15;56~59'
    
    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
    
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'
    xp=xu.xclean(xp)
    
if  __name__=="__main__":
    
    c92()
    d92()
    #d14()
    comb()      
