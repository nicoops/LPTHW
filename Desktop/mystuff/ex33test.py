def loop_func(top_limit, add):
    i = 0
    numbers = []
    while i < top_limit:
        print "At the top is: %d" % i
        numbers.append(i)

        i = i + add
        print "Numbers now: ", numbers
        print "At the bottom is %d" % i

    for num in range(10, 20):
        print num

print "Enter two numbers."
top_limit = int(raw_input())
add = int(raw_input())

loop_func(top_limit, add)
