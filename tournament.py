
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
        
        
    def __str__(self):
        return f'{self.id}'



    def create_match(self):
        # Match avec le bon algo
        # Suisse ou autre.
               nbre_matches = len(self.players) / 2
                self.match =  Match(self.players)
                self.match.scoring()

