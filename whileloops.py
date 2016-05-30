
#x = 10
#while x >= 0:
#	print x
#	x += -1

def countdown(number):
	while number >= 0:
		print number
		number += -1

def counter(x):
	if x > 0:
		while x >= 0:
			print x
			x += -1
	elif x < 0:
		while x < 1:
			print x
			x += 1
	else:
		print x

#counter(int(raw_input("N:")))

def counter2(x,y):
	if x > 0:
		while x >= y:
			print x
			x += -1
	elif x < 0:
		while x < y:
			print x
			x += 1
	else:
		print x

#counter2(-10,10)

def sumofodd(x):
	total = 0
	if float(x) > 0:
		while x >= 0:
			if x % 2 != 0:
				total += x
				x += -1
			elif x == 0:
				print total
				exit()
			else:
				x += -1		
	else:
		while x <= 0:
			if x % 2 != 0:
				total += x
				x += 1
			elif x == 0:
				print total
				exit()
			else:
				x += 1	


#sumofodd(13)

def grid(w,h):
	out = ""
	while w > 0:
		out += "."
		w -= 1
		return out
	
print grid(5,5)	
