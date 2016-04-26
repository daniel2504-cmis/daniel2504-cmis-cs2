# if i use "#", it is used so it wont activate. (SO just erase # if you want it to work)

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

def biggest():
	x = raw_input("Next Number:")
	if x:
		
