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

 #an iterative progress bar
for i in tqdm(range(0, 100), mininterval = 3, 
              desc ="LOADING HAUNTED COMBAT HOUSE:"):
    sleep(.1)

#Prints the title screen when called
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

#Items that the user can buy
weapons = {"1":60, "2":100, "3":20, "4":10, "5":300, "6":20}

#Stats of the player
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
 #Defines damage of the weapons       
    @property 
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5
        
        if self.curweap == "Great Sword":
            attack += 60

        if self.curweap == "WarSpear":
            attack += 110
        
        if self.curweap == "Fighting Gloves":
            attack += 25

        if self.curweap == "Ghost Shard":
            attack += 8
        
        if self.curweap == "Holy Sword":
            attack += 200
        
        return attack
        
#Classes for Enemies, Sets their stats
class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15
ZombieIG = Zombie("Zombie")

class Ghoul:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 60
        self.health = self.maxhealth
        self.attack = 9
        self.goldgain = 15
GhoulIG = Ghoul("Ghoul")

class Spiders:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 20
        self.health = self.maxhealth
        self.attack = 3
        self.goldgain = 2
SpidersIG = Spiders("Spiders")

class Slimes:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 5
SlimesIG = Slimes("Slimes")

class Skeletons_Swords:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 50
Skeletons_SwordsIG = Skeletons_Swords("Skeletons_Swords")

class MasutaWarrior:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 65
        self.health = self.maxhealth
        self.attack = 50
        self.goldgain = 200
MasutaWarriorIG = MasutaWarrior("MasutaWarrior")

class Reaper_Boss:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 500
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 300
Reaper_BossIG = Reaper_Boss("Reaper_Boss")

class The_Wind_Waker_Boss:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 20
        self.goldgain = 500
The_Wind_Waker_BossIG = The_Wind_Waker_Boss("The_Wind_Waker_Boss")
#Main menu, displays options for the user
def main():
    os.system('cls')
    print (TITLE)
    print ("1.) Start")
    print ("2.) Load")
    print ("3.) Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
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
            
    elif option == "3":
        sys.exit()
    else:
        main()
#Asks the user their name
def start():
    os.system('cls')
    print ("Hello, what is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()
#Main function of the game
def start1():
    os.system('cls')
    print ("Name: %s" % (PlayerIG.name))
    print ("Attack: %i" % (PlayerIG.attack))
    print ("Gold: %d" % (PlayerIG.gold))
    print ("Current Weapons: %s" % (PlayerIG.curweap))
    print ("Potions: %d" % (PlayerIG.pots))
    print ("Health: %i/%i\n" % (PlayerIG.health, PlayerIG.maxhealth))
    print ("1.) Fight")
    print ("2.) Store")
    print ("3.) Save")
    print ("4.) Exit")
    print ("5.) Inventory")
    option = input("--> ")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        os.system('cls')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print ("\nGame has been saved!\n")
        option = input(' ')
        start1()
    elif option == "4":
        sys.exit()
    elif option == "5":
        inventory()
    else:
        start1()
#Here they can equip weapons and see what is available to equip
def inventory():
    os.system('cls')
    print ("what do you want to do?")
    print ("1.) Equip Weapon")
    print ("b.) go back")
    option = input(">>> ")
    if option == "1":
        equip()
    elif option == 'b':
        start1()

def equip():
    os.system('cls')
    print ("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print (weapon)
    print ("b to go back")
    option = input(">>> ")
    if option == PlayerIG.curweap:
        print ("You already have that weapon equipped")
        option = input(" ")
        equip()
    elif option == "b":
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print ("You have equipped %s." % (option))
        option = input(" ")
        equip()
    else:
        print ("You don't have %s in your inventory" % (option))
    
    
    
#Random function for choosing enemies
def prefight():
    global enemy
    enemynum = random.randint(1, 9)
    if enemynum == 1:
        enemy = GoblinIG
    elif enemynum == 2:
        enemy = ZombieIG
    elif enemynum == 3:
        enemy = GhoulIG
    elif enemynum == 4:
        enemy = SpidersIG
    elif enemynum == 5:
        enemy = SlimesIG
    elif enemynum == 6:
        enemy = Skeletons_SwordsIG
    elif enemynum == 7:
        enemy = MasutaWarriorIG
    elif enemynum == 8:
        enemy = Reaper_BossIG
    elif enemynum == 9:
        enemy = The_Wind_Waker_BossIG
    fight()
#Fight function, Player can choose whether to run, drink a potion, or attack the enemy
def fight():
    os.system('cls')
    print ("%s     vs      %s" % (PlayerIG.name, enemy.name))
    print ("%s's Health: %d/%d    %s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print ("Potions %i\n" % (PlayerIG.pots))
    print ("1.) Attack")
    print ("2.) Drink Potion")
    print ("3.) Run")
    option = input(' ')
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()
#This is based on their fighting stats
def attack():
    os.system('cls')
    PAttack = random.uniform(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.uniform(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print ("You miss!")
    else:
        enemy.health -= PAttack
        print ("You deal %i damage!" % (PAttack))
    option = input(' ')
    if enemy.health <=0:
        win()
    os.system('cls')
    if EAttack == enemy.attack/2:
        print ("The enemy missed!")
    else:
        PlayerIG.health -= EAttack
        print ("The enemy deals %i damage!" % (EAttack))
    option = input(' ')
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()
    
def drinkpot():
    os.system('cls')
    if PlayerIG.pots == 0:
        print ("You don't have any potions!")
    else:
        PlayerIG.health += 50
        PlayerIG.pots - 1
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print ("You drank a potion!")
    option = input(' ')
    fight()

def run():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print ("You have successfully ran away!")
        option = input(' ')
        start1()
    else:
        print ("You failed to get away!")
        option = input(' ')
        os.system('cls')
        EAttack = random.uniform(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack/2:
            print ("The enemy missed!")
        else:
            PlayerIG.health -= EAttack
            print ("The enemy deals %i damage!" % (EAttack))
        option = input(' ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()

def win():
    os.system('cls')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    PlayerIG.pots += 1
    print ("You have defeated the %s" % (enemy.name))
    print ("You found %i gold!" % (enemy.goldgain))
    option = input(' ')
    start1()
    
def dead():
    os.system('cls')
    print ("You have died")
    option = input(' ')
    
def store():
    os.system('cls')
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    print ("1.) Great Sword, 60 gold: is strong against the foes in here!")
    print ("2.) WarSpear, 100 gold: It's quite pointy.")
    print ("3.) Fighting Gloves, 20 gold: Packs a punch!")
    print ("4.) Ghost Shard, 10 gold: I guess you can use this as a weapon but it's not that effective.")
    print ("5.) Holy Sword, 300 Gold: The sword that wields the power of the Gods!")
    print ("back")
    print (" ")
    option = input(' ')
    
    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            os.system('cls')
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print ("You have bought %s" % (option))
            option = input(' ')
            store()
        
        else:
            os.system('cls')
            print ("You don't have enough gold")
            option = input(' ')
            store()
    
    elif option == "back":
        start1()
    
    else:
        os.system('cls')
        print ("That item does not exist")
        option = input(' ')
        store()
    
main()
