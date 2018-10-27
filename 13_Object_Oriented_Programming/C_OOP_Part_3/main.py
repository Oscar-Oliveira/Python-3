"""
OOP - Game
"""
import random
from room import Room
from character import Hero, Enemy

DIRECTIONS = ["N", "S", "E", "W"]

def layout(castle):
    castle.append(Room("Room 1", "Room identified by id 1"))
    castle.append(Room("Room 2", "Room identified by id 2"))
    castle.append(Room("Room 3", "Room identified by id 3"))
    castle.append(Room("Room 4", "Room identified by id 4"))

    '''
    Room layout
    ROOM 1 [0] | ROOM 2 [1]
    ROOM 3 [2] | ROOM 4 [3]
    '''
    castle[0].link_to_room(castle[1], DIRECTIONS[2])
    castle[0].link_to_room(castle[2], DIRECTIONS[1])
    castle[1].link_to_room(castle[0], DIRECTIONS[3])
    castle[1].link_to_room(castle[3], DIRECTIONS[1])
    castle[2].link_to_room(castle[0], DIRECTIONS[0])
    castle[2].link_to_room(castle[3], DIRECTIONS[2])
    castle[3].link_to_room(castle[1], DIRECTIONS[0])
    castle[3].link_to_room(castle[2], DIRECTIONS[3])

def main():

    player = Hero("King", "The brave king of nowhere!")
    player.Talk = "Who is here?"

    enemy = Enemy("Wizard", "The evil wizard!")
    enemy.Talk = "Your worst enemy!!!!"

    castle = []
    layout(castle)
    current_room = castle[0]

    castle[random.randint(1, len(castle)-1)].Character = enemy

    print(player)
    print("I'm in:")
    print(current_room)

    print()
    while True:
        direction = input("Where to ? ").upper()
        if direction == "EXIT":
            break
        print()
        if direction in DIRECTIONS:
            current_room = current_room.move_to_direction(direction)
            print(current_room)
            if current_room.Character:
                print(player.Talk)
                print(enemy.Talk)
                if player.fight(current_room.Character):
                    print("\nWell done you have defeated your enemy!\n")
                    break
                print(player.Back)
                player.change_weapon()
        print()

if __name__ == "__main__":
    main()
    print("done!!")
