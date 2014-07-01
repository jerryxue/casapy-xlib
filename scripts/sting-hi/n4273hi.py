#line_vrange=[2240,2560]
execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4273/AT259_1','../n4273/AT259_2']
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

xp['imsize']            =2**6*10
xp['cell']              ='4.0arcsec'

xp['cleanmode']     = 'velocity'
xp['clean_start']   ='1855km/s'
xp['clean_nchan']   =int((2957-1855)/20.8+1)
xp['clean_width']   ='20.8km/s'

xp['phasecenter']   ='J2000 12h19m56.06 +05d20m35.90'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')






