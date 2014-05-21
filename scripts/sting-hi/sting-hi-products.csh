#!/bin/csh -f
#
#   this script will load data from maps repository
#
#	running location: /Volumes/data3/ruixue1/sting/products/cocube
#

set msc_repo="/Volumes/data3/ruixue1/hi/msc-mir/"
set pro_repo="/Volumes/data3/ruixue1/hi/msc-products/"

rm -rf ${pro_repo}/hicube
mkdir ${pro_repo}/hicube
rm -rf ${pro_repo}/hicont
mkdir ${pro_repo}/hicont
rm -rf ${pro_repo}/himom
mkdir ${pro_repo}/himom
rm -rf ${pro_repo}/hidmom
mkdir ${pro_repo}/hidmom
rm -rf ${pro_repo}/hipk
mkdir ${pro_repo}/hipk
  
foreach gal (	0337 0772 1156 1569 1637 \
                2782 2976 3147 3198 3486 \
                3593 4151 4254 4536 4605 \
                4654 5371 5713 6951 )

cd ${pro_repo}/hicube
foreach inp ( cm sen image )
	rm -rf n${gal}hi.line.${inp}.fits n${gal}hi.line.${inp}.fits.gz
	fits in=$msc_repo/n${gal}/n${gal}hi.line.${inp} out=n${gal}hi.line.${inp}.fits op=xyout
	#gzip -f n${gal}hi.line.${inp}.fits
end

cd ${pro_repo}/hicont
foreach inp ( cm sen image )
	rm -rf n${gal}hi.cont.${inp}.fits n${gal}hi.cont.${inp}.fits.gz
	fits in=$msc_repo/n${gal}/n${gal}hi.cont.${inp} out=n${gal}hi.cont.${inp}.fits op=xyout
	#gzip -f n${gal}hi.cont.${inp}.fits
end

cd ${pro_repo}/himom
foreach inp ( mmom0 mmom0.nse )
	rm -rf n${gal}hi.line.${inp}.fits n${gal}hi.line.${inp}.fits.gz
	fits in=$msc_repo/n${gal}/n${gal}hi.line.${inp} out=n${gal}hi.line.${inp}.fits op=xyout
	#gzip -f n${gal}hi.line.${inp}.fits
end

cd ${pro_repo}/hidmom
foreach inp ( dmom0 dmom0.nse )
	rm -rf n${gal}hi.line.${inp}.fits n${gal}hi.line.${inp}.fits.gz
	fits in=$msc_repo/n${gal}/n${gal}hi.line.${inp} out=n${gal}hi.line.${inp}.fits op=xyout
	#gzip -f n${gal}hi.line.${inp}.fits
end

cd ${pro_repo}/hipk
foreach inp ( peak )
	rm -rf n${gal}hi.line.${inp}.fits n${gal}hi.line.${inp}.fits.gz
	fits in=$msc_repo/n${gal}/n${gal}hi.line.${inp} out=n${gal}hi.line.${inp}.fits op=xyout
	#gzip -f n${gal}hi.line.${inp}.fits
end


end

#rm -rf products.tar.gz
#tar czvf products.tar.gz cocube codmom comom copk scripts
#scp products.tar.gz ruixue@mmwave:~/

# WWT Testing
# foreach file (../../maps/n*/ngc*co.line.mmom0)
#     rm -rf $root.rgd
#     regrid in=$file out=$root.rgd project=tan axes=1,2
#     rm -f $root.fits
#     fits in=$file out=$root.fits op=xyout
# end

# IDL code to add CD matrix to FITS header

#/usr/local/itt/idl71/bin/idl<<EOF
#image=readfits('ngc4254co.line.mmom0.fits',hdr)
#extast,hdr,astr,noparam
#putast,hdr,astr,cd_type=2
#writefits,'ngc4254.cd.fits',image,hdr
#EOF

#sethead ngc4254.cd.fits CFRAME='ICRS'
#sethead ngc4254.cd.fits EQUINOX=2000.0

