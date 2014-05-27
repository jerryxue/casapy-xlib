execfile(xlib+'xinit.py')

# IMPORT
xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
xp['rawfiles']          ='/Volumes/Scratch/raw/21cm/n0772/AE175_sb1124713_1.55310.66684534722.ms'
xp['importmode']        ='ms'
xp['importtimebin']     ='30s'

# CALIBRATION
xp['source']            ='NGC 0772 - CIG80'
xp['spw_source']        ='0'

xp['fluxcal']           = 'J0542+4951'
xp['uvrange_fluxcal']   =''
xp['phasecal']          = 'J0204+1514'
xp['uvrange_phasecal']  ='<100klambda'

xp['flagselect']        =["antenna='ea12'",
                          "antenna='ea17'",
                          "antenna='ea20'",
                          "antenna='ea26'",
                          "antenna='ea08&ea27'",
                          "antenna='ea21&ea27'",
                          ]
extraflag=["antenna='ea05&ea15'",
 "antenna='ea15&ea28'",
 "antenna='ea07&ea08'",
 "antenna='ea08&ea28'",
 "antenna='ea18&ea28'",
 "antenna='ea05&ea27'",
 "antenna='ea21&ea28'",
 "antenna='ea07&ea13'",
 "antenna='ea13&ea28'",
 "antenna='ea08&ea18'",
 "antenna='ea05&ea21'",
 "antenna='ea18&ea22'",
 "antenna='ea07&ea28'",
 "antenna='ea08&ea22'",
 "antenna='ea07&ea22'",
 "antenna='ea21&ea22'",
 "antenna='ea27&ea28'",
 "antenna='ea07&ea15'",
 "antenna='ea08&ea15'",
 "antenna='ea05&ea08'",
 "antenna='ea18&ea21'",
 "antenna='ea08&ea21'",
 "antenna='ea13&ea18'",
 "antenna='ea13&ea21'",
 "antenna='ea08&ea13'",
 "antenna='ea15&ea27'",
 "antenna='ea18&ea27'",
 "antenna='ea15&ea21'",
 "antenna='ea05&ea18'",
 "antenna='ea07&ea18'",
 "antenna='ea22&ea27'",
 "antenna='ea15&ea18'",
 "antenna='ea07&ea27'",
 "antenna='ea07&ea21'"]
#xp['flagselect']=xp['flagselect']+[x+" field='J0542+4951'" for x in extraflag]
xp['flagselect']=xp['flagselect']+[x+"" for x in extraflag]
extraflag=["antenna='ea04&ea21'",
 "antenna='ea04&ea28'",
 "antenna='ea04&ea08'",
 "antenna='ea04&ea27'","antenna='ea02&ea21'",
 "antenna='ea09&ea11'", "antenna='ea25&ea27'", "antenna='ea14&ea27'",
 "antenna='ea22&ea23'",
 "antenna='ea09&ea23'",
 "antenna='ea11&ea23'",
 "antenna='ea09&ea22'",
 "antenna='ea02&ea27'",
 "antenna='ea11&ea27'",
 "antenna='ea02&ea11'",
 "antenna='ea13&ea27'","antenna='ea11&ea21'", "antenna='ea02&ea08'", "antenna='ea11&ea27'",
 "antenna='ea04&ea18'","antenna='ea22&ea27'", "antenna='ea08&ea21'",
 "antenna='ea22&ea28'","antenna='ea21&ea22'", "antenna='ea08&ea22'", "antenna='ea08&ea21'",
 "antenna='ea18&ea19'"]
xp['flagselect']=xp['flagselect']+[x+"" for x in extraflag]

xp['syscal']            =''

# CONSOLIDATING
xp['spwrgd']            ='spw'
xp['scalewt']           =True
xp['uvcs']              =True
xp['fitspw']            ='*:0~5;45~50'
xp['fitorder']          =1

# IMAGING
xp['cleanspec']         =True
xp['cleancont']         =True

xp['imsize']            =2**5*10
xp['cell']              ='8.0arcsec'

xp['cleanmode']         ='velocity'
xp['clean_start']       ='2033.0km/s'
xp['clean_width']       ='15.5km/s'
xp['clean_nchan']       =51
xp['phasecenter']      ='J2000 01h59m19.58 +19d00m27.10'
xp['niter']             =0

# RUN SCRIPTS:
#execfile(xlib+'ximport.py')
execfile(xlib+'xcal.py')
# execfile(xlib+'xcalplot.py')
#execfile(xlib+'xconsol.py')
#execfile(xlib+'xclean.py')
