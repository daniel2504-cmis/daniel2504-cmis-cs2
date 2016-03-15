#import
import math
import random

#Function Defition
def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def think(x,y):
	return random.radint(x,y)

def what(x):
	x = return_input("What do you think it is?: x")
	return x
#Output
def output():
	out = """
I'm thinking of a number from {} to {}.

The target was {}.
Your guess was {}.
That's under by {}""".format()

#Main
def main():
	#Input Section
	minimum = raw_input("What is the minimum number?:")
	maximum = raw_input("What is the maximum number?:")

	#Processing
	Hmm = think(int(minimum), int(maximum))
	what(x)
	
	#Output
	out = output()
	print out


#Call Main
main()
	
	


