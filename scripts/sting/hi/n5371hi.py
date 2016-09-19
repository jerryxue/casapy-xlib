#line_vrange=[2330,2770]
xp=xu.init()

xp['prefix']        ='../comb/n5371hi'
xp['rawfiles']      =st['hi_raw']+'AG559_1'
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='8~10,17'
xp['importspw']     =''


# TRACK INFORMATION
xp['source']        = 'NGC5371'
xp['fluxcal']       = '1409+524'
xp['phasecal']      = '1419+419'

xp['spw_source']    = '2'
xp['spw_fluxcal']   = '1'
xp['spw_phasecal']  ='2'

xp['flagspw']       ='*:0~16;57~62'
xp['flagselect']    =["antenna='VA02'","antenna='VA06&VA17'"]

# CLEANING, IMAGING, & ANALYSIS
xp['uvcs']              =True
xp['fitspw']            ='*:17~27;56~57'
xp['fitorder']          = 1
# here order=0 works better
xp['fitspw']            ='*:17~27'
xp['fitorder']          = 0

xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**5*10
xp['cell']              ='12.0arcsec'

xp['cleanmode']         = 'velocity'
xp['clean_start']       ='2310.0km/s'
xp['clean_nchan']       =27
xp['clean_width']       ='20.8km/s'
xp['phasecenter']       ='J2000 13h55m39.9 +40d27m42.0'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =-1
xp['usescratch']        =True
xp['clean_mask']        ='circle[[13h55m43.9s,+40d27m46.0s],550arcsec]'

# RUN SCRIPTS
xp=xu.ximport(xp)
xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
xp=xu.xcal(xp)
xp=xu.xconsol(xp)
xp=xu.xclean(xp)











