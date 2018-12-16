#name: Zobeyda Chavez
#date: 11-28-18
#description: text-based adventure game in which you play a character who finds a diary detailing a legendary sandwhich.
#			that he made from special ingrediants surrounding the land. Do you make the sandwhich? Or do you fall
#			victim to treachery on your way? Your worst enemy might just be yourself.

import random
import time #to add pause effect
from adventurelib import *

#varables for user response
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]

def title():
	print("----------------------------------------------------------")
	print("                          ____")
	print("              .----------'    '-.")
	print("             /  .      '     .   \'\'")
	print("            /        '    .      /|")
	print("           /      .             \'' /")
	print("          /  ' .       .     .  || |")
	print("         /.___________    '    / //")
	print("         |._          '------'| /|")
	print("         '.............______.-' /  ")
	print("     jgs |-.                  | /")
	print("         `------------.....-'" )
	print("\n")
	print("                        SANDWICH QUEST                    ")
	print("----------------------------------------------------------")
	print("\n\n\n\n")

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
		the wall. 
	""")
	printBorder()
	time.sleep(2)
	say("""
	Where should you check first?\n
	A. The fridge.\n
	B. The cabinet.\n
	C. Too much effort, going back to bed.\n
	""")
	printBorder()
	choice1 =""
	while choice1 not in answer_a and choice1 not in answer_b and choice1 not in answer_c:
		choice1 = input(">>>")
	if choice1 in answer_a:
		checkFridge()
	elif choice1 in answer_b:
		checkCabinet()
	elif choice1 in answer_c: #will lead to end
		print("You go back to bed, dejected by life. Each pang of hunger pains reminding you of all your failures in life.")
		time.sleep(3)
		replay()

#choice if fridge is chosen
def checkFridge():
	printBorder()
	say("""
		You open the retro white fridge, and find the same bottle of 
		ketchup you drank last night, and a jar of pickles... man, disappointing.
		""")
	time.sleep(3)
	printBorder()
	say("""
		Keep looking for something to eat?\n
		A. All that's left is the cabinet.\n
		B. Guess I'll drink some ketchup and head to bed.\n
		""")
	printBorder()
	choice2 = ""
	#making sure that user input is correct
	while choice2 not in answer_a and choice2 not in answer_b:
		choice2= input(">>>")
	if choice2 in answer_a:
		checkCabinet()
	else:
		say("""You grab the bottle of ketchup and chugg the mix of semi-sweet and tart tomato puree.\n
			God, is this your lowest moment yet?\n
			""")
		time.sleep(3)
		replay()
#choice if cabinet is chosen.
def checkCabinet():
	printBorder()
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
		the map looks like the aread surrounding the cabin.\n 
		
		The author - your grandpa? - mentions how excuisite the sandwhich is, 
		the taste unparallel to all sandwhich's he has eaten. He spends a page talking about how he can die now that he's eaten this 
		'legendary' sandwhich.\n 
		
		There's somthing about a warning on the last few pages, but what looks like mustard stains the pages.
		You can only make out the words: "shine bright".\n

		This has got to be a joke, right?\n

		Old grandad, up to his old tricks. Of course he would know you're lazy ass would be looking for food.\n

		... But what if it's real? \n 

		Why else would your Grandpa have hidden the diary? Your stomach grumbles as you try to make sense of this.
		""") 
	time.sleep(4)
	printBorder()
	say("""
		A. Fuck it, check it out.\n
		B. Screw that.\n
		C. Think about it for a bit.\n
		""")
	printBorder()
	choice3 =""
	while choice3 not in answer_a and choice3 not in answer_b and choice3 not in answer_c:
		choice3= input(">>>")
	if choice3 in answer_a:
		getItem()
	elif choice3 in answer_b:
		say("""You place the diary into the fridge, nearly forgotten, as you grab all the takeout menus' on the fridge door.\n
			Hopefully one of these places is still open.""")
		time.sleep(2)
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
	printBorder()

	say("""
		You grab your coat after dashing to the bathroom.\n
		Is there anything else you need?\n
		You currently have the diary in your leather messenger bag, and are currently wearing a greay hoodie with a black puffy vest.\n 
		It's dark out, should you look for a flashlight?\n
		""")
	printBorder()
	time.sleep(3)
	say("""
		A. Dear god, you need a flashlight. Look for it now!\n
		B. Nah, you got cat-like reflexes and cat-like eyesight. You're gucci.\n
		""")
	printBorder()
	choice4 = ""
	while choice4 not in answer_a and choice4 not in answer_b:
		choice4 = input(">>>")
	if choice4 in answer_a:
		flashlight = True
		say("""
			You look all over the cabin, nearly giving up when you find the flashlight in the kitchen drawer full of random stuff.\
			Thank God, because you don't have any cat-like skills.
			""")
		printBorder()
		print("Hey, there's a slim jim in here! Should you take it?\n")
		time.sleep(3)
		say("""
		 	A. Fuck yeah, snap into a slim jim!\n
		 	B. Ew, gross. If I'm eating that I might as well eat those navy beans.\n
			""")
		printBorder()
		choice5= ""
		while choice5 not in answer_a and choice5 not in answer_b:
		 	choice5 = input(">>>")
		if choice5 in answer_a:# this option will GIVE flashlight and GIVE jerky - AA
		 	print("You greedily shove the slim jim in your messenger bag.\n")
		 	jerky = True
		 	lettuce()
		else:#this option will GIVE flashlight and NO jerky - AB
		 	print("You shove the slim jim deeper in the drawer, disgust on your face.\n") 
		 	jerky = False
		 	lettuce()
	elif choice4 in answer_b:# NO flashlight and NO jerky - B
		print("Yeah, not bothering looking for that.\n")
		flashlight = False
		jerky = False
		lettuce()

