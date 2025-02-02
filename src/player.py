# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def make_move(self, new_location):
        self.location = new_location
        print(f'You are in the {self.location.name}')
        print(self.location.description)