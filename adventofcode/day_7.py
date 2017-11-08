import os
myfile = open("day_7.txt","r")

list_1 = myfile.read().splitlines()
list_2 = list()
variables = {}

def check_type (command):
	print(command)
	cmd = "unknown"
	if (("OR" in command) or ("AND" in command) or ("LSHIFT" in command) or ("RSHIFT" in command)):
		cmd = command[1]
	elif ("NOT" in command):
		cmd = command[0]
	else:
		cmd = "ASSIGN"
	return cmd

i = 0
j = 0
while(len(list_1) != 0):
	print ("i:",i)
	print ("j:",j)
	words = list_1[i].split()
	cmd_type = check_type(words)
	if(cmd_type == "unknown"):
		raise NameError("Bad command parsing, senpai")

	### Try to assemble
	if(cmd_type == "ASSIGN"):
		print ("assembling ASSIGN")
		if(words[0].isdigit()):
			variables.update([(words[2],int(words[0]))])

			list_2.append(list_1[i])
			del list_1[i]
			print(len(list_1), len(list_2))
			j+=1
			print ("success")
		else:
			print ("Senpai, they assign not number!")
			variables.update([(words[2],variables.get(words[0]))])
			print ("a=",variables.get(words[0]))
			i+=1
			#os.system("pause")
			continue
		print(variables)
		#os.system("pause")
	elif(cmd_type == "OR"):
		if  (
			(variables.get(words[0])!=None and variables.get(words[2])!=None)or
			(variables.get(words[0])!=None and words[2].isdigit())or
			(words[0].isdigit() and variables.get(words[2])!=None)or
			(words[0].isdigit() and words[2].isdigit())
		    ):
			if (variables.get(words[0])!=None and variables.get(words[2])!=None):
				variables.update([(words[4],variables.get(words[0])|variables.get(words[2]))])
			elif (variables.get(words[0])!=None and words[2].isdigit()):
				variables.update([(words[4],variables.get(words[0])|int(words[2]))])
			elif (words[0].isdigit() and variables.get(words[2])!=None):
				variables.update([(words[4],int(words[0])|variables.get(words[2]))])
			elif (words[0].isdigit() and words[2].isdigit()):
				variables.update([(words[4],int(words[0])|int(words[2]))])

			list_2.append(list_1[i])
			del list_1[i]
			print(len(list_1), len(list_2))
			j+=1
			print("success")
		else:
			print ("Cannot do OR operation, senpai")
			i+=1
			#os.system("pause")

		print ("assembling OR")
	elif(cmd_type == "AND"):
		if  (
			(variables.get(words[0])!=None and variables.get(words[2])!=None)or
			(variables.get(words[0])!=None and words[2].isdigit())or
			(words[0].isdigit() and variables.get(words[2])!=None)or
			(words[0].isdigit() and words[2].isdigit())
		    ):
			if (variables.get(words[0])!=None and variables.get(words[2])!=None):
				variables.update([(words[4],variables.get(words[0])&variables.get(words[2]))])
			elif (variables.get(words[0])!=None and words[2].isdigit()):
				variables.update([(words[4],variables.get(words[0])&int(words[2]))])
			elif (words[0].isdigit() and variables.get(words[2])!=None):
				variables.update([(words[4],int(words[0])&variables.get(words[2]))])
			elif (words[0].isdigit() and words[2].isdigit()):
				variables.update([(words[4],int(words[0])&int(words[2]))])

			list_2.append(list_1[i])
			del list_1[i]
			print(len(list_1), len(list_2))
			j+=1
			print("success")
		else:
			print ("Cannot do AND operation, senpai")
			i+=1
			#os.system("pause")

		print ("assembling AND")
	elif(cmd_type == "LSHIFT"):
		if  (
			(variables.get(words[0])!=None and variables.get(words[2])!=None)or
			(variables.get(words[0])!=None and words[2].isdigit())or
			(words[0].isdigit() and variables.get(words[2])!=None)or
			(words[0].isdigit() and words[2].isdigit())
		    ):
			if (variables.get(words[0])!=None and variables.get(words[2])!=None):
				variables.update([(words[4],variables.get(words[0])<<variables.get(words[2]))])
			elif (variables.get(words[0])!=None and words[2].isdigit()):
				variables.update([(words[4],variables.get(words[0])<<int(words[2]))])
			elif (words[0].isdigit() and variables.get(words[2])!=None):
				variables.update([(words[4],int(words[0])<<variables.get(words[2]))])
			elif (words[0].isdigit() and words[2].isdigit()):
				variables.update([(words[4],int(words[0])<<int(words[2]))])

			list_2.append(list_1[i])
			del list_1[i]
			print(len(list_1), len(list_2))
			j+=1
			print("success")
		else:
			print ("Cannot do LSHIFT operation, senpai")
			i+=1
			#os.system("pause")

		print ("assembling LSHIFT")
	elif(cmd_type == "RSHIFT"):
		if  (
			(variables.get(words[0])!=None and variables.get(words[2])!=None)or
			(variables.get(words[0])!=None and words[2].isdigit())or
			(words[0].isdigit() and variables.get(words[2])!=None)or
			(words[0].isdigit() and words[2].isdigit())
		    ):
			if (variables.get(words[0])!=None and variables.get(words[2])!=None):
				variables.update([(words[4],variables.get(words[0])>>variables.get(words[2]))])
			elif (variables.get(words[0])!=None and words[2].isdigit()):
				variables.update([(words[4],variables.get(words[0])>>int(words[2]))])
			elif (words[0].isdigit() and variables.get(words[2])!=None):
				variables.update([(words[4],int(words[0])>>variables.get(words[2]))])
			elif (words[0].isdigit() and words[2].isdigit()):
				variables.update([(words[4],int(words[0])>>int(words[2]))])

			list_2.append(list_1[i])
			del list_1[i]
			print(len(list_1), len(list_2))
			j+=1
			print("success")
		else:
			print ("Cannot do RSHIFT operation, senpai")
			i+=1
			#os.system("pause")

		print ("assembling RSHIFT")
	elif(cmd_type == "NOT"):
		if((variables.get(words[1])!=None)or(words[1].isdigit())):
			#print(variables.get(words[0]), variables.get(words[2]), words[0].isdigit(), words[2].isdigit())
			print(variables.get(words[1]), words[1].isdigit())
			if (variables.get(words[1])!=None):
				variables.update([(words[3],65535-variables.get(words[1]))])
			elif (words[1].isdigit()):
				variables.update([(words[3],65535-int(words[1]))])

			list_2.append(list_1[i])
			del list_1[i]
			print(len(list_1), len(list_2))
			j+=1
			print("success")
		else:
			print ("Cannot do NOT operation, senpai")
			i+=1
			#os.system("pause")

		print ("assembling NOT")

	if(i+j==339):
		i = 0

myfile.close()