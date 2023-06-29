'''
    Section: Scheduler Statistics
    ---------------------------------------------------------------------- --------------- ------------------------------
    Instructions Per Active Issue Slot                                          inst/cycle                              1
    One or More Eligible                                                                 %                           2,63
    Issued Warp Per Scheduler                                                                                        0,03
    No Eligible                                                                          %                          97,37
    Eligible Warps Per Scheduler                                                      warp                           0,03
    ---------------------------------------------------------------------- --------------- ------------------------------
    WRN   Every scheduler is capable of issuing one instruction per cycle, but for this kernel each scheduler only      
          issues an instruction every 38.0 cycles. This might leave hardware resources underutilized and may lead to    
          less optimal performance. Out of the maximum of 8 warps per scheduler, this kernel allocates an average of    
          2.30 active warps per scheduler, but only an average of 0.03 warps were eligible per cycle. Eligible warps    
          are the subset of active warps that are ready to issue their next instruction. Every cycle with no eligible   
          warp results in no instruction being issued and the issue slot remains unused. To increase the number of      
          eligible warps either increase the number of active warps or reduce the time the active warps are stalled.    
'''


SchedulerStats = ["Theoretical Warps Per Scheduler", "Active Warps Per Scheduler"]

def collect_SchedulerStats(metrics):
  schedulerStats = {}
  for i in metrics:
    for j in SchedulerStats:
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
        schedulerStats[j] = val
  return schedulerStats
#  print("Collect Scheduler Statistics Metrics")