#!/bin/csh -f
#
#   this script will load the CASA HI fits into MIR cubes
#   note:   we apply the msklev=2 masking extracted from the first planes
#           to all planes
#
#	<n${gal}hi.line.image>-<n${gal}hi.line.res>=<n${gal}hi.line.con>
#	running location: /Volumes/data3/ruixue1/hi/msc/maps-mir

set currentdir="${cwd}"
set dir="/Volumes/data3/ruixue1/hi/msc-mir"
cd ${dir}

set msc_repo="/Volumes/data3/ruixue1/hi/msc"
  
set galist = (   0337 0772 1156 1569 1637 \
                2782 2976 3147 3198 3486 \
                3593 4151 4254 4536 4605 \
                4654 5371 5713 6951 ) 
set imlist = ( 	500 800 300 450 800 \
				400 450 400 800 800 \
				250 600 450 400 250 \
				600 400 400 400 )               

foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end


foreach i ( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 )

set gal=${galist[${i}]}
rm -rf n${gal}
mkdir n${gal}
echo " "
echo "n${gal}"
echo " "
foreach inp ( cm sen image )
	rm -rf n${gal}/n${gal}hi.line.$inp.fits
	ln -s $msc_repo/n${gal}/comb/n${gal}hi.line.$inp.fits n${gal}/n${gal}hi.line.$inp.fits
	wcsfix.csh file=n${gal}/n${gal}hi.line.$inp.fits frame='VELO-HEL'
	imsub in=n${gal}/n${gal}hi.line.$inp out=n${gal}/n${gal}hi.line.$inp.tmp \
		region="a,box(-$imlist[$i],-$imlist[$i],$imlist[$i],$imlist[$i])"
	rm -rf n${gal}/n${gal}hi.line.$inp.fits n${gal}/n${gal}hi.line.$inp
	mv n${gal}/n${gal}hi.line.$inp.tmp n${gal}/n${gal}hi.line.$inp
	minmax in=n${gal}/n${gal}hi.line.$inp
end

foreach inp ( cm sen image )
	rm -rf n${gal}/n${gal}hi.cont.$inp
	echo "$msc_repo/n${gal}/n${gal}hi.cont.$inp.fits"
	fits in="${msc_repo}/n${gal}/comb/n${gal}hi.cont.$inp.fits" \
		out=n${gal}/n${gal}hi.cont.$inp op=xyin
	imsub in=n${gal}/n${gal}hi.cont.$inp out=n${gal}/n${gal}hi.cont.$inp.tmp \
		region="a,box(-$imlist[$i],-$imlist[$i],$imlist[$i],$imlist[$i])"	
	rm -rf n${gal}/n${gal}hi.cont.$inp
	mv n${gal}/n${gal}hi.cont.$inp.tmp n${gal}/n${gal}hi.cont.$inp
	minmax in=n${gal}/n${gal}hi.cont.$inp
end

end

cd ${currentdir}