#first item on quest - lettuce!
def lettuce():
	global flashlight
	printBorder()
	say("""
		It takes about 20 minutes, but you come to the field detailed in the diary.\n
		... At least you think you're in the right spot.\n
		You walk around, tripping over the rocks. Nothing dangerous so far.\n
		""")
	printBorder()
	if flashlight == True:
		say("""
			You turn on the flashlight, pointing it towards the field before you.\n
			You notice something strange as you stare into the earthy-smelling field.\n

			There's an empty patch on the field, with numerous mushrooms in a circle around it. Without your flashlight you'd never have seen it.
			Slowly you approach the circle, stopping just outside the circle of mushrooms. There in the center is a head of the must 
			luscious lettuce you've ever seen. You take a cautionary step forward, before stopping.\n

			These mushrooms... you remember your grandpa telling you to be carful about stepping into a ring of mushrooms. What were his exact words?
			'Don't do it!'\n

			Cautiously you lean forward, quickly snatching the head of lettuce with ease. As you do so, the ground within the mushroom circle gives
			way, the dirt falling into a dark abyss.\n

			'Fairy circle' you mutter, the memory of learning them rushing back you you as you hold the lettuce tight.
			You shine the light down the hole, seeing no end in sight.\n

			You place the head of lettuce into your bag, the validity of the diary no longer doubted as you head to the next destination.
			""")
		locationBreak()
	else:
		say("""
			You keep falling on the moist field, your shoes coated heavily in mud. You're not sure if this is the right place,
			hell, you're barely sure you know the way back home.\n
			This was a horrible idea. Why did you think that leaving home without a flashlight was a good idea?\n 
			Dumbass, that's you for sure.\n
			Great joke, Grandad.\n
			As you stand up once again from the dirt, you reach a muddy hand into your bag, tossing the diary into the field.
			You walk glumly back in what you think is the direction of home. Hungry and dejected, you're reminded of why you hate life.\n
			""")
		time.sleep(5)
		replay()

