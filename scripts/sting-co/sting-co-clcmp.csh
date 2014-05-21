#!/bin/csh -f
#
#	this script will load data from repository

#set galist=( 4605 ) 
#set versions=( _1 _2 _3 _4 _5 _6 _7 _8 _9 _10 )
#set versions=( 	_11 _12 _13 _14 _15 _16 _17 _18 _19 _20 \
#				_21 _22 _23 _24 _25 _26 _27 _28 _29 _30 )
#set tag="_sig"
#set tag="_sig_st"
#set tag="_sig_st_brig"

#set galist=( 2976 )
#set versions=""
#set tag=""

#set galist=(	0337 0772 1156 1569 1637 \
				#				2681 2782 2976 3147 3198 \
				#3486 3593 3949 4151 4254 \
				#4273 4536 4605 4654 5371 \
				#5713 6503 6951 )
#set versions="" 
#set tag=""

set galist=(	0337 0772 1156 1569 1637 \
				2681 2782 2976 3147 3198 \
				3486 3593 3949 4151 4254 \
				4273 4536 4605 4654 5371 \
				5713 6503 6951 )
set versions=""
set tag=""

foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

foreach gal ( $galist )

	set currentdir="${cwd}"
	set dir="/Volumes/data2/ruixue1/co/msc-clcmp/n${gal}${tag}"
	rm -rf ${dir}
	mkdir ${dir}
	cd ${dir}
	set sdi_repo="/Volumes/data2/ruixue1/co/sdi/n${gal}"
	set msc_repo="/Volumes/data2/ruixue1/co/msc-mir/n${gal}${tag}" 
	
	echo " " 
	echo "--->"
	echo $gal
	echo "--->"
	echo " "
	
	# load ummasked sdi mmom0 maps
	rm -rf ngc${gal}.co.mmom0.um
	cp -rf $sdi_repo/ngc${gal}.co.mmom0 ngc${gal}.co.mmom0.um
	rm -rf ngc${gal}.co.mmom0.um/mask
	# load sdi clean/model cubes
	rm -rf ngc${gal}.co.cmmsk ngc${gal}.co.cln 
	cp -rf $sdi_repo/ngc${gal}.co.cmmsk ngc${gal}.co.cmmsk

	#cp -rf $sdi_repo/ngc${gal}.co.cln ngc${gal}.co.cln	
	
	if ( "$gal" == 0772 || "$gal" == 3147  ) then
		cp -rf $sdi_repo/ngc${gal}.co.cln ngc${gal}.co.cln 
	else
		cp -rf ${sdi_repo}/ngc${gal}.co.cln tmp1
		cp -rf ${sdi_repo}/ngc${gal}.co.gain tmp2
		regrid in=tmp2 out=tmp3 tin=tmp1
		maths exp="<tmp1>/<tmp3>" out=ngc${gal}.co.cln
		rm -rf tmp1 tmp2 tmp3
	endif
 

	# load casa cubes
	set casacube="ngc${gal}.co.cln"
	set maxbsize=0.0 
	if ( "$versions" == "" ) then
    	foreach version ( "" )
    else
    	foreach version ( $versions )
	endif
		rm -rf n${gal}co${version}.line.cm n${gal}co${version}.line.cln
		cp -rf ${msc_repo}/n${gal}co$version.line.cm n${gal}co${version}.line.cm
		cp -rf ${msc_repo}/n${gal}co$version.line.cln n${gal}co${version}.line.cln
		set casacube="${casacube},n${gal}co${version}.line.cm,n${gal}co${version}.line.cln"
		set bmaj=`gethd in=n${gal}co${version}.line.cm/bmaj`
		set bmaj=`calc -f f9.3 "$bmaj/2/pi*360*60*60"`
		echo "beam size: $bmaj" 
		set maxbsize=`calc "max(${maxbsize},${bmaj})"`
	end
	set bmaj=`gethd in=ngc${gal}.co.cmmsk/bmaj`
	set bmaj=`calc -f f9.3 "$bmaj/2/pi*360*60*60"`
	echo "beam size: $bmaj" 
	set maxbsize=`calc "max(${maxbsize},${bmaj})"`
	set maxbsize=`calc "${maxbsize}+0.001"`
	
	matcher.csh tin="ngc${gal}.co.cmmsk" \
		im=$casacube bsize=$maxbsize > matcher.log

	fits.csh "*.sr"	>fits.csh.log
	integrate_spec.csh "*.sr" > integrate_spec.log
	
	# load mmom maps
	rm -rf ngc${gal}.co.mmom0 ngc${gal}.co.mmom0.nse
	cp -rf $sdi_repo/ngc${gal}.co.mmom0 ngc${gal}.co.mmom0
	cp -rf $sdi_repo/ngc${gal}.co.mmom0.nse ngc${gal}.co.mmom0.nse
	rm -rf n${gal}co.line.mmom0 n${gal}co.line.mmom0.nse
	cp -rf ${msc_repo}/n${gal}co.line.mmom0 n${gal}co.line.mmom0
	cp -rf ${msc_repo}/n${gal}co.line.mmom0.nse n${gal}co.line.mmom0.nse
	matcher.csh tin="ngc${gal}.co.mmom0" \
		im="n${gal}co.line.mmom0,n${gal}co.line.mmom0.nse,ngc${gal}.co.mmom0.nse" bsize=$maxbsize axes='1,2'
	
end

cd ${currentdir}


