execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        ='n2782c'
xp['rawfiles']      ='../n2782/AS453_4'


# TRACK INFORMATION
xp['source']        ='NGC2782'

xp['fluxcal']         ='1328+307'
xp['fluxcal_uvrange']    =''
xp['phasecal']     = '0859+470'
xp['phasecal_uvrange']='<15klambda'

xp['spw_source']     = '0'
xxp['flagspw']        ='*:0~3;58~62'

# CALIBRATION & OPTIONS
xp['flagselect']     =     [
                    "timerange='01:09:00~01:09:20'",
                    "timerange='02:39:10~02:40:00'",
                    "timerange='02:52:00~02:54:10' antenna='VA13&VA17'",
                    "timerange='03:10:00~03:15:00' antenna='VA13&VA17;VA17&VA19'",
                    "timerange='03:20:50~03:24:10'",
                    "timerange='03:40:00~03:43:20'",
                    "timerange='03:57:30~04:00:50'",
                    "timerange='04:09:10~04:10:00'",
                    "timerange='04:35:50~04:40:00'",
                    "timerange='02:51:40~02:54:10'",
                    "timerange='03:10:50~03:13:20'",
                    "timerange='04:25:50~04:28:00'",
                    "timerange='04:54:10~04:55:00'",
                    "antenna='VA11&VA20' timerange='03:00:00~03:06:40'"
                    ]        
xp['niter']            =0


# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')







