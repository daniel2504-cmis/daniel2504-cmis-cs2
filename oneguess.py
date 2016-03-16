#import
import math
import random

#Function Defition
def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def think(x,y):
	return random.randint(x,y)

def what():
	x = raw_input("What do you think it is?: ") 
	return x
	


def theflipman():
	minimum = raw_input("What is the minimum number?:")
	maximum = raw_input("What is the maximum number?:")
	return minimum, maximum

def mydays(): 
	Hmm = think(int(minimum), int(maximum))
	return """
	I'm thinking of a number from {} to {}.""". format(minimum, maximum)

def correcting(x):
	x = what()
	if x > think(int(minimum), int(maximum)):
		False
	elif x < think(int(minimum), int(maximum)):
		False
	else:
		return x
#Main
def main():
	#Input Section
	theflipman()
	print mydays
	reply = what()

	#Processing
	correcting(int(reply))

	#Output

	


#Call Main
main()
	
	


