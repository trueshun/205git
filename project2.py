from adventurelib import *

import textwrap

# def intro():
#     say(""" Your stomach grumbles as you turn your ps4 off. In the midst of enjoying 
#     	yourself your forgot to eat, hell, you even forgot to pee. It’s been an 
#     	incredibly lazy winter break at your grandpa’s winter house, and this is
#     	usually how you end your nights. Cooped up inside, playing games and enjoying 
#     	the solitude. After using the bathroom you decide to eat something in the kitchen. """)

#room descriptions for look(). Lets the user look around the room they are currently
#in, as well as letting the user know which direction will lead them to what area.

# current_room = starting_room = living_room = Room(""" The living room is well lived in. Dirty 
# 	dishes and takeout cover the coffee table and floor. The crackling fireplace 
# 	warms the space, while softly lighting the room in hues of red and orange. 
# 	The kitchen lays to the west of the room, and your bedroom to the east. """)

# bedroom = starting_room.east = Room(""" Your room is the cleanest thing in the cabin. 
# 	You rarely make it to bed, more often than not sleeping on the couch. Besides a 
# 	painting of some creepy looking woods on the wall, the walls are bare. The only 
# 	furniture in the room is the bed, a dresser, and a night stand with a lamp. To the
# 	west is the living room, and to the north is the bathroom. """)

# bathroom = bedroom.north = Room(""" The bathroom is clean, the smell of pine wafting 
# 	in the air. Your toothbrush lays on the counter. The mirror could use a light 
# 	scrubbing. The bedroom is to the south. """)

# kitchen = starting_room.west = Room(""" The kitchen table is a mess, takeout containers
#  and pizza boxes cover the surface. The stove is relatively clean, as you don’t cook.
#   There is a cabinet above the counter top, and an old-school white fridge lays against
#   the wall. To the east is the living room. """)

# outside = Room(""" It’s freezing and dark. Why did you decide to go out? Oh, god is
# that a murderer over there?! N-no… it’s just the garden’s scarecrow. """)


# def playAgain():
# 	choice = ""
# 	while choice != "yes" or !="y" and choice != "no" or !="n": 
# 		choice = input("Do you want to play again?")
# 	if(choice == "yes" or "y"):
# 		game = True
# 		start_game()
# 	else:
# 		print("You end the game.")


def intro():
	say(""" Your stomach grumbles as you turn your ps4 off. In the midst of enjoying 
    	yourself your forgot to eat, hell, you even forgot to pee. It’s been an 
    	incredibly lazy winter break at your grandpa’s winter house, and this is
    	usually how you end your nights. Cooped up inside, playing games and enjoying 
    	the solitude. After using the bathroom you decide to eat something in the kitchen. """)

#firts choice
def first_choice():
	print(" You go into the kitchen where you see the fridge and a cabnit above the counter top.")
	print("1. Search the fridge for some food.")
	print("2. Seach the cabnit.")
	choice = ""
	while choice != "1" and choice != "2":
		choice = input("Where should you look first? (choose 1 or 2)")

	if choice == "1":
		print("You look in the fridge but there isn't much there, just ketchup and pickles.")
		print("Let's look at the cabnit")
	else:
		say(""" You look at the cabnit 
			""")

game = True
def start_game():
	intro()

while game == True:
	start_game()	
playAgain()
