#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)Conditional Execution
#b)Alternative Executrion
#c)Chained Conditionals
#
#2) What does 'return' do?
#return gives back the thing that function tells to out. For example, if i said
# to 'return' "Daniel". It will return the Daniel as the function tells.
#
#
#3) What are 2 ways indentation is important in python code?
#a)Indentation tells the end of the function definition.
#b)Without indentation, you will get a error or doesn't work during the function.
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)36
#problem1_b)square root of 3
#problem1_c)0
#problem1_d)-5
#
#problem2_a)true
#problem2_b)true
#problem2_c)false
#problem2_d)false
#
#problem3_a)0.3
#problem3_b)0.5
#problem3_c)0.5
#problem3_d)0.5
#
#problem4_a)7
#problem4_b)5
#problem4_c)0.125
#problem4_d)5

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

#definition
def thebiggest(x,y,z):
	if float(x) > float(y) and float(x) > float(z):
	 return str(x)
	elif float(y) > float(x) and float(y) > float(z):
	 return str(y)
	else:  return str(z)

def notfollowingorder(x,y,z):
	if float(x) == float(y) or float(y) == float(z):
	    print "You didn't follow directions."
	exit()

#Main
def main():
	#input
	print "Type in 3 different numbers(Decimals are OK!)"
	N1 = raw_input("A:")
	N2 = raw_input("B:")
	N3 = raw_input("C:")
	notfollowingorder(N1,N2,N3)

	#process
	thebiggest = thebiggest(N1,N2,N3)
	
	#output
	out = """
The largest number was {}""".format(thebiggest)
	print out

#MainCall
main()
