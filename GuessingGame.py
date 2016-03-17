import random

def main():
	l=raw_input("What is the minimum number?:")
	g=raw_input("What is the maximum number?:")
	print "I'm thinking of a number from {} to {}.".format(l,g)
	m=raw_input("What do you think it is?:")
	n=random.randint(int(l), int(g))
	print "The target was {}".format(int(n))
	print "Your guess was {}".format(int(m))
	if m==n:
		print "You guessed right! You must be psychic!"

main()

