'''
    Section: Occupancy
    ---------------------------------------------------------------------- --------------- ------------------------------
    Block Size                                                                                                        256
    Block Limit SM                                                                   block                             16
    Block Limit Registers                                                            block                             16
    Block Limit Shared Mem                                                           block                             16
    Block Limit Warps                                                                block                              4
    Warp Occupancy                                                                                                  1.698
    Warp Occupancy                                                                                                  4.256
    Warp Occupancy                                                                                                  1.904
    Registers Per Thread                                                   register/thread                             16
    Shared Memory Per Block                                                     byte/block                              0
    Theoretical Active Warps per SM                                                   warp                             32
    Theoretical Occupancy                                                                %                            100
    Achieved Occupancy                                                                   %                          23,24
    Achieved Active Warps Per SM                                                      warp                           7,44
    ---------------------------------------------------------------------- --------------- ------------------------------
'''
OccupancyMetrics = ["Theoretical Active Warps per SM", "Theoretical Occupancy", "Achieved Occupancy", "Achieved Active Warps Per SM"]

def collect_Occupancy(metrics):
  data = {}
  for i in range(len(metrics)):
    for j in OccupancyMetrics:
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
