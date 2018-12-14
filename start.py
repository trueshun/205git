
from adventurelib import *


#notes for myself:
    #print() will preserve the formatting of the strings you give it. 
    #This is sometimes needed; for example, to show a pre-formatted poem, 
    #or to display ASCII art.
    #Use say() to make it easier to output prose, in a way that will be 
    #easier for the player to read.

	#The @when decorator is written on the line above a function. 
	#The function will then be called when a player types a matching command.

#all code will go here
#all code will go here

#case insensitive will work if capitalized or a mix of lowercase and uppercase.

#when shouting/yelling
@when("shout loudly")
@when("shout")
@when("yell")
def yell():
	print("You bellow at the top of your lungs.")

#taking an item.
@when("take THING")
def take(thing):
    print(f"You take the {thing}.")

#When screaming
@when("scream")
def scream():
    print("You unleash a piercing shriek that reverberates around you.")

#when brushing teeth
@when("brush teeth")
def brush_teeth():
	#print("You brush your teeth. They feel clean.")
	say("""
		You squirt a bit too much toothpaste onto your brush and
		our reminded of what a failure you are once again.

		Why did you have to be such a failure?
		""")
#give item to person
@when("give ITEM to RECIPIENT")
def give(item, recipient):
    print(f"You give the {item} to the {recipient}.")

@when('look')
def look():
    print(current_room)

@when('exit')
def exit_room():
    global current_room
    if current_room.outside:
        current_room = current_room.outside
    else:
        say("Exit what? You're already outside.")
look()
start()