def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#age= 35, height=74, weight=180, iq=50
#answer -4391?

print "That becomes: ", what, "Can you do it by hand?"

test = add(45, multiply(age, subtract(iq, add(age, 10))))

print "The test equation equals", test

def test2f(a, b, c, d):
    return a + b / c - d

print test2f(24, 34, 100, 1023)

#write a forumal for add iq - weight * age / height

test2 = add(iq, subtract(weight, multiply(age, divide(height, 2))))

print "This is test2:", test2 
