def LiverpoolFC(phil, bobby):
    print "Phil will score %d worldies." % phil
    print "Bobby will rack up %d assists." % bobby
    print "Together, they will conrtibute for %d goals." % (phil + bobby)
    print "I'm excited to see for myself.\n"

print "Here are their numbers for this year."
LiverpoolFC(30, 15)

print "How many do you think they'll contribute?"
goals = int(raw_input("Phil will score: "))
assists = int(raw_input("Bobby will set up: "))
LiverpoolFC(goals, assists)

print "That seemse a little low, how about a suggestion."
LiverpoolFC(goals + 5, assists + 10)

print "Press enter to continue. This will execute my magic formula."
raw_input()
LiverpoolFC(goals, assists)
print "Pyche! I copied your guess."
