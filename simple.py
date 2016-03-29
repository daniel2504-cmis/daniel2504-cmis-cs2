#Math
import math

#Function Definition
def add(x,y):
	return int(x) + int(y)

def kiteperimeter(x,y):
	z = add(x,y)
	area = 2*z
	return area



#Output
def output(name, k1, k2, k):
	out = """
Hey {}
Did you know:
The kite perimeter will be 2({} + {}) = {}
""". format(name, k1, k2, k)
	return out

#Main
def main():
	#Input Section
	name = raw_input("What's your name?: ")
	k1 = raw_input("Kite first side: ")
	k2 = raw_input("kite second side: ")

	#Processing
	k = int(kiteperimeter(k1,k2))
	
	#Output
	out = output(name, k1, k2, k)
	print out

#Main Call
main()
