class Match:

    def __init__(self, player_1, player_2):
        self.status = None
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = 0
        self.score_player_2 = 0

    def __str__(self):
        return f'Player {self.player_1.id}' \
               f' -- VS -- ' \
               f'Player {self.player_2.id}'

    def scoring(self):

        print(self)
        winner = input('Choose who won this match: ')
    
        if self.player_1.id == winner:
            self.player_1.score += 1

        elif self.player_2.id == winner:
            self.player_2.score += 1

        else:
            self.player_1.score = 0.5
            self.player_2.score = 0.5

