from room import Room
from player import Player

# Declare all the rooms

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

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']
# room['overlook'].s_to = room['foyer'] fy w.to ?
# room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("1", room['outside'])

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


# def get_room(local):
#     print(local.name)
#     print(local.description)
    
move_choices = ['n', 's', 'e', 'w'] 
def get_move():
    if mv not in move_choices:
        print('Invalid direction')
        return player.location
    else:
        if mv == 'n' and hasattr(player.location, 'n_to'):
            next_room = player.location.n_to
            #print(mv)
            return(next_room)
        elif mv == 's' and hasattr(player.location, 's_to'):
            next_room = player.location.s_to
            #print(mv)
            return(next_room)
        elif mv == 'e' and hasattr(player.location, 'e_to'):
            next_room = player.location.e_to
            #print(mv)
            return(next_room)
        elif mv == 'w' and hasattr(player.location, 'w_to'):
            next_room = player.location.w_to
            #print(mv)
            return(next_room)
        else:
            print("Can't go that way")
            return player.location
    

#def make_move(move): #takes in a move then sets player location to 

while True:

    mv = input('Where would u like to go? -> Type n, s, e, or w: ')
    if mv == 'q':
        print('Deuces!')
        break
    
    player.make_move(get_move())
    