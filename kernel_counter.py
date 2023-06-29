def count_total_kernel(app_name):

  file = open(app_name, 'r')
  nof_lines = len(file.readlines())
  file.close()

  file = open(app_name, 'r')
  kernels = {"ids": [], "names": []}
  kid = 0
  for i in range(0, nof_lines):
    line = file.readline()
    if "==PROF== Disconnected from process" or "==ERROR==" in line:
      break

    if "==PROF== Profiling" in line:
      kernel_name =""
      counter = len("==PROF== Profiling  ")
      while True:
        if line[counter] != '"':
          kernel_name += line[counter]
        elif line[counter] == '"':
          break
        counter += 1
      kernels["ids"].append(kid)
      kernels["names"].append(kernel_name)
      kid += 1
    if kid > 50:
      break
  print(app_name)
  file.close()
  return kernels

