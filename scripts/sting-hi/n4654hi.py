def config():

    # CONSOLIDATING
    xp['spwrgd']            =''
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:1~15;56~59'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =False
    xp['cleancont']         =True
    
    xp['imsize']            =2**6*10
    xp['cell']              ='4.0arcsec'
    
    xp['cleanmode']     = 'velocity'
    xp['clean_start']    ='769km/s'
    xp['clean_nchan']    = 62
    xp['clean_width']    ='10.4km/s'
    xp['phasecenter']    ='J2000 12h43m56.6 +13d07m36.0'
    
    
    
    


def n4654c():

    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n4654/AP206_2']
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
    
    execfile(stinghi+'n4654_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n4654d():

    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n4654/AP206_1']
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
    
    execfile(stinghi+'n4654_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    


def n4654hi():
    #execfile(stinghi+'n4654d.py')
    #execfile(stinghi+'n4654c.py')
    
    xp=xu.init()
    
    xp['prefix_comb']       =['n4654c','n4654d']
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    
    # CLEANING, IMAGING, & ANALYSIS
    
    execfile(stinghi+'n4654_config.py')
    xp['clean_start']    ='810.6km/s'
    xp['clean_nchan']    = 54
    
    xp['multiscale']        =[0,4,12]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
if  __name__=="__main__":
    #n0772d99a()
    #n0772d99b()
    #n0772bc13a()
    #n0772bc13b()
    #n0772b13a()
    #n0772b13b()
    #n0772b13c()
    n0772hi()      
