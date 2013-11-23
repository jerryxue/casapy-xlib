execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n0772b13b' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/evla/n0772/13B-363.sb24635393.eb28501581.56608.280407708335.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~13'
xp['importmode']        ='ms'
xp['importwidth']       =['8','8']

# CALIBRATION
xp['source']            ='NGC0772'
xp['spw_source']        ='0,1'

xp['fluxcal']           = '0137+331=3C48'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = 'J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagselect']        =[]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['uvcs']              =True
xp['fitspw']            ='*:0~5;33~38'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512
xp['cell']              ='6.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2050.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =39
xp['phasecenter']      ='J2000 01h59m19.58 +19d00m27.10'
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
