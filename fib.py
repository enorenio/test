"""
Fibonacci numbers algorithms
"""


def fib_recursive(n):
	if n<2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fib_classic(n):
	f = [1 for x in range(n)]
	for i in range(2,n):
		f[i] = f[i-1] + f[i-2]
	print(f[i])

def fib_py(n):
	a = 0
	b = 1
	for __ in range(n):
		a, b = b, a + b
	return a


"""
An example of work
"""
if __name__ == '__main__':
	n = int(input())
	print(fib_py(n))