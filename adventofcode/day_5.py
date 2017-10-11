file = open("day_5.txt","r")

def check_1(s):
	vovels = ['a', 'e', 'i', 'o', 'u']
	counter = 0
	for letter in s:
		for v in vovels:
			if(letter==v):
				counter+=1
	if counter>2:
		return True
	else:
		return False


def check_2(s):
	for i, c in enumerate(s):
		if i-1>=0:
			if (s[i-1]==s[i]):
				return True
	return False

def check_3(s):
	bads = ["ab", "cd", "pq", "xy"]
	for i, c in enumerate(s):
		for badword in bads:
			if (i+1<len(s) and (s[i]+s[i+1])==badword):
				return False
	return True

cns = 0
for s in file:
    if(check_1(s) and check_2(s) and check_3(s)):
        cns += 1
print(cns)