execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n4151/12A-428.sb10515683.eb10641965.56087.07239451389.ms'
xp['importspw']         ='2'
xp['importmode']        ='ms'
xp['importchanbin']     =4


# CALIBRATION
xp['source']            ='NGC4536'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='1331+305=3C286'
xp['uvrange_fluxcal']   =''
xp['phasecal']          ='J1254+1141'
xp['uvrange_phasecal']  =''

# rfi at the spw center
xp['flagselect']        =[]#["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~1;22~23'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='1570.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =24
xp['phasecenter']       ='J2000 12h34m27.1 +02d11m16.0'
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
