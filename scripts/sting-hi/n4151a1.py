execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n4151/AB605B_6']
xp['starttime']     =''
xp['stoptime']      =''
xp['importscan']    ='19~32'
xp['importspw']     ='6,7,8'


# TRACK INFORMATION
xp['source']         = 'NGC4151'
xp['spw_source']    ='0'

xp['fluxcal']         = '1328+307'
xp['fluxcal_uvrange']=''
xp['phasecal']         = '1225+368' 
xp['phasecal_uvrange']=''

xp['spw_fluxcal']     ='2'
xp['spw_phasecal']    ='1'

xp['flagspw']       ='*:0;59~62'
xp['flagselect']    =["field='1225+368' antenna='VA09&VA25' spw='1:25'",
                      "field='1225+368' antenna='VA09&VA13' spw='1:25'",
                      "field='1225+368' antenna='VA25&VA26' spw='1:25'",
                      "field='1225+368' antenna='VA13&VA25' spw='1:25'",
                      "field='1225+368' antenna='VA06&VA26' spw='1:25'",
                      "field='1225+368' antenna='VA06&VA23' spw='1:25'",
                      "field='1225+368' antenna='VA06&VA09' spw='1:25'",
                      "field='1225+368' antenna='VA06&VA25' spw='1:25'"]


execfile(stinghi+'n4151_config.py')
xp['niter']        =0

# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

