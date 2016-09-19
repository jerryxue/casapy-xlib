def config(xp):
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='0:12~20;35~40'
    xp['fitorder']          =1
    
    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['imsize']            =2**5*10
    xp['cell']              ='8.0arcsec'
    
    xp['cleanmode']            ='velocity'
    xp['clean_start']        ='456km/s'
    xp['clean_width']        ='20.8km/s'
    xp['clean_nchan']        =int((1520-456)/20.8+1)
    xp['phasecenter']        ='J2000 12h10m32.6 +39d24m21.0'
    
    return xp


def a1():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AB605B_6'
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    ='19~32'
    xp['importspw']     ='6,7,8'
    
    
    # TRACK INFORMATION
    xp['source']         = 'NGC4151'
    xp['spw_source']    ='0'
    
    xp['fluxcal']         = '1328+307'
    xp['fluxcal_uvrange']=''
    xp['phasecal']         = '1225+368' 
    xp['phasecal_uvrange']=''
    
    xp['spw_fluxcal']     ='2'
    xp['spw_phasecal']    ='1'
    
    xp['flagspw']       ='*:0;57~62'
    xp['flagselect']    =["antenna='VA25'",
                          "antenna='VA26'",
                          "field='1225+368' antenna='VA09&VA25' spw='1:25'",
                          "field='1225+368' antenna='VA09&VA13' spw='1:25'",
                          "field='1225+368' antenna='VA25&VA26' spw='1:25'",
                          "field='1225+368' antenna='VA13&VA25' spw='1:25'",
                          "field='1225+368' antenna='VA06&VA26' spw='1:25'",
                          "field='1225+368' antenna='VA06&VA23' spw='1:25'",
                          "field='1225+368' antenna='VA06&VA09' spw='1:25'",
                          "field='1225+368' antenna='VA06&VA25' spw='1:25'"]
    
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    


def a2():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AB658_7',st['hi_raw']+'AB658_8']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    ='17~22'
    xp['importspw']     ='8~9'
    
    
    
    # TRACK INFORMATION
    xp['source']         = 'NGC4151'
    xp['spw_source']    ='0,1'
    
    xp['fluxcal']         = '1328+307'
    xp['fluxcal_uvrange']='0,1'
    xp['phasecal']         = '1225+368' 
    xp['phasecal_uvrange']='0,1'
    
    xp['flagspw']    ='*:30'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] =     []
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    


