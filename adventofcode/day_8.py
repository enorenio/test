import os
myfile = open("day_8.txt","r")

lis = myfile.read().splitlines()
lis2 = list()
first = 0
second = 0
T_total = 0
for i, j in enumerate(lis):
	stri = ""
	ascii = 0
	T_counter = 4
	for u, k in enumerate(lis[i]):
		if(u>0 and lis[i][u-1]=="\\" and lis[i][u]=="x"):
			ascii+=3
			stri=stri[:-1]
			stri+=lis[i][u-1]
			stri+=lis[i][u]
			T_counter+=1
			continue
		if(u>0 and lis[i][u-1]=="\\" and lis[i][u]=="\\"):
			lis[i] = lis[i][:u] + '0' + lis[i][u+1:]
			stri=stri[:-1]
			stri+=k
			T_counter+=2
			continue
		if (u>0 and lis[i][u-1]=="\\" and lis[i][u]=="\""):
			stri=stri[:-1]
			stri+=k
			T_counter+=2
			continue
		if (u!=0 and u+1!=len(lis[i])):
			stri+=k
			continue
		#print (lis[i][u],u)
		
	lis2.append(stri)
	del stri
	first += len(lis[i])
	second += len(lis2[i])-ascii
	T_total += T_counter

	print (len(lis[i])," ",len(lis2[i])-ascii, " ", lis[i], " ", lis2[i])
print (first)
print (second)
print("Part 1: ", first-second)
print ("Part 2:",T_total)

myfile.close()