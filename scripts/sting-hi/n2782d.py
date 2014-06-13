execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']        ='n2782d'
xp['rawfiles']      =['../n2782/AS389_1',
                      '../n2782/AS389_2']
xp['starttime']     ='1989/12/10/06:49:15.0'
xp['stoptime']      ='1989/12/10/16:13:15.0'
xp['importspw']     ='0'


# TRACK INFORMATION
xp['source']        ='NGC2782'

xp['fluxcal']         ='1328+307'
xp['fluxcal_uvrange']    =''
xp['phasecal']     = '0859+470'
xp['phasecal_uvrange']='<15klambda'

xp['spw_source']     = '0'
xp['flagspw']        ='*:0~3;58~62'

xp['flagselect']     =[
                    "timerange='10:50:00~10:52:20' antenna='VA09&VA12'",
                    "timerange='13:15:00~13:17:00' antenna='VA09&VA12'",
                    "timerange='09:23:20~09:26:40'",
                    "timerange='09:33:20~09:36:40'",
                    "timerange='09:51:40~09:53:20'",
                    "timerange='10:00:00~10:01:40'",
                    "timerange='10:19:10~10:20:00'",
                    "timerange='10:38:20~10:39:10'",
                    "timerange='12:56:40~12:57:30'",
                    "timerange='14:40:00~14:41:40'",
                    "timerange='14:48:20~14:50:00'",
                    "timerange='15:06:40~15:10:00'",
                    "timerange='13:17:30~13:19:10'",
                    "timerange='15:13:20~15:20:00'",
                    "timerange='11:00:40~11:01:20'",
                    "timerange='10:51:10~10:52:00'",
                    "timerange='15:25:00~15:50:00' field='NGC2782'",
                    "uvrange='<500lambda' field='0859+470'",
                    "timerange='10:10:00~10:11:40'",
                    "timerange='11:14:10~11:15:50'",
                    "timerange='11:21:40~11:23:20'",
                    "timerange='15:20:00~15:21:40'"
                ]


# RUN SCRIPTS
#execfile(xlib+'ximport.py')
#xu.checkvrange(xp['prefix']+'.ms')
#au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

