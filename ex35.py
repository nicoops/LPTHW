from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear."
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I've got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def purple_room():
    print "You enter a purple room."
    print "Dale cooper is sitting on a couch in front of a fireplace."
    print "A safe is buzzing behind him displaying the number 3. Approach the safe or talk to cooper?"

    safe_number_15 = False

    while True:
        choice = raw_input("> ")
        if "approach" in choice and safe_number_15 is False:
            print "Violent buzzing begins. Safe vaproizes you while Cooper looks on."
            dead("The Black Lodge Awaits")
        elif "talk" in choice:
            print "Cooper takes you up a ladder. You are now standing in the cosmos."
            print "Cooper flips a lever."
            print "Return downstairs?"
            raw_input()
            print "The safe now show the number 15."
            safe_number_15 = True
        elif "approach" in choice and safe_number_15 is True:
            print "Violent buzzing begins. You are teleported to a room of gold."
            gold_room()
        else:
            print "Keen on hanging out with cooper for eternity? Too bad."
            cthulhu_room()

def dead(why):
    print why, "RIP"
    exit(0)

def start():
    print "You are in a dark room."
    print "There are three doors. left, right and middle."
    print "Which door do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "middle":
        purple_room()
    else:
        dead("You stumble aroud the room until you starve.")


start()
