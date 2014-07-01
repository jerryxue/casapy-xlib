execfile(xlib+'xinit.py')

xp['prefix']        =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']      =['../n5713/AG559_2']
xp['starttime']     ='1999/04/25/11:04:45.0'
xp['stoptime']      ='1999/04/25/12:47:45.0'
xp['importfield']   ='NGC5713,1442+101,1409+524'
xp['importspw']     ='0'


# TRACK INFORMATION
xp['source']        = 'NGC5713'
xp['spw_source']    ='0'

xp['fluxcal']           = '1409+524'
xp['fluxcal_uvrange']   =''
xp['phasecal']          ='1442+101'
xp['phasecal_uvrange']  =''

xp['flagspw']           ='*:0;59~62'
xp['flagselect']        =[    "antenna='VA02'",    
                    "antenna='VA12'",    
                    "antenna='VA06&VA17'" , 
                    "antenna='VA06&VA28'",
                    "antenna='VA07&VA21'"
                    ]

execfile(stinghi+'n5713_config.py')
xp['niter']        =0

# RUN SCRIPTS
execfile(xlib+'ximport.py')
xu.checkvrange(xp['prefix']+'.ms')
au.timeOnSource(xp['prefix']+'.ms')
execfile(xlib+'xcal.py')
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')




