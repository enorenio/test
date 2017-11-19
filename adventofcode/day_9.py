from itertools import permutations

combos = {}
luust = []
miny = 0
with open("day_9.txt", "r") as myfile:
    for line in myfile.read().splitlines():
      line = line.split(" ")
      if (line[0] not in luust):
        luust.append(line[0])
      if (line[2] not in luust):
        luust.append(line[2])
      city1 = line[0]
      city2 = line[2]
      distance = line[4]
      combos[city1 + " " + city2] = distance
    for permutation in permutations(luust):
      suum = 0
      for i,tupl in enumerate(permutation):
        if i>0:
          if permutation[i-1]+ " " + permutation[i] in combos:
            suum+=int(combos[permutation[i-1]+ " " + permutation[i]])
          else:
            suum+=int(combos[permutation[i]+ " " + permutation[i-1]])
          if i==7:
            miny = max(miny,suum)
print(miny)
