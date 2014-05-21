execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n1637b13a' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/evla/n1637/13B-363.sb24606123.eb28499568.56605.30007186343.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~15'
xp['importmode']        ='ms'
xp['importchanbin']     =4


# CALIBRATION
xp['source']            ='NGC1637'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='0137+331=3C48'
xp['uvrange_fluxcal']   =''
xp['phasecal']          ='J0423-0120'
xp['uvrange_phasecal']  =''

# rfi at the spw center
xp['flagselect']        =["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~2;41~43'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+128
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='485km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =44
xp['phasecenter']       ='J2000 04h41m28.2 -02d51m29.0'
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
