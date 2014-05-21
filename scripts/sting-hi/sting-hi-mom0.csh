#!/bin/csh -f
#
# 	This script will call mommsc.csh to generate mom0/1 maps
#	
#	running ocation:	/Volumes/data3/ruixue1/sting/msc/maps-mir

set currentdir="${cwd}"
set dir="/Volumes/data3/ruixue1/hi/msc-mir"
cd ${dir}

set galist=(   0337 0772 1156 1569 1637 \
                2782 2976 3147 3198 3486 \
                3593 4151 4254 4536 4605 \
                4654 5371 5713 6951)
set fwhmlist= ( 75 120 21 20 60 \
				22 27 60 23 150 \
				45 30 24 30 16 \
				51 200 51 27 )
				
foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

foreach i ( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 )
    set fwhm=$fwhmlist[$i]
    set gal=$galist[$i]               
    cd n$gal
    sting-mom0.csh gal=$gal tag="hi" fwhm=$fwhm
    cd ../
end

gs -sDEVICE=pswrite -sOutputFile=mmom0_all.ps \
	-dNOPAUSE -dBATCH n*/*.mmom0.ps

cd ${currentdir}

