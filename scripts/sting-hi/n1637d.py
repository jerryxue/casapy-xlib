execfile(xlib+'xinit.py')

# IMPORT

xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles']          ='/Volumes/Scratch/reduc/sting-hi/msc/n1637/raw/STUDEN_1'
xp['importscan']        ='2~9'
xp['importspw']         ='0,1,8,9'

# CALIBRATION
xp['source']            ='NGC1637'
xp['fluxcal']           ='0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='0423-013' 
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'
xp['spw_phasecal']      ='0'
xp['spw_fluxcal']       ='0'

xp['flagspw']           ='*:0~1;60~62'
"""
xp['flagselect']        =["timerange='2003/04/11/22:30:22~22:30:29'",
                          "timerange='2003/04/11/20:56:00~20:56:40'",
                          "timerange='2003/04/11/21:15:45~21:16:10'",
                          "antenna='VA25'", "'antenna='VA10'",
                          "antenna='VA03&VA27'","antenna='VA08&VA15'","antenna='VA12&VA21'",
                          "antenna='VA03&VA17'","antenna='VA21&VA24'",
                          "uvrange='<1200lambda' field='0137+331'",
                          "uvrange='<900lambda' field='0423-013'",
                          "uvrange='<1200lambda' field='NGC1637' timerange='21:23:20~21:56:40'"]
xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2
"""
# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~2;41~43'
xp['fitorder']          =1
xp['combinespws']       =True   # polarization type varies with row

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =512+256+128
xp['cell']              ='4.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='485km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =44
xp['phasecenter']       ='J2000 04h41m28.2 -02d51m29.0'
xp['niter']             =0

line_vrange=[588,838]

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