#split in choices, user can pick to look for meat or cheese next
def locationBreak():
	printBorder()
	say("""
		You look at the map in the diary once again. There are two locations near the lettuce field, what look to be the same distance apart.
		Which should you go to first?
		""")
	printBorder()
	time.sleep(2)
	say("""
		A. Where's the beef.\n
		B. Gotta get that cheese.\n
		""")
	printBorder()
	choice6 = ""
	while choice6 not in answer_a and choice6 not in answer_b:
		choice6 = input(">>>")
	if choice6 in answer_a:
		print("You go look for the meat in the sandwhich.\n")
		meat()
	elif choice6 in answer_b:
		print("You go look for the cheese because that's your life now.")
		cheese()
#second ingrediant in quest - meat
def meat():
	global patty
	global cheeseLoaf

	printBorder()
	say("""
		As you walk towards the destination for the meat of the sandwhich, you barely catch the * symbol below the word 'meat'.
		You stop, shining the light onto the diary in the hopes of being able to make out the scrawled words.\n
		
		'Find Romano in Siren'\n
		
		God, of course you would start this quest at the wrong time. Still, you've come this far, you might as well go all the way.
		They have to have some kind of motel, even the smallest town does.\n

		You walk towards the town, diary in one hand and flashlight in the other. You don't remember a town being so close to home, your
		grandpa's cabin is out in the boonies, and you usually have to drive an hour to get to the nearest town.\n

		Maybe it's a magical town, or some shit, right? Maybe you need the lettuce or the diary to make it appear.\n

		Sure enough, after a somewhat tiring walk, a small town comes into view. You can't see anyone yet, but you can hear the bustling
		chatter of people.\n
		
		Unfucking believable, there really is a town here. Thank god, you may find Romano awake at this hour.\n

		Lowkey you wonder if you can order takeout from here. After all, it's a lot closer than the takeout near home.\n

		As you enter the town you overcome with a sever feeling of unease. The architecture looks like a mishmash of different eras,
		some buildings looking ancient, while others don't come close to anything you've seen in the present.\n
		It's hard to tear your gazeaway from the buildings, so you keep your gaze on the ground.\n

		You don't like this feeling.\n 

		What should you do?\n
		""")
	printBorder()
	time.sleep(4)
	say("""
		A. Go home.\n
		B. Ask people if they know Romano\n
		C. Look around the buildings\n 
		""")
	printBorder()
	choice7 =""
	while choice7 not in answer_a and choice7 not in answer_b and choice7 not in answer_c:
		choice7 = input(">>>")
	if choice7 in answer_a:
		say("""
			You don't like this feeling. It's not like finding the lettuce. This place makes you feel anxious and scared. If
			you wanted to feel like that you would have stayed at home, and thought about your future.\n

			With your eyes on the floor, you turn around and walk back home.\n

			The anxious feeling follows you for life.\n
			""")
		time.sleep(4)
		replay()
	elif choice7 in answer_b:
		say("""
			You walk through the town, your gaze on the ground. You don't see anyone despite hearing voices around you. Somehow you
			avoid looking up at the disembodied voices. You shout for Romano because at this point you just want to leave the town.\n
			
			Why would you care if a bunch of ghost think you're crazy? They're dead.\n

			On your last shout you hear a shout of acknowledgment. You turn towards the shout, gaze locked on the ground.\n

			'You can look up,' comes the voice.\n

			Hesitantly you look up, and are greeted by a young man standing behind a meat stand.

			'Here about the sandwhich?' he asks, voice smooth and numbing, as he hands you a packet of meat. It's tied with twine
			and in it's center is a farily sized stone. You attempt to respond, but can't focus enough to do so.\n

			'Just look down, and turn around. If you ever need meat again, come with a list.'\n

			You do as he says, and soon enough you're at the gates of the town, your thoughts once again your own. What the hell was that about?\n

			Was he some ghost, just forever selling meat? God, that must suck for an afterlife.\n

			You're never coming here again.\n
			""")
		patty = True
		time.sleep(4)
		#make boolean to see if they have gotten cheese already if so go to bread().
		if cheeseLoaf == False:
			printBorder()
			cheese()
		elif cheeseLoaf ==  True and patty == True: 
			forest()
	elif choice7 in answer_c:
		say("""
			You walk through the town, your gaze on the buildings as you try to look for a sign that mentions a butcher, or has the
			name Romano on it.\n

			As you gaze at the buildings the overwhelming unease builds to the point that you want to run from the town, but you push on,
			eyes scanning the buildings.\n 

			By the time you make it to the center of the town your focus is gone, and you can't remember what you were doing, or how
			you made it here.\n

			You never make it back to the cabin or your old life, but the new life you create in the town fulfills you in a way the old you
			would never understand.\n  
			""")
		time.sleep(5)
		replay()

