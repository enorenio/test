file = open('day_8.txt', 'r')



g_total=0
g_real=0
for line in file:
  total = 0
  real = 0
  for idx, ch in enumerate(line):
    real = real + 1
    total = total + 1
    next_idx = idx + 1
    if next_idx<len(line):
      if ch == "\\" and line[next_idx] == "\"":
        if next_idx+1!=len(line):
          real = real - 1
      if ch == "\\" and line[next_idx] == "\\":
        if idx-1>0 and idx-1 != "\\":
          real = real - 1
      if ch == "\\" and line[next_idx] == "x":
        if idx-1>0 and line[idx-1] != "\\":
          real = real - 3
  g_total = g_total + total
  g_real = g_real + real - 2 
print(g_total - g_real)