#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The "=" symbol is mainly used to define a variable.
#
#
#2 3pts) Write a technical definition for 'function'
#A function is a set of instructions executed to bring forth some type of
#output.
#
#3 1pt) What does the keyword "return" do?
#The keyword "Return" is used whilst defining a function to have the function
#produce some type of output after 'calling' the function after being defined.
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: Interger
#	2: String
#	3: Float
#	4: Boolean
#	5: Tuple
#	int(1), int(str(45))
#	str("Hi"), str(a)
#	21.0 + 42.35 == 63.35 
#	bool("True"), bool()
#	tup1 = ('cat', 'cat king', 42); \n print "tup1[0, 2.0]: ", tupl[0:2]
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#The difference between the two is that function definition is creating the
#set of instructions linking it to a command or 'call'.
#Calling a function then procedes to take that function defined and executes
#whatever instructions were defined.
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:Definition
#	2:Execution
#	3:Result
#	First the programs defines functions and set of instructions in which it must carry out later, to build the foundation of the program and it's overall purpose. The execution phase is when the program carries out the set of instructions through means of "calling" functions to have it start doing something. The third phase is the end product of the executed functions which have been defined earlier to produce some type of result based on the program's purpose.
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
x=int(raw_input("c1:"))
y=int(raw_input("c2:"))
z=int(raw_input("c3:"))
def circle_diameter(r):
	pi = (math.pi)
	
	return math.sqrt(r/pi)*2

a = circle_diameter(x)
b = circle_diameter(y)
c = circle_diameter(z)

print "Circle Diameter" \n "c1 "str(x) \n "c2 "str(y) \n "c3 "str(z) \n "TOTALS "str(a+b+c)

