import math
def add(a, b):
	return a + b #This functions adds a and b
a = add(3, 4)
def sub(a, b):
	return a - b #This function subtracts b from a
b = sub(5, 3)
def mul(a, b):
	return a * b #This function multiplies a by b
c = mul(4, 4)
def div(a, b):
	return a / b #This function divide b by a
d = div(2, 3)
def hours_from_seconds(a):
	return a / 60 #This function takes the seconds and divides it by 60 to give you the number of hours that amount of seconds represent
e = hours_from_seconds(86400)
def circle_area(r):
	pi = (math.pi)	
	return pi * r**2 #This function takes radius of a circle and converts it to the area of a circle.
f = circle_area(5)
def sphere_volume(r):
	pi = (math.pi)
	return pi * r**3 * 4/3 #This function takes the radius of a circle and convert it to the volume of that circle.
g = sphere_volume(5)
def avg_volume(a,b):
	pi = (math.pi)
	Vol1 = (((4/3.0) * pi) * a**3)
	Vol2 = (((4/3.0) * pi) * b**3)
	return Vol1 + Vol2/2 #This function states the average volume of two spheres
h = avg_volume (10, 20)
def area(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c)) #This function states the area of a triangle
i = area(1, 2, 2.5)
def right_align(a):
	return (a.rjust(80)) #This function places hello to the right side
j = right_align("Hello")
def center(a):
	return (a.center(40)) #This function that places hello to center
k = center("Hello")
def msg_box(y):
	x =    """		  + +
		  |  """+y+"""  |
		  +---------+"""
	print x
print msg_box("I eat cats!") # This function displays the word Hello and the sentence I eat cats! in a box 