def cheese():
	global patty
	global cheeseLoaf
	global jerky

	printBorder()
	say("""
		You've gotten real good at reading the little map in the diary. You eventually find yourself
		at a small farm, a faded red old-school barn lays to the west of you, the doors wide open.\n

		Sheep, goats, and cows linger outside the barn, and some loiter in between the doors. Despite the animals,
		there is no smell of manure in the air. In fact, it smells like nothing at all.\n

		Cautiously you walk towards the animals. Maybe if you acknowledge them, they'll let you through.\n

		'Baa,' you say to the sheep in what you hope is how you say 'hi, just passing through'. You do the same to the
		cows, but throw in a head nod, too.\n

		At the goat you stop and stare.\n
		""")
	printBorder()
	time.sleep(3)
	say("""
		A. Crave the mineral.\n
		B. Uh... goat noise?\n
		C. 'Bleat?'\n
		""")
	printBorder()
	choice8 =""
	while choice8 not in answer_a and choice8 not in answer_b and choice8 not in answer_c:
		choice8 = input(">>>")
	if choice8 in answer_a:
		say("""
			Incensed at your remark, the goat charges you. The other animals follow suit.\n

			They don't stop chasing you until you run into the lettuce fields.\n

			That's the last time you talk to a fucking goat.\n

			What an asshole.\n
		""")
		time.sleep(4)
		replay()
	elif choice8 in answer_b or choice8 in answer_c:
		say("""
			You swear the goats roll their eyes at you, yet they let you through.\n

			The inside of the barn is full of hay, and their is a warmth in the air that calms you
			like no other anxiety pill ever has.\n

			Sitting at a wooden picnic table is a woman. She nods at you as you enter, before returning her attention to
			the cheese and cracker platter before her.\n

			You awkwardly stand there.\n

			'Uh, I'm here about the cheese,' you say as you gesture towrds the diary in your hand.\n

			She nods and extends her hand out towards you.\n
			""")
		time.sleep(3)
		printBorder()
		say("""
			A. Check your bag.\n
			B. Give her a high-five.\n
			""")
		printBorder()
		choice9=""
		while choice9 not in answer_a and choice9 not in answer_b:
			choice9 = input(">>>")
		if choice9 in answer_a:
			if jerky == True:
				say("""
					The only thing in your bag is the slim jim you grabbed before you left, so
					you give her that.\n

					Who doesn't like a slim jim?\n

					From the way her brow furrows, you're guessing she doesn't like it.\n

					She throws the slim jim back at you, and points towards the doors.\n

					You leave dejected.\n

					How could anyone hate slim jims?\n
					""")
				time.sleep(3)
				replay()
			else:
				say("""
					You check your bag for something to give her, but can't find anything but a mint.
					Does she want the mint?\n

					You place the mint in her outstretched hand.\n

					At her quizical face, you just turn and leave.\n

					Why would you give her a mint, god. You can never show your face here again.\n
					""")
				time.sleep(3)
				replay()
		elif choice9 in answer_b:
			cheeseLoaf = True
			say("""
				You can't fight it, you see a hand and you have to high-five it. It's a compulsion.\n

				With the might of Zeus, you high-five her outstretched hand.\n

				At first she is bewildered, and then breaks into a chorus of genuine laughter. She grabs a loaf of cheese, and 
				wraps it in cloth, before handing it to you.\n

				You thank her, amazed that worked, and wave goodbye as you leave, her laughter ringing in the air.\n
				""")
			time.sleep(4)
			if patty == False:
				printBorder()
				meat()
			elif patty == True and cheeseLoaf == True:
				forest()

