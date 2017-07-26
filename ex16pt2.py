from sys import argv

script, filename = argv

txt = open(filename)

print "Tonight will be great because."
print txt.read()
txt.close()

txt_again = open(raw_input ("> "))
print "I repeat!"
print txt_again.read()
txt.close()
