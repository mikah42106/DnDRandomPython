import random
import math
import sys
import os
from PIL import Image, ImageDraw, ImageFont

file = sys.argv[1]
isfile = os.path.isfile(file)
isdir = os.path.isdir(file)
value = 3
raceval1 = 1
raceval2 = 9
classval1 = 1
classval2 = 12
hitdice = 0
level = 1
def image():
    global strengthmod, hitpoints, alignname, strength, dexteritymod, hitdice, dexterity, constitutionmod, constitution, intelligencemod, intelligence, wisdommod, wisdom, playername, charismamod, charisma, racestring, classname
    print('Processing')
    bigfont = ImageFont.truetype("/Library/Fonts/Arial.ttf", 100)
    medfont = ImageFont.truetype("/Library/Fonts/Arial.ttf", 60)
    medfont2 = ImageFont.truetype("/Library/Fonts/Arial.ttf", 70)
    medfont3 = ImageFont.truetype("/Library/Fonts/Arial.ttf", 50)
    img = Image.open(file)
    draw = ImageDraw.Draw(img)
    if len(str(strength)) == 2:
        draw.text((185, 650),"%s" % strength,(0,0,0), bigfont)
    else:
        draw.text((210, 650),"%s" % strength,(0,0,0), bigfont)
    draw.text((200, 770),"%s" % str(('{:+}'.format(strengthmod))),(0,0,0), medfont)
    if len(str(dexterity)) == 2:
        draw.text((185, 948),"%s" % dexterity,(0,0,0), bigfont)
    else:
        draw.text((210, 948),"%s" % dexterity,(0,0,0), bigfont)
    draw.text((210, 1068),"%s" % str(('{:+}'.format(dexteritymod))),(0,0,0), medfont)
    if len(str(constitution)) == 2:
        draw.text((185, 1245),"%s" % constitution,(0,0,0), bigfont)
    else:
        draw.text((210, 1245),"%s" % constitution,(0,0,0), bigfont)
    draw.text((210, 1365),"%s" % str(('{:+}'.format(constitutionmod))),(0,0,0), medfont)
    if len(str(intelligence)) == 2:
        draw.text((185, 1545),"%s" % intelligence,(0,0,0), bigfont)
    else:
        draw.text((210, 1545),"%s" % intelligence,(0,0,0), bigfont)
    draw.text((210, 1665),"%s" % str(('{:+}'.format(intelligencemod))),(0,0,0), medfont)
    if len(str(wisdom)) == 2:
        draw.text((185, 1845),"%s" % wisdom,(0,0,0), bigfont)
    else:
        draw.text((210, 1845),"%s" % wisdom,(0,0,0), bigfont)
    draw.text((210, 1965),"%s" % str(('{:+}'.format(wisdommod))),(0,0,0), medfont)
    if len(str(charisma)) == 2:
        draw.text((185, 2142),"%s" % charisma,(0,0,0), bigfont)
    else:
        draw.text((210, 2142),"%s" % charisma,(0,0,0), bigfont)
    draw.text((200, 2262),"%s" % str(('{:+}'.format(charismamod))),(0,0,0), medfont)
    draw.text((1125, 200),"%s  1" % classname,(0,0,0), medfont)
    draw.text((1125, 310),"%s" % racestring,(0,0,0), medfont)
    draw.text((1590, 310),"%s" % alignname,(0,0,0), medfont)
    draw.text((2000, 310),"0",(0,0,0), medfont)
    draw.text((1590, 200),"Hermit",(0,0,0), medfont) #Background
    draw.text((2000, 200),"%s" % str(playername),(0,0,0), medfont)
    draw.text((989, 607),"%s" % (str(11+dexteritymod).lstrip()),(0,0,0), medfont2)
    draw.text((1221, 607),"%s" % str(('{:+}'.format(dexteritymod))).lstrip(),(0,0,0), medfont2)
    draw.text((1472, 607),"30",(0,0,0), medfont2) #Speed
    draw.text((145, 2462),"%s" % (str(10+wisdommod).lstrip()),(0,0,0), medfont)
    draw.text((1205, 800),"%s" % str(hitpoints),(0,0,0), medfont2)
    draw.text((1030, 1320),"1d%s" % str(hitdice).lstrip(),(0,0,0), medfont3)
    img.show()
    return
