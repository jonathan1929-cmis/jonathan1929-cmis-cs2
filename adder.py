import math

def main():
	adder(0)


def adder(total):
	added = raw_input("Next Number: ")
	if float(added) > 0:
		total += float(added)
		print "Running Total: {}".format(float(total))
		adder(total)
	else:
		print "Your total run score is: {}".format(float(total))



main()
