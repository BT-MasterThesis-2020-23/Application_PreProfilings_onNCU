'''
    Section: Warp State Statistics
    ---------------------------------------------------------------------- --------------- ------------------------------
    Stall Barrier                                                                     inst                              0
    Stall Dispatch Stall                                                              inst                              0
    Stall Drain                                                                       inst                           0,52
    Stall IMC Miss                                                                    inst                          62,23
    Stall LG Throttle                                                                 inst                              0
    Stall Long Scoreboard                                                             inst                              0
    Stall Math Pipe Throttle                                                          inst                              0
    Stall Membar                                                                      inst                              0
    Stall MIO Throttle                                                                inst                              0
    Stall Misc                                                                        inst                           0,04
    Stall No Instruction                                                              inst                           2,61
    Stall Not Selected                                                                inst                           0,03
    Selected                                                                          inst                              1
    Stall Short Scoreboard                                                            inst                           2,72
    Stall Sleeping                                                                    inst                              0
    Stall Tex Throttle                                                                inst                              0
    Stall Wait                                                                        inst                           4,55
    smsp__issue_active.avg.per_cycle_active                                                                          0,03
    Avg. Active Threads Per Warp                                                                                    30,30
    Avg. Not Predicated Off Threads Per Warp                                                                        30,04
    ---------------------------------------------------------------------- --------------- ------------------------------
'''

WarpStateMetrics = ["Warp Cycles Per Issued Instruction", "Warp Cycles Per Executed Instruction", "Stall Barrier", "Stall Dispatch Stall", "Stall Drain", 
                    "Stall IMC Miss", "Stall LG Throttle", "Stall Long Scoreboard", "Stall Math Pipe Throttle", "Stall Membar", 
                    "Stall MIO Throttle", "Stall Misc", "Stall No Instruction", "Stall Not Selected", "Selected", "Stall Short Scoreboard", 
                    "Stall Sleeping", "Stall Tex Throttle", "Stall Wait",
]

def collect_WarpStateStats(metrics):
  warpState = {}
  for i in metrics:
    for j in WarpStateMetrics:
      if j in i:
        offset = len("    ---------------------------------------------------------------------- --------------- -")
        val = ''
        counter = 0
        string = i[offset:]
        while True:
          if counter == len(string):
            break
          if string[counter] != '.' and string[counter] != ',' and string[counter] != ' ':
            val += string[counter]
          if string[counter] == ',':
            val += '.'
          counter += 1
        warpState[j] = val
  return warpState
  print("Collect Warp state statistics")