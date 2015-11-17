def config():
    xp['spwrgd']            ='spw'
    xp['uvcs']            =True
    xp['fitspw']        ='0:0~7;47~57'
    xp['fitorder']        =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']     = 'velocity'
    xp['clean_start']    ='2200km/s'
    xp['clean_nchan']    =int((2850-2215.)/10.4)
    xp['clean_width']    ='10.4km/s'
    xp['phasecenter']    ='J2000 09h14m05.1 +40d06m49.0'

def n2782ab():
    
    xp=xu.init()

    xp['prefix']        ='n2782ab'
    xp['rawfiles']      ='../n2782/AS453_3'
    
    # TRACK INFORMATION
    xp['source']         ='NGC2782'
    
    xp['fluxcal']             = '0134+329'
    xp['fluxcal_uvrange']    ='<40klambda'
    xp['phasecal']            ='0917+449'
    xp['phasecal_uvrange']    ='<20klambda'
    
    xp['spw_source']        ='0'
    xp['flagsp']            ='*:0;60~62'
    
    xp['flagselect']         =     [
                        "timerange='06:10:40~06:10:50' field='0134+329'",
                        "timerange='06:12:20~06:13:00' field='0134+329'",
                        "antenna='VA01&VA12'"
                    ]        
    
    execfile(stinghi+'n2782_config.py')                            
    xp['niter']            =0
    
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
def n2782c():
    xp=xu.init()

    # IMPORT
    xp['prefix']        ='n2782c'
    xp['rawfiles']      ='../n2782/AS453_4'
    
    
    # TRACK INFORMATION
    xp['source']        ='NGC2782'
    
    xp['fluxcal']         ='1328+307'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']     = '0859+470'
    xp['phasecal_uvrange']='<15klambda'
    
    xp['spw_source']     = '0'
    xp['flagspw']        ='*:0;60~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect']     =     [
                        "timerange='01:09:00~01:09:20'",
                        "timerange='02:39:10~02:40:00'",
                        "timerange='02:52:00~02:54:10' antenna='VA13&VA17'",
                        "timerange='03:10:00~03:15:00' antenna='VA13&VA17;VA17&VA19'",
                        "timerange='03:20:50~03:24:10'",
                        "timerange='03:40:00~03:43:20'",
                        "timerange='03:57:30~04:00:50'",
                        "timerange='04:09:10~04:10:00'",
                        "timerange='04:35:50~04:40:00'",
                        "timerange='02:51:40~02:54:10'",
                        "timerange='03:10:50~03:13:20'",
                        "timerange='04:25:50~04:28:00'",
                        "timerange='04:54:10~04:55:00'",
                        "antenna='VA11&VA20' timerange='03:00:00~03:06:40'"
                        ]
    execfile(stinghi+'n2782_config.py')                            
    xp['niter']            =0
    
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
def n2782d():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']        ='n2782d'
    xp['rawfiles']      =['../n2782/AS389_1',
                          '../n2782/AS389_2']
    xp['starttime']     ='1989/12/10/06:49:15.0'
    xp['stoptime']      ='1989/12/10/16:13:15.0'
    xp['importspw']     ='0'
    
    
    # TRACK INFORMATION
    xp['source']        ='NGC2782'
    
    xp['fluxcal']         ='1328+307'
    xp['fluxcal_uvrange']    =''
    xp['phasecal']     = '0859+470'
    xp['phasecal_uvrange']='<15klambda'
    
    xp['spw_source']     = '0'
    xp['flagspw']        ='*:0;60~62'
    
    xp['flagselect']     =[
                        "timerange='10:50:00~10:52:20' antenna='VA09&VA12'",
                        "timerange='13:15:00~13:17:00' antenna='VA09&VA12'",
                        "timerange='09:23:20~09:26:40'",
                        "timerange='09:33:20~09:36:40'",
                        "timerange='09:51:40~09:53:20'",
                        "timerange='10:00:00~10:01:40'",
                        "timerange='10:19:10~10:20:00'",
                        "timerange='10:38:20~10:39:10'",
                        "timerange='12:56:40~12:57:30'",
                        "timerange='14:40:00~14:41:40'",
                        "timerange='14:48:20~14:50:00'",
                        "timerange='15:06:40~15:10:00'",
                        "timerange='13:17:30~13:19:10'",
                        "timerange='15:13:20~15:20:00'",
                        "timerange='11:00:40~11:01:20'",
                        "timerange='10:51:10~10:52:00'",
                        "timerange='15:25:00~15:50:00' field='NGC2782'",
                        "uvrange='<500lambda' field='0859+470'",
                        "timerange='10:10:00~10:11:40'",
                        "timerange='11:14:10~11:15:50'",
                        "timerange='11:21:40~11:23:20'",
                        "timerange='15:20:00~15:21:40'"
                    ]
    execfile(stinghi+'n2782_config.py')                            
    xp['niter']            =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    
    
    
    
    
    
    


def n2782hi():
    #2390,2725
    
    execfile(stinghi+'n2782ab.py')
    execfile(stinghi+'n2782c.py')
    execfile(stinghi+'n2782d.py')
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n2782ab',
                              'n2782c',
                              'n2782d']
    
    execfile(stinghi+'n2782_config.py')
    xp['imsize']            =2**6*10
    xp['cell']              ='4.0arcsec'
    xp['clean_start']    ='2252km/s'
    xp['clean_nchan']    =int((2824-2252.)/10.4)
    
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