def forest():
	global jerky

	printBorder()
	say("""
		The diary says there's a field around here, but you have to get through this forest first.\n

		It's dark out, and even with your flashlight you're struggling to see.\n

		The once loud forest turns eerily quiet, and you're not sure when that happened. You hold your messenger bag close
		as you listen intently to the silence.\n

		God, you're so stupid, what are you expecting to hear?\n

		Just as you think this, you hear it.\n

		The sound of a branch breaking.\n

		You stop, your stomach clenching tight as you hear the sound again.\n

		Holy shit, something is out here with you.\n

		You turn, flashlight aiming wildly into the trees, finally you see it, the glint of yellow wolf eyes 
		staring you down. It looks at you, teeth bared.\n
		""")
	time.sleep(5)
	printBorder()
	say("""
		A. Run\n
		B. Lay down and die\n
		C. Throw something\n
		""")
	printBorder()
	choice10=""
	while choice10 not in answer_a and choice10 not in answer_b and choice10 not in answer_c:
		choice10 = input(">>>")
	if choice10 in answer_a:
		say("""
			You bolt, sprinting with all your might as you hear the beast behind you. Several minutes later, and
			your lungs are burning, your sides hurting with each breath. You can't keep this up.\n
			""")
		time.sleep(3)
		printBorder()
		say("""
			A. Keep running.
			B. Throw something.
			""")
		printBorder()
		choice11=input(">>>")
		while choice11 not in answer_a and choice11 not in answer_b:
			choice11=input(">>>")
		if choice11 in answer_a:
			say("""
				You keep running, tears prickling your eyes. This is such shit, you're not Usain Bolt. With each painful breath you
				slow down just a bit. With a painful trip you seal your fate.
				""")
			time.sleep(3)
			replay()
		elif choice11 in answer_b:
			if jerky == True:
				say("""
					You reach into your bag, and wildly grasp the first thing you can. You pull out a slim jim, 
					of course! Everyone loves slim jim's!\n

					You erratically tear the wrapper off, and throw it as far behind the wolf as you can.\n

					The animal sniffs the air, nose twitching like mad as he turns to find the meaty treat.\n 

					You laugh crazily at its retreating form. Is there anyone who can deny the deliciousness of a slim jim?\n
					""")
				time.sleep(4)
				bread()
			elif jerky == False:
				say("""
					You reach into your bag, and wildly grasp the first thing you can. It's the pack of meat from that weird-ass town.
					Looking from the wolf to the meat, you nearly cry from frustration. \n

					You shake the meat before you, the wolf's eyes following the movements. You toss it as far as you can, the wolf giving
					chase after it.\n

					That's it. What's the point of continuing? You lost one of the ingredients, and you're not going through that again.\n
					""")
				time.sleep(4)
				replay()
	elif choice10 in answer_b:
		say("""
			That's it, you can't do this anymore. You lay down, and give up.\n
			Yeah, you're gonna die, but at least you won't have to walk back home.\n
			""")
		time.sleep(2)
		replay()
	elif choice10 in answer_c:
		if jerky == True:
			say("""
				You reach into your bag, and wildly grasp the first thing you can. You pull out a slim jim, 
				of course! Everyone loves slim jim's!\n

				You erratically tear the wrapper off, and throw it as far behind the wolf as you can.\n

				The animal sniffs the air, nose twitching like mad as he turns to find the meaty treat.\n 

				You laugh crazily at its retreating form. Is there anyone who can deny the deliciousness of a slim jim?\n
				""")
			time.sleep(4)
			bread()
		elif jerky == False:
			say("""
				You reach into your bag, and wildly grasp the first thing you can. It's the pack of meat from that weird-ass town.
				Looking from the wolf to the meat, you nearly cry from frustration. \n

				You shake the meat before you, the wolf's eyes following the movements. You toss it as far as you can, the wolf giving
				chase after it.\n

				That's it. What's the point of continuing? You lost one of the ingredients, and you're not going through that again.\n
				""")
			time.sleep(4)
			replay()

