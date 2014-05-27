execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      ='../../../raw/21cm/n0337/AM0873_3'
xp['importspw']     ='0,1'
xp['importscan']    ='6,8,10,12,14,16,18,30'

# CALIBRATION
xp['source']            ='NGC0337'
xp['spw_source']        ='0,1'

xp['fluxcal']           ='0137+331'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          ='0059+001'


xp['flagspw']           ="0:0~4;60~62,1:0~2;58~62"
xp['flagselect']        =["timerange='04:45:50~04:48:20'",
                          "timerange='04:43:20~04:44:50'",
                          "antenna='VA11&VA21'",
                          "antenna='VA06&VA21'",
                          "antenna='VA06&VA11'",
                          "antenna='VA03&VA04'",
                          "timerange='2006/11/04/03:25:00~03:26:40' antenna='VA06&VA15'",
                          "timerange='2006/11/04/02:28:40~02:29:30' antenna='VA07&VA15'",
                          "timerange='2006/11/04/01:59:35~01:59:45'",
                          "timerange='2006/11/04/03:07:15~03:07:25'",
                          "timerange='2006/11/04/04:15:00~04:15:15'",
                          "timerange='2006/11/04/10:03:45~10:04:15'",
                          "timerange='2006/11/04/10:04:54~10:05:06'",
                          "timerange='2006/11/04/10:06:04~10:06:16'",
                          "timerange='2006/11/04/04:33:06~04:34:05'"]

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['imcs']              =True
xp['fitchans']          ='0~22;84~106'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True

xp['imsize']            =320
xp['cell']              ='8.0arcsec'

xp['imstat_box_spec']   ='42,103,117,175'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='1360.00km/s'
xp['clean_width']       ='5.2km/s'
xp['clean_nchan']       =107
xp['phasecenter']       ='J2000 00h59m50.1 -07d34m41.0'
xp['niter']             =0
xp['usescratch']        =True

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
