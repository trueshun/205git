import time
import sys
import os

################
# Player Setup #
################

class player:
	def __init__(self):

		self.name=""
		self.won = False

class inventory:
	def __init__(self):
		self.name = ""
		self.type = ""

####################
# global variables #
####################

userChoice = ""
emaPoints = 0
alfredPoints = 0
userMorale = 0




player1 = player()

question1 = "Hey, it's ya boi."

for character in question1:
	#prints a single letter one-by-one on the same line. Along with sys.stdout.flush() 
	sys.stdout.write(character)
	#this along with sys.stdout.flush() will print out one word straight
	#print(character) down.
	sys.stdout.flush()
	time.sleep(0.09)