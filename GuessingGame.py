import math
mininum=raw_input("What is the minimum number?:")
maximum=raw_input("What is the maximum number?:")
print "I'm thinking of a number from {} to {}.".format(int(minimum),int(maximum))
guess=raw_input("What do you think it is?:")
target=random.random(int(minimum),int(maximum))
def output():
	if guess < target
		print "That's under by {}.".format(int(target)-int(guess)
	if guess > target
		print "That's over by {}.".format(int(guess)-int(target))
	if guess == target
		print "You guessed right! You must be psychic!"
print "The target was {}".format(int(target))
print "Your guess was {}".format(int(guess))
output()
