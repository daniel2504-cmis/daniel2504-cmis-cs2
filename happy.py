def clapYourHands():
	    print "clap clap"
def stompYourFeet():
	    print "stomp stomp"


def main():
	youreHappy = True
	youKnowIt = True

	Question = raw_input("Are you happy? ")


	if youreHappy and youKnowIt and Question:
		clapYourHands()
		stompYourFeet()
	print "Good bye"
	
main()