def function():
    global strengthmod, hitpoints, alignname, hitdice, strength, dexteritymod, dexterity, constitutionmod, constitution, intelligencemod, intelligence, wisdommod, wisdom, charismamod, charisma, racestring, classname
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    alignment = random.randint(1, 9)
    alignmentstring = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good", 5: "Neutral", 6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral", 9: "Chaotic Evil"}
    alignname = alignmentstring.get(alignment)
    race = random.randint(raceval1, raceval2)
    classval = random.randint(classval1, classval2)

    if race == 1:
        racestring = "Dragonborn"
        strength = strength + 2
        charisma = charisma + 1
    elif race == 2:
        racestring = "Dwarf"
        constitution = constitution + 2
    elif race == 3:
        racestring = "Elf"
        dexterity = dexterity + 2
    elif race == 4:
        racestring = "Gnome"
        intelligence = intelligence + 2
    elif race == 5:
        racestring = "Half-Elf"
        charisma = charisma + 2
    elif race == 6:
        racestring = "Halfling"
        dexterity = dexterity + 2
    elif race == 7:
        racestring = "Half-Orc"
        strength = strength + 2
    elif race == 8:
        racestring = "Human"
        strength = strength + 1
        dexterity = dexterity + 1
        constitution = constitution + 1
        intelligence = intelligence + 1
        wisdom = wisdom + 1
        charisma = charisma + 1
    else:
        racestring = "Tiefling"
        charisma = charisma + 2
        intelligence = intelligence + 1

    classstring = {1: 'Barbarian', 2: 'Bard', 3: 'Cleric', 4: 'Druid', 5: 'Fighter', 6: 'Monk', 7: 'Paladin', 8: 'Ranger', 9: 'Rogue', 10: 'Sorcerer', 11: 'Warlock', 12: 'Wizard'}
    classname = classstring.get(classval)
    if classname == "Sorcerer" or classname == "Wizard":
        hitdice = 4
    elif classname == "Bard" or classname == "Rogue" or classname == "Warlock":
        hitdice = 6
    elif classname == "Cleric" or classname == "Druid" or classname == "Monk" or classname == "Ranger":
        hitdice = 8
    elif classname == "Fighter" or classname == "Paladin":
        hitdice = 10
    else:
        hitdice = 12
    strength = strength + random.randint(value, 18)
    dexterity = dexterity + random.randint(value, 18)
    constitution = constitution + random.randint(value, 18)
    intelligence = intelligence + random.randint(value, 18)
    wisdom = wisdom + random.randint(value, 18)
    charisma = charisma + random.randint(value, 18)
    hitdicerandom = random.randint(1, hitdice)

    strengthmod = int(math.floor((strength-10)/2))
    dexteritymod = int(math.floor((dexterity-10)/2))
    constitutionmod = int(math.floor((constitution-10)/2))
    intelligencemod = int(math.floor((intelligence-10)/2))
    wisdommod = int(math.floor((wisdom-10)/2))
    charismamod = int(math.floor((charisma-10)/2))
    hitpoints = hitdicerandom + constitutionmod

    print('\nYour race is', racestring)
    print('Your class is', classname)
    print('Your level is (%s)' % str(level))
    print('Your Hitpoints are (%s)' % str(hitpoints))
    print('Your HitDice is (1d%s)' % (str(hitdice).lstrip()))
    print('Your ArmorClass is (%s)' % (str(11+dexteritymod).lstrip()))
    print('Your PassivePerception is (%s)' % (str(10+wisdommod).lstrip()))
    print('Your InitiativeBonus is (%s)' % (str(dexteritymod).lstrip()))
    print('\nThe following are StatScore (Base + Racial Bonus) [Modifier]')
    if racestring == "Dragonborn" or race == 7:
        print('\nYour Strength is:', strength, "(%s + 2)" % str(strength-2), "[%s]" % str(('{:+}'.format(strengthmod))).strip())
    elif racestring == "Human":
        print('\nYour Strength is:', strength, "(%s + 1)" % str(strength-1), "[%s]" % str(('{:+}'.format(strengthmod))).strip())
    else:
        print('\nYour Strength is:', strength, "[%s]" % str(('{:+}'.format(strengthmod))).strip())
    if racestring == "Elf" or race == 6:
        print('Your Dexterity is:', dexterity, "(%s + 1)" % str(dexterity-2), "[%s]" % str(('{:+}'.format(dexteritymod))).strip())
    elif racestring == "Human":
        print('Your Dexterity is:', dexterity, "(%s + 1)" % str(dexterity-1), "[%s]" % str(('{:+}'.format(dexteritymod))).strip())
    else:
        print('Your Dexterity is:', dexterity, "[%s]" % str(('{:+}'.format(dexteritymod))).strip())
    if racestring == "Dwarf":
        print('Your Constitution is:', constitution, "(%s + 1)" % str(constitution-2), "[%s]" % str(('{:+}'.format(constitutionmod))).strip())
    elif racestring == "Human":
        print('Your Constitution is:', constitution, "(%s + 1)" % str(constitution-1), "[%s]" % str(('{:+}'.format(constitutionmod))).strip())
    else:
        print('Your Constitution is:', constitution, "[%s]" % str(('{:+}'.format(constitutionmod))).strip())
    if racestring == "Gnome":
        print('Your Intelligence is:', intelligence, "(%s + 1)" % str(intelligence-2), "[%s]" % str(('{:+}'.format(intelligencemod))).strip())
    elif racestring == "Human":
        print('Your Intelligence is:', intelligence, "(%s + 1)" % str(intelligence-1), "[%s]" % str(('{:+}'.format(intelligencemod))).strip())
    else:
        print('Your Intelligence is:', intelligence, "[%s]" % str(('{:+}'.format(intelligencemod))).strip())
    if racestring == "Human" or racestring == "Tiefling":
        print('Your Wisdom is:', wisdom, "(%s + 1)" % str(wisdom-1), "[%s]" % str(('{:+}'.format(wisdommod))).strip())
    else:
        print('Your Wisdom is:', wisdom, "[%s]" % str(('{:+}'.format(wisdommod))).strip())
    if racestring == "Dragonborn" or racestring == "Human":
        print('Your Charisma is:', charisma, "(%s + 1)" % str(charisma-1), "[%s]" % str(('{:+}'.format(charismamod))).strip())
    elif racestring == "Tiefling" or race == 5:
        print('Your Charisma is:', charisma, "(%s + 1)" % str(charisma-2), "[%s]" % str(('{:+}'.format(charismamod))).strip())
    else:
        print('Your Charisma is:', charisma, "[%s]\n" % str(('{:+}'.format(charismamod))).strip())
    if race == 5:
        print('\n for the following, you can enter a stat name or RANDOM (case-insensitive).')
        st = input("Because you are a Half-Elf, you get +1 to 2 stats, what is your first stat you would like to add +1 to? " )
        if st.lower() == "strength":
            strength = strength + 1
            print('New Strength:', strength)
        elif st.lower() == "dexterity":
            dexterity = dexterity + 1
            print('New Dexterity:', dexterity)
        elif st.lower() == "constitution":
            constitution = constitution + 1
            print('New Constitution:', constitution)
        elif st.lower() == "intelligence":
            intelligence = intelligence + 1
            print('New Intelligence:', intelligence)
        elif st.lower() == "charisma":
            charisma = charisma + 1
            print('New Charisma:', charisma)
        elif st.lower() == "wisdom":
            wisdom = wisdom + 1
            print('New Wisdom:', wisdom)
        elif st.lower() == "random":
            val = random.randint(1, 6)
            if val == 1:
                strength = strength + 1
                print('New Strength:', strength)
            elif val == 2:
                dexterity = dexterity + 1
                print('New Dexterity:', dexterity)
            elif val == 3:
                constitution = constitution + 1
                print('New Constitution:', constitution)
            elif val == 4:
                intelligence = intelligence + 1
                print('New Intelligence:', intelligence)
            elif val == 5:
                charisma = charisma + 1
                print('New Charisma:', charisma)
            else:
                wisdom = wisdom + 1
                print('New Wisdom:', wisdom)
        nd = input("2nd stat? " )
        if nd.lower() == "strength":
            strength = strength + 1
            print('New Strength:', strength)
        elif nd.lower() == "dexterity":
            dexterity = dexterity + 1
            print('New Dexterity:', dexterity)
        elif nd.lower() == "constitution":
            constitution = constitution + 1
            print('New Constitution:', constitution)
        elif nd.lower() == "intelligence":
            intelligence = intelligence + 1
            print('New Intelligence:', intelligence)
        elif nd.lower() == "charisma":
            charisma = charisma + 1
            print('New Charisma:', charisma)
        elif nd.lower() == "wisdom":
            wisdom = wisdom + 1
            print('New Wisdom:', wisdom)
        elif nd.lower() == "random":
            val = random.randint(1, 6)
            if val == 1:
                strength = strength + 1
                print('New Strength:', strength)
            elif val == 2:
                dexterity = dexterity + 1
                print('New Dexterity:', dexterity)
            elif val == 3:
                constitution = constitution + 1
                print('New Constitution:', constitution)
            elif val == 4:
                intelligence = intelligence + 1
                print('New Intelligence:', intelligence)
            elif val == 5:
                charisma = charisma + 1
                print('New Charisma:', charisma)
            else:
                wisdom = wisdom + 1
                print('New Wisdom:', wisdom)
        else:
            print('One of those is not a stat name.')
    image()
    return
