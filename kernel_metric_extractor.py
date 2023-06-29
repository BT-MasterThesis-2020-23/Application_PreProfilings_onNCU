from metric_collection_files.SOL import *
from metric_collection_files.GPU_SOL_Roofline import *
from metric_collection_files.CWAnalysis import *
from metric_collection_files.MWAnalysis import *
from metric_collection_files.MWAnalysisChart import *
from metric_collection_files.MWAnalysisTable import *
from metric_collection_files.SchedulerStats import *
from metric_collection_files.WarpStateStats import *
from metric_collection_files.InstructionStats import *
from metric_collection_files.LaunchStatistics import *
from metric_collection_files.Occupancy import *
from metric_collection_files.SourceCounters import *

sections = ["Section: GPU Speed Of Light", "Section: GPU Speed Of Light Roofline Chart", "Section: Compute Workload Analysis", 
            "Section: Memory Workload Analysis", "Section: Memory Workload Analysis Chart", "Section: Memory Workload Analysis Tables", 
            "Section: Scheduler Statistics", "Section: Warp State Statistics", "Section: Instruction Statistics", 
            "Section: Launch Statistics", "Section: Occupancy", "Section: Source Counters"]

def collect_per_kernel_metrics(arr, section):
  #if section == "Section: Compute Workload Analysis":
  #  for i in range(0, len(arr)):
  #    print(arr[i][:len(arr[i])-1])
  a = 1
#  print(len(sections))

#  results_starts_after = len("    ---------------------------------------------------------------------- --------------- ")
#  results = []
#  for i in range(0, len(arr)):
#    line = arr[i]
#    for j in metrics_we_collect:
#      if j in line:
#        line = arr[i][results_starts_after+3:-1]
#        element = ""
#        counter = 0
#        while True:
#          if len(line) == counter:
#            break
#          if line[counter] != ' ':
#            element += line[counter]
#          counter += 1
#
#        new_ele = ""
#        counter = 0
#        while True:
#          if counter == len(element):
#            break
#          if element[counter] != '.' and element[counter] != ',':
#            new_ele += element[counter]
#          if element[counter] == ',':
#            new_ele += '.'
#          counter += 1
#        if 'n/a' in new_ele:
#          break
#        results.append(float(new_ele))
#
#  if len(metrics_we_collect) == len(results):
#    return results

# 0-th index -> ids ... 0,1,2,3..
# 1-st index -> names ... a,b,c
def collect_metrics(app_file, filename):   

  overall_metrics = {}
  with open(filename, "r") as fp:
    line = fp.readline()
    while "Disconnected from process" not in line:
      if "==ERROR==" in line:
        break
      line = fp.readline()

    curr_kname = ''
    for line in fp:
      if "Context" in line and "Stream" in line:
        kname = ''
        counter = 0
        while True:
          if line[counter] != ' ' and line[counter] != '(':
            kname += line[counter]
          if line[counter] == '(' or ',':
            break
          counter += 1
        if len(kname) > 60:
          kname = "Other_" + str(len(overall_metrics))
          overall_metrics[kname] = {}
        
        if kname in overall_metrics and "Other" not in kname:
          counter = 1
          old_kname = kname
          while kname in overall_metrics:
            kname = old_kname
            kname = kname + "_" + str(counter)
            counter += 1
        overall_metrics[kname] = {}
        curr_kname = kname
      if line[4:len(line)-1] in sections:
        curr_sec = line[4:len(line)-1]
        metrics = []
        counter = 0
        while True:
          crr_line = fp.readline()
          if "----------------------------------------------------------------------" in crr_line:
            counter += 1
          else:
            metrics.append(crr_line)
          if counter == 2:
            break

        if curr_sec == "Section: GPU Speed Of Light": 
          overall_metrics[curr_kname]["SOL"] = collect_SOL(metrics)
        elif curr_sec == "Section: Compute Workload Analysis":
          overall_metrics[curr_kname]["CWA"] = collect_CWAnalysis(metrics)
        elif curr_sec == "Section: Memory Workload Analysis":
          overall_metrics[curr_kname]["MWA"] = collect_MWAnalysis(metrics)
        elif curr_sec == "Section: Memory Workload Analysis Chart":
          overall_metrics[curr_kname]["MWA_Chart"] = collect_MWAnalysisChart(metrics)
        elif curr_sec == "Section: Memory Workload Analysis Tables":
          overall_metrics[curr_kname]["MWA_Table"] = collect_MWAnalysisTable(metrics)
        elif curr_sec == "Section: Warp State Statistics":
          overall_metrics[curr_kname]["WarpStateStats"] = collect_WarpStateStats(metrics)
        elif curr_sec == "Section: Scheduler Statistics": 
          overall_metrics[curr_kname]["SchedulerStats"] = collect_SchedulerStats(metrics)
        elif curr_sec == "Section: Instruction Statistics":
          overall_metrics[curr_kname]["InstStats"] = collect_InstructionStats(metrics)
        elif curr_sec == "Section: Launch Statistics":
          overall_metrics[curr_kname]["LaunchStats"] = collect_LaunchStatistics(metrics)
        elif curr_sec == "Section: Occupancy":
          overall_metrics[curr_kname]["OccupStats"] = collect_Occupancy(metrics)
        elif curr_sec == "Section: Source Counters":
          overall_metrics[curr_kname]["SourceCounters"] = collect_SourceCounters(metrics)
        elif curr_sec == "Section: GPU Speed Of Light Roofline Chart":
          overall_metrics[curr_kname]["SOL_Roffline"] = collect_GPU_SOL_Roofline(metrics)
#  print(len(sections), counter)
#    if "Section: GPU Speed Of Light" in line:
#      arr = []
#      while True:
#        line = file.readline()
#        if "Achieved Active Warps Per SM" in line:
#          arr.append(line)
#          break
#        else:
#          arr.append(line)
#      app_file["metrics"].append(collect_per_kernel_metrics(arr))

#      results = collect_per_kernel_metrics(arr)
#      if len(results) == len(metrics_we_collect):
#      else:
#        app_file["metrics"].append(None)
#  print(app_file)
  return overall_metrics

