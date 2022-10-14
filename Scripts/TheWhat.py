# Author: Michael O'Brien
# Copyright: forthcoming
import sys
import time


a = 2
b = 0.2
c = .08


def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("You can faintly hear a mechanical beep every few seconds")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold and damp. Thick vines snake along the smooth, rocky floor.")
    time.sleep(a)
    print("Drops of water echo periodically in the distance.")
    time.sleep(a)
    print("You feel a round rock that sinks into the ground when you press it.")
    time.sleep(a)
    print("The ground begins to rumble.")
    time.sleep(a)
    print("Shafts of light begin flooding in as dust swirls around you.")
    time.sleep(a)
    print()
    s = '"I\'m--I\'m in a cave..?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    time.sleep(a)
    print()
    m = '"...The doctor said..."'
    for character in m:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("Who said that?")
    time.sleep(a)
    print()
    print("A large boulder, in front of you, is released and rolls down a steep slope to the left over some vines into a hole. You never hear it hit the bottom.")
    time.sleep(a)
    print("Three paths are now revealed:")
    time.sleep(b)
    print()
    print("Path #1: Exit through the cave's entrance, into the light.")
    time.sleep(b)
    print("Path #2: Explore the depths of the cave, beyond where the boulder once stood, into the darkness.")
    time.sleep(b)
    print("Path #3: Climb down the vines, follow the boulder, into the bottomless hole.")
    time.sleep(b)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


def path1():
    print("You exit forward through the cave's entrance, into the light.")
    time.sleep(a)
    print("It's incredibly bright but your vision adjusts as you continue.")
    time.sleep(a)
    print("The cave exit closes, there's no going back now.")
    time.sleep(a)
    print("You look out and see that you're...standing atop an endlessly tall tower.")
    time.sleep(a)
    print("A man speaks to you.")
    time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is FRED. I thought you were my brother, GUS..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ahhh, now I remember you! Yes, you're looking for THE WHAT..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this...this place..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Yet, I cannot bring you to him..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Only the ANCIENT MAN can do that..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, I have heard that THE WHAT dwells in the deep SHADOWS."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    time.sleep(1)
    print()
    print()
    print("There are two paths to take to the bottom of the tower:")
    time.sleep(a)
    print("Path #1: Take the winding stairs down the tower.")
    time.sleep(a)
    print("Path #2: Scale down the rope hanging from the side of the tower.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()


def path1_1():
    print()
    print("You begin walking down the staircase toward the bottom.")
    time.sleep(a)
    print("The path is long and winding but the walk is not difficult.")
    time.sleep(a)
    print("The sky is bright and blue and a warm breeze hits your face.")
    time.sleep(a)
    s8 = '  "I could get used to this..."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("A voice calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey! Wait up!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is LIAM. I was just coming down the tower for some fresh air..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...this tower is the highest reaching tower on Earth and the air is especially thin..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...Anyhow, I see you're searching for the correct path, as we all are..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...It's not my place to tell you which path is correct..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, I will tell you this..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    s7 = '..."ONLY THROUGH SHADOWS WILL FREEDOM BE ATTAINED"'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path1_2():
    print()
    print("You begin scaling down the rope toward the bottom.")
    time.sleep(a)
    print("It's a long way down but you soon grow strong enough to appreciate the view. Tall mountains surround you.")
    time.sleep(a)
    print("Although you're still near the top of the tower, the clouds are below you and the world seems small.")
    time.sleep(a)
    s1 = '  "I don\'t believe my eyes..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You continue down the tower for what seems like days until you reach the bottom.")
    time.sleep(a)
    s2 = '  "Finally! I can face THE WHAT!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('--You yell, entering the base of the mountain through the largest red and black doors you\'ve ever seen')
    time.sleep(a)
    print("The darkness consumes you as you enter, unable to see a thing.")
    time.sleep(a)
    print("A thunderous voice calls out to you...")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're far too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...You can see through the light, but not the DARKNESS..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...You've developed some STRENGTH, but not enough..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to LEARN"
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you shall..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    intro()


