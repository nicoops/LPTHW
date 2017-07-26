#Using argument variable
from sys import argv
#Setting argv to retreive the file name
script, filename = argv
#Has txt set to open the designated file name
txt = open(filename)
#Print the below statement, showing what the file name is designated as using the argv
print "Here's your file %r:" % filename
#Print txt function to read the filename
print txt.read()
#Printing the statement to type the filename again
print "Type the filename again:"
#Setting the file_again equal to the user input of the txt file name
file_again = raw_input("> ")
#Setting the txt_again to open the user entered file name
txt_again = open(file_again)
#printing the opened user enetered file name
print txt_again.read()

txt_again.close()
