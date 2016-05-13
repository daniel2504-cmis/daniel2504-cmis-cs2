# This game is about one prisoner trying to escape the jail. He has been in this prison for 10 years, he is sick of this place and you need to help him to escape.
import random

print """This game is about one prisoner trying to escape the jail. He has been in this prison for 10 years, he is sick of this place and you need to help him to escape."""

def warmup():
	reply = raw_input("Ok for warmup you gotta type exactly same like the options (Ok):")
	if reply == "Ok":
			return warmup2()
	exit()

def warmup2():
	letsstart = raw_input("This is made by Daniel Kwon (Ok):")
	if letsstart == "Ok":
		return escapetool()
	exit()

def escapetool():
	tool = raw_input("Ok what tool should I take to escape?(Spoon, Food, Glasses, John Cena):")
	if tool == "John Cena":
		print "JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out)"
		exit()
	elif tool == "Spoon":
		return escapespoon()
	elif tool == "Glasses":
		return escapeglasses()
	elif tool == "Daniel'slove":
		print "AHHHHH~~~ Ok you escaped"
	else:
		print "You just ate your poisonous food"
		exit()


def escapespoon():
	print "You started digging the floor with spoon"
	reply = raw_input("What are you doing?? Ask a fellow prisoner(I'm trying to escape or Mind your own buisness):")
	if reply == "Mind your own buisness":
		print "Your fellow was actually JOHN CENA. JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out)"
		exit()
	else:
		print """I'll help you too.
Your fellow friend followed you! But his not gonna help for the entire game."""
		return escaperun()

def escapeglasses():
	wear = raw_input("Hmmm I don't wear glasses but I can try (Yes or No):")
	if wear == "Yes":
		print """You could see something outside the wall and it was...............JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out)"""
		exit()
	else:
		return escaperun()

def escaperun():
	answer = raw_input("There is stair where should I run? (1st floor or 2nd floor):")
	if answer == "1st floor":
		return Cops()
	else:
		return Math()

def Cops():
	bullet = random.randint(1,3)
	print "The cops saw you and shooting at you! You got a dodge the bullet in matrix style!!(type 1 or 2 or 3 to dodge cop's random bullets)"
	dodge = raw_input("Which way 1 or 2 or 3?:")
	if bullet == int(dodge):
		print "You got shot and killed"
		exit()
	else:
		print "Cop shot at " + str(bullet)
		return Cops2()

def Cops2():
	bullet = random.randint(1,3)
	dodge = raw_input("Which way 1 or 2 or 3?:")
	if bullet == int(dodge):
		print "You got shot and killed"
		exit()
	else:
		print "Cop shot at " + str(bullet)
		return Cops3()

def Cops3():
	bullet = random.randint(1,3)
	dodge = raw_input("Which way 1 or 2 or 3?:")	
	if bullet == int(dodge):
		print "You got shot and killed"
		exit()
	else:
		print "Cop: OMG its Neo!!"
		return lastrun()
 
def Math():
	print "John Cena stood in your way"
	print "Don't worry I'm not gonna fight this time. But you gotta solve quiz to pass"
	question = raw_input("What month is Daniel's birthday?")
	if int(question) == 2:
		return lastrun()
	else:
		print "No your wrong. JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out)"
		exit()

def lastrun():
	print "You see a door, if you pass through this door you will escape but suddenly somebody shot bullet."
	shot = random.random()
	if shot < 50:
		print "But the bullet missed"
		return lastrun2()
	else:
		print "You died"
		exit()

def lastrun2():
	choose = raw_input("Oh no what should I do?(Run away or fight or stay):")
	if choose == "Run away":
		print "He kept shooting and you died"
		exit()
	elif choose == "stay":
		print "Suddenly, John Cena came out and helped you.JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out). You successfully escaped with John Cena"
	else:
		return fight()

def fight():
	choose = raw_input("kick or punch?:")
	if choose == "punch":
		print "He blocked your punch and shot you"
		exit()
	else:
		print "You knock down him and he dropped his gun"
		return fight2()

def fight2():
	choose = raw_input("get the gun or kick or punch:")
	if choose == "punch":
		print "You punched him on the face he started to run to the gun."
		return fight3()
	elif choose == "kick": 
		print "He blocked your kick and you fell down."
		return fightlay()
	else:
		print "You ran to the gun, but he grabbed your leg and you fell down."
		return fightlay()

def fight3():
	choose = raw_input("get the gun or kick or punch:")
	if choose == "punch":
		print "He was bleeding badly now."
		return fight4()
	elif choose == "kick":
		print "He was bleeding badly now."
		return fight4()
	else:
		print "You ran to the gun, but he grabbed your leg and you fell down."
		return fightlay()

def fight4():
	choose = raw_input("get the gun or kick or punch:")
	if choose == "punch":
		print "He blocked your punch and he kicked you to your stomach."
		return fight5()
	elif choose == "kick":
		print "He fainted by your kick and you successfully ran away."
	else:
		print "You grabbed the gun and shot at him. You successfully ran away."

def fightlay():
	print "You and him were laying on the floor. Both of you started ran to the gun"
	Yourspeed = random.randint(0, 99)
	Hisspeed = random.randint(0, 99)
	if Yourspeed == Hisspeed:
		print "Both of you grabbed the gun at the same time. Intense struggle was happening with each other."
		return fight5()
	elif Yourspeed > Hisspeed:
		print "Your speed was " + str(Yourspeed)
		print "His speed was " + str(Hisspeed)
		print "You grabbed the gun first and shot at him. You successfully ran away."
	else:
		print "Your speed was " + str(Yourspeed)
		print "His speed was " + str(Hisspeed)
		print "He grabbed the gun first and shot at you. (GameOver)"
		exit()

def fight5():
	choose = raw_input("kick or punch:")
	if choose == "kick":
		print "He blocked your kick and hit you on the face. You fainted(Game Over)"
		exit()
	else:
		print "The punch went right into his face. You successfully ran away."

def main():
	#input
	warmup()
	#process
	name = raw_input("What is your prisoner name?:")
	#output
	output = """Good job you succcessfully helped {} to run away""".format(name)
	print output

main()
