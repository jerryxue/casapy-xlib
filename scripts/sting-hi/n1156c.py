
#
execfile(xlib+'xinit.py')


xp['prefix']   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
xp['rawfiles'] = ['../../../raw/21cm/n1156/AM418_1',
                  '../../../raw/21cm/n1156/AM418_2',
                  '../../../raw/21cm/n1156/AM418_3']
xp['starttime'] = '1993/08/09/10:59:45.0'
xp['stoptime'] ='1993/08/09/16:28:15.0'


xp['source']            = 'NGC1156'
xp['spw_source']        = '0,1'

xp['fluxcal']           = '0137+331'
xp['fluxcal_uvrange']   ='<40klambda'
xp['phasecal']          = '0318+164' 
xp['phasecal_uvrange']  ='<100klambda'
xp['passcal']           = '0137+331'
xp['passcal_uvrange']   ='<40klambda'

xp['flagspw']   ='*:0~3;123~126'
xp['flagselect'] = [    "mode='quack' quackinterval=3.0",
                "antenna='VA23' spw='1'",
                "antenna='VA09&VA11' ",
                "antenna='VA02&VA11' ",
                "antenna='VA11&VA21' ",
                "antenna='VA11&VA21' ",
                "antenna='VA10&VA11'",
                "antenna='VA11&VA27'",
                "antenna='VA11&VA14'",
                "antenna='VA11&VA22'"
                ]

xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='0:4~7;119~122,1:4~7;119~122'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True
xp['imsize']            =512+256
xp['cell']              ='2.0arcsec'

xp['cleanmode'] = 'velocity'
xp['clean_start']='300km/s'
xp['clean_nchan']=58
xp['clean_width']='2.6km/s'
xp['phasecenter']='J2000 02h59m42.2 +25d14m14.0'



line_vrange=[280,460]

# RUN SCRIPTS:
execfile(xlib+'ximport.py')
#execfile(xlib+'xcal.py')
#execfile(xlib+'xcalplot.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')

