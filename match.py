class Match:

    def __init__(self, id_player_1, id_player_2):
        self.status = None
        self.id_player_1 = id_player_1
        self.id_player_2 = id_player_2
        self.score_player_1 = 0
        self.score_player_2 = 0

    def __str__(self):
        return f'Player {self.id_player_1} ({self.score_player_1} pts)' \
               f' -- VS -- ' \
               f'Player {self.id_player_2} ({self.score_player_2} pts)'

    def scoring(self):

        print(self)
        winner = input('Choose who won this match: ')
    
        if self.id_player_1 == winner:
            self.score_player_1 = 1

        elif self.id_player_2 == winner:
            self.score_player_2 = 1

        else:
            self.score_player_1 = 0.5
            self.score_player_2 = 0.5

