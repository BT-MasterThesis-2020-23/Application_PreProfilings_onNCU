
SOLMetrics = [
"sm__inst_executed.avg", "sm__inst_executed_pipe_adu", "sm__inst_executed_pipe_cbu_pred_on_any", "sm__inst_executed_pipe_fp16", 
"sm__inst_executed_pipe_ipa", "sm__inst_executed_pipe_lsu", "sm__inst_executed_pipe_tex", "sm__inst_executed_pipe_uniform", 
"sm__inst_executed_pipe_xu", "DRAM Frequency", "SM Frequency", "Elapsed Cycles", "Memory [%]", "SOL DRAM", "Duration", 
"SOL L1/TEX Cache", "Waves Per SM", "SOL L2 Cache", "SM Active Cycles", "SM [%]"]

def collect_SOL(metrics):

  #print("Collect Speed Of Light Detailed Metrics")
  sol_detailed = {}
  for i in metrics:
    for j in SOLMetrics:
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
        sol_detailed[j] = val
  return sol_detailed


