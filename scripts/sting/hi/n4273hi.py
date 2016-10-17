
#line_vrange=[2240,2560]
xp=xu.init()

xp['prefix']        ='../n4273/comb/n4273hi'
xp['rawfiles']      =[st['hi_raw']+'AT259_1',st['hi_raw']+'AT259_2']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importfield']   ='NGC4273,0134+329,1148-001'
xp['importspw']     ='0'

# TRACK INFORMATION
xp['source']        ='NGC4273'
xp['fluxcal']       ='0134+329'
xp['phasecal']      ='1148-001'

xp['spw_source']    = '0'

xp['flagspw']       = '0:59~62'
xp['flagselect']    =[]

# CLEANING, IMAGING, & ANALYSIS
xp['uvcs']          =True
xp['fitspw']        ='0:5~15;50~58'
xp['fitorder']      =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['mosweight']         =True
xp['scalewt']           =True

xp['imsize']            =2**8*5
xp['cell']              ='3.0arcsec'

xp['clean_mask']        =0.1
xp['clean_mask_cont']   =0.005
xp['minpb']             =0.005

xp['cleanmode']     = 'velocity'
xp['clean_start']   ='1855km/s'
xp['clean_nchan']   =int((2957-1855)/20.8+1)
xp['clean_width']   ='20.8km/s'

xp['phasecenter']   ='J2000 12h19m56.06 +05d20m35.90'

xp['multiscale']        =[int(x*(13.0/3.0)) for x in [0.,1.,5.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS
#xp=xu.ximport(xp)
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#xp=xu.xcal(xp)
#xp=xu.xconsol(xp)


xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xp=xu.xclean(xp)






