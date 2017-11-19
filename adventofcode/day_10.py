inp = "1113122113"
counter = 0
temp = ""
for i in range(40):
	for index, char in enumerate(inp):
		if(index>0 and(inp[index]!=inp[index-1])):
			temp+=str(counter)+inp[index-1]
			counter = 1
		else:
			counter+=1
		#print(index,str(len(inp)-1))
		if(str(index)==str(len(inp)-1)):
			temp+=str(counter)+inp[index]
			inp = temp
			temp = ""
			counter = 0
	print(len(inp))
print("---------")
print(len(inp))