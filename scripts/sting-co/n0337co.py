track_list=['D1','D2','D3','D4','C1','C2','C3','C4','C5','C6']
mirfile_list=[  
                'ngc337_D1_08jul21.co.cal',
                'ngc337_D2_08jul30.co.cal',
                'ngc337_D3_08jul31.co.cal',
                'ngc337_D4_08aug08.co.cal', 
                'ngc337_C1_08oct24.co.cal',
                'ngc337_C2_08oct26.co.cal',
                'ngc337_C3_09may10.co.cal',
                'ngc337_C4_09may12.co.cal',
                'ngc337_C5_09may18.co.cal',
                'ngc337_C6_09may23.co.cal'
                ]
repo='../../../../raw/co10/n0337/vis/'
telescopes=['CARMA']*len(track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=repo+mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1510km/s'
    xp['clean_nchan']       =(1780-1510)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')


execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n0337co'
xp['prefix_comb']       =track_list     

xp['spwrgd']            ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='1510km/s'
xp['clean_nchan']       =(1780-1510)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 0h59m50.1 -07d34m41.00'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        ='circle[[160pix,160pix],60pix]'

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')
