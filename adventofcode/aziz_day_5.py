file = open("day_5.txt", 'r')

def check1(s):
  vovels = ['a', 'e', 'i', 'o', 'u']
  counter = 0;
  for c in s:
    for v in vovels:
      if(c == v):
        counter += 1
  if(counter > 2):
    return True
  else:
    return False

def check2(s):
  last = ''
  for c in s:
    if(c == last):
      return True
    last = c
  return False

def check3(s):
  banned = ["ab", "cd", "pq", "xy"]
  for i, c in enumerate(s):
    for st in banned:
      if(i+1<len(s) and (c + s[i+1]) == st):
          return False
  return True


c = 0
for s in file:
    if(check1(s) and check2(s) and check3(s)):
        c += 1
print(c)