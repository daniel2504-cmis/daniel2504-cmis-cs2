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

def avg_volume(a, b):
	c =((a**3*math.pi*4/3)+(b**3*math.pi*4/3))
	d =c/2
	return d

print avg_volume(10, 20)
	
