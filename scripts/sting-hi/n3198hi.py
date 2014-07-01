#[470,830]
execfile(xlib+'xinit.py')
xp['prefix_comb']       =[  'n3198d04',
                            'n3198d03b',
                            'n3198d03a',
                            'n3198c03',
                            'n3198c02c',
                            'n3198c02b',
                            'n3198c02a',
                            'n3198b05']
#for one in xp['prefix_comb']:
#    execfile(stinghi+one+'.py')                            

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =[  'n3198d04',
                            'n3198d03b',
                            'n3198d03a',
                            'n3198c03',
                            'n3198c02c',
                            'n3198c02b',
                            'n3198c02a',
                            'n3198b05']

execfile(stinghi+'n3198_config.py')
xp['fitchans']           ='0~13,85~101'
xp['clean_start']        ='406.8km/s'
xp['clean_width']        ='5.2km/s'
xp['clean_nchan']        =102
xp['imsize']            =2**6*10
xp['cell']              ='2.0arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True

# RUN SCRIPTS:
#execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

