from os import system, name
import os
import random
import math
from time import sleep
import time
from tqdm import tqdm
import sys 
import random
import pickle

def clear():
        # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

for i in tqdm(range(0, 100), mininterval = 3, 
              desc ="LOADING GAME:"):
    sleep(.1)


TITLE = (""" __     __     ______     __         ______     ______     __    __     ______       
/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\      
\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\      
 \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\    
  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/
==================================================================================
┌─┐┬─┐┌─┐┌─┐┌─┐  ╔═╗╔╗╔╔═╗  ┌┬┐┌─┐  ┌┐ ┌─┐┌─┐┬┌┐┌
├─┘├┬┘├┤ └─┐└─┐  ║ ║║║║║╣    │ │ │  ├┴┐├┤ │ ┬││││
┴  ┴└─└─┘└─┘└─┘  ╚═╝╝╚╝╚═╝   ┴ └─┘  └─┘└─┘└─┘┴┘└┘
=================================================================================
""")

weapons = {"Level 2 Room Sword":40}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.pots = 0
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]
        
    @property 
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5
        
        if self.curweap == "Great Sword":
            attack += 15
            
        return attack

class SpiderQueen:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 150
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 100
SpiderQueenIG = SpiderQueen("SpiderQueen")

class Spiders:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 25
        self.health = self.maxhealth
        self.attack = 2
        self.goldgain = 5
SpidersIG = Spiders("Spiders")

class Bear:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 5
BearIG = Bear("Bear")

def main():
    print ("Welcome to my game!\n")
    print ("1.) Start")
    print ("2.) Load")
    print ("3.) Exit")
    option = input("-> ")
    if option == ("1"):
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print ("Loaded Save State...")
            option = input(' ')
            start1()
        else:
            print ("You have no save file for this game.")
            option = input(' ')
            main()
            
    elif option == ("3"):
        sys.exit()
    else:
        main()

