# This game is about one prisoner trying to escape the jail. He has been in this prison for 10 years, he is sick of this place and you need to help him to escape.
import random

print """This game is about one prisoner trying to escape the jail. He has been in this prison for 10 years, he is sick of this place and you need to help him to escape."""

def escapetool():
	x = raw_input("Ok what tool should I take to escape?(Spoon, Food, Glasses, John Cena):")
	if x == "John Cena":
		print "JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out)"
		exit()
	elif x == "Spoon":
		return escapespoon()
	elif x == "Glasses":
		return escapeglasses()
	else:
		print "You just ate your food"


def escapespoon():
	print "You started digging the floor with spoon"
	y = raw_input("What are you doing?? Ask a fellow prisoner(Im trying to escape or Mind your own buisness")
	if y == "Mind your own buisness":
		print "Your fellow was actually JOHN CENA. JOOOOOHHHNNN CEEENNANANANAN(Epic Music comes out)"
		exit()
	else:
		print """I'll help you too.
Your fellow friend followed you! But his not gonna help for the entire game."""
		return escaperun()
escapetool()
