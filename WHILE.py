def count(x):
	while x > 0:
		print x
		x -= 1
	while x < 0:
		print x
		x += 1

#count(-10)



def countfrom(x, y):
	if x <= y:
		while x <= y:
			print x
			x += 1
	elif x >= y:
		while x >= y:
			print x
			x -= 1

#countfrom(0, 9)
#countfrom(10, 0)



def oddodds(x, stack):
	if x <= 0:
		while x <= 0:
			if not x % 2 == 0:
				stack += -x
			x += 1
	if x >= 0:
		while x >= 0:
			if not x % 2 == 0:
				stack += x
			x -= 1
	print stack

oddodds(10, 0)
oddodds(20, 0)



