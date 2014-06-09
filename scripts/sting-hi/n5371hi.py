#line_vrange=[2330,2770]
execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n5371/AG559_1']
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

xp['flagspw']       = '*:0~20;60~62'
xp['flagselect']    =["antenna='VA02'","antenna='VA06&VA17'"]

# CLEANING, IMAGING, & ANALYSIS
xp['uvcs']          =True
xp['fitspw']        ='2:21~31;56~59'
xp['fitorder']      = 1

xp['imsize']            =2**5810
xp['cell']              ='4.0arcsec'

xp['cleanmode']     = 'velocity'
xp['clean_start']   ='2300km/s'
xp['clean_nchan']   =33
xp['clean_width']   ='20.8km/s'
xp['phasecenter']   ='J2000 13h55m39.9 +40d27m42.0'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')











