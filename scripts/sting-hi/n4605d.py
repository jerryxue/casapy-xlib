execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4605/AC168_1']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='7,9,10,11,12,13,20'
xp['importspw']     ='1,3'

# TRACK INFORMATION
xp['source']         = 'NGC4254'
xp['fluxcal']         = '1331+305'
xp['phasecal']        = '1221+282'

xp['spw_source']     = '0'
xp['flagspw']         = '0:0~3;58~63'
xp['flagselect']    =[    "timerange='10:29:30~10:30:00'"]

execfile(stinghi+'n1569_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')