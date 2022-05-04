class Match:

    def __init__(self):
        self.score_player_1 = None
        self.score_player_2 = None

    def __str__(self):
        return f"scoring: {self.score_player_1[1]} -- {self.score_player_2[1]}"
                

    def set_score(self, id_player_1, id_player_2):

        
        winner = int(input(f'Choose who won this match ({id_player_1}, {id_player_2}): '))
    
        if id_player_1 == winner:
            self.score_player_1 = (id_player_1, 1)
            self.score_player_2 = (id_player_2, 0)

        elif id_player_2 == winner:
            self.score_player_2 = (id_player_2, 1)
            self.score_player_1 = (id_player_1, 0)
        else:
            self.score_player_1 = (id_player_1, 0.5)
            self.score_player_2 = (id_player_2, 0.5)

'''
def __init__(self, player1, player2):
  self.score_player_1 = (player1, 0)
  self.score_player_2 = (player2, 0)

def set_score(self):
  ...
  if (winner == self.score_player_1[0].id):
    self.score_player_1 = (self.score_player_1[0], 1)
    self.score_player_2 = (self.score_player_2[0], 0)
'''

