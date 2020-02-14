from room import Room, Treasure
from player import Player
from item import Item
# Declare all the rooms

items = {
    'rock': Item('rock', 'its a rock'),
    'stone': Item('stone', 'its a stone')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Treasure("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Putting items in rooms
room['outside'].current_items = [items['rock'], items['stone']]
# room['outside'].add_items(items['rock'], items['stone'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(input('What is your name? '), room['outside'])

print(f'Hello {player.name} \n')
print(f'{player.current_room}')

while True: 
    cmd = input(">>").lower()
    direction = cmd[0]

    if direction in ["n", "s", "e", "w"]:
        player.travel(direction)
    elif direction == "i":
        player.inventory()
    elif direction == 'f':
        player.search()
    elif direction == 't':
        thing = cmd[2:]
        room_items = player.current_room.current_items
        # print(thing)
        # print(type(thing))
        player.take_item(items[thing])
        # print(room[player.current_room])
        # index = room_items.index(thing)
        # print(index)
        # print(player.current_room.current_items)
        # player.current_room.current_items.remove(str(thing))
    elif direction == 'd':
        thing = cmd[2:]
        player.drop_item(thing)
    elif direction == "q":
        exit()
    else: 
        print("I did not understand")

    