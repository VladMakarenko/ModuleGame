"""
Class responsible for the actions
of the player and the enemy
"""

from random import randrange

from game_exceptions import EnemyDown, GameOver, InvalidInput
from settings import HP, PROMPT

"""Enemy functionality"""


class Enemy:

    def __init__(self, level):
        self.level = level
        self.lives = self.level

    """attack function"""

    @staticmethod
    def select_attack():
        character = randrange(1, 4)
        return character

    """health reduction on failed attack/defense"""

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


"""Player functionality"""


class Player:
    lives = HP
    score = 0
    allowed_attacks = (1, 2, 3)

    def __init__(self, name):
        self.name = name

    """returns attack/defense result"""

    @staticmethod
    def fight(attack, defense):
        result = attack - defense
        if result in (-1, 2):
            return 1
        if result in (-2, 1):
            return -1
        return 0

    """health reduction on failed attack/defense"""

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise GameOver(self)

    """Called if something other than 1-3 is entered"""

    def valid(self, character):
        if character.isdigit():
            if int(character) in self.allowed_attacks:
                return int(character)
        print("\nInvalid input!\n",
              PROMPT)
        raise InvalidInput

    """attack function"""

    def attack(self, enemy_obj):
        while True:
            try:
                attack = self.valid(input("Enter attack: "))
                break
            except InvalidInput:
                pass
        defence = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            Player.score += 1
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        if result == -1:
            print("You missed!")
            self.decrease_lives()
            print(f"Your lives: {self.lives}")

    """defence function"""

    def defence(self, enemy_obj):
        while True:
            try:
                defence = self.valid(input("Enter defence: "))
                break
            except InvalidInput:
                pass
        attack = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("You missed!")
            self.decrease_lives()
            print(f"Your lives: {self.lives}")
        if result == -1:
            print("You defenced successfully!")
