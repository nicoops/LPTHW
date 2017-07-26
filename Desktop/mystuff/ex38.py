ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#split(ten_things) calls split with argument of 'ten things'
stuff = ten_things.split(' ') #call split on 'ten things'
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #call pop on 'more_stuff'
    #pop(more_stuff, last item) call pop with argument of more_stuff
    print "Adding: ", next_one
    stuff.append(next_one) #call append on stuff and use 'next_one'
    #append(stuff, next_one) call append with arguments of stuff and next_one
    print "There are %d items now." % len(stuff) #call len with argument of stuff

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() #pop(stuff) prints the last item on the list
print ' '.join(stuff) #call join on stuff using ' '
#join(' ', stuff) call join using arguments ' ' and stuff
print '#'.join(stuff[3:5]) #call join on stuff using #
#join(#, stuff) #call join using arguments # and stuff

#look up requests
#restful test api 
