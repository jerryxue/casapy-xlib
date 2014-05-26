execfile(xlib+'xinit.py')

# IMPORT

xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='/Volumes/Scratch/reduc/sting-hi/msc/n3486/raw/AS428_1'
xp['importscan']        ='1,12,13,15'
xp['importspw']         ='0,1,8,9'

# CALIBRATION
xp['source']            ='NGC3486'
xp['fluxcal']           ='0134+329'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='1117+146' 
xp['phasecal_uvrange']  =''
xp['spw_source']        ='2,3'
xp['spw_phasecal']      ='2,3'
xp['spw_fluxcal']       ='0,1'

xp['flagspw']           ='*:0;62'
xp['flagselect']        =["antenna='VA18'",
                          "uvrange='<1200lambda' field='0134+329'",
                          "timerange='23:40:00~23:45:00' field='0134+329'",
                          "timerange='23:55:00~23:58:20' antenna='VA10'",
                          "timerange='23:55:00~23:58:20' antenna='VA14&VA17'"]
xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~3;44~46'
xp['fitorder']          =1
xp['combinespws']       =False   # polarization type varies with row

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =256
xp['cell']              ='20.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='400km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =48
xp['phasecenter']       ='J2000 11h00m23.9 +28d58m29.0'
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
