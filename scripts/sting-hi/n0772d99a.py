execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n0772/AG564_3'
xp['importspw']         ='1'

# CALIBRATION
xp['source']            ='ARP78'
xp['spw_source']        ='0'

xp['fluxcal']           = '0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = '0204+152'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagspw']           ='0:0~4;122~126'
xp['flagselect']        = [ "antenna='VA12&VA17' timerange='17:44:35~17:44:55'",
                            "timerange='01:00:00~17:44:10'", "antenna='VA05'",
                            "antenna='VA04&VA27'","antenna='VA03&VA27'",
                            "antenna='VA06&VA25'",
                            "antenna='VA12'","antenna='VA02&VA16'",
                            "antenna='VA06&VA24'","antenna='VA11&VA24'",
                            "field='0137+331' uvrange='<1klambda'",
                            "field='0204+152' uvrange='<1klambda'",
                            "antenna='VA21'",
                            "antenna='VA14&VA24'"]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~35;92~126'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =256
xp['cell']              ='12.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='1780km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =127
xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

