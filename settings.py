"""
Module for settings game
"""

from game_exceptions import InvalidInput

HP = 3
COMMANDS = ("start", "scores", "help", "exit")
PROMPT = ("Choose to defend or attack:\n"
          "Mage - (1), Warrior - (2), Rogue - (3)")

"""game menu class"""


class GameOptions:
    """list of menu commands"""

    @staticmethod
    def action_distributor(command):
        command = command.strip().lower()
        if command in COMMANDS:
            if command == "start":
                return command
            if command == "scores":
                return GameOptions.scores(command)
            if command == "help":
                return GameOptions.help(command)
            if command == "exit":
                return GameOptions.exit()
        raise InvalidInput

    """show game menu"""

    @staticmethod
    def help(command):
        print("\t'start'  ⏩ to start the game.\n"
              "\t'scores' ⏩ to get a table of records.\n"
              "\t'exit'   ⏩ to exit the game.")
        return command

    """show game scores"""

    @staticmethod
    def scores(command):
        with open("scores.txt") as scores_file:
            for line in scores_file:
                print(line)
        return command

    @staticmethod
    def exit():
        raise KeyboardInterrupt
