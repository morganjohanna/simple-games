from textwrap import dedent

room = "homeville"
bear = True
bearencounter = False
bearsnack = False
bearrage = False
spell = False
medal = False

descriptions = {
    "homeville": "\n" + dedent("""\
        You are in HOMEVILLE, your home town.
        It contains the local SHOP and is bordered by the lush and inviting FOREST.
        Nestled deep among the trees rises a distant TOWER."""),
    "forest": "\nYou harness the almighty power of walking to enter the FOREST. It seems nice.",
    "shop": "\nInside the SHOP, a friendly shopkeeper comes up to you with a smile.",
    "clearing": "\n" + dedent("""\
        It's nowhere near as adventurous as promised. There's simply a large, flat stone in the middle of the CLEARING.
        Something glints in the sunlight. It's a gold star. You take it.
        Congratulations, you thief.
        By the clever use of bad ethics, you won."""),
    "tower": "\nThe TOWER is old and crumbling, but crackles with wild magics.",
    "fail": "\nTyping is one of the most important skills of our age. Please go home and try again."
}

path = {
    "homeville": ["SHOP", "FOREST"],
    "forest": ["TOWER", "HOMEVILLE"],
    "shop": ["HOMEVILLE"],
    "tower": ["CLEARING", "FOREST"],
    "clearing": ["TOWER"]
}

story = {
    "forestbear": dedent("""\
        Except that you know there's a BEAR here so WHY
        JUST WHY
        Your deathwish immediately evaporated by a bone-chilling roar, you narrowly escape back to Homeville."""),
    "forestbear1": dedent("""\
        You walk for some time, enjoying the cool shade and deep quiet of a mossy, green FOREST.
        You hear a rustle. Probably some precious woodland creature!
        <rustle>
        <rustle>
        A bear!
        BEAR!
        BearbearbearBEARBEARfuckfuckfuckingRUN
        
        You have safely returned back to Homeville."""),
    "bearhappy": dedent("""\
        Just beyond the trees, you carefully unscrew the peanut butter jar and sort of smear it on a log.
        The bear appears and, as you carefully scooch away, just goes to town licking it off.
        He'll be busy for some time yet and won't bother you again."""),
    "bearhappy1": dedent("""\
        It's a good thing you brought this peanut butter because there is a freaking BEAR here.
        He's kind of chilling not far from you, so you carefully unscrew the peanut butter jar and sort of smear it on a log.
        You scooch away carefully as the bear approaches and just goes to town licking it off.
        He'll be busy for some time yet and won't bother you."""),
    "bearangry": dedent("""\
        Just beyond the trees, you carefully fling the steak off into the brush
        in the general direction of where you saw the bear.
        It appears, chomps the steak, then comes lumbering after you.
        Foolish adventurer, your hands are covered in delicious steak juice!
        And bears are surprisingly zippy for their size!
        RUN!!!"""),
    "bearangry1": dedent("""\
        It's a good thing you brought this steak because there is a freaking BEAR here.
        He's kind of chilling not far from you, so you carefully fling the steak off into the brush in his general direction.
        He approaches, chomps the steak, then comes lumbering after you.
        Foolish adventurer, your hands are covered in delicious steak juice!
        And bears are surprisingly zippy for their size!
        RUN!!!"""),        
    "shopkeeper": dedent("""\
        \"We have a variety of goods for the discerning shopper!\" they claim without any evidence.
        \"Anything against bears?\" you ask. You try to be casual about it but aren't very convincing.
        \"Good gods! Well bear spray would be your best bet, but we don't have any.
        Perhaps some PEANUT BUTTER or STEAK instead?\""""),
    "shopkeeper1": dedent("""\
        \"Welcome back, shopper!\" they greet you overexuberantly. "How was that steak for you, juicy enough?"
        You shudder. \"Maybe a bit too much. Do you have anything else?\"
        \"Bear problems, eh?\" The shopkeeper chuckles. They've never feared for their life."""),
    "shopempty": dedent("""\
        \"Sorry, there's not much left on the SHOP shelves.
        Seems people have been stocking up in advance of the bearpocalypse that's right around the corner!\""""),
    "mage": dedent("""\
        You enter through an ancient, heavy wooden door.
        Inside, you discover a mage with a long gray beard... in boxer shorts.
        \"I wasn't expecting company!\" he cries excitedly while reaching for a star-splashed robe.
        \"I suppose you're here for my magic cookies! Fresh out of the oven!\"
        \"Actually, I was just wondering if you knew what's beyond the FOREST.
        Any adventure out there?\"
        \"Well I do have one adventure available. Just hold on to your hat!\"
        Before you can say that you aren't wearing a hat, you're overcome by a strong aroma of wet metal.
        You're engulfed in purple smoke and sparks and, once it clears, you find yourself in a CLEARING."""),
    "mage1": dedent("""\
        \"You're back!\" cries the mage through magic cookie crumbs. \"Couldn't resist, could you?\"
        \"These aren't going to... like, do anything to me, right?\" you ask, gingerly picking up a cookie.
        The mage implores you to try it.
        It looks pretty tasty. You take a bite and are again transported to the CLEARING."""),
    "shopping": "Weird collection of stuff, but maybe something will work on bears. Which item do you choose?\n",
    "shopping1": "\"Well, I've still got that PEANUT BUTTER, if you want it. What'll it be?\"\n",
    "peanutbutter": "You pay for a jar of crunchy peanut butter and leave the SHOP.",
    "steak": "You pay for a big, juicy steak and leave the SHOP.",
    "other": "\"Sorry, we don't have any.\""
}

