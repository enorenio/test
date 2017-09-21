"""
Binary search algorithm
Input: list >> searchable variable
"""

def bs(lst, x):
	lb = 0
	ub = len(lst)
	while lb != ub:
		cv = (lb + ub)//2
		if x == lst[cv]:
			return x
		elif x < lst[cv]:
			ub = cv
		else:
			lb = cv+1
	return None

"""
An example of work
"""

#lst = sorted([int(x) for x in input().split()])
#x = int(input())
#print (bs(lst,x))
