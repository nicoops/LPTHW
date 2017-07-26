people = 20
cars = 20
trucks = 20

#Using an if statement to deicide which block of code to use here. Checking against the variables set above
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright let's just take the trucks."
else:
    print "Fine, let's stay home then."

if cars > people and trucks > cars:
    print "That's too many trucks, we should take the cars."
else:
    print "Let's take the trucks."
