file = open("day_2.txt","r")
content = file.read()

values = content.split("\n")

total = 0
atotal = 0
for a in values:
	asd = a.split("x")
	l = int(asd[0])
	h = int(asd[1])
	w = int(asd[2])
	total+= 2*l*w + 2*w*h + 2*h*l + min(min(l*w,w*h),min(w*h,h*l))

	mins = [0,0,0]
	if(l>w and l>h):
		mins[0]=l
		mins[1]=w
		mins[2]=h
	if(w>l and w>h):
		mins[0]=w
		mins[1]=l
		mins[2]=h
	if(h>l and h>w):
		mins[0]=h
		mins[1]=l
		mins[2]=w

	atotal+= 2*l + 2*h + l*h*w
print(total)
print(atotal)
print(total+atotal)