def a3():

    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AM591_14',st['hi_raw']+'AM591_15']
    xp['starttime']     =''
    xp['stoptime']      =''
    xp['importscan']    ='21~28'
    xp['importspw']     ='3'
    
    # TRACK INFORMATION
    xp['source']         = 'NGC4151'
    xp['spw_source']    ='0'
    
    xp['fluxcal']         = '1328+307'
    xp['fluxcal_uvrange']=''
    xp['phasecal']         = '1223+395' 
    xp['phasecal_uvrange']=''
    
    
    xp['flagspw']    ='*:0;59~62'
    
    # CALIBRATION & OPTIONS
    xp['flagselect'] =     []
    
    xp=config(xp)
    xp['niter']        =0
    
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

    
def b93():


    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AP251_9',st['hi_raw']+'AP251_10']
    xp['starttime']     ='1993/04/23/22:58:15.0'
    xp['stoptime']      ='1993/04/24/10:31:15.0'
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source']         = 'NGC4151'
    xp['spw_source']    ='0'
    
    xp['fluxcal']        = '1328+307'
    xp['fluxcal_uvrange']=''
    xp['spw_fluxcal']    ='0'
    
    xp['phasecal']         = '1225+368' 
    xp['phasecal_uvrange']=''
    
    
    
    # CALIBRATION & OPTIONS
    xp['flagspw']        ='*:0;60~62'
    xp['flagselect']     = [     "antenna='VA11'",
                    "mode='quack' quackinterval=4.0",
                    "timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA21&VA22'",
                    "timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA14&VA21'",
                    "timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA14&VA22'"
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
    
    
    

    
def c1():


    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =st['hi_raw']+'AP104_1'
    xp['importband']    ='L'
    xp['starttime']     ='1985/09/12/15:10:15.0'
    xp['stoptime']      ='1985/09/12/19:43:15.0'
    xp['importscan']    =''
    xp['importspw']     ='0'
    
    
    # TRACK INFORMATION
    xp['source'] = 'N4151'
    
    xp['fluxcal'] = '3C286'
    xp['fluxcal_uvrange']=''
    xp['phasecal'] = '1216+487' 
    xp['phasecal_uvrange']=''
    xp['passcal']= '3C286'
    xp['passcal_uvrange']=''
    xp['spw_source'] = '0'
    
    # CALIBRATION & OPTIONS
    
    xp['flagselect']=        [    "antenna='VA20'",
                        "antenna='VA18&VA27' timerange='1985/09/12/16:14:10.0~1985/09/12/16:14:20.0'",
                        "uvrange='<500lambda' field='1216+487'",
                        "timerange='1985/09/12/18:45:00.0~1985/09/12/18:45:30.0'"
                    ]
    xp['ref_ant']    ='16'
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    
    
    

    
def c2():
    


    xp=xu.init()
    
    xp['prefix']        ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']      =[st['hi_raw']+'AP104_2',
                          st['hi_raw']+'AP104_3',
                          st['hi_raw']+'AP104_4',
                          st['hi_raw']+'AP104_5']
    xp['importband']    ='L'
    xp['starttime']     ='1985/09/14/17:02:15.0'
    xp['stoptime']      ='1985/09/15/03:19:15.0'
    xp['importscan']    =''
    xp['importspw']     =''
    
    # TRACK INFORMATION
    xp['source'] = 'N4151'
    
    xp['fluxcal'] = '3C286'
    xp['fluxcal_uvrange']=''
    xp['phasecal'] = '1216+487' 
    xp['phasecal_uvrange']=''
    xp['passcal']= '3C286'
    xp['passcal_uvrange']=''
    xp['spw_source'] = '0'
    
    # CALIBRATION & OPTIONS
    
    xp['flagselect']=   [  "antenna='VA20' timerange='24:55:00~24:56:40'",
                    "antenna='VA18&VA27'",
                    "antenna='VA11&VA27'",
                    "antenna='VA06&VA19'",
                    "antenna='VA08' timerange='17:08:00~17:16:40'",
                    "timerange='19:15:00~19:15:50'",
                    "antenna='VA11&VA18'",
                    "antenna='VA21&VA27'",
                    "antenna='VA21&VA25'",
                    "antenna='VA25&VA27'",
                    "antenna='VA06&VA18'",
                    "antenna='VA18&VA21'",
                    "scan='17~36'"
                ]
    xp['ref_ant']    ='16'
    
    xp=config(xp)
    xp['niter']        =0
    
    # RUN SCRIPTS
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)
    

def comb():
    
    #  [865,1120]

    
    
    xp=xu.init()
    
    # CONSOLIDATING
    xp['prefix']            ='../comb/n4151hi'
    xp['prefix_comb']       =[#'n4151a1', large bandpass offset 
                              '../a2/a2',
                              '../a3/a3',
                              '../b93/b93',
                              '../c1/c1',
                              '../c2/c2']
    
    xp=config(xp)
    
    xp['imsize']            =2**7*10
    xp['cell']              ='2.0arcsec'
    xp['clean_start']        ='726.4km/s'
    xp['clean_width']        ='20.8km/s'
    xp['clean_nchan']        =int((1267.2-726.4)/20.8+1)
    
    xp['multiscale']        =[0,4,12]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True
    xp['outertaper']        =['8arcsec']
    xp['clean_mask']        ='circle[[12h10m32.6,+39d24m21.0],650arcsec]'
    
    # RUN SCRIPTS:
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

if  __name__=="__main__":
    a2()
    a3()
    b93()
    c1()
    c2()
    comb()