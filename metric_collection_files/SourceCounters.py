'''
    stall_barrier                                                                     warp                              0
    stall_dispatch                                                                    warp                              0
    stall_drain                                                                       warp                              0
    stall_imc                                                                         warp                              0
    stall_lg                                                                          warp                              0
    stall_long_sb                                                                     warp                              0
    stall_math                                                                        warp                              0
    stall_membar                                                                      byte                              0
    stall_mio                                                                         warp                              0
    stall_misc                                                                        warp                              0
    stall_no_inst                                                                     inst                              0
    stall_not_selected                                                                warp                              0
    stall_selected                                                                    warp                              0
    stall_short_sb                                                                    warp                              0
    stall_sleep                                                                       warp                              0
    stall_tex                                                                         warp                              0
    stall_wait                                                                        warp                              0
    Predicated-On Thread Instructions Executed                                        inst                          1.592
    ---------------------------------------------------------------------- --------------- ------------------------------
'''

sourceMetrics = ["Memory Ideal L2 Transactions Global", "Memory Ideal L1 Transactions Shared", 
"Memory L1 Transactions Global", "Memory L2 Transactions Global", "Memory L2 Transactions Local","Memory L1 Transactions Shared", 
"stall_barrier  ", "stall_dispatch  ", "stall_drain  ", "stall_imc  ", "stall_lg  ", "stall_long_sb  ", "stall_math  ", 
"stall_membar  ", "stall_mio  ", "stall_misc  ", "stall_no_inst  ", "stall_not_selected  ", "stall_selected  ","stall_short_sb  ", 
"stall_sleep  ", "stall_tex  ",
"stall_wait  "]

def collect_SourceCounters(metrics):
  warpState = {}
  for i in metrics:
    for j in sourceMetrics:
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
        warpState[j] = val
  return warpState
#  print("collect Source Counter Metrics")