
from kernel_counter import *
from kernel_metric_extractor import *
from export_to_csv import *

sections_renamed = ["SOL", "CWA", "MWA", "MWA_Chart", "MWA_Table", "WarpStateStats", "SchedulerStats", 
                    "InstStats", "LaunchStats", "OccupStats", "SourceCounters"]#, "SOL_Roffline"]

prof_results = {}
#graphs = ["4.txt", "4w.txt", "asia_osm.txt", "chesapeake.txt", "coAuthorsCiteseer.txt", "coAuthorsDBLP.txt", "coPapersCiteseer.txt", 
#          "coPapersDBLP.txt", "germany_osm.txt", "great-britain_osm.txt", "higgs-twitter.txt", "higgs-twitter_mention.txt", 
#          "higgs-twitter_reply.txt", "higgs-twitter_retweet.txt", "indochina-2004.txt", "italy_osm.txt", "min-1DeadEnd.txt", 
#          "socEpinions1.txt", "soc-LiveJournal1.txt", "socLiveJournal1.txt", "soc-Slashdot0811.txt", "soc-Slashdot0902.txt", 
#          "test_bc.txt", "test_cc.txt", "test_mst.txt", "test_pr.txt", "test_scc.txt", "test_sgd.txt", "test_small_scc.txt", 
#          "web-Google.txt", "web-NotreDame.txt", "web-Stanford.txt"]
#gardenia = ["bc_linear_base", "bc_linear_lb", "bc_topo_base", "bc_topo_lb", "bfs_linear_base", "bfs_linear_lb", "cc_afforest", 
#            "cc_base", "cc_warp", "mst_topo", "pr_base", "pr_warp", "spmv_base", "spmv_push", "spmv_vector", "spmv_warp",
#            "sssp_linear_base", "sssp_linear_lb", "vc_linear_base", "vc_linear_bitset"]
#gardenia_apps = {}
#gardenia_kernels = {} 
#for i in gardenia:
#  gardenia_apps[i] = {}
#  for j in graphs:
#    if not(i == 'mst_topo' and "indochina" in j):
#      kernels = count_total_kernel("Gardenia/" + i + '/' + j)
#      gardenia_apps[i][j[:len(j)-len(".txt")]] = collect_metrics(kernels, "Gardenia/" + i + '/' + j)
#  export_result_per_app(gardenia_apps[i], i, "Gardenia/" + i)
#prof_results["gardenia"] = gardenia_apps

#"adi" "fdtd2d"
#polybench = ["2DConvolution", "2mm", "3DConvolution", "3mm", "atax", "bicg", "correlation", 
#             "covariance", "doitgen", "gemm", "gemver", "gesummv", "jacobi1d", "jacobi2d", "lu", "mvt", "syr2k", "syrk"]
polybench = ["atax", "bicg", "correlation", "covariance", "gemver", "gesummv", "mvt"]
polybench_apps = {}
for i in polybench:
  polybench_apps[i] = {}
  kernels = count_total_kernel('PolyBench/' + i + '.txt')
  polybench_apps[i] = collect_metrics(kernels, 'PolyBench/' + i + '.txt')
export_result_per_app(polybench_apps, None, "PolyBench")
prof_results["polybench"] = polybench_apps


#rodinia = ["backrop", "bfs", "b+tree", "cfd_02M", "cfd_097K", "cfd_193K", "heartwall_40", "hotspot", 
#           "huffman", "hybridsort", "lavaMD", "lud_cuda", "nn", "nw", "pathfinder", "srad_v1", "srad_v2"]
#rodinia_apps = {}
#for i in rodinia:
#  rodinia_apps[i] = {}
#  kernels = count_total_kernel("Rodinia_3-1/" + i + '.txt')
#  print(i)
#  rodinia_apps[i] = collect_metrics(kernels, 'Rodinia_3-1/' + i + '.txt')
#export_result_per_app(rodinia_apps, None, "Rodinia_3-1")
#prof_results["rodinia"] = rodinia_apps

