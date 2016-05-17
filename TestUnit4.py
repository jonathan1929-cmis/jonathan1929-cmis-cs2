#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a function that calls itself, creating a loop.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#It simply calls itself until the computer crashes or reaches it's recursion
#limit, it then returns an error.
#
# 3) What is the first thing to consider when designing a recursive function?
#Ideally what the function will do exactly, but technically the base case.
#
#
# 4) How do we put data into a function call?
#Add an argument when calling the function in the parenthesis. Add commas if
#more than one argument.
# 
# 5) How do we get data out of a function call?
#Simply return it.
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = x = 2, n = 0
#a2 = x = 6, n = 0
#a3 = x = -1, n = -1

#b1 = a = 2, b = 2
#b2 = a = 1, b = 0
#b3 = a = 1, b = 1,

#c1 = a = -2, b = 0
#c2 = a = 4, b = -2
#c3 = a = 5, b = 0

#d1 = a = 1, b = 1, c = 3
#d2 = a = 3, b = 3, c = 1
#d3 = a = 1, b = 1, c = 2

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def oddaverage(number, numbertrack):
	x = float(track)/float(numbertrack)
		return x

def checkodd(number, numbertrack):
	if int(number) % 2 == not 0
		numbertrack += 1
		oddtrack += number
		
def ask(track, numbertrack, oddtrack):
	number = raw_input("type a number:")
	if number == "":
		oddaverage(number, numbertrack)
		print "Your odd average was {}.".format(oddaverage(number, numbertrack))
	else:
		checkodd(number, numbertrack)
		track += int(number)
		ask(track)

def main():
numbertrack = 0
oddtrack
track = 0
ask(track, numbertrack, oddtrack)
