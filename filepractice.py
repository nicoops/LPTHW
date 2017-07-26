from sys import argv

script, filename1, filename2 = argv

print "Copying the first file to the second"
open(filename2, 'w').write(open(filename1).read())

target = open(filename2, 'a')

line1 = raw_input("Write in line 1: ")
line2 = raw_input("Write in line 2: ")
line3 = raw_input("Write in line 3: ")

print "Now we will write these lines to file2"

target.write("%s\n%s\n%s" % (line1, line2, line3))

target.close()
