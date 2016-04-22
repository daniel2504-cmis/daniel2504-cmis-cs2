def countup(n):

	if int(n) >= 0:
		print "WoW!"
	else:
		print n
		countup(n+1)

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

def main():
	
	a = int(raw_input("Number that we will call WOW!:"))
	b = int(raw_input("Number we will start counting:"))
	return countup_from(b, a)

main()
