import math

def circlearea(x):
	z = x**2
	y = z/(4*math.pi)
	return y

def output(name, x, y, z):
	a = """
Hey {}
Did you know:
{} + {} = {}
""". format(name, x, y, z) 
	return a

def main():
	name = raw_input("What's your name?: ")
	x = raw_input("Type a number: ")
	y = raw_input("Type a number: ")

	z = add(int(x), int(y))

	a = output(name, x, y, z)
	print a

main()
