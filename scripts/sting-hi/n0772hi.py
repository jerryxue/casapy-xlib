#2172->2716
execfile(stinghi+'n0772b13a.py')
execfile(stinghi+'n0772b13b.py')
execfile(stinghi+'n0772b13c.py')
execfile(stinghi+'n0772bc13a.py')
execfile(stinghi+'n0772bc13b.py')
#execfile(stinghi+'n0772bc00.py') # short track / low velocity resolution
execfile(stinghi+'n0772d99a.py')
execfile(stinghi+'n0772d99b.py')

execfile(xlib+'xinit.py')


# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =['n0772d99a',
                          'n0772d99b',
                          'n0772bc13a',
                          'n0772bc13b',
                          'n0772b13a',
                          'n0772b13b',
                          'n0772b13c']

execfile(stinghi+'n0772_config.py')
xp['scalewt']           =True
xp['fitspw']            ='*:0~5;75~79'

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**7*10
xp['cell']              ='2.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2031.2km/s'
xp['clean_width']       ='10.4km/s'
xp['clean_nchan']       =80

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')



# # CONSOLIDATING
# xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
# xp['prefix_comb']       =['n0772d99a',
#                           'n0772d99b',
# #                          'n0772bc00',
#                           'n0772bc13a',
#                           'n0772bc13b',
#                           'n0772b13a',
#                           'n0772b13b',
#                           'n0772b13c']
# xp['scalewt']           =True
# xp['spwrgd']            ='spw'
# xp['uvcs']              =True
# xp['fitspw']            ='0:2~5;37~40,1:4~9;75~80'
# 
# # IMAGING
# xp['cleanspec']         =True
# xp['cleancont']         =True
# 
# xp['imsize']            =2**7*10
# xp['cell']              ='2.0arcsec'
# 
# xp['imsize']            =2**5*10
# xp['cell']              ='4.0arcsec'
# 
# xp['cleanmode']         ='velocity'
# xp['clean_start']       ='2036.4km/s'
# xp['clean_width']       ='20.8km/s'
# xp['clean_nchan']       =39
# xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
# 
# xp['multiscale']        =[0,4,12]
# xp['clean_gain']        =0.3
# xp['cyclefactor']       =5.0
# xp['negcomponent']      =0
# xp['usescratch']        =True
# 
# # RUN SCRIPTS:
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')