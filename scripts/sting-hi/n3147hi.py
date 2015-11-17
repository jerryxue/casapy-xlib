def config():
    
    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~16;40~56'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2200.0km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =int((3400-2200)/20.8)
    xp['phasecenter']       ='J2000 10h16m53.6 +73d24m03.0'

    
def n3147a03():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          =['../n3147/AB1069_11',\
                              '../n3147/AB1069_12']
    xp['starttime']         ="1989/12/15/05:48:45"
    xp['stoptime']          ="2003/06/22/23:59:55"
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['fluxcal']           ='1328+307'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='0950+748'
    xp['phasecal_uvrange']  ='>15klambda'
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:60~62'
    xp['flagselect']        =["timerange='21:53:00~21:56:00'",
                              "timerange='23:12:00~23:17:40'",
                              "timerange='23:34:00~23:35:40'",
                              "antenna='VA04'",
                              "mode='quack' quackinterval=10.0 field='0950+748'"]
    xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147b13a():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='../n3147/13B-363.sb24214388.eb28581165.56639.23767209491.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           ='0542+498=3C147'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J0841+7053'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect_cal']    =["mode='tfcrop' freqcutoff=7.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3147b13b():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
    xp['rawfiles']          ='../n3147/13B-363.sb24214388.eb28583795.56641.325683414354.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           ='0542+498=3C147'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J0841+7053'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147b13c():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='../n3147/13B-363.sb24214388.eb28587660.56645.32513625.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~13'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6
    
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['spw_source']        ='0,1'
    
    xp['fluxcal']           ='0542+498=3C147'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J0841+7053'
    xp['uvrange_phasecal']  =''
    
    # rfi at the spw center
    xp['flagselect']        =["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147bc04():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          =['..//n3147/AS787_13']
    xp['starttime']         ="2004/02/22/08:21:25"
    xp['stoptime']          ="2004/02/22/13:00:00"
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['fluxcal']           ='0542+498'
    xp['fluxcal_uvrange']   ='<50klambda'
    xp['phasecal']          ='0841+708'
    xp['phasecal_uvrange']  ='<20klambda'
    xp['spw_source']        ='0,1'
    
    xp['flagspw']           ='0:0;62,1:0,60~62'
    xp['flagselect']        =["antenna='VA04' timerange='2004/02/22/09:41:40~09:53:30.6'",
                              "antenna='VA06' timerange='2004/02/22/09:41:40~09:53:30.6'",
                              "antenna='VA08' timerange='2004/02/22/11:28:00~11:35:25.0'",
                              "antenna='VA10' timerange='2004/02/22/10:16:00~10:39:00.0'",
                              "antenna='VA11' timerange='2004/02/22/10:16:00~10:39:00.0'",
                              "antenna='VA22' ",
                              "timerange='2004/02/22/08:28:49~08:28:59.5' field='1'",
                              "timerange='2004/02/22/11:50:53~11:51:00.0' field='1'",
                              "timerange='2004/02/22/08:21:20~08:21:40.0' field='0'",
                              "antenna='VA02&VA04'",
                              "antenna='VA08&VA14'",
                              "antenna='VA18&VA04'",
                              "antenna='VA18&VA25'",
                              "timerange='10:59:15~10:59:25'",
                              "mode='quack' quackinterval=5.0 field='NGC3147'",
                              "timerange='11:29:30~11:30:00' field='NGC3147'"]
    
    # CONSOLIDATING & IMAGING
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    xp['spwrgd_method']     ='mstransform'
    xp['fitorder']          =0
    # some record with half spw flagged; oder=1 will create bad line data
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147c90():
    
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          =['../n3147/AV183_2',\
                              '../n3147/AV183_3']
    xp['starttime']         ="1989/12/15/05:48:45"
    xp['stoptime']          ="2003/06/22/23:59:55"
    
    # CALIBRATION
    xp['source']            ='N3147'
    xp['fluxcal']           ='0137+331'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          ='0945+664'
    xp['phasecal_uvrange']  ='<15klambda'
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:0;60~62'
    xp['flagselect']        =["timerange='16:26:40~16:40:00' antenna='VA02&VA24'",
                              "timerange='16:40:20~16:41:40'",
                              "timerange='19:16:35~19:17:00'",
                              "timerange='10:25:50~10:28:20'",
                              "timerange='16:40:40~16:41:20'",
                              "timerange='10:18:10~10:18:50'",
                              "timerange='16:40:00~16:41:00' field='N3147'",
                              "antenna='VA19&VA28'",
                              "antenna='VA17&VA26'"]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147d03a():
    
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          =['../n3147/AB1069_4',\
                              '../n3147/AB1069_5',\
                              '../n3147/AB1069_6']
    xp['starttime']         ="1989/12/15/05:48:45"
    xp['stoptime']          ="2003/03/04/06:09:25"
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['fluxcal']           ='0134+329'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          ='0836+710'
    xp['phasecal_uvrange']  ='<20klambda'
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:60~62'
    xp['flagselect']        =["timerange='03:43:40~03:44:00'",
                              "timerange='01:58:55~01:59:15'",
                              "mode='quack' quackinterval='5.0'",
                              "antenna='VA17' timerange='02:07:40~02:07:50'"]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147d03b():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
    xp['rawfiles']          =['../n3147/AS750_7',\
                              '../n3147/AS750_8',\
                              '../n3147/AS750_9',\
                              '../n3147/AS750_10']
    xp['starttime']         ="2003/03/19/02:41:15.0"
    xp['stoptime']          ="2003/03/19/05:25:15"
    
    # CALIBRATION
    xp['source']            ='NGC3147'
    xp['fluxcal']           ='1331+305'
    xp['fluxcal_uvrange']   =''
    xp['phasecal']          ='0841+708' 
    xp['phasecal_uvrange']  ='<20klambda'
    xp['spw_source']        ='1,0'
    
    xp['flagspw']           ='0:0~1;62,1:0;59~62'
    xp['flagselect']        =["mode='quack' quackinterval=8.0",
                              "field='NGC3147' timerange='02:45:00~02:50:00'",
                              "field='NGC3147' timerange='04:39:40~04:39:50'",
                              "timerange='05:16:50~05:17:00'", "antenna='VA24'",
                              "timerange='05:21:12~05:21:18' field='1331+305' antenna='VA01'"]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    xp['spwrgd_method']     ='mstransform'
    xp['fitorder']          =0
    # some record with half spw flagged; oder=1 will create bad line data
    
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    #xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

    
def n3147d89():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          =['../n3147/AV170_1']
    xp['starttime']         ="1989/12/15/05:48:45"
    xp['stoptime']          ="1989/12/15/10:00:00"
    
    # CALIBRATION
    xp['source']            ='N3147'
    xp['fluxcal']           ='0137+331'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          ='0949+662'
    xp['phasecal_uvrange']  ='<15klambda'
    xp['spw_source']        ='0'
    
    xp['flagspw']           ='*:0;60~62'
    xp['flagselect']        =["timerange='06:05:50~06:06:40'"]
    
    execfile(stinghi+'n3147_config.py')
    xp['niter']             =0
    
    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def n3147hi():
    xp=xu.init()
    
    xp['prefix_comb']       =['n3147a03',
                              'n3147bc04',
                              'n3147c90',
                              'n3147d03b',
                              'n3147d89',
                              'n3147d03a',
                              'n3147b13a',
                              'n3147b13b',
                              'n3147b13c']
    # for one in xp['prefix_comb']:
    #     execfile(stinghi+one+'.py')     
        
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n3147a03',
                              'n3147bc04',
                              'n3147c90',
                              'n3147d03b',
                              'n3147d89',
                              'n3147d03a',
                              'n3147b13a',
                              'n3147b13b',
                              'n3147b13c']
    
    execfile(stinghi+'n3147_config.py')
    
    xp['imsize']            =2**7*10
    xp['cell']              ='2.0arcsec'
    
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2532.8km/s'
    xp['clean_width']       ='20.8km/s'
    xp['clean_nchan']       =int((3052.8-2532.8)/20.8)+1
    
    xp['multiscale']        =[0,3,9]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    
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