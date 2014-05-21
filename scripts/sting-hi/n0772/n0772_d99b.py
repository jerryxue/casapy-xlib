execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n0772d99b' 
xp['rawfiles']          =['/Volumes/Scratch/reduc/sting-hi/msc/n0772/raw/AG564_4',
                          '/Volumes/Scratch/reduc/sting-hi/msc/n0772/raw/AG564_5']
xp['importspw']         ='1'

# CALIBRATION
xp['source']            ='ARP78'
xp['spw_source']        ='0'

xp['fluxcal']           = '0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          = '0204+152'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagspw']           ='0:0~2;124~126'
xp['flagselect']        = [ "timerange='16:06:40~17:29:15'", 
                            "timerange='19:57:25~19:57:35'", 
                            "timerange='17:38:00~17:40:00'",
                            "field='0137+331' uvrange='<800lambda'",
                            "field='0204+152' uvrange='<800lambda'",
                            "timerange='19:51:20~19:54:00' antenna='VA05'",
                            "antenna='VA14&VA24'",
                            "antenna='VA14&VA28'",
                            "antenna='VA14&VA12'",
                            "antenna='VA19&VA26'"]

# CONSOLIDATING
xp['spwrgd']            =''
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='0:6~31;95~109'
xp['fitorder']          =1
xp['spwrgd']            ='spw'
xp['scalewt']           =True
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
# evla tracks have nchan=39 to avoid spws with different corrs merging into one.
xp['clean_nchan']       =40
xp['phasecenter']      ='J2000 01h59m19.58 +19d00m27.10'
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

