"""
This module for handling exceptions
"""

from datetime import datetime

"""class responsible for outputting the final score and saving the score to a table"""


class GameOver(Exception):
    def __init__(self, player):
        self.player = player
        self.output_of_result()
        self.saving_result()

    """after the game ends, displays the results on the screen"""

    def output_of_result(self):
        print(f"\n\tPLAYER_____{self.player.name}\n"
              f"\tSCORE________{self.player.score}\n")

    """responsible for maintaining the table of records and saving the results"""

    def saving_result(self):
        now_data = datetime.today()
        res = ["1. ", self.player.name, f"{now_data:%d-%m-%Y}", f"{now_data:%H:%M:%S}",
               str(self.player.score), '\n']

        with open("scores.txt", "a+") as scores_file:
            scores_file.write("|".join(res))
            scores_file.seek(0)

            # sorts the results
            res = sorted([line.split("|")[1:] for line in scores_file],
                         key=lambda x: int(x[3]), reverse=True)

        # save top 10 records
        with open("scores.txt", "w") as scores_file:
            for k, v in enumerate(res, 1):
                if k < 11:
                    scores_file.write(f"{k}. |" + '|'.join(v))


class EnemyDown(Exception):
    """
    for something important!
    """


class InvalidInput(Exception):
    """
    for something important!
    """
