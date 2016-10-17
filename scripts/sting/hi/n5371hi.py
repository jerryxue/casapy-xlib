#line_vrange=[2330,2770]


xp=xu.init()

xp['prefix']        ='../n5371/comb/n5371hi'
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

xp['flagspw']       ='*:0;59~62'
xp['flagselect']    =["antenna='VA06&VA17'"]

# CLEANING, IMAGING, & ANALYSIS
xp['uvcs']              =True
xp['fitspw']            ='0:1~25'
xp['fitorder']          = 0

xp['cleanspec']         =True
xp['cleancont']         =True

xp['mosweight']         =True
xp['scalewt']           =True

xp['imsize']            =2**8
xp['cell']              ='15.0arcsec'

xp['clean_mask']        =0.2
xp['clean_mask_cont']   =0.01
xp['minpb']             =0.01

xp['cleanmode']         = 'velocity'
xp['clean_start']       ='2287.25km/s'
xp['clean_nchan']       =int((3441.52-2287.25)/20.8)+1
xp['clean_width']       ='20.8km/s'
xp['phasecenter']       ='J2000 13h55m39.9 +40d27m42.0'

xp['multiscale']        =[int(x*(45/15.0)) for x in [0.,2.,6.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =False

# RUN SCRIPTS
#xp=xu.ximport(xp)
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
xp=xu.xcal(xp)
xp=xu.xconsol(xp)
    
xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xp=xu.xclean(xp)











