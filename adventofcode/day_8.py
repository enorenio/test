import os
myfile = open("day_8.txt","r")

strings = myfile.read().splitlines()

i = 0
while(i<len(strings)):
	print(strings[i].count())
	i+=1



myfile.close()