#for i in rodinia:
#  app_name = i[:len(i)-len(".txt")]
#  for j in range(0, len(rodinia_apps[app_name]["ids"])):
#    if rodinia_apps[app_name]["metrics"] != None and len(rodinia_apps[app_name]["metrics"]) != 0 and \
#       rodinia_apps[app_name]["metrics"][j] != None:
#      if rodinia_apps[app_name]["metrics"][j][11] < 40 and  rodinia_apps[app_name]["metrics"][j][12] < 40:
#        print(i)
#        print(rodinia_apps[app_name]["ids"][j])
#        print(rodinia_apps[app_name]["names"][j])
#        print(rodinia_apps[app_name]["metrics"][j])
#        print('\n')

#tango = ["alex_next.txt", "cifar_net.txt", "gru.txt", "lstm.txt", "res_net.txt", "squeeze_net.txt"]
#tango_apps = {}
#for i in tango:
#  tango_apps[i[:len(i)-len(".txt")]] = count_total_kernel("Tango/" + i)
#  tango_apps[i[:len(i)-len(".txt")]] = collect_metrics(tango_apps[i[:len(i)-len(".txt")]], "Tango/" + i)
#metrics["tango"] = tango_apps

#for i in tango:
#  app_name = i[:len(i)-len(".txt")]
#  for j in range(0, len(tango_apps[app_name]["ids"])):
#    if tango_apps[app_name]["metrics"] != None and len(tango_apps[app_name]["metrics"]) != 0 and \
#       tango_apps[app_name]["metrics"][j] != None:
#      if tango_apps[app_name]["metrics"][j][11] < 50 and tango_apps[app_name]["metrics"][j][12] < 50:
#        print(i)
#        print(tango_apps[app_name]["ids"][j])
#        print(tango_apps[app_name]["names"][j])
#        print(tango_apps[app_name]["metrics"][j])
#        print('\n')


# 0 "Elapsed Cycles"                # 10 "Max Bandwidth"
# 1 "Memory [%]"                    # 11 "L1/TEX Hit Rate"
# 2 "SOL DRAM"                      # 12 "L2 Hit Rate"
# 3 "SOL L1/TEX Cache"              # 13 "Mem Pipes Busy"
# 4 "SOL L2 Cache"                  # 14 "Warp Cycles Per Executed Instruction"
# 5 "SM Active Cycles"              # 15 "Block Size"
# 6 "SM [%]"                        # 16 "Grid Size"
# 7 "Executed Ipc Active"           # 17 "Shared Memory Configuration Size"
# 8 "SM Busy"                       # 18 "Waves Per SM",
# 9 "Mem Busy"                      # 19 "Achieved Occupancy"

#for i in gardenia:
#  for j in graphs:
#    app_name = i
#    data_name = j[:len(j)-len(".txt")]
#    for k in range(0, len(gardenia_apps[app_name][data_name]["ids"])):
#      if gardenia_apps[app_name][data_name]["metrics"] != None and len(gardenia_apps[app_name][data_name]["metrics"]) != 0 and \
#         gardenia_apps[app_name][data_name]["metrics"][k] != None:
#          if gardenia_apps[app_name][data_name]["metrics"][k][11] < 40 and gardenia_apps[app_name][data_name]["metrics"][k][12] < 40 and \
#             gardenia_apps[app_name][data_name]["metrics"][k][0] > 50000:
#            print(i + ' ------' + j)
#            print(gardenia_apps[app_name][data_name]["ids"][k])
#            print(gardenia_apps[app_name][data_name]["names"][k])
#            print(gardenia_apps[app_name][data_name]["metrics"][k])
#            print('\n')


#for i in polybench:
#  app_name = i[:len(i)-len(".txt")]
#  for j in range(0, len(polybench_apps[app_name]["ids"])):
#    if polybench_apps[app_name]["metrics"] != None and len(polybench_apps[app_name]["metrics"]) != 0 and \
#       polybench_apps[app_name]["metrics"][j] != None:
#      if polybench_apps[app_name]["metrics"][j][11] < 55 and polybench_apps[app_name]["metrics"][j][12] < 55 and \
#         polybench_apps[app_name]["metrics"][j][0] > 50000:
#        print(i)
#        print(polybench_apps[app_name]["ids"][j])
#        print(polybench_apps[app_name]["names"][j])
#        print(polybench_apps[app_name]["metrics"][j])
#        print('\n')
#
#export_metrics_to_csv(metrics)
