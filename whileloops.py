
# x = 10
# while x >= 0:
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

counter(int(raw_input("N:")))
