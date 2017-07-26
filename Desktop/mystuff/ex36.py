from sys import exit

print "Twin Peaks: The Game"

characters = ['Dale Cooper', 'Hawk', 'BOB', 'Laura Palmer', 'Ben Horne', 'Lucy' ]
clues = []
player_name = raw_input("What should we call you...?")
print "Welcome to twin peaks, %s" % player_name

def start():
    print "The beareu sent you to Twin Peaks to investigate coopers disapearence"
    print "Driving through the town, you spot the RR Diner."
    print "Want to stop in for some pie and coffee? This might be a good place to start."

    choice = str.lower(raw_input("..."))

    if "yes" in choice:
        RR_diner()
    else:
        print "That was %s favorite place. Too bad he isn't around anymore!" % characters[0]
        print "You quit the investigation and get fired by the FBI."
        dead("The world runs on coffee...dummy.")

def dead(why):
    print why, "RIP"
    exit(0)

def RR_diner():
    print "Norma and Shelly welcome you to the diner."
    print "Would you like to sit down for a cup of coffee and pie?"

    coffee = str.lower(raw_input("..."))

    if 'yes' in coffee:
        chat_with_norma()
    else:
        print "You ask Norma and Shelly if they've heard anything about %s." % characters[0]
        print "They tell you to try asking around the Sheriff station."
        print "They haven't heard from Coop in years."
        sheriff_station()

def chat_with_norma():
    print "Norma brings over the cofvefe. She asks what brings you to town."
    print "You mention you're with the beareu looking for %s" % characters[0]
    print "She asks if she can join you."

    choice = str.lower(raw_input("Let Norma sit down? \n..."))

    if 'yes' in choice:
        print "Norma takes a seat. She starts remincing about Coop."
        print "Mentioning how much he loved his coffee and pie."
        print "Norma says, \"I really hope you find him."
        print "Twin peaks hasn't been the same since he left.\""
        print "She wishes you good luck, and mentions the sherriff."
        print "Maybe you should check out the station."
        print "Norma gets up to leave and you pay the check."

        tip_amount = int(raw_input("How much do you want to tip? \n...$"))

        if tip_amount >= 5:
            clue = 'coffee'
            clues.append(clue)
            "Time to head to the sheriff station \n."
            sheriff_station()
        elif tip_amount < 5:
            print "Boy %s, you sure are cheap!" % player_name
            print "Time to hit the road."
            raw_input("(Press enter to continue to Sheriff Station.)")
            sheriff_station()

    else:
        print "\"Well, ok then. Enjoy the coffee and best of luck."
        print "He stayed at the Northern Hotel, might be a good place to start.\""
        raw_input("(Continue to Northern Hotel?)")
        northern_hotel()

def sheriff_station():
    print "You enter the Sheriff Station. Mmm smells like donuts."
    print "%s greets you...in a very frazzled manner." % characters[5]
    raw_input("(Mention Cooper.)")
    print "Bringing up %s makes %s's eyes light up." % (characters[0], characters[5])
    print "Shocked and taken aback, she yells for %s." % characters [1]
    print "...%s comes in and grabs you. \"Let's chat he says\"" %characters[1]
    print "You head to Hawks office while he grabs some coffee."
    print "\"So, here about Coop, huh?\""
    raw_input("(Tell him what you know so far.)")
    print "\"Not much, then.\""

    if 'coffee' in clues:
        print "\"You know it's funny, before Coop left he stopped drinking coffee."
        print "Went from his favorite thing to something completley unimportant."
        print "I can't help you much, but Log Lady might be able to."
        print "She's always been more intune to these strange happeneings anyway.\""
        raw_input("(Press enter to visit the Log Lady.)")
        log_lady()
    else:
        print "While Coop was here, he was staying at the Nother Hotel"
        print "Might be worth checking out."
        print "I think he was staying in room 315."
        clue = '315'
        clues.append(clue)
        raw_input("(Press enter to continue to Northern Hotel.)")
        northern_hotel()

def northern_hotel():
    if "315" in clues:
        print "You head up to room 315 before asking around."
        print "The door is slightly cracked, inside you see a giant man."
        print "\"Cooper is who you seek. But the lodge gets it's soul\""
        print "\"I have something of his. Can you guess what?\""
        print "\"1. A cup."
        print "2. A ring"
        print "3. A tape\""

        guess = raw_input("...")

        if guess == '2' or guess == 'ring':
            print "The owls are not what they seem."
            print "Good luck."
            clue = 'owls'
            clues.append(clue)
            log_lady()
            print clues
        elif guess == '3' or guess == 'tape':
            print "A tape? Don\'t be ridiculous."
            print "I can be of no help right now."
            raw_input("(Go see the log lady)")
            log_lady()
        else:
            print "A wild haired man suddenly appears. Evil in his eyes"
            print "It\'s %s!" % characters[2]
            print "The trail goes cold here bucko..."
            dead("Nooooooooooooo...")
    else:
        print "You go up to find Ben Horne."
        print "Ben tells you to check in with the Log Lady."
        print "Mentioning that there are rumours of Owl Cave being sp00ky"
        log_lady()

