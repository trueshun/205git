#name: Zobeyda Chavez
#date: 11-28-18
#description: text-based adventure game in which you play a character who finds a diary detailing a legendary sandwhich
#			that he made from special ingrediants surrounding the land. Do you make the sandwhich? Or do you fall
#			victim to treachery on your way? Your worst enemy might just be yourself.

import random
import time #to add pause effect
from adventurelib import *

#varables for user response
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]

yes= ["yes", "y", "Yes", "Y"]
no= ["no", "n", "No,", "N"]


def title():
	print("\n\n\n\n")
	print("----------------------------------------------------------")
	print("                        SANDWHICH QUEST                   ")
	print("----------------------------------------------------------")

#display intro to the game
def displayIntro():
	say(""" 
	Your stomach grumbles as you turn your ps4 off. In the midst of enjoying yourself your
	forgot to eat, hell, you even forgot to pee. It’s been an incredibly lazy winter break 
	at your grandpa’s winter house, and this is usually how you end your nights, cooped up 
	inside, playing games and enjoying the solitude.\n

	You walk into the kitchen, where the kitchen table is a mess, takeout containers
	and pizza boxes cover the surface. The stove is relatively clean, as you don’t cook.
	There is a cabinet above the counter top, and an old-school white fridge lays against
	the wall. """)
	time.sleep(2)
	say("""
	Where should you check first?\n
	A. The fridge.\n
	B. The cabinet.\n
	C. Too much effort, going back to bed.
	""")
	choice1 =""
	while choice1 not in answer_a and choice1 not in answer_b and choice1 not in answer_c:
		choice1 = input(">>>")
	if choice1 in answer_a:
		checkFridge()
	elif choice1 in answer_b:
		checkCabinet()
	elif choice1 in answer_c: #will lead to end
		print("You go back to bed, dejected by life. Each pang of hunger pains reminding you of all your failures in life.")
		replay()

#choice if fridge is chosen
def checkFridge():
	say("""
		You open the retro white fridge, and find the same bottle of 
		ketchup you drank last night, and a jar of pickles... man, disappointing.
		""")
	time.sleep(2)
	say("""
		Keep looking for something to eat?\n
		A. All that's left is the cabinet.\n
		B. Guess I'll drink some ketchup and head to bed.
		""")
	choice2 = ""
	#making sure that user input is correct
	while choice2 not in answer_a and choice2 not in answer_b:
		choice2= input(">>>")
	if choice2 in answer_a:
		checkCabinet()
	else:
		say("""You grab the bottle of ketchup, and for a second consider grabbing a cup, before opening the 
			bottle and chugging a mix of semi-sweet/tart tomato puree.\n
			God, is this your lowest moment yet?
			""")
		replay()
#choice if cabinet is chosen.
def checkCabinet():
	say("""
		You check the bottom shelf of the cabinet, but don't see anything but a packet of wheat spaghetti noodles.
		Maybe the upper middle shelf has some food? You stand on your toes for more leverage, avoiding a can of
		navy beans. It'll be a cold day in hell before you eat that.\n

		... Wait, what's that? Your fingertips lightly graze something smooth and leathery -- God, you hope it's nothing dead or rotten -- 
		You lightly inch the object towards you, grasping it when it's close enough.\n

		It's a diary.\n

		Is it your Grandpa's? You wish you could say that you hesitated before openining it, but the truth is you ripped it open once
		it registered what you found. \n

		As you open the diary, your eyes glaze over the words, excitement fading. \n

		The diary details the information on a 'Legendary' sandwhich, with a hand-drawn map on the front page of the diary. You notice that
		the map looks like the aread surrounding the cabin. The author - your grandpa? - mentions how excuisite the sandwhich is, 
		the taste unparallel to all sandwhich's he has eaten. He spends a page talking about how he can die now that he's eaten this 
		'legendary' sandwhich. There's somthing about a warning on the last few pages, but what looks like mustard stains the pages.
		You can only make out the words: "shine bright".\n

		This has got to be a joke, right?\n

		Old grandad, up to his old tricks. Of course he would know you're lazy ass would be looking for food.\n

		... But what if it's real? \n 

		Why else would your Grandpa have hidden the diary? Your stomach grumbles as you try to make sense of this.
		""") 
	time.sleep(2)
	say("""
		A. Fuck it, check it out.\n
		B. Screw that.\n
		C. Think about it for a bit.\n
		""")
	choice3 =""
	while choice3 not in answer_a and choice3 not in answer_b and choice3 not in answer_c:
		choice3= input(">>>")
	if choice3 in answer_a:
		getItem()
	elif choice3 in answer_b:
		say("""You place the diary into the fridge, nearly forgotten, as you grab all the takeout menus' on the fridge door.\n
			Hopefully one of these places is still open.""")
		replay()
	elif choice3 in answer_c:
		print("You consider if it could be a joke, and while your grandpa loves jokes, you're not sure if this is one...")
		time.sleep(2)
		print("You decide to see if it's true.")
		getItem()

#func if player choses to see if diary is real.
def getItem():
	#global items 
	global flashlight
	global jerky

	say("""
		You grab your coat after dashing to the bathroom.\n
		Is there anything else you need?\n
		You currently have the diary in your leather messenger bag, and are currently wearing a greay hoodie with a black puffy vest.\n 
		It's dark out, should you look for a flashlight?\n
		""")

	time.sleep(1)
	say("""
		A. Dear god, you need a flashlight. Look for it now!\n
		B. Nah, you got cat-like reflexes and cat-like eyesight. You're gucci.\n
		""")
	choice4 = ""
	while choice4 not in answer_a and choice4 not in answer_b:
		choice4 = input(">>>")
	if choice4 in answer_a:
		flashlight = True
		say("""
			You look all over the cabin, nearly giving up when you find the flashlight in the kitchen drawer full of random stuff.\
			Thank God, because you don't have any cat-like skills.
			""")

		print("Hey, there's a slim jim in here! Should you take it?\n")
		time.sleep(1)
		say("""
		 	A. Fuck yeah, snap into a slim jim!\n
		 	B. Ew, gross. If I'm eating that I might as well eat those navy beans.\n
			""")
		
		choice5= ""
		while choice5 not in answer_a and choice5 not in answer_b:
		 	choice5 = input(">>>")
		if choice5 in answer_a:# this option will GIVE flashlight and GIVE jerky - AA
		 	print("You greedily shove the slim jim in your messenger bag.\n")
		 	jerky = True
		 	lettuce()
		else:#this option will GIVE flashlight and NO jerky - AB
		 	print("You shove it deeper in the drawer, disgust on your face.\n") 
		 	jerky = False
		 	lettuce()
	elif choice4 in answer_b:# NO flashlight and NO jerky - B
		print("Yeah, not bothering looking for that.\n")
		flashlight = False
		jerky
		lettuce()

#first item on quest lettuce
def lettuce():
	print("this si lettuce")

#give option to replay game
def replay():
	global playAgain
	print("\nGAME OVER")
	print("\nWould you like to play again?")
	playAgain = input(">>>")

#global variables
flashlight = False
jerky = False

#setting up global variable for main game while loop
#when this changes from 'yes' || 'y' to something else, game ends.
playAgain = "yes"
#This is the main game loop
while playAgain == "yes" or playAgain == "y":
	title()
	displayIntro()
