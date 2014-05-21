#!/bin/csh -f
#
# 	This script will call mommsc.csh to generate mom0/1 maps
#	
#	running ocation:	/Volumes/data3/ruixue1/sting/mscn/maps-mir
#	or
#	running ocation:	/Volumes/data3/ruixue1/sting/mscs/maps-mir (for standard clean versions)



set currentdir="${cwd}"
set dir="/Volumes/data2/ruixue1/co/msc-mir"
cd ${dir}

#set galist=( 4254 )

set tag=""
set version="co"
set galist=( 	0337 0772 1156 1569 1637 \
				2681 2782 2976 3147 3198 \
				3486 3593 3949 4151 4254 \
				4273 4536 4605 4654 5371 \
				5713 6503 6951 )  


foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

foreach gal (  $galist )

	echo " " 
	echo "--->"
	echo $gal
	echo "--->"
	echo " "

    cd n${gal}${tag}
    sting-mom0.csh gal=$gal tag=${version}
    cd ../
end

gs -sDEVICE=pswrite -sOutputFile=mmom0_all.ps \
	-dNOPAUSE -dBATCH n*/*.mmom0.ps

cd ${currentdir}
