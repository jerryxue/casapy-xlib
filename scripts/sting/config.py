#
#   SET SOME PROJECT-RELATED GLOBAL VARIABLES
#

st={    'hi_raw':       '/Volumes/Scratch/raw/21cm/',
        'hi_proc':      '/Volumes/Scratch/proc/21cm/',
        'co_raw':       '/Volumes/Scratch/raw/co/',
        '12co_proc':    '/Volumes/Scratch/proc/12co/',
        '13co_proc':    '/Volumes/Scratch/proc/13co/'
    }

stinghi=os.path.dirname(xlib_path)+'/scripts/sting/hi/'
stingco=os.path.dirname(xlib_path)+'/scripts/sting/12co/'
sting13co=os.path.dirname(xlib_path)+'/scripts/sting/13co/'

###################################################################
#   Directory Structure:
#   proc/line/->
#               galaxy->
#                     ->track:  calibration+snapshot+diagnosis
#                     ->comb:   final combined imaging
#                     ->logs:   .log .last folder
###################################################################

