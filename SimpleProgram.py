def storytelling(name,favmov,hobby,father,mother,yearsleft,crush,friend,vehicle):
	print """On a bright sunny day you, """ + str(name) +""", was walking down the street. You were thinking about """ + str(crush) + """ and felt {}. You were back from a day of {} at work. For a long time you wanted to become {}, but rethought your chocie and decided to be {}. Considering you've only got {} numbers of years left to live, you don't really have a lot of time. While walking, you see {} across the street, and {} pulling over next to her in a {}.""".format(favmov,hobby,father,mother,yearsleft,crush,friend,vehicle)

def main():
	name=raw_input("What is your name?:")
	age=raw_input("How old are you?:")
	sex=raw_input("What is your sex?:")
	hobby=raw_input("What do you enjoy doing in your free time?:")
	drink=raw_input("What is your favorite drink?:")
	vehicle=raw_input("What kind of vehicle would you like?:")
	childhood=raw_input("What was your favorite childhood object?:")
	crush=raw_input("What is the name of your crush?:")
	father=raw_input("Father's occupation?(add a/an before):")
	mother=raw_input("Mother's occupation?(add a/an before):")
	catch=raw_input("What if your favorite catchphrase?:")
	friend=raw_input("Who is your best friend?:")
	thrillride=raw_input("Describe the first thrill ride you ever got on:")
	oneself=raw_input("Desribe yourself in one word:")
	favmov=raw_input("What was your reaction to your favorite movie?:")
	kill=raw_input("If you were confronted by a serial killer, how would you act?:")
	yearsleft=75-int(age)
	story=storytelling(name,favmov,hobby,father,mother,yearsleft,crush,friend,vehicle)
	print story

main()

