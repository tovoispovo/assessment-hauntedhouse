from os import system, name
import random
import math
from time import sleep
import time
from tqdm import tqdm

mylist = [1,2,3,4,5,6,7,8]
for i in tqdm(mylist):
    time.sleep(1)


TITLE = """ __     __     ______     __         ______     ______     __    __     ______       
/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\      
\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\      
 \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\    
  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/

==================================================================================


            ╔═╗╦═╗╔═╗╔═╗╔═╗  ╔═╗╔╗╔╔╦╗╔═╗╦═╗  ╔╦╗╔═╗  ╔╗ ╔═╗╔═╗╦╔╗╔
            ╠═╝╠╦╝║╣ ╚═╗╚═╗  ║╣ ║║║ ║ ║╣ ╠╦╝   ║ ║ ║  ╠╩╗║╣ ║ ╦║║║║
            ╩  ╩╚═╚═╝╚═╝╚═╝  ╚═╝╝╚╝ ╩ ╚═╝╩╚═   ╩ ╚═╝  ╚═╝╚═╝╚═╝╩╝╚╝

=================================================================================
"""
print(TITLE)

sleep(2)

def clear():
        # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

class Player:
    def __init__(self, name, health, bag, room_name):
        self.name = name
        self.room = world[room_name]
        self.health = health
        self.bag = bag
        
    def move(self, direction):
        if direction not in self.room.exits:
            print("Cannot move in that direction!")
            return
        new_room_name = self.room.exits['room']
        print('moving to', new_room_name)
        self.room = world[new_room_name]
        
player = Player("Bob", 100, [], "introd")

while True:
    command = raw_input('>>')
    if command in {'W', 'A', 'D'}:
        player.move(command)
    elif command == 'S':
        print(player.room.description)
        print('Exits', player.room.exits.keys())
    else:
        print('Invalid command')
    

class Room:
    def __init__(name, description, links):
        self.name = name
        self.description = description
        self.links = links

world = {}
world['introd'] = Room(
    "introd",
    """Welcome to my mansion, the door behind you is locked, you are stuck in here forever. If you listen to my commands you might survive. Move forward."""
    ['W', 'upstairs']
)
world['upstairs'] = Room(
    'upstairs',
    'You are now upstairs go to the right in to that hallway',
    ['S', 'introd']
)


