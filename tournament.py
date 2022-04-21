
from match import Match
class Tournament:
    
    def __init__(self, id,
                 total_number_of_rounds=4, ongoing_round=1,
                 list_of_rounds=None, scores=None, opponents=None):

        

        self.id = id
        self.total_number_of_rounds = total_number_of_rounds
        self.ongoing_round = ongoing_round
        self.players = []
        self.list_of_rounds = list_of_rounds
        self.scores = scores
        self.opponents = opponents
        self.match = [] 
        
    def __str__(self):
        return f'{self.id}'



    def create_first_match(self):
        # match les gens au hasard.

        _players = []
        for player in self.players: # 0,1,2,3
            _players.append(player)
            if len(_players) == 2:
                self.match.append(Match(*_players)) # (_players[0],players[1])
                _players = []
        for match in self.match: # match1, match2
            match.scoring()
        


    def create_other_match(self):
        # a verifier que le sorting fonctionne bien
        self.players.sort(key=lambda x: x.score, reverse=True) # sort by score
        # une fois le sort fais on reprend la meme logique.
        _players = []
        for player in self.players: # 0,1,2,3
            _players.append(player)
            if len(_players) == 2:
                self.match.append(Match(*_players)) # (_players[0],players[1])
                _players = []
        for match in self.match: # match1, match2
            match.scoring()
        # match les gens avec les meme score

                