import xlsxwriter

def export_result_per_app(app, app_name, app_path):
  print(app_name)
  sections_1 = ["SOL", "CWA", "MWA", "MWA_Chart", "MWA_Table", "WarpStateStats", "SchedulerStats", 
              "InstStats", "LaunchStats", "OccupStats", "SourceCounters"]

  #"Section: GPU Speed Of Light Roofline Chart",
  sections_2 = ["Section: GPU Speed Of Light", "Section: Compute Workload Analysis", "Section: Memory Workload Analysis", 
                "Section: Memory Workload Analysis Chart", "Section: Memory Workload Analysis Tables", "Section: Warp State Statistics",
                "Section: Scheduler Statistics", "Section: Instruction Statistics", "Section: Launch Statistics", "Section: Occupancy", 
                "Section: Source Counters"]

  if "Gardenia" in app_path:
    graph_datasets = list(app.keys())
    workbook = xlsxwriter.Workbook(app_path + '/' + 'ProfRes.xlsx')
    for i in graph_datasets:
      kernels = list(app[i].keys())
      worksheet = workbook.add_worksheet(i)
      worksheet.write(0, 0, "Metrics/Kernels")
      for k in range(len(kernels)):
        worksheet.write(0, k + 2, kernels[k])
        last_row = 1
        for j in range(len(sections_1)):
          subsections = list(app[i][kernels[k]][sections_1[j]].keys())
          for x in range (len(subsections)):
            if k == 0:
              worksheet.write(last_row, 0, sections_2[j])
              worksheet.write(last_row, 1, subsections[x])
            worksheet.write(last_row, k + 2, app[i][kernels[k]][sections_1[j]][subsections[x]])
            last_row += 1
    workbook.close()
  elif "PolyBench" in app_path or "Rodinia" in app_path:
    workbook = xlsxwriter.Workbook(app_path + '/' + 'ProfRes.xlsx')
    apps = list(app.keys())
    for i in apps:
      kernels = list(app[i].keys())
      worksheet = workbook.add_worksheet(i)
      worksheet.write(0, 0, "Metrics/Kernels")
      for k in range(len(kernels)):
        worksheet.write(0, k + 2, kernels[k])
        last_row = 1
        for j in range(len(sections_1)):
          subsections = list(app[i][kernels[k]][sections_1[j]].keys())
          for x in range (len(subsections)):
            if k == 0:
              worksheet.write(last_row, 0, sections_2[j])
              worksheet.write(last_row, 1, subsections[x])
            worksheet.write(last_row, k + 2, app[i][kernels[k]][sections_1[j]][subsections[x]])
            last_row += 1
    workbook.close()


#  else:
#    workbook = xlsxwriter.Workbook(app_path + '/' + 'ProfRes.xlsx')
#    for i in graph_datasets:
#      kernels = list(app[i].keys())
#      worksheet = workbook.add_worksheet(i)
#      worksheet.write(0, 0, "Metrics/Kernels")
#      for k in range(len(kernels)):
#        worksheet.write(0, k + 2, kernels[k])
#        last_row = 1
#        for j in range(len(sections_1)):
#          subsections = list(app[i][kernels[k]][sections_1[j]].keys())
#          for x in range (len(subsections)):
#            if k == 0:
#              worksheet.write(last_row, 0, sections_2[j])
#              worksheet.write(last_row, 1, subsections[x])
#            worksheet.write(last_row, k + 2, app[i][kernels[k]][sections_1[j]][subsections[x]])
#            last_row += 1


