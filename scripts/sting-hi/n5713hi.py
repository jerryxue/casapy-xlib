
def config():

    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['imcs']              =True
    xp['fitchans']          ='4~5,21~23'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1570.0km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =24
    xp['phasecenter']       ='J2000 14h40m11.5 -00d17m20.3'


def n5713c12a():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n5713/12A-270.sb8048385.eb8554875.55974.55755017361.ms'
    xp['importmode']        ='ms'
    xp['importspw']         ='2,3,4,10,11,12'
    xp['importchanbin']     =4
    xp['importtimebin']     ='30s'
    
    # CALIBRATION
    xp['source']            ='NGC 5713'
    xp['spw_source']        ='0,1,2,3,4,5'
    
    xp['fluxcal']           ='3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J1445+0958'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =[]#["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    execfile(stinghi+'n5713_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n5713c12b():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n5713/12A-270.sb8048385.eb8591108.55979.37765980324.ms'
    xp['importmode']        ='ms'
    xp['importspw']         ='2,3,4,10,11,12'
    xp['importchanbin']     =4
    xp['importtimebin']     ='30s'
    
    # CALIBRATION
    xp['source']            ='NGC 5713'
    xp['spw_source']        ='0,1,2,3,4,5'
    
    xp['fluxcal']           ='3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J1445+0958'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =[  "antenna='ea06&ea22'",
                                "antenna='ea06&ea19'",
                                "antenna='ea06&ea17'",
                                "timerange='10:08:20~10:11:40' field='NGC 5713'",
                                "timerange='10:18:20~10:20:50' field='NGC 5713'",
                                "timerange='10:27:30~10:30:00' field='NGC 5713'",
                                "timerange='10:55:00~10:56:40' field='NGC 5713'"]
    xp['flagtsys_range']    =[5.0,200.0]
    
    execfile(stinghi+'n5713_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n5713c92():

    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n5713/AP225_1']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    =''
    xp['importspw']     =''
    
    
    # TRACK INFORMATION
    xp['source']        = 'NGC5713'
    xp['spw_source']    ='0'
    
    xp['fluxcal']           = '1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          = '1445+099'
    xp['phasecal_uvrange']  =''
    
    xp['flagspw']           ="*:0~4;56~62"
    xp['flagselect']        =["timerange='12:33:40.0~12:36:30.0'"]
    
    execfile(stinghi+'n5713_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    

    
def n5713d99():
    
    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n5713/AG559_2']
    xp['starttime']     ='1999/04/25/11:04:45.0'
    xp['stoptime']      ='1999/04/25/12:47:45.0'
    xp['importfield']   ='NGC5713,1442+101,1409+524'
    xp['importspw']     ='0'
    
    
    # TRACK INFORMATION
    xp['source']        = 'NGC5713'
    xp['spw_source']    ='0'
    
    xp['fluxcal']           = '1409+524'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='1442+101'
    xp['phasecal_uvrange']  =''
    
    xp['flagspw']           ='*:0;59~62'
    xp['flagselect']        =[    "antenna='VA02'",    
                        "antenna='VA12'",    
                        "antenna='VA06&VA17'" , 
                        "antenna='VA06&VA28'",
                        "antenna='VA07&VA21'"
                        ]
    
    execfile(stinghi+'n5713_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    
    
    
    
def n5713hi():
    # [1760,2060]
    #execfile(stinghi+'n5713c12a.py')
    #execfi le(stinghi+'n5713c12b.py')
    #execfile(stinghi+'n5713c92.py')
    #execfile(stinghi+'n5713d99.py')
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n5713c12a',
                              'n5713c12b',
                              'n5713c92',
                              'n5713d99']
    
    execfile(stinghi+'n5713_config.py')
    xp['scalewt']           =True
    xp['clean_start']       ='1653.2km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =20
    xp['fitchans']          ='0~2,17~19'
    xp['fitorder']          =1
    
    xp['imsize']            =2**6*10
    xp['cell']              ='4.0arcsec'
    
    xp['multiscale']        =[0,4,12]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    
    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
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

