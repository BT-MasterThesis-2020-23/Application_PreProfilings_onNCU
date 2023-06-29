'''
    Section: Instruction Statistics
    ---------------------------------------------------------------------- --------------- ------------------------------
                                                                                      inst                             53
                                                                                                                       53
    Avg. Executed Instructions Per Scheduler                                          inst                           0,95
    Avg. Issued Instructions Per Scheduler                                            inst                           1,23
    Executed Instructions                                                             inst                             53
    Issued Instructions                                                               inst                             69
    ---------------------------------------------------------------------- --------------- ------------------------------
'''
InstructionMetrics = ["Executed Instructions", "Issued Instructions"]

def collect_InstructionStats(metrics):
#  print("Collect Instruction Statistic Metrics")
  instructionMetrics = {}
  for i in metrics:
    for j in InstructionMetrics:
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
        instructionMetrics[j] = val
  return instructionMetrics