def bread():
	printBorder()
	say("""
		You pratically run out of the forest, man, you gave coach Holt so much crap, but now you're glad he forced you to run 
		because there was no way you would have been able to get through that.\n

		As you walk towards the field, everything seems to get darker. It was subtle at first, almost as if a filter is slowly being
		applied on your vision. You stop, and glance behind you, but now the darkness seems to be there, too.\n

		What is happening?\n

		You keep walking staight, eyes wide as your vision gets darker.\n

		The light from the flashlight is so very faint, you can barely see it.\n

		This is the last piece of the Legendary sandwich, you've come too far to quit.\n

		You've given up on so much easier things than this. You push on, no longer able to see your own hands.
		Everything is dark, and you are left alone with nothing but your thoughts.\n
		""")
	printBorder()
	say("""
		A. Cry.\n
		B. Keep going.\n
		C. Turn back.\n
		""")
	printBorder()
	choice12=""
	while choice12 not in answer_a and choice12 not in answer_b and choice12 not in answer_c:
		choice12=input(">>>")
	if choice12 in answer_a:
		say("""
			You start crying, and can't seem to stop.\n

			It pisses you off, and you proceed to cry even harder.\n

			This black void is literally what your whole life has felt like. You wander aimlessly, never finding your way out.\n
			""")
		time.sleep(3)
		replay()
	elif choice12 in answer_b:
		say("""
			You clutch your bag tight against yourself, and keep going. You still can't see yourself, can't even see your feet, 
			god you hope that there's nothing hiding in the darkness. \n

			You wish that you still had that slim jim.\n
			""")
		printBorder()
		say("""
			A. Check bag.\n
			B. Shout.\n
			""")
		printBorder()
		choice13=""
		while choice13 not in answer_a and choice13 not in answer_b:
			choice13=input(">>>")
		if choice13 in answer_a:
			say("""
				You check your bag, well, more like feel through it. There's the head of lettuce, the packet of meat,
				the cheese loaf, and the diary.\n

				The diary... there was something there about the danger's of the journey. What had it said to do?\n

				... 'Shine bright', that's what it was! But what is it supposed to mean?

				You feel through the contents again, pressing the flashlight against every item - it doesn't give much light, but enough
				for you to see if you can use one of them.
				""")
			printBorder()
			say("""
				A. Inspect lettuce.\n
				B. Inspect cheese.\n
				C. Inspect meat.\n
				""")
			printBorder()
			choice14=""
			while choice14 not in answer_a and choice14 not in answer_b and choice14 not in answer_c:
				choice14 = input(">>>")
			if choice14 in answer_a:
				say("""
					Yeah, that's a head of lettuce alright. There's nothing you see that can help you.\n
					Absolutly crushed you sit and eat the lettuce like a hand fruit.\n
					""")
				time.sleep(3)
				replay()
			elif choice14 in answer_b:
				say("""
					You check the cheese, but there's nothing hidden in the cheese or the cloth that it was wrapped in.\n
					... You shouldn't have high-fived that lady so hard, maybe if you had been normal you wouldn't be in this mess.\n
					Well, it looks like you're gonna be here forever, might as well eat some cheese.\n
					""")
				time.sleep(3)
				replay()
			elif choice14 in answer_c:
				say("""
					You're not really sure what to expect, it's meat after all.\n
					... Meat from a town you're NEVER going to again.\n
					You push the light against the packet, attempting to get the twine off, as you do so, the nearly transparent light hits 
					something on the packet, and a blast of white lights blinds you. \n
					You nearly drop the package of meat and the flashlight. It takes a few minutes for your vision to stop swimming,
					which is a weird sensation all on it's own, as you can't even see at the moment.\n

					When your eyes settle, you start grasping around the package, you feel a smooth stone, in the shape of a triangle.\n

					Wait... a triangle? It's been awhile since you've taken middle school geology, but is it a prism? Did that Romano guy
					tie a prism to the packet? Why would he do that?\n

					'Fuck it, I don't need to know,' you say. 'I'll shine bright,' you say as you close your eyes and press the flashlight
					to the twine wrapped package.\n

					A blinding light engulfs the room, even with your eyes closed, and face turned away, you can feel the sheer blinding light.\n

					You only open your eyes when feel the intensity dissipate.\n

					You find yourself standing in a literal field of bread. \n

					There are loafs, of what smell like sourdough, popping up from the ground.\n

					Your at a loss for words.\n

					You find a particularly crispy loaf and, looking around confused, take it. You have no idea what kind of fucking place
					this is, and quite frankly you don't want to know.\n
					""")
				printBorder()
				time.sleep(7)
				say("""
					The walk back home is a faint blur, you only remember being grateful you didn't pass through any other weird shit.\n

					You sit down at the table in the kitchen, the diary and ingrediants laid out before you. You cut everything the way
					the diary stated you should, and arrange it in the proper order.\n

					You pick it up and take a bite.\n

					Immediatly you're hit with wave after wave of salty, cheesy goodness.\n

					This sandwich was worth all the counseling you're going to need in the future.\n
					""")
				time.sleep(7)
				replay()
		elif choice13 in answer_b:
			say("""
				'Hey!' you shout, your voice echoing through the abyss. You scream again, taking breaks to see if you hear anything.\n

				You keep at it for what seems hours, and finally you hear laughter. It's light, hell, you may even have imagined it, but
				you rush towards the sound, shouting 'I'm here!'

				The sounds of 'baas', 'moos', and 'blets' has never made you so happy, you're basically running towards the sounds, the strength
				of the light on the flashlight coming back. \n
				When you finally make it through the darkness, you hear a pop, and suddently you find yourself running towards that old, faded red barn.\n

				Had you walked that whole distance from the wheat field to the dairy farm in the dark?\n

				You laugh miserably at the thought, thankful to be out of that hell.\n
				""")
			time.sleep(5)
			replay()
	elif choice12 in answer_c:
		say("""
			You turn back, trying to walk back in the direction that you came from, but nothing changes.\n

			This is such bullshit.\n

			'Hey!' you shout, your voice echoing through the abyss. You scream again, taking breaks to see if you hear anything.\n

			You keep at it for what seems hours, and finally you hear laughter. It's light, hell, you may even have imagined it, but
			you rush towards the sound, shouting 'I'm here!'

			The sounds of 'baas', 'moos', and 'blets' has never made you so happy, you're basically running towards the sounds, the strength
			of the light on the flashlight coming back. \n
			When you finally make it through the darkness, you hear a pop, and suddently you find yourself running towards that old, faded red barn.\n

			Had you walked that whole distance from the wheat field to the dairy farm in the dark?\n

			You laugh miserably at the thought, thankful to be out of that hell.\n
			""")
		time.sleep(6)
		replay()

#use to print border, so more aesthetically pleasing.
def printBorder():
	print("----------------------------------------------------")

#give option to replay game
def replay():
	printBorder()
	global playAgain
	print("\nGAME OVER")
	print("\nWould you like to play again?")
	playAgain = input(">>>")
	printBorder()

#global variables
flashlight = False
jerky = False
patty = False
cheeseLoaf = False

#setting up global variable for main game while loop
#when this changes from 'yes' || 'y' to something else, game ends.
playAgain = "yes"
#This is the main game loop
while playAgain == "yes" or playAgain == "y":
	title()
	displayIntro()
