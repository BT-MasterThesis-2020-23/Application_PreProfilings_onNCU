#!/bin/bash
if [ $# -eq 0 ];
then
  echo "$0: Arguments are missing"
  exit 1
else
  sm_id="$1"  #sm_id
  arg1="$2"   #simulator_exe

  nvcc 2DConvolution.cu -arch=$sm_id -o 2DConvolution 
  nvcc 2mm.cu -arch=$sm_id -o 2mm 
  nvcc 3DConvolution.cu -arch=$sm_id -o 3DConvolution 
  nvcc 3mm.cu -arch=$sm_id -o 3mm 
  nvcc atax.cu -arch=$sm_id -o atax 
  nvcc bicg.cu -arch=$sm_id -o bicg 
  nvcc correlation.cu -arch=$sm_id -o correlation 
  nvcc covariance.cu -arch=$sm_id -o covariance 
  nvcc fdtd2d.cu -arch=$sm_id -o fdtd2d 
  nvcc gemm.cu -arch=$sm_id -o gemm 
  nvcc gesummv.cu -arch=$sm_id -o gesummv 
#  nvcc gramschmidt.cu -arch=$sm_id -o gramschmidt 
  nvcc mvt.cu -arch=$sm_id -o mvt 
  nvcc syrk.cu -arch=$sm_id -o syrk 

  mkdir apps
  mv 2DConvolution apps
  mv 2mm apps
  mv 3DConvolution apps
  mv 3mm apps
  mv atax apps
  mv bicg apps
  mv correlation apps
  mv covariance apps
  mv fdtd2d apps
  mv gemm apps
  mv gesummv apps
#  mv gramschmidt apps
  mv mvt apps
  mv syrk apps

  mkdir prof_results

  ncu --set full --target-processes all apps/2DConvolution > prof_results/2DConvolution.txt.txt 
  ncu --set full --target-processes all apps/2mm > prof_results/2mm.txt.txt 
  ncu --set full --target-processes all apps/3DConvolution > prof_results/3DConvolution.txt.txt 
  ncu --set full --target-processes all apps/3mm > prof_results/3mm.txt.txt 
  ncu --set full --target-processes all apps/atax > prof_results/atax.txt.txt 
  ncu --set full --target-processes all apps/bicg > prof_results/bicg.txt.txt 
  ncu --set full --target-processes all apps/correlation > prof_results/correlation.txt.txt 
  ncu --set full --target-processes all apps/covariance > prof_results/covariance.txt.txt 
  ncu --set full --target-processes all apps/fdtd2d > prof_results/fdtd2d.txt.txt 
  ncu --set full --target-processes all apps/gemm > prof_results/gemm.txt.txt 
  ncu --set full --target-processes all apps/gesummv > prof_results/gesummv.txt.txt 
#  ncu --set full --target-processes all apps/gramschmidt > prof_results/gramschmidt.txt 
  ncu --set full --target-processes all apps/mvt > prof_results/mvt.txt 
  ncu --set full --target-processes all apps/syrk > prof_results/syrk.txt
fi


