# Section: Memory Workload Analysis
# ---------------------------------------------------------------------- --------------- ------------------------------
# Memory Throughput                                                         Gbyte/second                           5,81
# Mem Busy                                                                             %                           3,13
# Max Bandwidth                                                                        %                           6,47
# L1/TEX Hit Rate                                                                      %                              0
# L2 Hit Rate                                                                          %                          41,20
# Mem Pipes Busy                                                                       %                           0,06
# ---------------------------------------------------------------------- --------------- ------------------------------

MWAMetrics = ["Memory Throughput", "Mem Busy", "Max Bandwidth", "L1/TEX Hit Rate", "L2 Hit Rate", "Mem Pipes Busy"]
def collect_MWAnalysis(metrics):
#  print("Collect Memory Workload Analysis Metrics")
  mwa = {}
  for i in metrics:
    for j in MWAMetrics:
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
        if ' Gbyte' in i:
          val += ' Gbyte'
        elif ' Mbyte' in i:
          val += ' Mbyte'
        elif ' Kbyte' in i:
          val += ' Kbyte'
        elif ' Byte' in i:
          val += ' Byte'
        elif ' byte' in i:
          val += ' Byte'
        mwa[j] = val
#  print(mwa)
  return mwa
