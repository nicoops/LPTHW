#This creates the funtion 'cheese_and_crackers' with two arguments. It then prints the remaining 4 lines, two of which call back to the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#This block defines the two function variables by assigning the values directly
print "We can just give the funcion numbers directly:"
cheese_and_crackers(20, 30)

#This block defines the function variables by creating variables outside the fucntion, then assigining them to the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This sets the funtcion variables using maths for each
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#This combines using the previously set up variables and maths to define the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#The function is printed each time that it is called because we specified that in the first 6 lines 
