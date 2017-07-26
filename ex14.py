from sys import argv

script, user_name, certain_death = argv
prompt = "..."

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where will this cliff lead you too? %s" % certain_death


print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about likeing me.
You live in %r. Not sure where that is.
And you have %r computer. Nice
""" % (likes, lives, computer)
