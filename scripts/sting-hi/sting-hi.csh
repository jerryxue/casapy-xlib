#!/bin/csh -f 
# 	due to some issue with casapy,
#	one has to switch to csh and source this script
#	to keep all processes in the parent shell.

## parallel multi-track processing

goto tracks

tracks:
set currentdir="${cwd}"
set source=n0337

set tracklist=`ls /Volumes/Scratch/reduc/sting-hi/msc/${source} | grep "/" | grep -v "comb"`	
echo $tracklist
foreach track ( $tracklist )

	echo "processing ${source} ${track}"
	set script_repo="~/Worklib/casapy/scripts/sting-hi/${source}/"
	set reducdir="/Volumes/Scratch/reduc/sting-hi/msc"
	set trackdir=${reducdir}${track}
	set configfile=${script_repo}${source}_config.inp
	set trackfile=${script_repo}${source}_${track}.inp
	
	cd $trackdir
	echo "#" > ${source}_${track}.py
	echo "# this CASA reduction script was automatically generated from configuration files:" >> ${source}_${track}.py
	echo "#   $configfile" >> ${source}_${track}.py
	echo "#   $trackfile" >> ${source}_${track}.py
	echo "# by $user on `date`">> ${source}_${track}.py
	echo "#" >> ${source}_${track}.py
	
	echo "" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "#              track-independent setting" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	cat ${configfile} >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	
	echo "" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "#               track-dependent setting" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	cat ${trackfile} >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	
	echo "# RUN SCRIPTS:" >> ${source}_${track}.py
	echo "execfile(script_home+'iload_'+script_version+'.py')" >> ${source}_${track}.py
	echo "execfile(script_home+'ical_'+script_version+'.py')" >> ${source}_${track}.py
	echo "execfile(script_home+'icalplot_'+script_version+'.py')" >> ${source}_${track}.py
	echo "execfile(script_home+'imerge_'+script_version+'.py')" >> ${source}_${track}.py
	echo "checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)" >> ${source}_${track}.py
	echo "execfile(script_home+'iclean_'+script_version+'.py')" >> ${source}_${track}.py
	#`/usr/bin/casapy --nologger --nogui -c  ${source}_${track}.py `  &
end
cd ${currentdir}
goto end


combine:
set currentdir="${cwd}"
set sourcelist="n1156"
set tracklist="comb"
foreach source ( $sourcelist )
	
	set track='comb'
	set script_repo="~/Worklib/casapy/scripts/sting-hi/${source}/"
	set reducdir="/Volumes/data3/ruixue1/hi/msc/${source}/"
	set trackdir=${reducdir}${track}
	set configfile=${script_repo}${source}_config.inp
	set trackfile=${script_repo}${source}_${track}.inp
	
	cd $trackdir
	echo "#" > ${source}_${track}.py
	echo "# this CASA reduction script was automatically generated from configuration files:" >> ${source}_${track}.py
	echo "#   $configfile" >> ${source}_${track}.py
	echo "#   $trackfile" >> ${source}_${track}.py
	echo "# by $user on `date`">> ${source}_${track}.py
	echo "#" >> ${source}_${track}.py
	
	echo "" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "#              track-independent setting" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	cat ${configfile} >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	
	echo "" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "#               track-dependent setting" >> ${source}_${track}.py
	echo "######################################################" >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	cat ${trackfile} >> ${source}_${track}.py
	echo "" >> ${source}_${track}.py
	
	echo "# RUN SCRIPTS:" >> ${source}_${track}.py
	echo "execfile(script_home+'imerge_'+script_version+'.py')" >> ${source}_${track}.py
	echo "execfile(script_home+'iclean_'+script_version+'.py')" >> ${source}_${track}.py
	`/usr/bin/casapy --nologger --nogui -c  ${source}_${track}.py `  &
end
cd ${currentdir}
goto end

end:


#foreach source (   n0337 n0772 n1156 n1569 n1637 \
#                n2782 n2976 n3147 n3198 n3486 )
#foreach source  ( n3593 n4151 n4254 n4536 n4605 \
#                 n4654 n5371 n5713 n6951 ) 
#
#set script_repo="~/Worklib/casapy/scripts/sting-hi/${source}/"
#set reducdir="/Volumes/data3/ruixue1/hi/msc/${source}/"
#set track="comb"
#set trackdir=${reducdir}${track}
#
#rm -rf ${trackdir}-na
#cp -rf ${trackdir} ${trackdir}-na
#launch_casa.csh \
#	dir="${trackdir}-na" \
#	inp="${script_repo}${source}_${track}_na.inp"
#end






