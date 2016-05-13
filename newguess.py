#import random
import random

def guess(tell,roundnumber,answer,wins,chances,rounds):
	if chances == 0:
		print "Your not really good at this game"
		guess2(roundnumber-1,answer,wins,rounds-1)
	elif tell < answer:
		print "Too low!"
		guess(int(raw_input("Your guess:")),roundnumber,answer,wins,chances-1,rounds)
	elif tell > answer:
		print "Too high!" 
		guess(int(raw_input("Your guess:")),roundnumber,answer,wins,chances-1,rounds)
	elif tell == answer:
		print "Correct!"
		print "Round" + str(rounds+1)
		guess(int(raw_input("Your guess:")),roundnumber,random.randint(0,100),wins+1,4,rounds+1)

def guess2(x,y,c,e):
	if e == 0:
		print str(c)
		exit()
	else: 
		print "Round" + str(x)
		return guess(int(raw_input("Your guess:")),x,random.randint(0,100),c,4,e)

#print "Round 1"
#guess(int(raw_input("Your guess:")),2,random.randint(0,100),0,4,1)

def humanguess(tell, answer, humanwins, AIwins, chances, rounds):
	print answer
	if chances == 0:
		print "Your not really good at this game"
		return AIguess()
	elif tell < answer:
		print "Too low!"
		humanguess(int(raw_input("Your guess:")), answer, humanwins, AIwins, chances-1, rounds):
	elif tell > answer:
		print "Too high!"
		humanguess(int(raw_input("Your guess:")), answer, humanwins, AIwins, chances-1, rounds):
	elif tell == answer:
		print "Correct!"
		print "Round " + str(rounds-1)
		AIguess(50, humanwins, AIwins, chances, rounds)

def AIguess(tell, humanwins, AIwins, chances, rounds):
	print str(tell)
	reply = raw_input("correct(c) higher(h) lower(l): ")
	if chances == 0:
		print "Alphago lost once to human, so I'll understand."
		return howmanyroundsleft(humanwins, AIwins, rounds)
	elif reply == "c"
		return howmanyroundsleft(humanwins, AIwins, rounds)
	elif reply == "h"
		return AIguess(
