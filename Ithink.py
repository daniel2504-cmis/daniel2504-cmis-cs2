# This is a function definiton, which won't really spit anything but just putting a variable. The function will check if there is anything same from the elif and if what you typed. If nothing match, it will randomly give a number from 1-10. As a return, it will give the numberit got times random number from 1-10.

import random

def eat(item):

    if item == "lava":
        strength = 0    
    elif item == "grapes":
        strength = 1
    elif item == "peanuts":
        strength = 2
    elif item == "shoes":
        strength = 3
    elif item == "bear liver":
        strength = 4
    elif item == "mud":
        strength = 5
    elif item == "toe nails":
        strength = 6
    elif item == "finger nails":
        strength = 7
    elif item == "tuna":
        strength = 8
    elif item == "eternity":
        strength = 9
    elif item == "fried rice":
        strength = 10
    else:
        strength = random.randint(0,10)
    return strength * random.random()

def main():
	x = raw_input("What item do you have?: ") 

	print "Your strength would be" + " " + str(eat(x))

main()
