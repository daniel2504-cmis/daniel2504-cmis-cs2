# if i use "#", it is used so it won't activate. (SO just erase # if you want it to work)

def countdown(n):
	
	if int(n) >= 0:
		print "WoW!"
	else:
		print n
		countdown(n-1)

def countup_from(start, stop):
	if start >= stop:
		print "WoW!"
	else:
		print start
		countup_from(start+1, stop)

def countdown_from(start, stop):
	pass
	countdown_from(start-1, stop)

# def main():
	
	a = int(raw_input("Number that we will call WOW!:"))
	b = int(raw_input("Number we will start counting:"))
	return countup_from(b, a)

# main()

# print "Running Total: 0.0"

def adder(number):
	total = 0.0
	x = raw_input("Next Number:")
	if x: 
		total += float(x) + number
		print "The sum is " + str(total)
		return adder(total)
	else:	
		total = number
		print "The sum is " + str(total)
# print adder(0.0)

def biggest(number):
	inp = raw_input("Next Number:")
	if inp == '':
		return str(number)
	elif number > float(inp):
		return biggest(number)
	else:
		return biggest(float(inp)) 

# print biggest(float(raw_input("Next:")))

def smallest(number):
	inp = raw_input("Next Number:")
	if inp == '':
		return str(number)
	elif number < float(inp):
		return smallest(number)
	else:
		return smallest(float(inp))

# print smallest(float(raw_input("Next:")))
