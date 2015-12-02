PRO PBTEST

;pbplot
;pbplot telescop=OVRO freq=111.4319554 device=/xs log=mir_ovro.log
;pbplot telescop=BIMA freq=111.4319554 device=/xs log=mir_bima.log
;pbplot telescop=CARMA freq=111.4319554 device=/xs log=mir_carma.log
    
readcol,'mir_carma.log',carma_r,carma_pb
readcol,'mir_ovro.log',ovro_r,ovro_pb
readcol,'mir_bima.log',bima_r,bima_pb

set_plot,'ps'
device,filename='pbtest.eps',bits=8,$
    xsize=4.5,ysize=5.5,$
    /inches,/encapsulated,/color
!p.thick=1.5
!x.thick = 1.5
!y.thick = 1.5
!z.thick = 1.5
!p.charsize=0.8
!p.charthick=1.5
!x.gridstyle = 0
!y.gridstyle = 0
xyouts,'!6'

plot,carma_r,carma_pb,/nodata,xrange=[0,1.5],yrange=[0.0,1.1],xstyle=1,ystyle=1,$
    xtitle='Radial Distance [arcmin]',ytitle='PB Response'

oplot,ovro_r,ovro_pb,color=cgcolor('red'),thick=7,linestyle=0
fwhmd_ovro=2.0*interpol(ovro_r,ovro_pb,0.5)

oplot,carma_r,carma_pb,color=cgcolor('green'),thick=7,linestyle=0
fwhmd_carma=2.0*interpol(carma_r,carma_pb,0.5)

oplot,bima_r,bima_pb,color=cgcolor('blue'),thick=7,linestyle=0
fwhmd_bima=2.0*interpol(bima_r,bima_pb,0.5)

al_legend,['OVRO','BIMA','CARMA']+' '+string([fwhmd_ovro,fwhmd_bima,fwhmd_carma],format='(f5.3)')+'"',$
    /top,/right,textc=['red','blue','green']
;oplot,carma_r,sqrt((bima_pb*ovro_pb)),linestyle=1

rp=radprofile_analyzer('n4254_e2_bima.flux.fits',/center,/nosub,rbin=0.25,extrad=120,/silent,refxy=[400,400])
oplot,rp.center/60.0,rp.median,color=cgcolor('blue'),thick=1.0,linestyle=2
print,n_elements(rp.center/60.0),n_elements(rp.mean)
;oplot,rp.center/60.0,rp.mean,color=cgcolor('red'),thick=2
fwhmc_bima=2.0*interpol(rp.center/60.0,rp.median,0.5,/nan)
print,'-->',fwhmc_bima
;fwhmd=fwhmd+0.08
;psf=psf_gaussian(npixel=401,fwhm=fwhmd*60/0.25,ndim=1)
;psf=psf/max(psf)
;oplot,findgen(200)*0.25/60.0,psf[201:*],thick=2

rp=radprofile_analyzer('n4254_e2_ovro.flux.fits',/center,/nosub,rbin=0.25,extrad=120,/silent,refxy=[400,400])
oplot,rp.center/60.0,rp.median,color=cgcolor('red'),thick=1.0,linestyle=2
;oplot,rp.center/60.0,rp.mean,color=cgcolor('blue'),thick=10.0
fwhmc_ovro=2.0*interpol(rp.center/60.0,rp.median,0.5,/nan)
print,'-->',fwhmc_ovro

rp=radprofile_analyzer('n4254_e2_carma.flux.fits',/center,/nosub,rbin=0.25,extrad=120,/silent,refxy=[400,400])
oplot,rp.center/60.0,rp.median,color=cgcolor('green'),thick=1.0,linestyle=2
;oplot,rp.center/60.0,rp.mean,color=cgcolor('green'),thick=5
fwhmc_carma=2.0*interpol(rp.center/60.0,rp.median,0.5,/nan)
print,'-->',fwhmc_carma

oplot,[0,10],[0.5,0.5],linestyle=1

al_legend,['CASA','MIRIAD'],linestyle=[2,0],/bot,/left
;
;rp=radprofile_analyzer('n4254_e2_carma.flux.pbcoverage.fits',/center,/nosub,rbin=0.25,extrad=120,/silent,refxy=[400,400])
;;oplot,rp.center/60.0,rp.median,color=cgcolor('blue'),thick=1.0
;oplot,rp.center/60.0,rp.mean,color=cgcolor('yellow'),thick=2

;oplot,x_ovro,sqrt(y_bima*y_ovro)

device,/close
set_plot,'x'


END

PRO PBTEST_FFT

hd=mk_hd([0,0],[401,401],1)
psf=psf_gaussian(npixel=401,fwhm=20,ndim=2)
psf=psf/max(psf)
f_psf=fft(psf,/center)
writefits,'f_psf_real.fits',real_part(f_psf)
writefits,'f_psf_image.fits',IMAGINARY(f_psf)

END