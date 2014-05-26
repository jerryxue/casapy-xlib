execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n0772/AE175_sb1124713_1.55310.66684534722.ms'
xp['importmode']        ='ms'
xp['importtimebin']     ='30s'

# CALIBRATION
xp['source']            ='NGC0772'
xp['spw_source']        ='0,1'

xp['fluxcal']           = '0137+331=3C48'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = 'J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagselect']        =["antenna='ea08' spw='*:16'",
                          "antenna='ea16' spw='*:16'",
                          "antenna='ea20' spw='*:16'",
                          "antenna='ea25' spw='*:16'",
                          "antenna='ea26' spw='*:16'",
                          "antenna='ea28' spw='*:16'"]
xp['flagtsys_range']    =[5.0,200.0]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
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
execfile(xlib+'ximport.py')
# execfile(xlib+'xcal.py')
# execfile(xlib+'xcalplot.py')
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
