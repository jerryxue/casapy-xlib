execfile(xlib+'xinit.py')

xp['prefix']        ='n2782ab'
xp['rawfiles']      ='../n2782/AS453_3'

# TRACK INFORMATION
xp['source']         ='NGC2782'

xp['fluxcal']             = '0134+329'
xp['fluxcal_uvrange']    ='<40klambda'
xp['phasecal']            ='0917+449'
xp['phasecal_uvrange']    ='<20klambda'

xp['spw_source']        ='0'
xp['flagsp']            ='*:0;60~62'

xp['flagselect']         =     [
                    "timerange='06:10:40~06:10:50' field='0134+329'",
                    "timerange='06:12:20~06:13:00' field='0134+329'",
                    "antenna='VA01&VA12'"
                ]        

execfile(stinghi+'n2782_config.py')                            
xp['niter']            =0

#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



