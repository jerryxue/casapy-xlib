#!/bin/csh -f
#
#   this script will load data from maps repository
#
#	running location: /Volumes/data3/ruixue1/sting/products/cocube
#

set msc_repo="../../maps-mir/"
set msc_repo="/Volumes/data2/ruixue1/co/msc-mir/"
set pro_repo="/Volumes/data2/ruixue1/co/msc-products/"
set clcmp_repo="/Volumes/data2/ruixue1/co/msc-clcmp/"


#rm -rf ${pro_repo}/cocube
#mkdir ${pro_repo}/cocube
#rm -rf ${pro_repo}/comom
#mkdir ${pro_repo}/comom
#rm -rf ${pro_repo}/codmom
#mkdir ${pro_repo}/codmom
#rm -rf ${pro_repo}/copk
#mkdir ${pro_repo}/copk
#rm -rf ${pro_repo}/comodel
#mkdir ${pro_repo}/comodel
rm -rf ${pro_repo}/clcmp
mkdir ${pro_repo}/clcmp

foreach gal (	0337 0772 1156 1569 1637 2681 \
				2782 2976 3147 3198 3486 3593 \
				3949 4151 4254 4273 4536 4605 \
				4654 5371 5713 6503 6951)	

#cd ${pro_repo}/cocube
#foreach inp ( cm sen psf )
#	rm -rf n${gal}co.line.${inp}.fits n${gal}co.line.${inp}.fits.gz
#	fits in=$msc_repo/n${gal}/n${gal}co.line.${inp} out=n${gal}co.line.${inp}.fits op=xyout
#	gzip -f n${gal}co.line.${inp}.fits
#end
#
#cd ${pro_repo}/comodel
#foreach inp ( image model cmodel residual cln clnc res flux )
#	rm -rf n${gal}co.line.${inp}.fits n${gal}co.line.${inp}.fits.gz
#	fits in=$msc_repo/n${gal}/n${gal}co.line.${inp} out=n${gal}co.line.${inp}.fits op=xyout
#	gzip -f n${gal}co.line.${inp}.fits
#end
#
#cd ${pro_repo}/comom
#foreach inp ( mmom0 mmom0.nse )
#	rm -rf n${gal}co.line.${inp}.fits n${gal}co.line.${inp}.fits.gz
#	fits in=$msc_repo/n${gal}/n${gal}co.line.${inp} out=n${gal}co.line.${inp}.fits op=xyout
#	gzip -f n${gal}co.line.${inp}.fits
#end
#
#cd ${pro_repo}/codmom
#foreach inp ( dmom0 dmom0.nse )
#	rm -rf n${gal}co.line.${inp}.fits n${gal}co.line.${inp}.fits.gz
#	fits in=$msc_repo/n${gal}/n${gal}co.line.${inp} out=n${gal}co.line.${inp}.fits op=xyout
#	gzip -f n${gal}co.line.${inp}.fits
#end
#
#cd ${pro_repo}/copk
#foreach inp ( peak )
#	rm -rf n${gal}co.line.${inp}.fits n${gal}co.line.${inp}.fits.gz
#	fits in=$msc_repo/n${gal}/n${gal}co.line.${inp} out=n${gal}co.line.${inp}.fits op=xyout
#	gzip -f n${gal}co.line.${inp}.fits
#end

cd ${pro_repo}/clcmp
foreach inp ( cln.sr cm.sr mmom0.sr mmom0.nse.sr )
	rm -rf n${gal}co.line.${inp}.fits n${gal}co.line.${inp}.fits.gz
	fits in=$clcmp_repo/n${gal}/n${gal}co.line.${inp} out=n${gal}co.line.${inp}.fits op=xyout
	#gzip -f n${gal}co.line.${inp}.fits
end
foreach inp ( cln.sr cmmsk.sr mmom0.sr mmom0.nse.sr )
	rm -rf ngc${gal}.co.${inp}.fits ngc${gal}.co.${inp}.fits.gz
	fits in=$clcmp_repo/n${gal}/ngc${gal}.co.${inp} out=ngc${gal}.co.${inp}.fits op=xyout
	#gzip -f ngc${gal}.co.${inp}.fits
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

