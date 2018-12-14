from adventurelib import *

space = Room("""
You are drifting in space. It feels very cold.

A slate-blue spaceship sits completely silently to your left,
its airlock open and waiting.
""")

spaceship = Room("""
The bridge if the spaceship is shiny and white, with thousands of small, red, blinking lights.
""")

# current_room will be a global variable. Let's start out in
# space, so assign the 'space' room from above.
current_room = space


@when('enter airlock')
def enter_spaceship():
    # To set a global variable from within a function you have
    # to include the 'global' keyword, to avoid creating a
    # local variable instead.
    global current_room

    # Got to check if this action can be done here
    if current_room is not space:
        print('There is no airlock here.')
        return

    current_room = spaceship

    # You should include some narrative for every action to
    # ensure the transition doesn't feel abrupt.
    say("""
        "You heave yourself into the airlock and slam your 
        hand on the button to close the outer door."
    """)

    # Show the room description to indicate we have arrived.
    print(current_room)

print(current_room)
start()