execfile(xlib+'xinit.py')

xp['prefix']        ='n3198c02a'
xp['rawfiles']      =['../n3198/AT285_4']
xp['starttime']     ='2002/11/16/12:34:50.0'
xp['stoptime']      ='2002/11/16/12:57:10.0'



# TRACK INFORMATION
xp['source']         = 'NGC3198'
xp['spw_source']    ='0,1'

xp['fluxcal']         = '1331+305'
xp['fluxcal_uvrange']=''
xp['phasecal']         = '1006+349'
xp['phasecal_uvrange']='<30klambda'

spw_edge=6
# CALIBRATION & OPTIONS
xp['flagselect']     = [
            "timerange='2002/11/16/12:55:41~2002/11/16/12:56:00' field='1006+349'",
            "uvrange='<600lambda' field='1006+349'"
                ]

execfile(stinghi+'n3198_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
