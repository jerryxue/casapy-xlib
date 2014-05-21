#!/bin/csh -f 
# 	cleanup scratch files

set sdir=`pwd -L`	#	get the script path. 
					#	This may be safer than <set currentdir="${cwd}">
set pdir="$sdir:h"	#	get the working directory path

ls -lrtd ${pdir}/msc/n*/C* ${pdir}/msc/n*/D* ${pdir}/msc/n*/E* ${pdir}/msc/n*/Temp*
rm -rf ${pdir}/msc/n*/C* ${pdir}/msc/n*/D* ${pdir}/msc/n*/E* ${pdir}/msc/n*/Temp*	
