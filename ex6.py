#Designating x as this string
x = "There are %d types of people." % 10
#Designating the variable binary to represent 'binary'
binary = "binary"
#Designating the variable do_not to don't
do_not = "don't"
#Designating y to equal the below string within string
y = "Those who know %s and those who %s." % (binary, do_not)

#This will print the variable x
print x
#This will print the variable y
print y

#This will print the statement, and then include the x variable as an additional statement
print "I said: %r." % x
#This will print the below statement and include the y variable
print "I also said: '%s'." % y

#Setting hilarious as a variable equal to false
hilarious = False
#Setting the joke_evaluation variable to equal the below string, and then including a format string
joke_evaluation = "Isn't this joke so funny?! %s"

#Printing the joke evaluation variable, and then calling the hilarious variable using a format string
print joke_evaluation % hilarious

#Setting W and E as variables for the below strings
w = "This is the left side of..."
e = "a string with a right side"

#Adding the two variables together to complete a statement
print w + e
