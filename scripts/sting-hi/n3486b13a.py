execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/reduc/evla/n3486/13B-363.sb24635611.eb28558623.56626.60561628472.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~13'
xp['importmode']        ='ms'
xp['importchanbin']     =4


# CALIBRATION
xp['source']            ='NGC3486'
xp['spw_source']        ='0,1'

xp['fluxcal']           = '1331+305=3C286'
xp['uvrange_fluxcal']   =''
xp['phasecal']          = 'J1120+1420'
xp['uvrange_phasecal']  =''

xp['flagselect']        =[]
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~3;44~46'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='400km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =47
xp['phasecenter']       ='J2000 11h00m23.9 +28d58m29.0'
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
