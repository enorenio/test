"""
Simpliest gcd algorithm
Input: int >> int
"""

def gcd (a, b):
	if b==0:
		return a
	else:
		return gcd(b, a%b)

"""
An example of work
"""

#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#GCD=gcd(a,b)
#print("GCD is: ")
#print(GCD)