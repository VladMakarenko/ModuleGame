"""
The main module for running the game
"""

from game_exceptions import GameOver, EnemyDown, InvalidInput
from models import Player, Enemy
from settings import GameOptions, PROMPT


def play():
    # accepts the name and outputs the greeting
    while True:
        user = input("Enter your name: ")

        if len(user.strip()):
            print(f"Hi, {user}!")
            print("*"*50)
            break

        print("\nInvalid input! Try entering the name again")

    print("\nEnter 'start' to start the game.\n"
          "Enter 'help' for see all commands.\n")

    # offers to enter start to start the game
    while True:
        try:

            action = GameOptions.action_distributor(input('Enter command: '))
            if action == "start":
                print(PROMPT)
                break
        except InvalidInput:
            print("\nInvalid input!")

    player = Player(user)
    level = 1
    enemy_obj = Enemy(level)

    # outputs attack/defense and in case of transition
    # to a new level creates a new enemy with a higher level
    while True:
        try:
            print("_"*50)
            player.attack(enemy_obj)
            print("_"*50)
            player.defence(enemy_obj)

        except EnemyDown:
            level += 1
            enemy_obj = Enemy(level)
            Player.score += 5
            print(f"\nYou win!\nLevel {level}")


# launch the game
if __name__ == '__main__':
    try:
        play()

    except GameOver:
        print("\nGame Over")

    except KeyboardInterrupt:
        pass

    finally:
        print("\nGood bye!")
