def countdown_down_to(start, stop):
    if start < stop:
        print "Invalid Pair!"
    elif float(start) == float(stop):
        print stop
    else:
        print start
        countdown_down_to(start-1, stop)
	

countdown_down_to(3, 4)
print """countdown_from_to(3, 4)
"""

countdown_down_to(10, 1)
print """countdown_from_to(10, 1)
"""


def countdown_up_to(start, stop):
    if start > stop:
        print "Invalid Pair!"
    elif float(start) == float(stop):
        print stop
    else:
        print start
        countdown_up_to(start+1, stop)
	

countdown_up_to(4, 3)
print """countdown_from_to(4, 3)
"""

countdown_up_to(1, 10)
print """countdown_from_to(1, 10)
"""

countdown_up_to(4, 3)
print """countdown_from_to(3, 4)
"""
