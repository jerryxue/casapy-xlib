execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4605/AC168_1','../n4605/AC168_2','../n4605/AC168_3']
xp['starttime']     =''
xp['stoptime']      =''
xp['importfield']   ='N4605,1203+645,3C286'
xp['importscan']    ='32,34,35,36,37,38,57'
xp['importspw']     ='3,8'

# TRACK INFORMATION
xp['source']         = 'N4605'
xp['fluxcal']        = '3C286'
xp['phasecal']       = '1203+645'

xp['spw_source']     = '1'
xp['spw_fluxcal']    = '1'
xp['spw_phasecal']   = '0'

xp['flagspw']        ='' #'0:0~3;58~63'
xp['flagselect']    =[]

execfile(stinghi+'n4605_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')