execfile(xlib+'xinit.py')

# IMPROT INFO
xp['prefix']            ='n0772bc13a_cont' 
xp['rawfiles']          ='/Volumes/Scratch/reduc/evla/n0772/13B-363.sb24382374.eb25239554.56540.51835789352.ms'
xp['importspw']         ='0,1,3,5,8,9,10,11,13,15'
xp['importspw']         ='0'
xp['importscan']        ='2~15'
xp['importcorr']        ='rr, ll'
xp['importmode']        ='ms'
#
# CALIBRATION INFO
xp['source']            ='NGC0772'
xp['spw_source']        ='0'

xp['fluxcal']           ='0137+331=3C48'
xp['uvrange_fluxcal']   ='<40klambda'
xp['phasecal']          ='J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagspw']           ="0:0~16,0:19~21,0:26,0:36,0:46,0:49~51"
xp['flagselect']        =["spw='0:0~27'",
                          "spw='0:36'",
                          "spw='0:46'"]
# 

# IMAGING INFO
xp['cleanspec']         =False
xp['cleancont']         =True
xp['imsize']            =512
xp['cell']              ='6.0arcsec'
xp['phasecenter']      ='J2000 01h59m19.58 +19d00m27.10'
xp['spwrgd']            =False

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

