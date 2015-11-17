def config():
    # CONSOLIDATING
    xp['spwrgd']            ='spw'
    xp['scalewt']           =True
    xp['uvcs']              =True
    xp['fitspw']            ='*:0~2;41~43'
    xp['fitorder']          =1

    # IMAGING
    xp['cleanspec']         =True
    xp['cleancont']         =True

    xp['imsize']            =512+256
    xp['cell']              ='4.0arcsec'

    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='485km/s'
    xp['clean_width']       ='10.4km/s'
    xp['clean_nchan']       =44
    xp['phasecenter']       ='J2000 04h41m28.2 -02d51m29.0'

def b():
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='../n1637/13B-363.sb24606123.eb28499568.56605.30007186343.ms'
    xp['importspw']         ='2,12'
    xp['importscan']        ='2~15'
    xp['importmode']        ='ms'
    xp['importchanbin']     =6


    # CALIBRATION
    xp['source']            ='NGC1637'
    xp['spw_source']        ='0,1'

    xp['fluxcal']           ='0137+331=3C48'
    xp['uvrange_fluxcal']   =''
    xp['phasecal']          ='J0423-0120'
    xp['uvrange_phasecal']  =''

    # rfi at the spw center
    xp['flagselect']        =["mode='tfcrop' freqcutoff=3.0 flagdimension='freq'"]                        
    xp['flagtsys_range']    =[5.0,200.0]

    execfile(stinghi+'n1637_config.py')
    xp['niter']             =0

    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

def c():
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['rawfiles']          ='../n1637/AR351_A960213.xp1'

    # CALIBRATION
    xp['source']            ='NGC1637'
    xp['fluxcal']           ='0134+329'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          ='0420-014' 
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'
    xp['spw_phasecal']      ='0'
    xp['spw_fluxcal']       ='0'

    xp['flagspw']           ='*:0~1;60~62'
    xp['flagselect']        =["timerange='1996/02/14/00:26:25~00:26:35'", 
                              "timerange='1996/02/14/00:28:28~00:28:32'",
                              "timerange='1996/02/14/03:30:25~03:30:35'",
                              "timerange='1996/02/13/26:24:25~26:24:45'",
                              "timerange='1996/02/13/27:25:25~27:25:35'"]
    xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2

    execfile(stinghi+'n1637_config.py')
    xp['niter']             =0

    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    execfile(xlib+'xcalplot.py')
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

def d():
    xp=xu.init()

    # IMPORT
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
    xp['rawfiles']          ='../n1637/raw/STUDEN_1'
    xp['importscan']        ='2~9'
    xp['importspw']         ='0,1,8,9'

    # CALIBRATION
    xp['source']            ='NGC1637'
    xp['fluxcal']           ='0137+331'
    xp['fluxcal_uvrange']   ='<40klambda'
    xp['phasecal']          ='0423-013' 
    xp['phasecal_uvrange']  =''
    xp['spw_source']        ='0'
    xp['spw_phasecal']      ='0'
    xp['spw_fluxcal']       ='0'

    xp['flagspw']           ='*:0~1;60~62'
    """
    xp['flagselect']        =["timerange='2003/04/11/22:30:22~22:30:29'",
                              "timerange='2003/04/11/20:56:00~20:56:40'",
                              "timerange='2003/04/11/21:15:45~21:16:10'",
                              "antenna='VA25'", "'antenna='VA10'",
                              "antenna='VA03&VA27'","antenna='VA08&VA15'","antenna='VA12&VA21'",
                              "antenna='VA03&VA17'","antenna='VA21&VA24'",
                              "uvrange='<1200lambda' field='0137+331'",
                              "uvrange='<900lambda' field='0423-013'",
                              "uvrange='<1200lambda' field='NGC1637' timerange='21:23:20~21:56:40'"]
    xp['flagselect_default']=[]     # mode='shadow' doesn't work with B1960 in v4.2
    """
    execfile(stinghi+'n1637_config.py')
    xp['niter']             =0


    # RUN SCRIPTS:
    #xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def hi():
    #588->838
    #execfile(stinghi+'n1637b.py')
    #execfile(stinghi+'n1637c.py')
    #execfile(stinghi+'n1637d.py')

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            =os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['n1637b',
                              'n1637c',
                              'n1637d']

    execfile(stinghi+'n1637_config.py')

    #xp['outertaper']        =['10arcsec']
    xp['multiscale']        =[0,4,12]
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True

    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

if  __name__=="__main__":
    #n0772d99a()
    #n0772d99b()
    #n0772bc13a()
    #n0772bc13b()
    #n0772b13a()
    #n0772b13b()
    #n0772b13c()
    n0772hi()      