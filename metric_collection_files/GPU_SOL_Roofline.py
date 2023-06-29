
# Section: GPU Speed Of Light Roofline Chart
# ---------------------------------------------------------------------- --------------- ------------------------------
# dram__bytes.sum.peak_sustained                              byte/cycle    128
# dram__bytes.sum.per_second                                Gbyte/second   5,81
# dram__cycles_elapsed.avg.per_second                      cycle/nsecond  16,70
# sm__cycles_elapsed.avg.per_second                        cycle/nsecond   1,14
# sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_s    inst/cycle     28
# sm__sass_thread_inst_executed_op_ffma_pred_on.sum.peak_s    inst/cycle    896
# smsp__cycles_elapsed.avg.per_second                      cycle/nsecond   1,14
# smsp__sass_thread_inst_executed_op_dadd_pred_on.sum.per_    inst/cycle      0 # of DADD thread instructions executed where all predicates were true
# smsp__sass_thread_inst_executed_op_dfma_pred_on.sum.per_    inst/cycle      0
# smsp__sass_thread_inst_executed_op_dmul_pred_on.sum.per_    inst/cycle      0
# smsp__sass_thread_inst_executed_op_fadd_pred_on.sum.per_    inst/cycle      0
# smsp__sass_thread_inst_executed_op_ffma_pred_on.sum.per_    inst/cycle      0
# smsp__sass_thread_inst_executed_op_fmul_pred_on.sum.per_    inst/cycle      0
# ---------------------------------------------------------------------- --------------- ------------------------------
# OK    The ratio of peak float (fp32) to double (fp64) performance on this device is 32:1. The kernel achieved 0% of 
#       this device's fp32 peak performance and 0% of its fp64 peak performance.                                      




def collect_GPU_SOL_Roofline(metrics):
  a = 1
  #print("collect GPU SOL Roofline Metrics")