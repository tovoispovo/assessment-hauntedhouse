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

clear()

def clear():
        # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Player:
    def __init__(self, name, health, bag, room_name):
        self.name = name
        self.room = world[room_name]

player = Player("Bob", 100, [], "introd")



        

                                                                                    
