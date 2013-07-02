#!/bin/csh -f
#
#   load CASA fits cubes into MIR cubes
#   note:   we apply a msklev=4 2d masking
#
#	postfix: 
#	cm			cleaned map 
#	cln 		model
#	clnc 		convolved model
#	res			residual
#
#	image 		pb-uncorrected cleaned map
#	model  		pb-uncorrected model (jy/pixel)
#	cmodel 		pb-uncorrected convolved model (image-residual jy/cbeam)
#	residual 	pb-uncorrected residual (jy/dbeam)
#
#	sen 		sensitivity map for the cleaned map
#	flux 		pb-correction pattern
#	psf 		psf
#

#set galist=( 4605 ) 
#set versions= ( _1 _2 _3 _4 _5 _6 _7 _8 _9 _10 )
#set versions= ( _11 _12 _13 _14 _15 \
#				_16	_17 _18 _19 _20 \
#				_21 _22 _23 _24 _25 \
#				_26 _27 _28 _29 _30 )
#set tag="_sig"
#set galist=( 2976 )
#set versions=""
#set tag="_st"

set galist=(	0337 0772 1156 1569 1637 \
				2681 2782 2976 3147 3198 \
				3486 3593 3949 4151 4254 \
				4273 4536 4605 4654 5371 \
				5713 6503 6951 )
set galist= ( 2976 )				
set versions="" 	# different msc versions in the msc folder
set tag=""			# postfix for the msc folder
 																 																
set msklev=4

foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

foreach gal ( $galist )

	set sdir=`pwd -L`	#	get the script path. 
						#	This may be safer than <set currentdir="${cwd}">
	set pdir="$sdir:h"	#	get the working directory path

	set currentdir=`pwd -L`
	set dir="${pdir}/msc-mir/n${gal}${tag}"
	rm -rf ${dir}
	mkdir ${dir}
	cd ${dir}
	set msc_repo="${pdir}/msc/n${gal}${tag}"
	
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
		# load msc cubes
		foreach inp ( cm sen flux psf image model cmodel residual )
			rm -rf n${gal}co${version}.line.$inp.fits
			cp -rf $msc_repo/n${gal}co${version}.line.$inp.fits n${gal}co${version}.line.$inp.fits
			wcsfix.csh file=n${gal}co${version}.line.$inp.fits frame='VELO-LSR'
			rm -rf n${gal}co${version}.line.$inp.fits
		end
		
		rm -rf n${gal}co${version}.line.cln
		maths exp="<n${gal}co${version}.line.model>/<n${gal}co${version}.line.flux>" \
			out=n${gal}co${version}.line.cln
		
		rm -rf n${gal}co${version}.line.clnc
		maths exp="<n${gal}co${version}.line.cmodel>/<n${gal}co${version}.line.flux>" \
			out=n${gal}co${version}.line.clnc
		
		rm -rf n${gal}co${version}.line.res
		maths exp="<n${gal}co${version}.line.residual>/<n${gal}co${version}.line.flux>" \
			out=n${gal}co${version}.line.res						
		
		# create a 2D masking
		set nmaps=`gethd in=n${gal}co${version}.line.sen/naxis3`
		set mi=`calc -i "$nmaps/2"`
		rm -rf n${gal}co${version}.line.sen0 n${gal}co${version}.line.sen1 n${gal}co${version}.line.sen2
		imsub in=n${gal}co${version}.line.sen out=n${gal}co${version}.line.sen0 region="images($mi)"
		set minval=`histo in=n${gal}co${version}.line.sen0 | grep Min | awk '{print $3}'`
		set clip=`calc "$msklev*$minval"`
		maths exp="<n${gal}co${version}.line.sen0>" mask="<n${gal}co${version}.line.sen0>.lt.$clip" \
		    out=n${gal}co${version}.line.sen1
		imblr in=n${gal}co${version}.line.sen1 value=$clip out=n${gal}co${version}.line.sen2
		
		# use the masking image to mask cubes, shrink the cube to the unmkased region size.
		foreach inp ( cm sen flux psf image model cmodel residual cln clnc res )
			rm -rf n${gal}co${version}.line.${inp}msk n${gal}co${version}.line.${inp}.tp
			imblr in="n${gal}co${version}.line.${inp}" out="n${gal}co${version}.line.${inp}.tp" value=0.0
			rm -rf n${gal}co${version}.line.${inp}
			mv n${gal}co${version}.line.${inp}.tp n${gal}co${version}.line.${inp}
			maths exp="<n${gal}co${version}.line.${inp}>" \
				out=n${gal}co${version}.line.${inp}msk \
			    mask="<n${gal}co${version}.line.sen2>.lt.$clip" \
			    options=grow
			rm -rf n${gal}co${version}.line.${inp}
			maths exp="<n${gal}co${version}.line.${inp}msk>" out=n${gal}co${version}.line.${inp} \
				region="mask(n${gal}co${version}.line.${inp}msk)"
			rm -rf n${gal}co${version}.line.${inp}msk
			minmax in=n${gal}co${version}.line.${inp}
		end
		rm -rf n${gal}co${version}.line.sen0 n${gal}co${version}.line.sen1 n${gal}co${version}.line.sen2
	
	end 
	
end

cd ${currentdir}



