#name: trueshun
#date: 11-28.18
#description: text-based space adventure game

import random
import time

#display intro to the game

def displayIntro():
	print("You awake with an intense hunger for a sandwhich")
	print("But not any sandwhich will do.")
	print("You want the ultimate sandwhich...")
	print("You look for the keys to your ship.")
	print("1. Look in your pants from last night.")
	print("2. Go back to bed, you can't afford going on a trip.")

def choosePath():
	path = "" #choice is nothing
	while path != "1" and path != "2": #input validation
		path = input("Which path will you choose? (1 or 2: ")

	return path

def checkPath(choosenPath):
	print("You look for your pants.")
	print("Laying on the floor of your bathroom, you find your pants.")
	

displayIntro()