#[470,830]
execfile(stinghi+'n1156b.py')
execfile(stinghi+'n1156c.py')
execfile(stinghi+'n1156d.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['prefix_comb']       =[    'n3198d04a',
                            'n3198d03b',
                            'n3198d03a',
                            'n3198c02d',
                            'n3198c02c',
                            'n3198c02b',
                            'n3198c02a',
                            'n3198b05']

execfile(stinghi+'n3198_config')

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['usescratch']        =True
xp['niter']             =0

# RUN SCRIPTS:
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')

