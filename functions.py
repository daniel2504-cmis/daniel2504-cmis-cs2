def add(a, b):
	return a+b

def sub(a, b):
	return a-b

def mul(a, b):
	return a*b

def div(a, b):
	return a/b

def hours_from_seconds(a):
	return a/3600

import math

def area_of_circle(r):
    a = r**2 * math.pi
    return a

def sphere_volume(r):
	a = r**3*math.pi*4/3
	return a

def avg_volume( a, b):
	t = a/2
	y = b/2
	c = t**3*math.pi*4/3
	d = y**3*math.pi*4/3
	e = (c+d)/2
	return e

def area(a, b, c):
	p = (a+b+c)/2
	e = p-a
	f = p-b
	g = p-c
	d = g*f*e
	h = d*p
	i = math.sqrt(h)
	return i

def right_align(a):
	b = 84 - len(a)
	c = " " * b + a
	return c

def center(a):
	b = 84 - len(a)
	c = b/2
	d = " " * c + a
	return d

def msg_box(a):
	b = "+"+"-"*len(a)+"----"+"+"
	c ="|  " + a + "  |"
	d = "+"+"-"*len(a)+"----"+"+"
	return b + "\n" + c + "\n" + d 
	
print add(1,2)
print sub(3,1)
print mul(4,2)
print div(4,2)
print hours_from_seconds(3)
print area_of_circle(5)
print sphere_volume(5)
print avg_volume( 3, 2)
print area(1, 4, 3)
print right_align("Greetings")
print center("Steven plz")
print msg_box("Hello")
print msg_box("NP")

print msg_box


	
