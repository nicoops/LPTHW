#creating the initial argument, setting what file to input
from sys import argv
#the variables for the argv (two total)
script, input_file = argv
#first function is print_all which will print the input file. 'f' is the variable here
def print_all(f):
    print f.read()
#second function which will use seek to set the cursor back to byte 0, aka rewind the file
def rewind(f):
    f.seek(0)
#third function, which will print out a single line. the variable line_count and file.
def print_a_line(line_count, f):
    print line_count, f.readline(),
#sets current_file as the variable for the input file. opens the file
current_file = open(input_file)
#stating the print, and will then run the print_all function to print the entire file
print "First let's print the whole file:\n"

print_all(current_file)
#rewinding the file to get back to the beginning using our rewind function
print "Now let's rewind, kind of like a tape."

rewind(current_file)
#running the print_a_line function to run the first 3 lines of the txt file
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) #current line is set to 1. since we start at the beginning of the file, the print_a_line fucntion uses 1 for the line count

current_line += 1
print_a_line(current_line, current_file) #current line was set to 1, then we add 1 making two. this is the line count for this fuction

current_line += 1
print_a_line(current_line, current_file) #current line is 2 then + 1 makes the current line 3 for the function
