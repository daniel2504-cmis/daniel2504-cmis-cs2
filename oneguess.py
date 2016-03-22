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

def output(answer, guess, tada):
	output = """
The target was {}.
Your guess was {}.
That's under by {}.""". format(answer,guess,tada)
	return output
	
	


#Main
def main():
	#Input Section
	minimum = raw_input("What is the minimum number?:")
	maximum = raw_input("What is the maximum number?:")
	print "I'm thinking of a number from " + minimum + " to " + maximum+ "."
	

	#Processing
	guess = int(raw_input("What do you think it is?: "))
	answer = think(int(minimum),int(maximum))
	if int(guess) > int(maximum):
        	print "The guess is too high"   
	elif int(guess) < int(minimum):
        	print "The guess is too low"
	
	else: tada = sub(answer, guess)

	#Output
	print output(answer, guess, tada)

#Call Main
main()