def log_lady():
    print "\"Even though it has stopped growing larger, my log is aware\""
    print "Well that's a strange greeting..."
    raw_input("(You begin to explain why you're there, but the log lady interrupts.)")
    print "\"Only when we are everywhere will there be just one."
    print "It has been a pleasure speaking to you.\""
    print "You ask what she means, but she just points. At a map."
    print "The location is marked Owl Cave."

    if 'coffee' in clues:
        print "Just as with this map, owl cave contains another."
        print "Look within to find the key."
        clue = 'reflection'
        clues.append(clue)
        raw_input("(Press enter to continue to Owl Cave)")
        owl_cave()
    elif 'owls' in clues:
        print "Ah the owls are not what they seem. Indeed."
        print "The answer you seek is in the stone."
        clue = 'stone'
        clues.append(clue)
        raw_input("(Press enter to continue to Owl Cave)")
        owl_cave()
    else:
        print "I will tell you one thing."
        print "The writing is on the wall."
        clue = 'bad ending'
        clues.append(clue)
        raw_input("(Press enter to continue to Owl Cave)")
        owl_cave()

def owl_cave():
    print "Within owl cave, you see a painting on one of the walls."
    print "A strange hum eminates from the stone."
    print "You approach a strange painting."

    if 'reflection'in clues:
        print "The time has come...cooper awaits"
        print "You\'ve done well so far, but there is one more test."
        raw_input("(Press Enter to continue)")
        violet_room()
    elif 'owls' in clues:
        print "The time has come...cooper awaits"
        print "You\'ve done well so far, but there is one more test."
        raw_input("(Press Enter to continue)")
        violet_room()
    else:
        print "You\'ve failed Cooper and yourself."
        print "This will not end nicely for you."
        raw_input("(Press Enter to continue)")
        black_lodge()

def violet_room():
    print "You enter a room, entirely Violet."
    print "Dale cooper is sitting on a couch in front of a fireplace."
    print "A safe is buzzing behind him displaying the number 3."
    print "Approach the safe, or talk to Cooper?"

    safe_number_15 = False

    while True:
        choice = str.lower(raw_input("..."))
        if 'approach' in choice and safe_number_15 is False:
            print "Violent buzzing begins. Safe vaproizes you while Cooper looks on."
            black_lodge()
        elif 'talk' in choice:
            print "Cooper takes you up a ladder. You are now standing in the cosmos."
            print "All of existance seems to be permeating around you."
            print "Cooper reaches for and flips a lever."
            print "He is shocked into oblivion by 10000 volts"
            raw_input("(Return downstairs)")
            print "The safe now show the number 15."
            print "Now what?"
            safe_number_15 = True
        elif 'approach' or 'Approach' in choice and safe_number_15 is True:
            if 'owls' in clues:
                print "You reach for the safe as a violent buzzing sound increases."
                print "There is a massive shock of power as you turn the safe."
                print "Things get fuzzy here....but it seems you're being transported."
                white_lodge()
            elif 'coffee' in clues:
                print "You reach for the safe as a violent buzzing sound increases."
                print "There is a massive shock of power as you turn the safe."
                print "Things get fuzzy here....but it seems you're being transported."
                white_lodge()
            else:
                black_lodge()
        else:
            print "You've come all this way, and no response?!?!"
            dead("A horrific pale demon breaks through the door and devours you")

def white_lodge():
    print "This room looks strangely similar to the safe."
    print "You see Cooper, alert and aware sitting on a couch listening to music."
    print "Cooper thanks you, peace at last."
    end_game()

def black_lodge():
    print "Welcome to the waiting room."
    print "The Man from another Place sits on a couch."
    print "Decisions you\'ve made have led you here."
    print "Unfortunately for you, there is no turning back."
    dead("Trapped in the Black Lodge for eternity")

def end_game():
    print "Congrats on completing the game and saving Coop!"
    print "Although, let\'s be honest, you probably wrote the damn thing."
    print "Bye!"
    exit(0)

start()
