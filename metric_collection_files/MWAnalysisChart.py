'''
    Section: Memory Workload Analysis Chart
    ---------------------------------------------------------------------- --------------- ------------------------------
    dram__bytes_read.sum                                                             Kbyte                           2,59
    dram__bytes_write.sum                                                            Kbyte                              8
    l1tex__data_pipe_lsu_wavefronts_mem_shared_cmd_read.sum                                                             0
    l1tex__data_pipe_lsu_wavefronts_mem_shared_cmd_write.sum                                                            0
    l1tex__m_l1tex2xbar_write_bytes.sum                                               byte                             64
    l1tex__m_xbar2l1tex_read_bytes.sum                                                byte                              0
    l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum                              request                              0
    l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum                                request                              0
    l1tex__t_requests_pipe_lsu_mem_global_op_red.sum                               request                              0
    l1tex__t_requests_pipe_lsu_mem_global_op_st.sum                                request                              1
    l1tex__t_requests_pipe_lsu_mem_local_op_ld.sum                                 request                              0
    l1tex__t_requests_pipe_lsu_mem_local_op_st.sum                                 request                              0
    l1tex__t_requests_pipe_tex_mem_surface_op_atom.sum                             request                              0
    l1tex__t_requests_pipe_tex_mem_surface_op_ld.sum                               request                              0
    l1tex__t_requests_pipe_tex_mem_surface_op_red.sum                              request                              0
    l1tex__t_requests_pipe_tex_mem_surface_op_st.sum                               request                              0
    l1tex__t_requests_pipe_tex_mem_texture.sum                                     request                              0
    l1tex__t_sector_hit_rate.pct                                                         %                              0
    lts__t_sector_hit_rate.pct                                                           %                          41,20
    lts__t_sectors_srcunit_tex_aperture_sysmem_op_read.sum                          sector                              0
    lts__t_sectors_srcunit_tex_aperture_sysmem_op_write.sum                         sector                              0
    sass__inst_executed_global_loads                                                  inst                              0
    sass__inst_executed_global_stores                                                 inst                              1
    sass__inst_executed_local_loads                                                   inst                              0
    sass__inst_executed_local_stores                                                  inst                              0
    sass__inst_executed_shared_loads                                                  inst                              0
    sass__inst_executed_shared_stores                                                 inst                              0
    smsp__inst_executed_op_generic_atom_dot_alu.sum                                   inst                              0
    smsp__inst_executed_op_generic_atom_dot_cas.sum                                   inst                              0
    smsp__inst_executed_op_global_red.sum                                             inst                              0
    smsp__inst_executed_op_shared_atom.sum                                            inst                              0
    smsp__inst_executed_op_surface_atom_dot_alu.sum                                   inst                              0
    smsp__inst_executed_op_surface_atom_dot_cas.sum                                   inst                              0
    smsp__inst_executed_op_surface_ld.sum                                             inst                              0
    smsp__inst_executed_op_surface_red.sum                                            inst                              0
    smsp__inst_executed_op_surface_st.sum                                             inst                              0
    smsp__inst_executed_op_texture.sum                                                inst                              0
    ---------------------------------------------------------------------- --------------- ------------------------------
'''
MWAChartMetrics = [
  "dram__bytes_read.sum ", "dram__bytes_write.sum ", "l1tex__data_pipe_lsu_wavefronts_mem_shared_cmd_read", 
  "l1tex__data_pipe_lsu_wavefronts_mem_shared_cmd_write", "l1tex__m_l1tex2xbar_write_bytes", "l1tex__m_xbar2l1tex_read_bytes", 
  "l1tex__t_requests_pipe_lsu_mem_global_op_ld", "l1tex__t_requests_pipe_lsu_mem_global_op_st", 
  "l1tex__t_requests_pipe_lsu_mem_local_op_ld", "l1tex__t_requests_pipe_lsu_mem_local_op_st", 
  "sass__inst_executed_global_loads", "sass__inst_executed_global_stores", "sass__inst_executed_local_loads", 
  "sass__inst_executed_local_stores", "sass__inst_executed_shared_loads", "sass__inst_executed_shared_stores"
]

def collect_MWAnalysisChart(metrics):
#  print("Collect Memory Workload Analysis Chart Metrics")
  mwachart = {}
  for i in metrics:
    for j in MWAChartMetrics:
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
        mwachart[j] = val
  return mwachart

