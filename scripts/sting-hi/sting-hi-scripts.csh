#!/bin/csh -f 
#
#	generate reduction scripts for HI
#

goto tracks

tracks:

set currentdir="${cwd}"
set inplist=`ls ~/Dropbox/Worklib/casapy/scripts/sting-hi/*inp | sed -e 's/.*\///'`	

foreach inp ( $inplist )

set inp=`echo $inp | sed 's/_/ /g'`
set track=$inp[2]
set track=$track:r
set source=$inp[1]
echo $source $track

set script_repo="~/Dropbox/Worklib/casapy/scripts/sting-hi/"
set reducdir="/Volumes/Scratch/reduc/sting-hi/msc/${source}/"
set trackdir=${reducdir}${track}
set configfile=${script_repo}${source}_config.inp
set trackfile=${script_repo}${source}_${track}.inp
set casapyfile=${trackdir}/${source}_${track}.py

if ($track != 'config') then

	echo "processing ${source} ${track}"

	echo "#" > ${casapyfile}
	echo "# this CASA reduction script was automatically generated from configuration files:" >> ${casapyfile}
	echo "#   $configfile" >> ${casapyfile}
	echo "#   $trackfile" >> ${casapyfile}
	echo "# by $user on `date`">> ${casapyfile}
	echo "#" >> ${casapyfile}
	
	echo "" >> ${casapyfile}
	echo "######################################################" >> ${casapyfile}
	echo "#              track-independent setting" >> ${casapyfile}
	echo "######################################################" >> ${casapyfile}
	echo "" >> ${casapyfile}
	cat ${configfile} >> ${casapyfile}
	echo "" >> ${casapyfile}
	
	echo "" >> ${casapyfile}
	echo "######################################################" >> ${casapyfile}
	echo "#               track-dependent setting" >> ${casapyfile}
	echo "######################################################" >> ${casapyfile}
	echo "" >> ${casapyfile}
	cat ${trackfile} >> ${casapyfile}
	echo "" >> ${casapyfile}
	echo "# RUN SCRIPTS:" >> ${casapyfile}
	
	if ($track != 'comb') then
		echo "execfile(script_home+'ximport'+script_version+'.py')" >> ${casapyfile}
		echo "execfile(script_home+'xcal'+script_version+'.py')" >> ${casapyfile}
		echo "execfile(script_home+'xcalplot'+script_version+'.py')" >> ${casapyfile}
	endif
	echo "execfile(script_home+'xmerge'+script_version+'.py')" >> ${casapyfile}	
	if ($track != 'comb') then
		echo "checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)" >> ${casapyfile}
	endif	
	echo "execfile(script_home+'xclean'+script_version+'.py')" >> ${casapyfile}
	#`/usr/bin/casapy --nologger --nogui -c  ${source}_${track}.py `  &

endif

end

goto end
end:







