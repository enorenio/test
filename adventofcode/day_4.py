import hashlib

i = 0
flag=0
while(flag==0):
	initial = "yzbqklnj"
	i+=1
	result = initial+str(i)
	hashres = hashlib.md5(result.encode('utf-8')).hexdigest()

	#print ("Hash: {0}  ,  {1}".format(hashres,i))
	#Success statement
	if(hashres.startswith("00000")):
		flag=1
		print (i)

#print(hashlib.md5("yzbqklnj".encode('utf-8')).hexdigest())
