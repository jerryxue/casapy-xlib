execfile(xlib+'xinit.py')

# IMPORT

xp['prefix']            ='n1637c96' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/sting-hi/msc/n1637/raw/AR351_A960213.xp1'

# CALIBRATION
xp['source']            ='NGC1637'
xp['fluxcal']           ='0134+329'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='0420-014' 
xp['phasecal_uvrange']  =''
xp['spw_source']        ='0'
xp['spw_phasecal']      ='0'
xp['spw_fluxcal']       ='0'

xp['flagspw']           ='*:0~1;60~62'
xp['flagselect']        =["timerange='1996/02/14/00:26:25~00:26:35'", 
                          "timerange='1996/02/14/00:28:28~00:28:32'",
                          "timerange='1996/02/14/03:30:25~03:30:35'",
                          "timerange='1996/02/13/26:24:25~26:24:45'",
                          "timerange='1996/02/13/27:25:25~27:25:35'"]
xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2

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
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
