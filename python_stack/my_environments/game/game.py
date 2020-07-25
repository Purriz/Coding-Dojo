class Warrior:
    def __init__(self, w_type):
        self.health = 500
        self.type = w_type
    # an attack method
    def attack(self, target):
        # when target is hit, health points will drop
        if self.type == "ninja":
            target.warrior.health -= 50
            print(f"{self.type} threw a throwing star at {target.name}, it did 50 damage. Targets health: {target.warrior.health}")
        elif self.type == "wizard":
            target.warrior.health -= 75
            print(f"{self.type} shot a fireball at {target.name}, current target health: {target.warrior.health}")
        else:
            target.warrior.health -= 100
            print(f"{self.type} sliced {target.name} in half! Target health: {target.warrior.health}")
        return self

merlin = Warrior('wizard')
jack = Warrior('samurai')

# print(player_one)
# print(player_one.warrior)

# player_one.warrior.attack(player_three.warrior)


class Player:
    def __init__(self, name, w_type):
        self.name = name
        self.warrior = Warrior(w_type)
    def greet(self, message, other_player):
        print(f"{self.name} says {message} to {other_player.name}")
        return self
    def edit_name(self, new_name):
        self.name = new_name
        return self 

from player import *
# Creating players
player_one = Player('Pat', 'samurai')
player_two = Player('Ethan', 'wizard')
player_three = Player('Odion', 'ninja')

# printing player one data
print(player_one)
print(player_one.warrior)

# player one attacks
player_one.warrior.attack(player_three)