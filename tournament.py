
from match import Match
class Tournament:
    
    def __init__(self, id,
                 list_of_rounds=None, scores=None):

        

        self.id = id
        self.players = []
        self.list_of_rounds = list_of_rounds
        self.scores = scores
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
        self.players = sorted(self.players, key=lambda x: x.get(""), reverse=True)
        # une fois le sort fais on reprend la meme logique.
        _players = []
        for player in self.players: # 0,1,2,3
            _players.append(player)
            if len(_players) == 2:
                self.match.append(Match(*_players)) # (_players[0],players[1])
                _players = []
        for match in self.match: # match1, match2
            match.scoring()
        # match les gens avec les memes scores

                