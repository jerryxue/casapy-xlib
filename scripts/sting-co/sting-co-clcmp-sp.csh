#!/bin/csh -f
#
#	this script will load data from repository

set galist=( 4605 ) 
set versions=( _1 _2 _3 _4 )
set tag="_sig"
set bsize="4.141"

foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

foreach gal ( $galist )

	set currentdir="${cwd}"
	set dir="/Volumes/data2/ruixue1/co/clcmp/n${gal}${tag}"
	#rm -rf ${dir}
	#mkdir ${dir}
	cd ${dir}
	set sdi_repo="/Volumes/data2/ruixue1/co/sdi/n${gal}${tag}"
	set msc_repo="/Volumes/data2/ruixue1/co/msc-mir/n${gal}${tag}" 
	
	echo " " 
	echo "--->"
	echo $gal
	echo "--->"
	echo " "
	if ( "$versions" == "" ) then
    	foreach version ( "" )
    else
    	foreach version ( $versions )
	endif
	echo $version 
	# load sdi clean/model cubes
	rm -rf ngc${gal}${version}.co.cmmsk ngc${gal}${version}.co.cln
	cp -rf $sdi_repo/ngc${gal}${version}.co.cmmsk ngc${gal}${version}.co.cmmsk 
	
	cp -rf ${sdi_repo}/ngc${gal}${version}.co.cln tmp1
	cp -rf ${sdi_repo}/ngc${gal}${version}.co.gain tmp2
	regrid in=tmp2 out=tmp3 tin=tmp1
	maths exp="<tmp1>/<tmp3>" out=ngc${gal}${version}.co.cln
	rm -rf tmp1 tmp2 tmp3
	
	#cp -rf $sdi_repo/ngc${gal}${version}.co.cln ngc${gal}${version}.co.cln 
	
	convol map=ngc${gal}${version}.co.cmmsk out=tmp \
		options=final fwhm=4.1411,4.1411 pa=0
	rm -rf ngc${gal}${version}.co.cmmsk.sr
	regrid in=tmp out=ngc${gal}${version}.co.cmmsk.sr tin=ngc${gal}.co.cmmsk.sr
	immask in=ngc${gal}${version}.co.cmmsk.sr \
		region="mask(ngc${gal}.co.cmmsk.sr)" logic=and
		rm -rf tmp
	convol map=ngc${gal}${version}.co.cln out=tmp \
		options=final fwhm=4.142,4.142 pa=0
	rm -rf ngc${gal}${version}.co.cln.sr
	regrid in=tmp out=ngc${gal}${version}.co.cln.sr tin=ngc${gal}.co.cln.sr
	immask in=ngc${gal}${version}.co.cln.sr \
		region="mask(ngc${gal}.co.cln.sr)" logic=and
	rm -rf tmp	
	end
	
end

fits.csh "*.sr"	>fits.csh.log

cd ${currentdir}


