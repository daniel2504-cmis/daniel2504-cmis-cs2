#1 1pt) What is the symbol "=" used for?
# = is called assignment operator, it is used to put a value into a variable.
# For example, if you put Myname = Daniel Kwon. Myname will be the variable
# and the value will be Daniel Kwon.

#2 3pts) Write a technical definition for 'function'
# A fuction is a named sequence of statements that performs a computation.
# So when you define a function, you determine the name and the sequence of
# statements.

#3 1pt) What does the keyword "return" do?
# "Return" output/results to the calling function.
# "return" doesn't simply end the definiton. It instead is the point at
# which the function returns the result to the caller.

#4 5pts) We know 5 basic data types. Write the name for each one and provide two examples of each below
#	1: "int" - integer: a whole number
# example 1 : 0
# example 2 : -34
#	2: "float" - floating point value : a number with a fractional part
# example 1 : 0.0
# example 2 : 8.0
#	3: "bool" - boolean. Telling if its true of false
# example 1 : bool(0.0) is false
# example 2 : bool("Daniel Kwon") is ture
#	4: "str" - "string" of letters
# example 1 : "Hello, Computer"
# example 2 : "I wish i get a good grade"
#	5: tuple - a sequence of python objects
# example 1 : ("Daniel Kwon", 17, "students")
# example 2 : ("Steven", 16, "lol")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# function definition is for telling definiton and funciton call is the #return value


#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input : raw data
#	2: Process : data processing
#	3: Output : information
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

import math

def circle_area(a):

	b = a**2/math.pi
	c = b*2
	return c

def main():

	c1 = raw_input("Area of C1: ")
	c2 = raw_input("Area of C2: ")
	c3 = raw_input("Area of C3: ")
	c1a = circle_area(int(c1))
	c2a = circle_area(int(c2))
	c3a = circle_area(int(c3))
	t = c1a + c2a + c3a
	out = "Circle" + "  " + "Diameter" + "\n" + "c1" + "     " + str(c1a) + "\n" + "c2" + "     " + str(c2a) + "\n" + "c3" + "     " + str(c3a) + "\n" + "Totals" + " " + str(t)
	print out

main()
#Hint: Radius is the square root of the area divided by pi

