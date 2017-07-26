from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two on one line, how?
open(to_file, 'w').write(open(from_file).read())

to_file.close()
from_file.close()
