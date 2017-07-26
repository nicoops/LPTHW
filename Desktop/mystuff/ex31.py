print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "A wild Klopp appears! Kloppo has a question for you. \n Who do you want us to sign this year?"
    print "1. Salah"
    print "2. Naby Keita"
    print "3. VVD"
    print "4. All of them."

    signing = raw_input("> ")

    if signing == "1":
        print "That's a spicy selection."
    elif signing == "2":
        print "Kieta? I hardly new ya!"
    elif signing == "3":
        print "VVD, is what it be."
    elif signing == "4":
        print "Boss THA!"
    else:
        "Well that's not much help. Back to the room with you."

elif door == "4":
    print "This door is a mystery. Enter between any number you please."

    x = raw_input("> ")

    if x in range(1, 68):
        print "Well, that was a poor decision."
    elif x == "69":
        print "Heh."
    else:
        print "Meh, I expected more."
        
else:
    print "You stumble around and fall on a knife and die. Good job!"
