# ---------- IMPORT DATA

track_list=['D1','D2','C1','C2','C3','C4','E2','E3','E4']

mirfile_list=[  '../../../../raw/co10/n4254/vis/ngc4254_D1_08jun08.13co.cal',
				'../../../../raw/co10/n4254/vis/ngc4254_D2_08jun09.13co.cal',
			    '../../../../raw/co10/n4254/vis/n4254_C1_08OCT20.13co.cal',
				'../../../../raw/co10/n4254/vis/n4254_C2_08OCT24.13co.cal',
				'../../../../raw/co10/n4254/vis/n4254_C3_08OCT25.13co.cal',
				'../../../../raw/co10/n4254/vis/n4254_C4_08OCT28.13co.cal',
				'../../../../raw/co10/n4254/vis/ngc4254_E2_09jul02.13co.cal',
				'../../../../raw/co10/n4254/vis/ngc4254_E3_09jul05.13co.cal',
				'../../../../raw/co10/n4254/vis/ngc4254_E4_09jul19.13co.cal'	]

# track_list=['C1','C2','C3','C4','E2','E3','E4']
# mirfile_list=[ 	'../../../../raw/co10/n4254/vis/n4254_C1_08OCT20.13co.cal',
# 				'../../../../raw/co10/n4254/vis/n4254_C2_08OCT24.13co.cal',
# 				'../../../../raw/co10/n4254/vis/n4254_C3_08OCT25.13co.cal',
# 				'../../../../raw/co10/n4254/vis/n4254_C4_08OCT28.13co.cal',
# 				'../../../../raw/co10/n4254/vis/ngc4254_E2_09jul02.13co.cal',
# 				'../../../../raw/co10/n4254/vis/ngc4254_E3_09jul05.13co.cal',
# 				'../../../../raw/co10/n4254/vis/ngc4254_E4_09jul19.13co.cal'	]

telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
	
	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 	='velocity'
	xp['clean_start']	   	='2265km/s'
	xp['clean_nchan']	   	=(2525-2265)/10+1
	xp['clean_width']	   	='10km/s'
	xp['restfreq']		  	='110.201353GHz'
	xp['outframe']		  	='LSRK'

# 	xp=xu.ximport(xp)
# 	xp=xu.xconsol(xp)
 	
# ---------- IMAGE DATA 

#   vrange tracks 
track_list=['C1','C2','C3','C4','E2','E3','E4']

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='../n4254/n4254co13'
xp['prefix_comb']       =track_list     

xp['spwrgd']            ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']		 	='velocity'
xp['clean_start']	   	='2265km/s'
xp['clean_nchan']	   	=(2525-2265)/10+1
xp['clean_width']	   	='10km/s'
xp['restfreq']		  	='110.201353GHz'
xp['outframe']		  	='LSRK'
    
xp['phasecenter']       ='J2000 12h18m49.56 +14d24m58.50'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =320
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.025
xp['clean_mask']        =0.20
xp['multiscale']        =[int(x*(2.0/1.0)) for x in [0.,1.,5.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

#xu.xconsol(xp)
#xu.carmapb(xp['prefix']+'.src.ms',effdish=True)

xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xu.xclean(xp)
# xu.mossen(vis=xp['prefix']+'.src.ms',
#           log=xp['prefix']+xp['ctag']+'.line.sens.log',
#           nchan=xp['clean_nchan'],ftmachine='mosaic',
#           mosweight=True,imsize=xp['imsize'],
#           weight=xp['cleanweight'])

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
#xu.xclean(xp)
# xu.mossen(vis=xp['prefix']+'.src.ms',
#           log=xp['prefix']+xp['ctag']+'.line.sens.log',
#           nchan=xp['clean_nchan'],ftmachine='mosaic',
#           mosweight=True,imsize=xp['imsize'],
#           weight=xp['cleanweight'])

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
#xu.xclean(xp)
#os.system('cp -rf '+xp['prefix']+'_na.line.sens.log '+xp['prefix']+'_st.line.sens.log')

# xp['threshold_spec']	='19.1726874267mJy'
# xp['cresume']			=False
# xp['niter']=200
# 
# # RUN SCRIPTS
# #xp=xu.xconsol(xp)
# for	i in range(0,10):
# 	xp=xu.xclean(xp)
# 	xu.cleanup('n4254co13.line',tag='.n'+str(i))
# 	xp['cresume']		=True
	