while room != "clearing":
    if room not in descriptions:
        print(descriptions["fail"])
        room = "homeville"
    
    print(descriptions[room])

    if room == "forest" and bear:
        if bearencounter == False:
            if bearrage == False and bearsnack == False:
                print(story["forestbear1"])
                bearencounter = True
                room = "homeville"
            elif bearsnack:
                print(story["bearhappy1"])
                bearencounter = True
                bear = False
            elif bearrage:
                print(story["bearangry1"])
                bearencounter = True
                room = "homeville"
        else:
            if bearrage == False and bearsnack == False:
                print(story["forestbear"])
                room = "homeville"
            elif bearsnack:
                print(story["bearhappy"])
                bear = False
            elif bearrage:
                print(story["bearangry"])
                room = "homeville"
           
    if room == "shop":
        if bearsnack:
            print(story["shopempty"])
        elif bearrage:
            print(story["shopkeeper1"])
            stuff = input(story["shopping1"])
            stuff = stuff.lower()
            if stuff == "peanut butter":
                print(story["peanutbutter"])
                bearsnack = True
                room = "homeville"
            else:
                print(story["other"])
        else:
            print(story["shopkeeper"])
            stuff = input(story["shopping"])
            stuff = stuff.lower()
            if stuff == "peanut butter":
                print(story["peanutbutter"])
                bearsnack = True
                room = "homeville"
            elif stuff == "steak":
                print(story["steak"])
                bearrage = True
                room = "homeville"
            else:
                print(story["other"])

    if room == "tower":
        if spell == False:
            print(story["mage"])
            final = input("\nDo you wish to CONTINUE or FLEE in terror?\n")
            final = final.lower()
            spell = True
            if final == "continue":
                room = "clearing"
                break
            elif final == "flee":
                room = "tower"
            else:
                print(descriptions["fail"])
                room = "homeville"
        else:
            print(story["mage1"])
            final = input("\nDo you wish to CONTINUE like a real adventurer this time or FLEE in terror again like coward?\n")
            final = final.lower()
            if final == "continue":
                room = "clearing"
                break
            elif final == "flee":
                room = "tower"
            else:
                print(descriptions["fail"])
                room = "homeville"

    print("\nWhere do you want to go next?")
    target = input("From here, you can reach " + " or ".join(path[room]) + ".\n")
    target = target.upper()
    
    if target in path[room]:
        target = target.lower()
        room = target
    else:
        print(descriptions["fail"])
        room = "homeville"

if room == "clearing":
    print(descriptions[room])
    medal = True