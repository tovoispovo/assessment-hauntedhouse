from os import system, name
import random
import math
from time import sleep
import time
from tqdm import tqdm

class Character:
    def __init__(self, class_name, strength, dexterity, intelligence):
        self.name = name
        self.lose_chance = lose
        self.health = health

def character_select():
    global player_class
    woman = Character
    man = Character

def clear():
        # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
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

def main_menu():
    while True:
        title_screen = input(TITLE)
        if (title_screen == "1"):
            break
        elif (title_screen != "1"):
            title_screen = input(TITLE)
        
main_menu()


sleep(2)


clear()

class State:
    def __init__(self, starting_loc):
        self.alive = True
        self.location = starting_loc
        self.locations = {}

    def addloc(self, position):
        self.locations[position.name] = position

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
                print ("  {0}. {1}").format(i, self.options[i].text)

    def get_choice(self, state):
        choice = input("> ")
        print ("You chose \"{0}\"").format(choice)
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
There is a door leading into the hall infront of you.""",
                    [Option("Left", GoToLocation("level 1 empty room")),
                     Option("Right", GoToLocation("blood room")),
                     Option("Forward", GoToLocation("level 1 hall")),
                     Option("Back", GoToLocation("start"))])

blood_room = Location("blood room", "It smells like body parts. I better leave quickly.",
                    [Option("Back", GoToLocation("entrance"))]) 

                    
level_1_hall = Location("level 1 hall",
                        """further down the hall.""",
                        [Option("Forward", GoToLocation("level 2 hall")),
                         Option("Left", GoToLocation("level 1 empty room")),
                         Option("Right", GoToLocation("frogs!")),
                         Option("Back", GoToLocation("entrance"))])

level_1_empty_room = Location("level 1 empty room",
"Why am i in here, this room is boring", 
                        [Option("Back", GoToLocation("level 1 hall"))])

   


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

frog_room = Location("frogs!", """Woah so many frogs!""", 
                        [Option("Back", GoToLocation("level 1 hall")),
                        Option('Explore',
                        MultiAction([Message("""        ()-()
      .-(___)-.
       _<   >_
jgs    \/   \/"""),OptionMutator("you pick up a frog", 2, Option("Poison", GoToLocation("entrance")))]))])



                        

if(__name__=="__main__"):
    s = State(start_loc)
    s.addloc(start_loc)
    s.addloc(entrance)
    s.addloc(upstairs)
    s.addloc(blood_room)
    s.addloc(level_1_empty_room)
    s.addloc(frog_room)
    s.addloc(level_1_hall)
    s.location.start()
    while(s.alive):
        s.location.print_opts()
        s.location.get_choice(s)
