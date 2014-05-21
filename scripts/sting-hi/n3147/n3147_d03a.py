execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n3147d03a' 
xp['rawfiles']          =['/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AB1069_4',\
                          '/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AB1069_5',\
                          '/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AB1069_6']
xp['starttime']         ="1989/12/15/05:48:45"
xp['stoptime']          ="2003/03/04/06:09:25"

# CALIBRATION
xp['source']            ='NGC3147'
xp['fluxcal']           ='0134+329'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='0836+710'
xp['phasecal_uvrange']  ='<20klambda'
xp['spw_source']        ='0'

xp['flagselect']        =["timerange='03:43:40~03:44:00'",
                          "timerange='01:58:55~01:59:15'",
                          "mode='quack' quackinterval='5.0'",
                          "antenna='VA17' timerange='02:07:40~02:07:50'"]

execfile(stinghi+'n3147_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
