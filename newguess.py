#import random
import random

def guess(x,y,z,w):
	if y == 0:
		return str(w)
	elif int(x) < z:
		print "Too low!"
		guess(raw_input("Your guess:"),y,z,w)
	elif int(x) > z:
		print "Too high!" 
		guess(raw_input("Your guess:"),y,z,w)
	else:
		print "Correct!"
		print "Round" + str(y)
		guess(raw_input("Your guess:"),y+1,random.randint(0,100),w+1)

print "Round 1"
print guess(raw_input("Your guess:"),2,random.randint(0,100),0)
