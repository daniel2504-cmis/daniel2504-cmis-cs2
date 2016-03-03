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
	c = sphere_volume(t)
	d = sphere_volume(y)
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
	b = 80 - len(a)
	c = " " * b +a
	return c

def center(a):
	b = 80 - len(a)
	c = b/2
	d = " " * c + a
	return d

def msg_box(a):
	b = "+"+"-"*len(a)+"----"+"+"
	c ="|  " + a + "  |"
	d = "+"+"-"*len(a)+"----"+"+"
	return b + "\n" + c + "\n" + d 
	
def msg_box2(a):
	e = str(a)
	b = "+"+"-"*len(e)+"----"+"+"
	c ="|  " + e + "  |"
	d = "+"+"-"*len(e)+"----"+"+"
	return b + "\n" + c + "\n" + d 

#Call each of the functions you defined 2 times and store the result in a variable.
add1 = add(1,2)
add2 = add(2, 5)
sub1 = sub(3, 2)
sub2 = sub(4 , 5)
mul1 = mul(4,2)
mul2 = mul(6,2)
div1 = div(4, 2)
div2 = div(6,3)
hs1 = hours_from_seconds(3)
hs2 = hours_from_seconds(2)
ac1 = area_of_circle(5)
ac2 = area_of_circle(3)
sv1 = sphere_volume(5)
sv2 = sphere_volume(3)
av1 = avg_volume( 3, 2)
av2 = avg_volume(4, 2)
a1 = area(1, 2, 2.5)
a2 = area(1, 2, 3)
ra1 = right_align("Greetings")
ra2 = right_align("Daniel Kwon")
c1 = center("Steven plz")
c2 = center("CS")

print msg_box("Hello")
print msg_box("NP")

#print output
print msg_box2(add1)
print msg_box2(add2)
print msg_box2(sub1)
print msg_box2(sub2)
print msg_box2(mul1)
print msg_box2(mul2)
print msg_box2(div1)
print msg_box2(div2)
print msg_box2(hs1)
print msg_box2(hs2)
print msg_box2(ac1)
print msg_box2(ac2)
print msg_box2(sv1)
print msg_box2(sv2)
print msg_box2(av1)
print msg_box2(av2)
print msg_box2(a1)
print msg_box2(a2)


	