def path2():
    print("You explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("It's incredibly dark but your vision adjusts as you continue forward.")
    time.sleep(a)
    print("A huge boulder slides into place behind you, blocking your path back.")
    time.sleep(a)
    print("You notice that the cave floor is declining to the left, like a spiral.")
    time.sleep(a)
    print("A voice calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is BENNETT... I thought you were my cousin, LIAM..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ah, now I remember you! Yes, you're looking for THE WHAT..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this dark place..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...However, I cannot bring you to him..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Only the ANCIENT MAN can do that..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, I have heard that THE WHAT dwells in the deep SHADOWS of this cave..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    print("There are two paths to continue through the cave:")
    time.sleep(a)
    print("Path #1: Go to the left.")
    time.sleep(a)
    print("Path #2: Go to the right.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path2_1()
    elif secondPath == '2':
        path2_2()


def path2_1():
    print()
    print("You take the fork in the cave to the left and continue walking.")
    time.sleep(a)
    print("The cave floor is still declining but is becoming much steeper than before.")
    time.sleep(a)
    print("It's so dark and the winding cave seems to go on forever.")
    time.sleep(a)
    s1 = "I have no choice, I must keep going..."
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Still going, fortifying your will, until finally, you reach the largest red and black door in existence.")
    time.sleep(a)
    print()
    s2 = '  "Finally! I can face THE WHAT!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You erupt as you enter the doors at the base of the cave inside Mount OLYMPUS')
    time.sleep(a)
    print()
    print("You are standing in the largest room you've ever seen. The walls and ceiling seem miles away. Before you stands a massive figure. A man?")
    time.sleep(a)
    print("No. Not a man. Shaped liked one...but...a shadow. The edges of the shadow shifting and swirling.")
    time.sleep(a)
    print("The room is dark. A booming voice calls out to you from everywhere at once, yet seemingly from nowhere at all.")
    time.sleep(a)
    print()
    s3 = "Ahhhhh... I've been expecting you. But you're still too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = '"...However, you haven\'t developed quite enough strength..."'
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to learn..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you will..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path2_2():
    print()
    print("You take the fork in the cave to the right and continue walking.")
    time.sleep(a)
    print("The cave floor is now inclining and is becoming quite steep.")
    time.sleep(a)
    print("It's so dark but after what seems like days of walking, you see a glow in the distance.")
    time.sleep(a)
    s1 = '  "What in the world can that be...?"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Approaching the brilliant light, you reach the end of this path and see an old book perched atop a pedestal")
    time.sleep(a)
    print()
    s2 = '  "THE SECRETS OF SHADOW"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You read the large inscription on the cover before opening the book.')
    print()
    time.sleep(a)
    s3 = '"If you stumble upon this tomb...'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It may save you from your doom..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen, that much is clear..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...But you have yet to face your fear..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = '...The truest path is one of toil..."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...Climb down vines beneath the soil..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...Speak with ELLIS, help her first..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...Then you will complete your search..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    intro()


def path3():
    print("You climb down the vines into the bottomless hole.")
    time.sleep(a)
    print("It's dark, damp, and hard to climb down the vines, but your vision and muscles eventually adjust.")
    time.sleep(a)
    print("You hear a rumble. Above you a large boulder slides into place, blocking your escape.")
    time.sleep(a)
    print("You sigh, but continue climbing down the vines until you hear something whirring up at you.")
    time.sleep(a)
    print("Someone calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey! You there!..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()

    print("An ancient man with a red beard that reaches the ground smiles at you. You spot a large, dusty, leather-bound book on the floor by his feet.")
    print()
    s3 = '"Another traveler searching the Abyss. I know all about you, yes. Just like the little redhead girl..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s4 = '"...Yes, yes...you\'re looking for THE WHAT..."'
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s5 = '"THE WHAT brought her here. Your sister. I taught her how to bring you here..."'
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print()
    print("Your sister? You had forgotten you had a sister.")
    time.sleep(a)
    print()
    s6 = '"This is THE WHAT\'S realm. I have almost no power here. Except, I am able to transport you anywhere you like within this world..."'
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s7 = '"But you must confront THE WHAT. You must defeat him."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("The ANCIENT MAN will transport you anywhere in the THE WHAT'S realm:")
    time.sleep(a)
    print("Path #1: Continue below to confront THE WHAT.")
    time.sleep(a)
    print("Path #2: Read: THE SECRETS OF SHADOW.")
    time.sleep(a)
    print("Path #3: Speak with GUS.")
    time.sleep(a)
    print("Path #4: Speak with FRED.")
    time.sleep(a)
    print("Path #5: Speak with BENNETT.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2/3/4/5): ")
    if secondPath == '2':
        path2_2()
    elif secondPath == '3':
        path1_1()
    elif secondPath == '4':
        path1()
    elif secondPath == '5':
        path2()
    else:
        print()
    print("You continue down the vines until you reach the bottom.")
    time.sleep(a)
    print("You see a small old woman next to the largest red and black wrought-iron double doors you've ever seen.")
    time.sleep(a)
    print("The old woman calls out to you.")
    time.sleep(a)
    print()
    s8 = '"Hello there, young traveler..."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = '"...My name is ELLIS. I am in great need of help..."'
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s10 = '"...I know whom you seek...THE WHAT is just beyond this door..."'
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s11 = '"...If you enter, you may speak with THE WHAT and perhaps free yourself..."'
    for character in s11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s12 = '"...But before you do so, would you take me HOME, to my family?..."'
    for character in s12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s13 = '"...I\'m unable to escape this cold, dark realm on my own..."'
    for character in s13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s14 = '"...The trip would be long...and arduous...the choice is yours..."'
    for character in s14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print()
    print("Path #1: Forget the old woman. Enter the doors and confront THE WHAT")
    time.sleep(a)
    print("Path #2: Honor the woman's request. Help ELLIS return home safely.")
    time.sleep(a)
    thirdPath = input("Which path will you take? (1/2): ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()


def path3_1():
    print()
    print("You begin walking toward the doors, ignoring ELLIS' request.")
    time.sleep(a)
    s15 = '"I would help you but I\'m in a hurry, you see. You understand, right?"'
    for character in s15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    print("You pull open the massive doors with all your might and enter.")
    time.sleep(a)
    print("You are standing in the largest room you've ever seen. The walls and ceiling seem miles away. Before you stands a massive figure. A man?")
    time.sleep(a)
    print("No. Not a man. Shaped liked one...but...a shadow. The edges of the shadow shifting and swirling.")
    time.sleep(a)
    print("The room is dark. A booming voice calls out to you from everywhere at once, yet seemingly from nowhere at all.")
    time.sleep(a)
    print()
    s16 = '"Ahhhh...I have been expecting you. But you are much...much too early..."'
    for character in s16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()

    s17 = '"It appears you have taken...a difficult route to find me..."'
    for character in s17:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s18 = '"...your vision is keen. You can see through this darkness...intriguing, yes? Yes. Unexpected..."'
    for character in s18:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s19 = '"...And you are but a child. Your strength must have grown from your travels."'
    for character in s19:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s20 = '"...However, you seek your sister..."'
    for character in s20:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s21 = '"...yet, she is not here..."'
    for character in s21:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s22 = '"...perhaps you are not quite ready..."'
    for character in s22:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()

    intro()


def path3_2():
    print("You approach ELLIS, honoring her request.")
    time.sleep(a)
    print()

    s23 = '"I understand. I know what it\'s like to miss your family...That\'s why I need to find my sister and get her out of here."'
    for character in s23:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s24 = '"But before I walk through those doors, I promise I will get you back home safely."'
    for character in s24:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("You kneel in front of ELLIS, allowing her to climb onto your back.")
    time.sleep(a)
    print("Standing up, you make your way to the vines to make your ascent.")
    time.sleep(a)
    print("Just as you grab the vines, the enormous iron doors thrust open, slamming to a halt.")
    time.sleep(a)
    print("A massive shadow in the shape of a man floats through, thunderous booms echoing around him.")
    time.sleep(a)
    print()
    w = "THE WHAT..."
    for character in w:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    s25 = '"Ahhhhh, I have been expecting you. And you\'re right on time..."'
    for character in s25:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()

    s26 = '"It appears you have taken...a difficult route to find me..."'
    for character in s26:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s27 = '"...your vision is keen. You can see through this darkness...intriguing, yes? Yes."'
    for character in s27:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s28 = '"...And you are but a child. Your strength must have grown from your travels."'
    for character in s28:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s29 = '"You even put the needs of others before your own..."'
    for character in s29:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()

    print("The shadowy figure raises it's arm...shadows swirling and shifting all around...")
    time.sleep(a)
    print("Shadows float up from the ground below, enveloping the old woman next to you...")
    time.sleep(a)
    s30 = '"NO!", you shout.'
    for character in s30:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s31 = 'THE WHAT continues..."You have learned everything I have to teach you..."'
    for character in s31:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    s32 = '"...you may finally be free..."'
    for character in s32:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    print("The shadows unfurl from the old woman next to you revealing a red headed little girl. Your Sister!")
    time.sleep(a)
    print("You embrace.")
    time.sleep(a)
    s33 = '"Thank you", she says.'
    for character in s33:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()

    s34 = '"It is time to return...", THE WHAT says.'
    for character in s34:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print("You wake up in a hospital room. Mechanical beeping rings loudly in your ear. You lift your head from the edge of a hospital bed.")
    time.sleep(a)
    print("You're sitting in a chair and...your holding your sister's hand.")
    time.sleep(a)
    s35 = '"You saved me...", she says, smiling at you.'
    for character in s35:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()

    s36 = '"...she might be in a coma for two weeks. Maybe more.", you hear your mother\'s voice in the hallway'
    for character in s36:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    print("Everything around you seems to slow down as you see the color return to your sister's face. She seems...fine.")
    time.sleep(a)
    print("The doctor rushes in with a few nurses. Shock on their faces as they see your sister awake and doing well.")
    time.sleep(a)
    print("Your parents walk in, holding each other. They're happily crying.")
    time.sleep(5)
    print()
    print()
    print("     ##########################")
    print("     #                        #")
    print("     #        The End         #")
    print("     # Thank you for playing! #")
    print("     #                        #")
    print("     ##########################")
    print()


print()
print()
print("     ##########################")
print("     #                        #")
print("     #        The What        #")
print("     #                        #")
print("     ##########################")
print()
print()
time.sleep(a)
print("Wha--What happened? Where am I?")
time.sleep(a)
print("It's too dark to see anything...")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == 'n' or startGame == 'N':
    print("Maybe another time. Bye bye.")
elif startGame == 'y' or startGame == 'Y':
    intro()