def export_metrics_to_csv(benchmark_set):
  metrics_we_collect = ["Elapsed Cycles", "Memory [%]", "SOL DRAM", "SOL L1/TEX Cache", "SOL L2 Cache", "SM Active Cycles",
                      "SM [%]", "Executed Ipc Active", "SM Busy", "Mem Busy", "Max Bandwidth", "L1/TEX Hit Rate",
                      "L2 Hit Rate", "Mem Pipes Busy", "Warp Cycles Per Executed Instruction", "Block Size", "Grid Size",
                      "Shared Memory Configuration Size", "Waves Per SM", "Achieved Occupancy"]

  workbook = xlsxwriter.Workbook('benchmark_prof_results.xlsx')
  worksheet_rd = workbook.add_worksheet("rodinia_profs")
  merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})
  worksheet_rd.merge_range('D1:J1', 'GPU Speed Of Light', merge_format)
  worksheet_rd.merge_range('K1:L1', 'Compute Workload Analysis', merge_format)
  worksheet_rd.merge_range('M1:Q1', 'Memory Workload Analysis', merge_format)
  worksheet_rd.write('R1', 'Warp State Statistics', merge_format)
  worksheet_rd.merge_range('S1:V1', 'Launch Statistics', merge_format)
  worksheet_rd.write('W1', 'Occupancy', merge_format)

  for i in range(0,  len(metrics_we_collect)):
    worksheet_rd.write(1, 3 + i, metrics_we_collect[i], merge_format)    

  rodinia = ["backprop", "bfs", "b+tree", "hotspot", "huffman", "hybridsort", "lavaMD", "lud_cuda", 
             "nn", "nw", "particle_filter_float", "particle_filter_naive", "pathfinder", "srad_v1", "srad_v2"]
  count_kernel = 0
  for i in rodinia:
    for j in range(0, len(benchmark_set["rodinia"][i]["ids"])):
      worksheet_rd.write(j + count_kernel + 2, 0, i)
      worksheet_rd.write(j + count_kernel + 2, 1, benchmark_set["rodinia"][i]["ids"][j])
      worksheet_rd.write(j + count_kernel + 2, 2, benchmark_set["rodinia"][i]["names"][j])
      if benchmark_set["rodinia"][i]["metrics"] != None and len(benchmark_set["rodinia"][i]["metrics"]) != 0 and \
         benchmark_set["rodinia"][i]["metrics"][j] != None:
        for k in range(0, len(benchmark_set["rodinia"][i]["metrics"][j])):
          worksheet_rd.write(j + count_kernel + 2, k + 3, benchmark_set["rodinia"][i]["metrics"][j][k])
    count_kernel += len(benchmark_set["rodinia"][i]["ids"]) 


  worksheet_tn = workbook.add_worksheet("tango_profs")
  worksheet_tn.merge_range('D1:J1', 'GPU Speed Of Light', merge_format)
  worksheet_tn.merge_range('K1:L1', 'Compute Workload Analysis', merge_format)
  worksheet_tn.merge_range('M1:Q1', 'Memory Workload Analysis', merge_format)
  worksheet_tn.write('R1', 'Warp State Statistics', merge_format)
  worksheet_tn.merge_range('S1:V1', 'Launch Statistics', merge_format)
  worksheet_tn.write('W1', 'Occupancy', merge_format)
  for i in range(0,  len(metrics_we_collect)):
    worksheet_tn.write(1, 3 + i, metrics_we_collect[i], merge_format)    

  tango = ["alex_next", "cifar_net", "gru", "lstm", "res_net", "squeeze_net"]
  count_kernel = 0
  for i in tango:
    for j in range(0, len(benchmark_set["tango"][i]["ids"])):
      worksheet_tn.write(j + count_kernel + 2, 0, i)
      worksheet_tn.write(j + count_kernel + 2, 1, benchmark_set["tango"][i]["ids"][j])
      worksheet_tn.write(j + count_kernel + 2, 2, benchmark_set["tango"][i]["names"][j])
      if benchmark_set["tango"][i]["metrics"] != None and len(benchmark_set["tango"][i]["metrics"]) != 0 and \
         benchmark_set["tango"][i]["metrics"][j] != None:
        for k in range(0, len(benchmark_set["tango"][i]["metrics"][j])):
          worksheet_tn.write(j + count_kernel + 2, k + 3, benchmark_set["tango"][i]["metrics"][j][k])
    count_kernel += len(benchmark_set["tango"][i]["ids"]) 

  worksheet_pol = workbook.add_worksheet("polybench_profs")
  worksheet_pol.merge_range('D1:J1', 'GPU Speed Of Light', merge_format)
  worksheet_pol.merge_range('K1:L1', 'Compute Workload Analysis', merge_format)
  worksheet_pol.merge_range('M1:Q1', 'Memory Workload Analysis', merge_format)
  worksheet_pol.write('R1', 'Warp State Statistics', merge_format)
  worksheet_pol.merge_range('S1:V1', 'Launch Statistics', merge_format)
  worksheet_pol.write('W1', 'Occupancy', merge_format)
  for i in range(0,  len(metrics_we_collect)):
    worksheet_pol.write(1, 3 + i, metrics_we_collect[i], merge_format)    

  polybench = ["2DConvolution", "3mm", "correlation", "gemm", "mvt", "2mm", "atax", "covariance", 
               "gesummv", "syrk", "3DConvolution", "bicg", "fdtd2d", "gramschmidt"]
  count_kernel = 0
  for i in polybench:
    for j in range(0, len(benchmark_set["polybench"][i]["ids"])):
      worksheet_pol.write(j + count_kernel + 2, 0, i)
      worksheet_pol.write(j + count_kernel + 2, 1, benchmark_set["polybench"][i]["ids"][j])
      worksheet_pol.write(j + count_kernel + 2, 2, benchmark_set["polybench"][i]["names"][j])
      if benchmark_set["polybench"][i]["metrics"] != None and len(benchmark_set["polybench"][i]["metrics"]) != 0 and \
         benchmark_set["polybench"][i]["metrics"][j] != None:
        for k in range(0, len(benchmark_set["polybench"][i]["metrics"][j])):
          worksheet_pol.write(j + count_kernel + 2, k + 3, benchmark_set["polybench"][i]["metrics"][j][k])
    count_kernel += len(benchmark_set["polybench"][i]["ids"]) 


  graphs = ["4", "4w", "asia_osm_coord", "asia_osm", "chesapeake", "coAuthorsCiteseer", "coAuthorsDBLP", 
            "coPapersCiteseer", "coPapersDBLP", "germany_osm_coord", "germany_osm", "great-britain_osm_coord",                   
            "great-britain_osm", "higgs-twitter_mention", "web-BerkStan", "web-Google", "web-NotreDame", 
            "web-Stanford", "soc-Slashdot0902", "test_bc", "test_cc", "test_mst", "test_pr", "test_scc", 
            "test_sgd", "test_small_scc", "min-1DeadEnd", "min-2SCC", "min-4SCC", "min-NvgraphEx", 
            "soc-Epinions1","soc-LiveJournal1", "soc-Slashdot0811", "higgs-twitter_reply", "higgs-twitter_retweet", 
            "higgs-twitter_temporal_edges", "higgs-twitter", "italy_osm_coord", "italy_osm", "indochina-2004"]

  gardenia = ["bfs_linear_base", "mst_topo", "spmv_base", "vc_linear_base", "bc_linear_base", 
              "cc_base", "pr_base", "sssp_base"]

  worksheet = []
  app_counter = 0
  for i in gardenia:
    worksheet.append(workbook.add_worksheet("gard_" + i + "_poly"))
    worksheet[app_counter].merge_range('D1:J1', 'GPU Speed Of Light', merge_format)
    worksheet[app_counter].merge_range('K1:L1', 'Compute Workload Analysis', merge_format)
    worksheet[app_counter].merge_range('M1:Q1', 'Memory Workload Analysis', merge_format)
    worksheet[app_counter].write('R1', 'Warp State Statistics', merge_format)
    worksheet[app_counter].merge_range('S1:V1', 'Launch Statistics', merge_format)
    worksheet[app_counter].write('W1', 'Occupancy', merge_format)
    for xx in range(0,  len(metrics_we_collect)):
      worksheet[app_counter].write(1, 3 + xx, metrics_we_collect[xx], merge_format)    

    count_kernel = 0
    for j in graphs:
      for k in range(0, len(benchmark_set["gardenia"][i][j]["ids"])):
        worksheet[app_counter].write(k + count_kernel + 2, 0, j)
        worksheet[app_counter].write(k + count_kernel + 2, 1, benchmark_set["gardenia"][i][j]["ids"][k])
        worksheet[app_counter].write(k + count_kernel + 2, 2, benchmark_set["gardenia"][i][j]["names"][k])
        if benchmark_set["gardenia"][i][j]["metrics"] != None and len(benchmark_set["gardenia"][i][j]["metrics"]) != 0 and \
           benchmark_set["gardenia"][i][j]["metrics"][k] != None:
          for x in range(0, len(benchmark_set["gardenia"][i][j]["metrics"][k])):
            worksheet[app_counter].write(k + count_kernel + 2, x + 3, benchmark_set["gardenia"][i][j]["metrics"][k][x])
      count_kernel += len(benchmark_set["gardenia"][i][j]["ids"])
    app_counter += 1
  workbook.close()
  


