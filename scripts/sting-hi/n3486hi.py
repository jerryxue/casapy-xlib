
def config():
    
    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~3;44~46'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='400km/s'
    xp['clean_width']       ='10.4km/s'
    xp['clean_nchan']       =47
    xp['phasecenter']       ='J2000 11h00m23.9 +28d58m29.0'
    

    
def n3486b13a():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='../n3486/13B-363.sb24635611.eb28558623.56626.60561628472.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1120+1420'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)



def n3486b13b():


    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
    xp['rawfiles']          ='../n3486/13B-363.sb24635611.eb28563417.56632.4332934375.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1120+1420'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3486c13a():
    
    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n3486/13A-107.sb21345593.eb24163653.56499.04867690972.ms'
    xp['importspw']         ='0'
    xp['importscan']        ='2~18'
    xp['importmode']        ='ms'
    xp['importchanbin']     =1
    xp['importtimebin']     ='30s'
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1125+2610'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def n3486c13b():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n3486/13A-107.sb21389050.eb24163301.56497.97860929398.ms'
    xp['importspw']         ='0'
    xp['importscan']        ='2~9'
    xp['importmode']        ='ms'
    xp['importchanbin']     =1
    xp['importtimebin']     ='30s'
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1125+2610'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3486c13c():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n3486/13A-107.sb21767032.eb24161877.56496.99179714121.ms'
    xp['importspw']         ='0'
    xp['importscan']        ='2~9'
    xp['importmode']        ='ms'
    xp['importchanbin']     =1
    xp['importtimebin']     ='30s'
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1125+2610'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3486c13d():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n3486/13A-107.sb21767248.eb24085777.56481.08748224537.ms'
    xp['importspw']         ='0'
    xp['importscan']        ='2~18'
    xp['importmode']        ='ms'
    xp['importchanbin']     =1
    xp['importtimebin']     ='30s'
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1125+2610'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3486c13e():

    xp=xu.init()
    
    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n3486/13A-107.sb24167009.eb24172200.56503.02696798611.ms'
    xp['importspw']         ='0'
    xp['importscan']        ='2~18'
    xp['importmode']        ='ms'
    xp['importchanbin']     =1
    xp['importtimebin']     ='30s'
    
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['spw_source']        ='0'
    
    xp['fluxcal']           = '1331+305=3C286'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          = 'J1125+2610'
    xp['uvrange_phasecal']  =''
    
    xp['flagselect']        =[]
    xp['flagtsys_range']    =[5.0,200.0]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3486d91():
    
    xp=xu.init()
    
    # IMPORT
    
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
    xp['rawfiles']          ='../n3486/AS428_1'
    xp['importscan']        ='1,12,13,15'
    xp['importspw']         ='0,1,8,9'
    
    # CALIBRATION
    xp['source']            ='NGC3486'
    xp['fluxcal']           ='0134+329'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          ='1117+146' 
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='2,3'
    xp['spw_phasecal']      ='2,3'
    xp['spw_fluxcal']       ='0,1'
    
    xp['flagspw']           ='*:0;60~62'
    xp['flagselect']        =["antenna='VA18'",
                              "uvrange='<1200lambda' field='0134+329'",
                              "timerange='23:40:00~23:45:00' field='0134+329'",
                              "timerange='23:55:00~23:58:20' antenna='VA10'",
                              "timerange='23:55:00~23:58:20' antenna='VA14&VA17'"]
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    # xp=xu.ximport(xp)
    # xu.checkvrange(xp['prefix']+'.ms')
    # au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def n3486hi():
    # execfile(stinghi+'n3486c13a.py')
    # execfile(stinghi+'n3486c13b.py')
    # execfile(stinghi+'n3486c13c.py')
    # execfile(stinghi+'n3486c13d.py')
    # execfile(stinghi+'n3486c13e.py')
    # execfile(stinghi+'n3486b13b.py')
    # execfile(stinghi+'n3486b13a.py')
    # execfile(stinghi+'n3486d91.py')
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n3486d91',
                              'n3486b13a',
                              'n3486b13b',
                              'n3486c13a',
                              'n3486c13b',
                              'n3486c13c',
                              'n3486c13d',
                              'n3486c13e']
    
    # CONSOLIDATING
    execfile(stinghi+'n3486_config.py')
    xp['imsize']            =2**7*10
    xp['cell']              ='2.0arcsec'
    
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