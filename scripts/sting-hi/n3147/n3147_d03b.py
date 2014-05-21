execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            ='n3147d03b' 
xp['rawfiles']          =['/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AS750_7',\
                          '/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AS750_8',\
                          '/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AS750_9',\
                          '/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AS750_10']
xp['starttime']         ="2003/03/19/02:41:15.0"
xp['stoptime']          ="2003/03/19/05:25:15"

# CALIBRATION
xp['source']            ='NGC3147'
xp['fluxcal']           ='1331+305'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='0841+708' 
xp['phasecal_uvrange']  ='<20klambda'
xp['spw_source']        ='0,1'

xp['flagselect']        =["mode='quack' quackinterval=8.0",
                          "field='NGC3147' timerange='02:45:00~02:50:00'",
                          "field='NGC3147' timerange='04:39:40~04:39:50'",
                          "timerange='05:16:50~05:17:00'", "antenna='VA24'",
                          "timerange='05:21:12~05:21:18' field='1331+305' antenna='VA01'"]

execfile(stinghi+'n3147_config.py')
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
