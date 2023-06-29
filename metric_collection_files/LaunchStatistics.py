'''
    Section: Launch Statistics
    ----------------------------------------------------------------- -------
    Block Size                                                            256
    Grid Size                                                               1
    Registers Per Thread                              register/thread      16
    Shared Memory Configuration Size                            Kbyte   32,77
    Driver Shared Memory Per Block                         byte/block       0
    Dynamic Shared Memory Per Block                        byte/block       0
    Static Shared Memory Per Block                         byte/block       0
    Threads                                                    thread     256
    Waves Per SM                                                         0,02
    sm__maximum_warps_per_active_cycle_pct                          %     100
    sm__warps_active.avg.pct_of_peak_sustained_active               %   23,24 cumulative # of warps in flight
    ----------------------------------------------------------------- -------
    WRN   The grid for this launch is configured to execute only 1 blocks, which is less than the GPU's 14              
          multiprocessors. This can underutilize some multiprocessors. If you do not intend to execute this kernel      
          concurrently with other workloads, consider reducing the block size to have at least one block per            
          multiprocessor or increase the size of the grid to fully utilize the available hardware resources.            
'''

KernelLaunchMetrics = ["Block Size", "Grid Size", "Threads", "Waves Per SM", "sm__maximum_warps_per_active_cycle_pct",
                       "sm__warps_active"]

def collect_LaunchStatistics(metrics):
  data = {}
  for i in range(len(metrics)):
    for j in KernelLaunchMetrics:
      if j in metrics[i]:
        offset = len("---------------------------------------------------------------------- --------------- ----")
        string = metrics[i][offset:len(metrics[i])-1]
        counter = 0
        while string[counter] == ' ':
          counter += 1

        string = string[counter:]
        counter = 0
        new_str = ''
        while True:
          if counter == len(string):
            break
          if string[counter] != '.' and string[counter] != ',':
            new_str += string[counter]
          if string[counter] == ',':
            new_str += '.'
          counter += 1
        data[j] = new_str
  return data
