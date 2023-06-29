#!/bin/bash
if [ $# -eq 0 ];
then
  echo "$0: Arguments are missing"
  exit 1
else
  sm_id="$1"  #sm_id
  arg1="$2"   #simulator library

  nvcc AlexNet/alexnet_host.cu -o AlexNet/alex_next -arch=$sm_id 
  nvcc CifarNet/CN_cuda.cu -o CifarNet/cifar_net -arch=$sm_id
  nvcc GRU/gru_host.cu -o GRU/gru -arch=$sm_id
  nvcc LSTM/lstm.cu -o LSTM/lstm -arch=$sm_id
  nvcc ResNet/resnet_host.cu -o ResNet/res_net -arch=$sm_id
  nvcc SqueezeNet/SN.cu -o SqueezeNet/squeeze_net -arch=$sm_id

  mkdir prof_results

  cd AlexNet
  ncu --set full --target-processes all alex_next 1 > ../prof_results/alex_next.txt 

  cd ../CifarNet
  ncu --set full --target-processes all cifar_net 1 > ../prof_results/cifar_net.txt 

  cd ../GRU
  ncu --set full --target-processes all gru > ../prof_results/gru.txt 

  cd ../LSTM
  ncu --set full --target-processes all lstm 1 > ../prof_results/lstm.txt 

  cd ../ResNet
  ncu --set full --target-processes all res_net 1 > ../prof_results/res_net.txt 

  cd ../SqueezeNet
  ncu --set full --target-processes all SqueezeNet/squeeze_net 1 > ../prof_results/squeeze_net.txt 

fi


