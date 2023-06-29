# Application PreProfilings on NVIDIA Nsight Compute Tool CLI (NCU) 

Here

The below list includes the profiled applications with data on RTX1650. However, I have included the scripts such that you can clone them into your local machines and runs them after small manipulations. To conduct this profiling analysis, you must provide application binaries correspondingly and re-configure the related .sh files. 
 <br> 
In addition, the other Python files extract some of the features resulting from all the profiling results and record them to **ProfRes.xlsx** file. 

For more information, you can contact with us or address your requests on the issues. :) 
topcuburak@gmail.com

> **Gardenia** [Gardenia](https://github.com/chenxuhao/gardenia)  <br> 
>> **BC Linear Base** <br> 
>> **BC Linear LB** <br>
>> **BC Topo Base** <br>
>> **BC Topo LB** <br>
>> **BFS Linear Base** <br>
>> **BFS Linear LB** <br>
>> **CC Afforest** <br>
>> **CC Base** <br>
>> **CC Warp** <br>
>> **MST Topo** <br>
>> **PR Base** <br>
>> **PR Warp** <br>
>> **SPMV Base** <br>
>> **SPMV Push** <br>
>> **SPMV Vector** <br>
>> **SPMV Warp** <br>
>> **SSSP Linear Base** <br>
>> **SSSP Linear LB** <br>
>> **VC Linear Base** <br>
>> **VC Linear Bitset** <br>
>>> **Datasets** 
```console
4.mtx, 4w.mtx, asia_osm.mtx, chesapeake.mtx, coAuthorsCiteseer.mtx, coAuthorsDBLP.mtx, <br>
coPapersCiteseer.mtx, coPapersDBLP.mtx, germany_osm.mtx, great-britain_osm.mtx, higgs-twitter_mention.mtx, higgs-twitter_reply.mtx, higgs-twitter_retweet.mtx, higgs-twitter.mtx, indochina-2004.mtx, italy_osm.mtx, min-1DeadEnd.mtx, ProfRes.mtx, socEpinions1.mtx, socLiveJournal1.mtx, soc-Slashdot0811.mtx, soc-Slashdot0902.mtx, test_bc.mtx, test_cc.mtx, test_mst.mtx, test_pr.mtx, test_scc.mtx, test_sgd.mtx, test_small_scc.mtx, web-Google.mtx, web-NotreDame.mtx, web-Stanford.mtx
``` 

> **PolyBench** : [PolyBench](https://web.cs.ucla.edu/~pouchet/software/polybench/GPU/index.html)
>> **2DConvolution**
>> **2mm**
>> **3DConvolution**
>> **3mm**
>> **adi**
>> **atax**
>> **bicg**
>> **correlation**
>> **covariance**
>> **doitgen**
>> **fdtd2d**
>> **gemm**
>> **gemver**
>> **gesummv**
>> **jacobi1d**
>> **jacobi2d**
>> **lu**
>> **mvt**
>> **syr2k**
>> **syrk**

> **Rodinia-3.1** [Rodinia 3.1](https://www.cs.virginia.edu/rodinia/doku.php)
>> **backrop**
>> **bfs**
>> **b+tree**
>> **cfd_02M**
>> **cfd_097K**
>> **cfd_193K**
>> **heartwall_40**
>> **hotspot**
>> **huffman**
>> **hybridsort**
>> **lavaMD**
>> **lud_cuda**
>> **nn**
>> **nw**
>> **pathfinder**
>> **srad_v1**
>> **srad_v2**

> **TangoDNN** [Tango](https://gitlab.com/Tango-DNNbench/)
>> **alex_next**
>> **cifar_net**
>> **gru**
>> **lstm**
>> **res_net**
>> **squeeze_net**






