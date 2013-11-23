execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n0772d99a' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/sting-hi/msc/n0772/raw/AG564_3'
xp['importspw']         ='1'

# CALIBRATION
xp['source']            ='ARP78'
xp['spw_source']        ='0'

xp['fluxcal']           = '0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = '0204+152'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagspw']           ='0:0~2;124~126'
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
xp['uvcs']              =True
xp['fitspw']            ='*:0~5;33~38'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =256
xp['cell']              ='12.0arcsec'

xp['cleanmode']        ='velocity'
xp['clean_start']       ='2050.0km/s'
xp['clean_width']       ='20.8km/s'
xp['clean_nchan']       =39
xp['phasecenter']      ='J2000 01h59m19.58 +19d00m27.10'

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

