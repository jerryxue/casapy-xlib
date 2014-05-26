execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          =['/Volumes/Scratch/reduc/sting-hi/msc/n3147/raw/AV170_1']
xp['starttime']         ="1989/12/15/05:48:45"
xp['stoptime']          ="1989/12/15/10:00:00"

# CALIBRATION
xp['source']            ='N3147'
xp['fluxcal']           ='0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          ='0949+662'
xp['phasecal_uvrange']  ='<15klambda'
xp['spw_source']        ='0'

xp['flagselect']        =["timerange='06:05:50~06:06:40'"]

execfile(stinghi+'n3147_config.py')
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
