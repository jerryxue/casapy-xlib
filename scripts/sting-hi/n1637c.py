execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='../n1637/AR351_A960213.xp1'

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

execfile(stinghi+'n1637_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xcalplot.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
