def config():

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
    
    
def n4605b():
    
    
    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n4605/AB1038_2',
            '../n4605/AB1038_3',
            '../n4605/AB1038_4',
            '../n4605/AB1038_5',
            '../n4605/AB1038_6',
            '../n4605/AB1038_7']
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
    
    execfile(stinghi+'n4605_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    
    
def n4605c():

    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      = ['../n4605/AB1038_8',
                           '../n4605/AB1038_9',
                           '../n4605/AB1038_10']
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
    
    execfile(stinghi+'n4605_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    


def n4605d():
    
    xp=xu.init()

    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n4605/AC168_1','../n4605/AC168_2','../n4605/AC168_3']
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
    
    execfile(stinghi+'n4605_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def n4605hi():
    
    #execfile(stinghi+'n4605b.py')
    #execfile(stinghi+'n4605c.py')
    #execfile(stinghi+'n4605d.py')
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n4605b',
                              'n4605c',
                              'n4605d']
    
    execfile(stinghi+'n4605_config.py')
    xp['clean_start']       ='1.6km/s'
    xp['clean_nchan']       =15
    xp['imsize']            =2**6*10
    xp['cell']              ='2.0arcsec'
    
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

