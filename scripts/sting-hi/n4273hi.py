#line_vrange=[2240,2560]
execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4273/AT259_A010714.xp1']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    =''
xp['importspw']     ='0'

# TRACK INFORMATION
xp['source']        ='NGC5371'
xp['fluxcal']       ='1409+524'
xp['phasecal']      ='1419+419'

xp['spw_source']    = '2'
xp['spw_fluxcal']   = '1'
xp['spw_phasecal']  ='2'

xp['flagspw']       = '*:0~20;58~62'
xp['flagselect']    =["antenna='VA02'","antenna='VA06&VA17'"]

# CLEANING, IMAGING, & ANALYSIS
xp['uvcs']          =True
xp['fitspw']        = '0:21~23;55~57'
xp['fitorder']      = 1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='4.0arcsec'

xp['cleanmode']     = 'velocity'
xp['clean_start']   ='2288km/s'
xp['clean_nchan']   =34
xp['clean_width']   ='20.8km/s'

xp['phasecenter']   ='J2000 13h55m39.9 +40d27m42.0'
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')






