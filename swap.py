def swap(a,b):
	a = a^b
	b = a^b
	a = a^b
	return [a,b]


#realization
if __name__ == '__main__':
	x = int(input())
	y = int(input())
	swap(x,y)
	print(swap(x,y))