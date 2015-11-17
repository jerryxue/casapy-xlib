
def config():

    xp['spwgrid']       =''
    xp['uvcs']          =True
    xp['fitspw']        ='0:5~18,1:45~56'
    xp['fitorder']      =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**6*10
    xp['cell']              ='4.0arcsec'
    
    xp['cleanmode']      = 'velocity'
    xp['clean_start']='410km/s'
    xp['clean_nchan']=88
    xp['clean_width']='5.2km/s'
    
    xp['phasecenter']='J2000 11h14m37.0 +12d49m3.6'
    
    
    
def n3593c96():
    
    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n3593/AC459_2','../n3593/AC459_3','../n3593/AC459_4']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    =''
    xp['importspw']     =''
    
    
    # TRACK INFORMATION
    xp['source'] = 'NGC3593'
    
    xp['fluxcal'] = '1328+307'
    xp['fluxcal_uvrange']=''
    xp['phasecal'] = '1117+146'
    xp['phasecal_uvrange']=''
    
    xp['spw_source'] = '0,1'
    xp['flagspw'] = '*:0~4;57~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] = ["mode='quack' quackinterval=8.0",
                    "timerange='03:42:30~03:43:00 ",
                    "timerange='06:51:10~06:51:20'",
                    "timerange='05:02:30~05:02:50'",
                    "timerange='07:11:14~07:11:16'",
                    "timerange='07:53:40~07:53:50'",
                    "timerange='08:02:10~08:02:20' "
                    ]
    execfile(stinghi+'n3593_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)





def n3593d96():

    xp=xu.init()
    
    xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']      =['../n3593/AC459_5','../n3593/AC459_6']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    ='2~9'
    xp['importspw']     =''
    
    
    
    # TRACK INFORMATION
    xp['source'] = 'NGC3593'
    
    xp['fluxcal'] = '1328+307'
    xp['fluxcal_uvrange']=''
    xp['phasecal'] = '1117+146'
    xp['phasecal_uvrange']=''
    
    xp['spw_source'] = '0,1'
    xp['flagspw'] = '*:0~4;57~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] =  [  "mode='quack' quackinterval=8.0 ",
                    "timerange='23:25:40~23:26:20'",
                    "timerange='23:32:40~23:50:00'",
                    "antenna='VA17' timerange='23:30:00~23:31:00'",
                    "antenna='VA16' timerange='22:13:00~22:13:30'",
                    "antenna='VA16' timerange='22:32:30~22:33:00'",
                    "antenna='VA16' timerange='23:01:30~23:02:00'",
                    "antenna='VA01' timerange='22:44:00~22:44:30'",
                    "timerange='22:48:00~22:48:30'",
                    "antenna='VA28' timerange='22:58:30~22:59:00'"
                    "uvrange='900lambda'",
                    "timerange='23:26:30~23:27:00' field='1328+307' antenna='VA16'",
                    "antenna='VA12' timerange='22:07:30~22:08:00'",
                    "antenna='VA12' timerange='23:16:30~23:17:00'"
                    ]
    execfile(stinghi+'n3593_config.py')
    xp['niter']        =0
    
    # RUN SCRIPTS
    #xp=xu.ximport(xp)
    #xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    


def n3593hi():
    #[470,770]
    
    #execfile(stinghi+'n3593c96.py')
    #execfile(stinghi+'n3593d96.py')
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n3593c96',
                              'n3593d96']
    
    execfile(stinghi+'n3593_config.py')
    
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