def classinput():
    global classval1
    global classval2
    classyesno = input('\nDo you have a class you would like to be? (Yes or no?) ')
    if classyesno.lower() == "yes":
        classinput = int(input("\nWhat class? \n1: Barbarian \n2: Bard \n3: Cleric \n4: Druid \n5: Fighter \n6: Monk \n7: Paladin \n8: Ranger \n9: Rogue \n10: Sorcerer \n11: Warlock \n12: Wizard \n(Enter Value) "))
        classval1 = classinput
        classval2 = classinput
        function()
    elif classyesno.lower() == "no":
        classval1 = 1
        classval2 = 12
        function()
    return
def raceinput():
    global raceval2
    global raceval1
    raceyesno = input('\nDo you have a race you would like to be? (Yes or no?) ')
    if raceyesno.lower() == "yes":
        raceinput = int(input("\nWhat race? \n1: Dragonborn \n2: Dwarf \n3: Elf \n4: Gnome \n5: Half-Elf \n6: Halfling \n7: Half-Orc \n8: Human \n9: Tiefling \n(Enter Value) "))
        raceval1 = raceinput
        raceval2 = raceinput
        classinput()
    elif raceyesno.lower() == "no":
        raceval1 = 1
        raceval2 = 9
        classinput()
    return
global playername
playername = input("\nWhat is your name? " )
fullyrandom = input("\nWould you like your character to be fully random (Yes or no?) " )
if fullyrandom.lower() == "no":
    houserule = input("\nDo you have a house rule with a minimum stat value? (Yes or no?) " )
    if houserule.lower() == "yes":
        housevalue = int(input("What is the value? " ))
        if housevalue > 18:
            print('This number is bigger than 18!')
        else:
            value = housevalue
            raceinput()
    elif houserule.lower() == "no":
        raceinput()
else:
    function()
