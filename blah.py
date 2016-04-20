def countup(n,z):

	if int(n) >= int(z):
		print "WoW!"
	else:
		print n
		countup(n+1)

def main():
	b = raw_input("The wow number:")
	a = raw_input("Write something that goes lower than the wow number:")
	if int(a) >= int(b):
		print "Do u math?"
		exit()



	countup(a,b)
	return

main()
