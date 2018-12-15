#name: trueshun
#date: 11-28.18
#description: text-based space adventure game

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


	# print("			_.---._")
	# print("			_.-~       ~-._")
	# print("			_.-~               ~-._") 
	# print("		_.-~                       ~---._") 
	# print("	_.-~                                 ~\'")
	# print(" .-~                                    _.;") 
	# print(" :-._                               _.-~ ./") 
	# print(" `-._~-._                   _..__.-~ _.-~") 
	# print("  /  ~-._~-._              / .__..--~----._") 
	# print(" \'_____(_;-._\'.        _.-~_/       ~).. . \'") 
	# print("    /(_____  '\'`--...--~_.-~______..-+_______)") 
	# print("  .(_________/`--...--~/    _/        /'\' ") 
	# print(" /-._     '\'_     (___./_..-~__.....__..-~./") 
	# print(" `-._~-._   ~'\'--------~  .-~_..__.-~ _.-~") 
	# print("     ~-._~-._ ~---------'  / .__..--~") 
	# print("         ~-._'\'.        _.-~_/") 
	# print("             '\'`--...--~_.-~") 
	# print("              `--...--~") 
	print("    SANDWHICH QUEST     ") 

#display intro to the game
def displayIntro():
	say(""" 
	Your stomach grumbles as you turn your ps4 off. In the midst of enjoying yourself your forgot to eat, hell, you even forgot to pee. 
	It’s been an incredibly lazy winter break at your grandpa’s winter house, and this is usually how you end your nights, cooped up 
	inside, playing games and enjoying the solitude.

	You walk into the kitchen, where the kitchen table is a mess, takeout containers
	and pizza boxes cover the surface. The stove is relatively clean, as you don’t cook.
	There is a cabinet above the counter top, and an old-school white fridge lays against
	the wall.
	""")
	time.sleep(2)
	say("""
	Where should you check first?\n
	A. The fridge.\n
	B. The cabinet.\n
	C. Too much effort, going back to bed.
	""")
	choice1 = input(">>>")
	if choice1 in answer_a:
		fridge()
	elif choice1 in answer_b:
		cabinet()
	elif choice1 in answer_c: #will lead to end
		print("You go back to bed, dejected by life. Each pang of hunger pains reminding you of all your failures life.")
		replay()
#choice if fridge is chossen
def checkFridge():
	say("""
		You open the retro white fridge, and find the same bootle of 
		ketchup you drank last night, and a jar of pickles... man, disappointing.
		""")
	time.sleep(1)
	say("""
		Keep looking for something to eat? \n
		A. I'll check the cabinet.
		B. 
		""")
#give option to replay game
def replay():
	global playAgain
	print("\n Would you like to play again?")
	playAgain = input(">>>")

#setting up global variable for main game while loop
#when this changes from 'yes' || 'y' to something else, game ends.
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
	title()
	displayIntro()
