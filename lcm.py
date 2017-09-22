"""
Simpliest lcm algorithm
Input: int >> int
"""


from gcd import gcd

def lcm (a, b):
	return a // gcd (a, b) * b


"""
An example of work
"""

#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#LCM=lcm(a,b)
#print("LCM is: ")
#print(LCM)