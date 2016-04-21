def main(n):
    if n == 10:
        print "Blastoff!"
    elif n > 10:
        print "Number needs to be 10 or under."
    else:
        print n
        main(n + 1)

main(1)
