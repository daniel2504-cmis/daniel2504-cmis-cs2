# This game is about one prisoner trying to escape the jail. He is been in this prison for 10 years, he is sick of this place and something tells him that it is time to escape.

#import
import random

#intro
print "its already past 10 years. I'm sick of this place. Sick of the food, prisoners, weather, and everything in this place. I heard that the captain Poomi left this for a moment. It is time."

#item you took
def take(item):
 if item == "pistol":
        luck = -5    
	elif item == "spoon":
        luck = 7
	elif item == "cloth":
        luck = 10
	elif item == "shoes":
        luck = 25
	elif item == "box":
        luck = 0
	elif item == "pin":
        luck = 10
   
    else:
        luck = random.randint(0,10)
    return luck

#How to escape
def plan:
	if plan == "Revolt":
        luck2 = -100    
    elif plan == "Secretly":
        luck2 = 50
	else:
        luck2 = -75
    return luck2

#Getting Help from different prisoner
def help():
	x = raw_input("Hah! Escape? I saw a lot of people who try it, but everytime their head was hold on the roof (Option: Trust me or Well then):")
	if x == "Well then"
	 print "I guess I'll see your head tomorrow (Laugh)"
	else: y = raw_input("If you want help, give me the item you have right now(Yes or No): ")
	return y

def help2(y):
	if y == "Yes"
	print "When you escape, you need to go outside by second floor."
	else: print "Well then, good luck.

#Escape
def escape():
	x = ("There is second floor and first floor, where should I go?: ")
	if x == "first floor"
	print "At the first floor, there was full of cops."
	else: print "I ran as fast I could."

#Main
def main():
	#Input
	playeritem = raw_input("I need item to escape, there are pistol, spoon, cloth, shoes, box, pin. I can only take one. Which should I take?:")

	playeritemluck = take(playeritem)
	playerluck = int(playeritemluck) + int(plan)
	help2(help())
