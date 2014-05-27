# PIPELINE DEFAULT PARAMETER SETTING
# xp is the dict containing pipeline setup parameters

xp={
# FILES NAME
'rawfiles':None,        # name(s) of the data files to be imported
'msfile':'',
'prepfile':'',
'srcfile':'',
'srcfile_comb':'',

# IMPORT DATA
'prefix':'test',
'importspw':'',
'importmirspw':'',
'importscan':'',  
'importcorr':'',
'importtimerange':'',
'importmode':'vla',   # import data mode
'importchanbin':1,
'importfield':'',
'importband':'',
'importmirarray':'CARMA',
'importmirnocal':False,
'importtimebin':'0s',
'importmirline':'',

'starttime':'',       # import starttime
'stoptime':'',        # import stoptime

# OBS INFO
'source':'',
'fluxcal':'',
'passcal':'',
'phasecal':'',
'spw_source':'',
'spw_fluxcal':'',
'spw_passcal':'',
'spw_phasecal':'',
'uvrange_source':'',
'uvrange_fluxcal':'',
'uvrange_passcal':'',
'uvrange_phasecal':'',

# FLAGGING
'flagselect':[],
'flagselect_cal':[],
'flagspw':'',
'flagreset':True,
'flagtest':False,

# by default, importvla & importevla will flag shadowed antennas. 
# no extra "mode='shadow'" is needed. 
# "mode='shadow'" will crash flagcmd if source is in B1950...
'flagselect_default':[], 
'dirtol':'',
'freqtol':'',

# BASELINE
'bcant':'',
'bctype':'antposvla',
'bcpara':[],

# CAL
'interpmode':['linear','nearest'],
'ref_ant':'15',
'calwt':True,
'syscal':'default', # syscal='default': choose the best caltype according to the dataset
                    # syscal=''       : no system pre-calibration
                    # syscal='tsys'....
                    
#    gaincurvel will be turned on if:
#        * data were from VLA
#        * taken before 2001
'scalsmooth':False,
'scalsmoothtime':60,

'flagtsys':True,
'flagtsys_range':[5.0,1000.0],

# CONSOLIDATE
'prefix_comb':[],
'wtscale':[],
'usevconcat':False,
'spwrgd':'',    # if spwrgd='spw', we will regrid spw to the clean setup
                # if spwrgd='', we will keep the spw from observations
                # 
                # * clean()/concat() can't work with a dataset with TOPO+LSRK or TOPO+BARY frames
                # if spwrgd='frame', we will only transform the spw frame to the desired one, which
                # might help resolve the above issue when combing multiple tracks with various frames.
                # spwgrd='spw' will help to reduce the vis data size to the mininmal required because
                # 
                # * the split vis already has the channel rebinned. This will also
                # speed up the CLEAN() because a smaller number vis records was handled during
                # the major cycle.
                # * If two corrs setup are in one spw (which may happen if two tracks with different 
                #   corr-config were regridding to the same channel setup), CLEAN() will consider
                #   one corr and ignore another corr. So you want to void two corr-setup in one spw
                #   -> avoid regridding dual-pol and single-pol tracks into the same channel setup.
                #
                #    
                #
'spwrgd_method':'cvel',
'combinespws':True,
'chanbin':0,
# CONTINUE SUBTRACTION
'fitspw':'',
'fitchans':'',
'fitorder':0,
'uvcs':False,
'imcs':False,
'freqtol':'',
'uvcs_combine':'spw',
'scalewt':False,
'scalewt_fitspw':'',
'scalewt_uvrange':'',
'hs':False,
'unchflag':False, # unflagged records with several channel flagged
                  # so each channel has the same flagging 

# CLEANing
'restorbeam':[''],
'resmooth':True,
'restorbeam_default':[''],
'restorbeam_method':'maximum',

'threshold_spec':'0.0mJy',
'threshold_cont':'0.0mJy',

'minpb':0.1,
'cleanspw':'',
'phasecenter':'',
'spinterpmode':'linear',
'restfreq':'1420405752.0Hz', #1420.405752
'outframe':'BARY',
'allowchunk':False,

'imsize':512,
'cell':'4.0arcsec',

'clean_mask':0.2,
'niter':10000,
'sigcutoff_spec':2.0,
'sigcutoff_cont':2.0,

'imstat_box_spec':'',
'imstat_rg_spec':'',
'imstat_chan':'',
'imstat_box_cont':'',
'imstat_rg_cont':'',

'ftmachine':'ft',
'imagermode':None,

'multiscale':[],
'cyclefactor':1.5,
'clean_gain':0.1,
'clean_field':'',

'cleanweight':'briggs',
'cleanspw':'',
'iterchan':False,
'outertaper':[],
'cleanspec':True,
'wrobust':0.5,
'gridmode':'aprojection',
'cleanmode':'channel',
# 
# MOSWEIGHT determines whether to calculate the gridding weights for each field independently
# or together, so mosweight doesn't matter for natural weighting.
#
# mosweight=True will produce an image optimzed local SNR, but sacrafy the uniformity 
# of noise and psf across the whole mosaicing pattern. Usually it will produced a slight larger
# beam. Since a global UV sampling density function doesn't make much sense when combing
# multiple tracks with several pointing because the phase-shifting from different point 
# will reduce local sensitiviy by bluring phase information.  
# 
# mosweight=True is closer to MIRAID's linear-mosaicing approach becaue each pointig are
# inverted independently (less phase bluring). 
# Although the primary pattern & the weight for each pointing (from integration time) are still embeded in the
# the basic weight and the additional PB pattern convolved during UV gridding.
#
# If the UV coverage is very different, it might doesn't much difference.
#
'mosweight':False, 

'psfmode':'clark',
'fitpsf':False,
'negcomponent':-1,
'cleancont':False,
'usescratch':False,

'clean_start':'',
'clean_width':1,
'clean_nchan':-1,

# PLOTTING
'plotformat':'pdf',

# INFOMATIVE
'email':'',     # NOTIFICATION EMAIL ADDRESS
'password':'',  # NOTIFICATION EMAIL PASSWORD
'version':'',   # SCRIPT VERSION
'log_listobs_msfile':'',
'keepcasaimage':True
}
