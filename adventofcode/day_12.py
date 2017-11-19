import json
from pprint import pprint

summ = 0
j = 0
with open('day_12.json') as data_file:    
    data = json.load(data_file)
for i in data:
	print(j,":: ",i)
	j+=1
pprint(data)
print(summ)