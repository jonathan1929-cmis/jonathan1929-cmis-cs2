import math
def adder():
	total = 0
	added = float(raw_input("Next Number: "))
	if float(added) > 0:
		total = total + added
		print "Running Total: {}".format(float(total))
		adder()
	else:
		print "Your total run score is: {}".format(float(total))

def track()

adder()
