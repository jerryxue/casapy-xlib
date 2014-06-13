# line_vrange=[1760,2060]
execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n6503/AD211_A880125.xp1']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     ='3,8'

# TRACK INFORMATION
xp['source']        = 'N6503'
xp['fluxcal']       = '1328+307'
xp['phasecal']      = '1803+784'

xp['spw_source']    = '1'
xp['spw_fluxcal']   = '0'
xp['spw_phasecal']  ='1'

xp['flagspw']       =''# '*:0~20;58~62'
xp['flagselect']    =[]#["antenna='VA02'","antenna='VA06&VA17'"]

xp['uvcs']          =True
xp['fitspw']        = '0:21~23;55~57'
xp['fitorder']      = 1

xp['imsize']        =512+128
xp['cell']          ='4.0arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

xp['cleanmode']     = 'velocity'
xp['clean_start']   ='2288km/s'
xp['clean_nchan']   =34
xp['clean_width']   ='20.8km/s'

xp['phasecenter']   ='J2000 13h55m39.9 +40d27m42.0'


# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')





