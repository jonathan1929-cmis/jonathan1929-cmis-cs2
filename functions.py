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

print sphere_volume(5)
def avg_volume(a, b):
	c = sphere_volume(a) + sphere_volume(b)
	return c / 2
print avg_volume(10, 20)
