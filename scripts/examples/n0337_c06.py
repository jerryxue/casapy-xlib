execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        ='n0337c06' 
xp['rawfiles']      ='/Volumes/Scratch/reduc/sting-hi/msc/n0337/raw/AM0873_3'
xp['importspw']     ='0,1'
xp['importscan']    ='6,8,10,12,14,16,18,30'

# CALIBRATION
xp['source']            ='NGC0337'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          ='0059+001'


xp['flagspw']           ='*:0~2;60~62'
xp['flagselect']        =["timerange='04:38:30~04:51:20.0'",
                          "antenna='VA11&VA21'",
                          "antenna='VA06&VA21'",
                          "antenna='VA06&VA11'",
                          "antenna='VA03&VA04'",
                          "timerange='2006/11/04/03:25:00~03:26:40' antenna='VA06&VA15'",
                          "timerange='2006/11/04/02:28:40~02:29:30' antenna='VA07&VA15'",
                          "timerange='2006/11/04/01:59:35~01:59:45'",
                          "timerange='2006/11/04/03:07:15~03:07:25'",
                          "timerange='2006/11/04/04:15:00~04:15:15'",
                          "antenna='VA22'",
                          "timerange='2006/11/04/10:03:45~10:04:15'",
                          "timerange='2006/11/04/10:04:54~10:05:06'",
                          "timerange='2006/11/04/10:06:04~10:06:16'",
                          "timerange='03:00:00~11:00:00.0' antenna='VA03'",
                          "antenna='VA11'",
                          "antenna='VA06'",
                          "antenna='VA05'",
                          "timerange='2006/11/04/04:33:06~04:34:05'"]

# CONSOLIDATING
xp['imcs']              =True
xp['fitchans']          ='0~4;69~77'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+256+128
xp['cell']              ='4.0arcsec'

xp['imstat_box_spec']   ='93,206,234,350'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='1450.00km/s'
xp['clean_width']       ='5.2km/s'
xp['clean_nchan']       =78
xp['phase_center']      ='J2000 00h59m50.1 -07d34m41.0'

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
xu.checkstatwt(xp['prefix']+'.src.ms',fitspw=xp['fitspw'])
execfile(xlib+'xclean.py')
