import random
def main():
	mininum=raw_input("What is the minimum number?:")
	maximum=raw_input("What is the maximum number?:")
	print "I'm thinking of a number from {} to {}.".format(int(minimum),int(maximum))
	g=raw_input("What do you think it is?:")
	n=random.randomint(int(minimum),int(maximum))
	print "The target was {}".format(int(n))
	print "Your guess was {}".format(int(g))
	if g == n
		print "You guessed right! You must be psychic!"\

def feedback():
	if int(g) == int(n)
		print "You guessed right! You must be psychic!"
	elif int(g) < (n)
		print "That's under by {}.".format(int(n)-int(m))
	elif int(g) > int(n)
		print "That's over by {}.".format(int(m)-int(n))

n=random.randint(int(l), int(g))
