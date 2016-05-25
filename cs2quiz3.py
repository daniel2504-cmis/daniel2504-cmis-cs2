#Section 1: Terminology
#1p
# 1) What is a recursive function?
#	A function that calls himself and is able to repeat the function until it reaches to a limit that you made(Or forever).
#
#1p
# 2) What happens if there is no base case defined in a recursive function?
#	The function will never stop working without base case.
#
#1p
# 3) What is the first thing to consider when designing a recursive function?
#	basecase	
#
#1p
# 4) How do we put data into a function call?
#	When you repeat the function make it do the samething but with a different variable(IDK if that is the correct word).
#	For example,
# 	Carcrash(15, 0)
#	When you call it again you say
#	Carcrash(11, 6)  <- different data!
#
#0pt
# 5) How do we get data out of a function call?
#	You can print out the function or make it return some kind of variable.
#
#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.
#3pt
#a1 = 8
#a2 = 8
#a3 = -1
#1pt
#b1 = 2
#b2 = 1
#b3 = 6
#1pt
#c1 = 1
#c2 = 4
#c3 = 10
#1pt
#d1 = 10
#d2 = 8
#d3 = 8
#(I just guessed it)


#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def oddaverage(write,average,count):
	if write == "":
		return "The average of your odd numbers " + str(average/count)
	elif float(write) % 2 == 0:
		return oddaverage(raw_input("next:"),average,count)
	else:
		return oddaverage(raw_input("next:"),average+float(write),count+1)

print oddaverage(raw_input("next:"),0,0)

#all-1
