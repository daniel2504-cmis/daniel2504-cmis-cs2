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
	a = 80 - len(a)
	b = 

print right_align(a)
	

	