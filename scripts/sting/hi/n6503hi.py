# line_vrange=[1760,2060]
xp=xu.init()

xp['prefix']        ='../comb/n6503hi'
xp['rawfiles']      =st['hi_raw']+'AD211_A880125.xp1'
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='16~21'
xp['importspw']     ='7,8'
xp['importfield']   ='N6503,1803+784,1328+307'

# TRACK INFORMATION
xp['source']        = 'N6503'
xp['fluxcal']       = '1328+307'
xp['phasecal']      = '1803+784'

xp['spw_source']    = '1'
xp['spw_fluxcal']   = '0'
xp['spw_phasecal']  = '1'

xp['flagspw']       ='*:0~10;236~254'
xp['flagselect']    =["timerange='14:30:20~14:32:20' field='1328+307'",
                      "timerange='15:00:50~15:05:10' field='1803+784'"]


xp['uvcs']          =True
xp['fitspw']        ='0:11~30;219~225'
xp['fitorder']      =1

xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']        =2**6*10
xp['cell']          ='4.0arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

xp['cleanmode']     = 'velocity'
xp['clean_start']   ='-161km/s'
xp['clean_nchan']   =49
xp['clean_width']   ='10.4km/s'

xp['phasecenter']   ='J2000 17h49m26.5 +70d08m39.6'

# RUN SCRIPTS
xp=xu.ximport(xp)
xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
xp=xu.xcal(xp)
xp=xu.xconsol(xp)
xp=xu.xclean(xp)