def start():
    print ("Hello, what is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)

def start1():
    print ("Name: {!s}".format(PlayerIG.name))
    print ("Attack: %i" %(PlayerIG.attack))
    print ("Gold: %d" %(PlayerIG.gold))
    print ("Current Weapons: {!s}".format(PlayerIG.curweap)) 
    print ("Potions: %d" %(PlayerIG.pots))
    print ("Health: %i/%i\n" %(PlayerIG.health, PlayerIG.maxhealth))
    print ("1.) Play")
    print ("2.) Store")
    print ("3.) Save")
    print ("4.) Exit")
    print ("5.) Inventory")
    option = input("--> ")
    if option == ("1"):
        start2()
    elif option == ("2"):
        store()
    elif option == ("3"):
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print ("\nGame has been saved!\n")
        option = input(' ')
        start1()
    elif option == ("4"):
        sys.exit()
    elif option == ("5"):
        inventory()
    else:
        start1()

sleep(2)


clear()

class State:
    def __init__(self, starting_loc):
        self.alive = True
        self.location = starting_loc
        self.locations = {}

    def addloc(self, location):
        self.locations[location.name] = location

    def gotoloc(self, locname):
        self.location = self.locations[locname]
class Location:
    def __init__(self, name, desc, options=None):
        self.name = name
        self.desc = desc
        self.options = options

    def start(self):
        print (self.desc)

    def print_opts(self):
        if(self.options != None):
            for i in range(len(self.options)):
                print ("  {0}. {1}".format(i, self.options[i].text))

    def get_choice(self, state):
        choice = input("> ")
        print ("You chose \"{0}\"".format(choice))
        try:
            index = int(choice)
            self.options[index].action.execute(state)
            return True
        except Exception as e:
            print(e)
            print("Please choose a valid option")
            return False

class Option:
    def __init__(self, text, action):
        self.text = text
        self.action = action
class GoToLocation:
    def __init__(self, location):
        self.loc = location

    def execute(self, state):
        state.gotoloc(self.loc)
        state.location.start()

class KillPlayer:
    def __init__(self, message):
        self.message = message
        main()

    def execute(self, state):
        state.alive = False
        print(self.message)

start_loc = Location("start",
                     "You're standing at the entrance to a spooky mansion",
                     [Option("Go Inside", GoToLocation("entrance")),
                      Option("Leave", KillPlayer("Scardy Cat"))])

entrance = Location("entrance",
                    """You are standing in the entrance hall.
There is a room on the left, a room on the right, and a kitchen in the back.    
There is also a set of stairs in front of you.""",
                    [Option("Left", GoToLocation("level 0 empty room")),
                     Option("Right", GoToLocation("blood room")),
                     Option("Forward", GoToLocation("level 1 hall")),
                     Option("Back", GoToLocation("start"))])

blood_room = Location("blood room",
                      """ It smells like body parts in here and it is not a pleasant.
Can I leave already?""",
                      [Option("Back", GoToLocation("entrance"))])

                    
level_1_hall = Location("level 1 hall",
                        """further down the hall.""",
                        [Option("Forward", GoToLocation("level 2 hall")),
                         Option("Left", GoToLocation("level 1 empty room")),
                         Option("Right", GoToLocation("frogs!")),
                         Option("Back", GoToLocation("level 1 hall"))])

frog_room = Location("frogs!",
                     """frogs!
                         ()-()       
                       .-(___)-.
                        _<   >_
                        \/   \/
                         ()-()       
                       .-(___)-.
                        _<   >_
                        \/   \/
                         ()-()       
                       .-(___)-.
                        _<   >_
                        \/   \/
""",
                     [Option("I should leave quickly", GoToLocation("level_1_hall")),
                      Option("Explore", KillPlayer("The frogs were poisonous and you got poisoned. you died a painful death"))])


class Message:
    def __init__(self, msg):
        self.msg = msg
    def execute(self, state):
        print (self.msg)
class OptionMutator:
    def __init__(self, location, index, newoption):
        self.locname = location
        self.index = index
        self.newoption = newoption
    def execute(self, state):
        loc = state.locations[self.locname]
        if(self.index < 0 or self.index >= len(loc.options)):
            loc.options.append(self.newoption)
        else:
            loc.options[self.index] = self.newoption
class MultiAction:
    def __init__(self, actions=None):
        self.actions = actions
    def execute(self, state):
        if(self.actions == None): return
        for action in self.actions:
            action.execute(state)
            
upstairs = Location("upstairs", """You arrive in the attic.
It is very creepy up here""",
                       [Option("Downstairs", GoToLocation("entrance")),
                        Option("Explore",
                               MultiAction([Message("You find a trapdoor!"),
                                            OptionMutator("upstairs", 3, Option("Trapdoor", KillPlayer("You die. It was a trapped door.")))]))])
level_0_empty_room = Location("level 0 empty room",
                              "Seems pretty empty, should I explore?",
                              [Option("Back", GoToLocation("entrance")),
                               Option("Explore", MultiAction([Message("It's just a table of fruit"),
                                                              OptionMutator("level 0 empty room", 3, Option("Leave", GoToLocation("level 1 hall")))]))])




if(__name__=="__main__"):
    s = State(start_loc)
    s.addloc(start_loc)
    s.addloc(entrance)
    s.addloc(upstairs)
    s.addloc(level_1_hall)
    s.addloc(frog_room)
    s.addloc(blood_room)
    s.addloc(level_0_empty_room)
    s.location.start()
    while(s.alive):
        s.location.print_opts()
        s.location.get_choice(s)


def inventory():
    print ("what do you want to do?")
    print ("1.) Equip Weapon")
    print ("b.) go back")
    option = input(">>> ")
    if option == ("1"):
        equip()
    elif option == ('b'):
        start1()

def equip():
    print ("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print (weapon)
    print ("b to go back")
    option = input(">>> ")
    if option == PlayerIG.curweap:
        print ("You already have that weapon equipped")
        option = input(" ")
        equip()
    elif option == ("b"):
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print ("You have equipped {!s}.".format(option))
        option = input(" ")
        equip()
    else:
        print ("You don't have {!s} in your inventory".format(option))
    
    
    

def prefight():
    global enemy
    enemynum = random.randint(1, 2, 3)
    if enemynum == 1:
        enemy = SpiderQueenIG
    elif enemynum == 2:
        enemy = SpidersIG
    else:
        enemy = BearIG
    fight()
    
def fight():
    print ("%s     vs      %s" %(PlayerIG.name, enemy.name))
    print ("%s's Health: %d/%d    %s's Health: %i/%i" %(PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print ("Potions %i\n" %(PlayerIG.pots)) 
    print ("1.) Attack")
    print ("2.) Drink Potion")
    print ("3.) Run")
    option = input(' ')
    if option == ("1"):
        attack()
    elif option == ("2"):
        drinkpot()
    elif option == ("3"):
        run()
    else:
        fight()

def attack():
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.uniform(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print ("You miss!")
    else:
        enemy.health -= PAttack
        print ("You deal %i damage!" %(PAttack))
    option = input(' ')
    if enemy.health <=0:
        win()
    if EAttack == enemy.attack/2:
        print ("The enemy missed!")
    else:
        PlayerIG.health -= EAttack
        print ("The enemy deals %i damage!" %(EAttack))
    option = input(' ')
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()
    
def drinkpot():
    if PlayerIG.pots == 0:
        print ("You don't have any potions!")
    else:
        PlayerIG.health += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print ("You drank a potion!")
    option = input(' ')
    fight()

def run():
    runnum = random.randint(1, 3)
    if runnum == 1:
        print ("You have successfully ran away!")
        option = input(' ')
        start1()
    else:
        print ("You failed to get away!")
        option = input(' ')
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack/2:
            print ("The enemy missed!")
        else:
            PlayerIG.health -= EAttack
            print ("The enemy deals %i damage!" %(EAttack))
        option = input(' ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()

def win():
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    print ("You have defeated the {!s}".format(enemy.name))
    print ("You found %i gold!" %(enemy.goldgain))
    option = input(' ')
    start1()
    
def dead():
    print ("You have died")
    option = input(' ')
    
def store():
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    print ("1.) Great Sword")
    print ("back")
    print (" ")
    option = input(' ')
    
    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print ("You have bought {!s}".format(option))
            option = input(' ')
            store()
        
        else:
            print ("You don't have enough gold")
            option = input(' ')
            store()
    
    elif option == ("back"):
        start1()
    
    else:
        print ("That item does not exist")
        option = input(' ')
        store()
    
main()
