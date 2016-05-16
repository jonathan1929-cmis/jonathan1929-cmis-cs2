#Rock paper scissors game
import math
import random

def game():
	opp = random.randint(1, 3)
	if opp == 1:
		opponent = 1		
	elif opp == 2:
		opponent = 2	
	elif opp == 3:
		opponent = 3
	return opponent


def initiate():
	initiate = raw_input("rock, paper, or scissors!:")
	if initiate == "rock":
		choice = 1
	elif initiate == "paper":
		choice = 2
	elif initiate == "scissors":
		choice = 3
	return choice

def calc(yourhand, opponenthand):
	if yourhand == 3 and opponenthand == 1 or yourhand == 1 and opponenthand == 2:
		print "Opponent Wins!"
	elif yourhand == 2 and not opponenthand != 3:
		print "Opponent Wins!"
	elif yourhand == opponenthand:
		print "It's a tie!"
	else:
		print "You Win!"

def printopp(opponenthand):
	if opponenthand == 1:
		return "rock"
	elif opponenthand == 2:
		return "paper"
	elif opponenthand == 3:
		return "scissors"


def main():
	print """A challenger has appeared!
You participate in a rock paper scissors duel! Choose your hand!"""
	yourhand = initiate()
	opponenthand = game()
	print "Opponent chose {}!".format(printopp(opponenthand))
	calc(yourhand, opponenthand)
	print "You earned {} points!".format(round(random.random()*80))


main()
