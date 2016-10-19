def config(xp):
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
    return xp

def b13():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'13B-363.sb24606123.eb28499568.56605.30007186343.ms'
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

    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

def c96():
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'AR351_A960213.xp1'

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

    xp=config(xp)
    xp['niter']             =0

    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    #execfile(xlib+'xcalplot.py')
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)

def d03():
    
    xp=xu.init()

    # IMPORT
    xp['prefix']            ='../'+inspect.stack()[0][3]+'/'+inspect.stack()[0][3]
    xp['rawfiles']          =st['hi_raw']+'STUDEN_1'
    xp['importscan']        ='2~9'
    #xp['importspw']         ='0,1,8,9'

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
    xp=config(xp)
    xp['niter']             =0


    # RUN SCRIPTS:
    xp=xu.ximport(xp)
    xu.checkvrange(xp['prefix']+'.ms')
    #au.timeOnSource(xp['prefix']+'.ms')
    xp=xu.xcal(xp)
    xp=xu.xconsol(xp)
    xp=xu.xclean(xp)


def comb():
    #588->838
    #execfile(stinghi+'n1637b.py')
    #execfile(stinghi+'n1637c.py')
    #execfile(stinghi+'n1637d.py')

    xp=xu.init()

    # CONSOLIDATING
    xp['prefix']            ='../n1637/comb/'+os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
    xp['prefix_comb']       =['../n1637/b13/b13',
                              '../n1637/c96/c96',
                              '../n1637/d03/d03']

    xp=config(xp)
    
    xp['cleanspec']         =True
    xp['cleancont']         =True
    
    xp['mosweight']         =True
    xp['scalewt']           =True
    
    xp['imsize']            =2**8*5
    xp['cell']              ='3arcsec'

    xp['clean_mask']        =0.1
    xp['clean_mask_cont']   =0.01
    xp['minpb']             =0.01

    xp['multiscale']        =[int(x*(15/3.0)) for x in [0.,2.]]
    xp['smallscalebias']    =0.9
    
    xp['clean_gain']        =0.3
    xp['cyclefactor']       =5.0
    xp['negcomponent']      =0
    xp['usescratch']        =True

    xp['fitspw']            ='*:0~2;41~43'
    
    # RUN SCRIPTS:
    #xp=xu.xconsol(xp)
    
    xp['ctag']              ='_ro'
    xp['cleanweight']       ='briggs'
    xp=xu.xclean(xp)

if  __name__=="__main__":

    #b13()
    #c96()
    #d03()
    comb()