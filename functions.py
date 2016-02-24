import math
def add(a, b):
	return a + b #This functions adds a and b

def sub(a, b):
	return a - b #This function subtracts b from a

def mul(a, b):
	return a * b #This function multiplies a by b

def div(a, b):
	return a / b #This function divide b by a

def hours_from_seconds(a):
	return a / 60 #This function takes the seconds and divides it by 60 to give you the number of hours that amount of seconds represent

def circle_area(r):
	pi = (math.pi)	
	return pi * r**2 #This function takes radius of a circle and converts it to the area of a circle.

def sphere_volume(r):
	pi = (math.pi)
	return pi * r**3 * 4/3 #This function takes the radius of a circle and convert it to the volume of that circle.

def avg_volume(a,b):
	pi = (math.pi)
	Vol1 = (((4/3.0) * pi) * a**3)
	Vol2 = (((4/3.0) * pi) * b**3)
	return Vol1 + Vol2/2 #This function states the average volume of two spheres

def area(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c)) #This function states the area of a triangle

def right_align(a):
	return (a.rjust(80)) #This function places hello to the right side

def center(a):
	return (a.center(40)) #This function places hello to center

def msg_box(n):
    return "+" + (len(n) + 4) * "-" + "+\n" "|" + "  " + n + "  " + "|\n" "+" + (len(n) + 4) * "-" + "+"

print msg_box("Hello")

print msg_box("I eat cats!") # This function displays the word Hello and the sentence I eat cats! in a box 

m = add(3, 4)
l = add(1, 2)
print msg_box(str(m))
print msg_box(str(l))
b = sub(5, 3)
o = sub(3, 4)
print msg_box(str(b))
print msg_box(str(o))
c = mul(4, 4)
p = mul(5, 6)
print msg_box(str(c))
print msg_box(str(p))
d = div(2, 3)
q = div(7, 8)
print msg_box(str(d))
print msg_box(str(q))
e = hours_from_seconds(86400)
r = hours_from_seconds(9101112)
print msg_box(str(e))
print msg_box(str(r))
f = circle_area(5)
s = circle_area(13)
print msg_box(str(f))
print msg_box(str(s))
g = sphere_volume(5)
t = sphere_volume(14)
print msg_box(str(g))
print msg_box(str(t))
h = avg_volume (10, 20)
u = avg_volume (15, 16)
print msg_box(str(h))
print msg_box(str(u))
i = area(1, 2, 2.5)
v = area(17, 18, 25)
print msg_box(str(i))
print msg_box(str(v))
j = right_align("Hello")
w = right_align("Hey")
print msg_box(str(j))
print msg_box(str(w))
k = center("Hello")
x = center("Yo")
print msg_box(str(k))
print msg_box(str(x)) #Every functions apart from the first two message boxes called twice
