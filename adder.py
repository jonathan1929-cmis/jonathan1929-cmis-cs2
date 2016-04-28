import math


def adder(total):
	added = raw_input("Next Number: ")
	if added == "":
            print "Your total runscore is: {}".format(total)
	else:
            total+=float(added)
            print "Running Total: {}".format(total)
            adder(total)


def main():
	total = 0
	adder(total)

main()


def adderbig(total, biggest):
	added = raw_input("Next Number: ")
	if added == "":
            print "Your highest runscore was: {}".format(biggest)
	else:
		total+=float(added)
		print "Running Total: {}".format(total)
		if added > total:
			biggest = added
		adderbig(total, biggest)




def main():
	total = 0
	biggest = 0
	adderbig(total, biggest)

main()
