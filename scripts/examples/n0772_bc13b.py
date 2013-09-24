execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n0772bc13b' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/evla/n0772/13B-363.sb24382374.eb25241357.56541.46377263889.ms'
xp['importspw']         ='2,12'
xp['importscan']        ='2~15'
xp['importmode']        ='ms'
xp['importwidth']       =['8','8']

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

# CONSOLIDATING
xp['uvcs']              =True
xp['fitspw']            ='*:0~9;53~63'
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
xp['phase_center']      ='J2000 01h59m19.58 +19d00m27.10'

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
