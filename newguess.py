#import random
import random

def guess(tell,roundnumber,answer,wins,chances):
	print answer
	if chances == 0:
		print "Your not really good at this game"
		guess2(roundnumber,answer,wins)
	elif tell < answer:
		print "Too low!"
		guess(int(raw_input("Your guess:")),roundnumber,answer,wins,chances-1)
	elif tell > answer:
		print "Too high!" 
		guess(int(raw_input("Your guess:")),roundnumber,answer,wins,chances-1)
	elif tell == answer:
		print "Correct!"
		print "Round" + str(wins+1)
		guess(int(raw_input("Your guess:")),answer,random.randint(0,100),wins+1,4)

def guess2(x,y,c):
	if x == 0:
		print str(y)
		exit()
	else: 
		print "Round" + str(wins-1)
		returnguess(int(raw_input("Your guess:")),roundnumber-1,random.randint(0,100),c,4)
print "Round 1"
guess(int(raw_input("Your guess:")),2,random.randint(0,100),0,4)
