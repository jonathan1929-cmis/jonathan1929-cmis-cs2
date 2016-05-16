#Rock paper scissors, 3 rounds
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


def gametime(yourhand, opponenthand):
	if yourhand == 1 and opponenthand not == 1 or 2:
		yourhand = 4
	elif opponenthand == 1 and yourhand not == 1 or 2:
		opponenthand = 4
	


def calc(yourhand, opponenthand):
	if yourhand > opponenthand:
		print "You Win!"
	elif yourhand < opponenthand
		print "Opponent Wins!"

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
	gametime(yourhand, opponenthand)
	print "Opponent chose {}!".format(printopp(opponenthand))
	calc(yourhand, opponenthand)
	


main()
