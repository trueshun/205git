from adventurelib import *


def intro():
    say(""" 
    	Your stomach grumbles as you turn your ps4 off. In the midst of enjoying 
    	yourself your forgot to eat, hell, you even forgot to pee. It’s been an 
    	incredibly lazy winter break at your grandpa’s winter house, and this is
    	usually how you end your nights. Cooped up inside, playing games and enjoying 
    	the solitude. On the table is a letter from your grandpa, it says to type read me.
    """)

#room descriptions for look(). Lets the user look around the room they are currently
#in, as well as letting the user know which direction will lead them to what area.

current_room = starting_room = living_room = Room(""" The living room is well lived in. Dirty 
	dishes and takeout cover the coffee table and floor. The crackling fireplace 
	warms the space, while softly lighting the room in hues of red and orange. 
	The kitchen lays to the west of the room, and your bedroom to the east. """)

bedroom = starting_room.east = Room(""" Your room is the cleanest thing in the cabin. 
	You rarely make it to bed, more often than not sleeping on the couch. Besides a 
	painting of some creepy looking woods on the wall, the walls are bare. The only 
	furniture in the room is the bed, a dresser, and a night stand with a lamp. To the
	west is the living room, and to the north is the bathroom. """)

bathroom = bedroom.north = Room(""" The bathroom is clean, the smell of pine wafting 
	in the air. Your toothbrush lays on the counter. The mirror could use a light 
	scrubbing. The bedroom is to the south. """)

kitchen = starting_room.west = Room(""" The kitchen table is a mess, takeout containers
	and pizza boxes cover the surface. The stove is relatively clean, as you don’t cook.
	There is a cabinet above the counter top, and an old-school white fridge lays against
	the wall. To the east is the living room. """)


outside = starting_room.south = Room(""" It’s freezing and dark. Why did you decide to go out? Oh, god is
that a murderer over there?! N-no… it’s just the garden’s scarecrow. """)

inventory = Bag()

#Room atrributes for actions
#brushing only done in bathroom
Room.can_brush= False
bathroom.can_brush = True

#function for moving
# @when('n', direction='north')
# @when('s', direction='south')
# @when('e', direction='east')
# @when('w', direction='west')
@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)

        if room == bathroom:
            set_context('pee')
        else:
            set_context('default')
        if room == kitchen:
        	set_context('examine')
        else:
        	set_context('default')

        look()

#explain how to play game.        
@when("read")
@when("read me")
def explain():
	print("--------------------------- How to play ----------------------------")
	print(" 1. You can go from room to room by typing east, west, north, south.")
	print(" 2. If you don't remember what room you're in, you can type look.")
	print(" 3. If you're not sure what command to type you can type ? or help.")
	print(" 4. To quit type quit.")
	print("--------------------------------------------------------------------")

#going to the bathroom
youPeed = "no"
@when("pee", context="pee")
@when("use the toilet", context="pee")
def useBathroom():
	global youPeed
	if youPeed == "no":
		print("You use the toilet. Boy, is that a relief!")
		youPeed = "yes"
	else:
		print("You already used the bathroom.")

#brushing teeth
@when("brush teeth")
@when("brush")
def brushTeeth():
	if current_room.can_brush:
		print("Minty fresh. Should you floss? Nah, who has time for that.")
	else:
		print("You can't do that here.")

#function for looking around room
@when('look')
def look():
    say(current_room)

#examining cabnit or fridge

@when("examine TARGET")
def examine(target):
	if target == "fridge":
		print(f"You examined the old {target}. You're amazed at its good condition.")
		print("There's nothing inside, but a ketchup bottle and some pickles.")
		print("You decide to check the cabnit.")
	if target == "cabnit":
		print("There's nothing good on the bottom of the cabnit, you stand on your toes ")
		print("and ")

#Put all game functions here
def play():
	intro()
	playGame()
	#start always goes last
	start()

#play function. Will keep going until statement proves false
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
	play()