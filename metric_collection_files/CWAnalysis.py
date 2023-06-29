#    Section: Compute Workload Analysis
#    ---------------------------------------------------------------------- --------------- ------------------------------
#    Executed Ipc Active                                                         inst/cycle   0,07 +
#    Executed Ipc Elapsed                                                        inst/cycle   0,00 +
#    ADU                                                                                  %   2,23 +
#    CBU                                                                                  %   0,31 +
#    FP16                                                                                 %      0 +
#    FP64                                                                                 %      0 +
#    LSU                                                                                  %   2,51 +
#    Tensor (FP)                                                                          %      0 +
#    Tensor (INT)                                                                         %      0 +
#    TEX                                                                                  %      0 +
#    Uniform                                                                              %      0 +
#    XU                                                                                   %      0 +
#    Issue Slots Busy                                                                     %   2,41 +
#    Issued Ipc Active                                                           inst/cycle   0,10 +
#    sm__inst_issued.max.pct_of_peak_sustained_active                                     %  33,73 +
#    SM Busy                                                                              %   2,41 +
#    ALU                                                                                  %   1,26 +
#    FMA                                                                                  %   0,63 +
#    ---------------------------------------------------------------------- --------------- ------------------------------
#    WRN   All pipelines are under-utilized. Either this kernel is very small or it doesn't issue enough warps per       
#          scheduler. Check the Launch Statistics and Scheduler Statistics sections for further details.                 


CWAMetrics = ["ADU", "CBU", "FP16", "FP64", "LSU", "Tensor (FP)", "Tensor (INT)", "TEX",
              "Uniform","XU","ALU","FMA","Issue Slots Busy","Issued Ipc Active","SM Busy"]

def collect_CWAnalysis(metrics):
  cwametrics = {}
  for i in metrics:
    for j in CWAMetrics:
      if j in i:
        offset = len("    ---------------------------------------------------------------------- --------------- -")
        val = ''
        counter = 0
        string = i[offset:len(i)-1]
        while True:
          if counter == len(string):
            break
          if string[counter] != '.' and string[counter] != ',' and string[counter] != ' ':
            val += string[counter]
          if string[counter] == ',':
            val += '.'
          counter += 1
        cwametrics[j] = val
  return cwametrics
#  print("Collect Compute Workload Analysis Metrics")
    
