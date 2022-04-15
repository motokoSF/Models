
class Tournament:
    
    def __init__(self, id, name, date, time_control, description,
                 total_number_of_rounds=4, ongoing_round=1,
                 players=None, status='',
                 list_of_rounds=None, scores=None, opponents=None):


        self.id = id
        self.name = name
        self.date = date
        self.time_control = time_control
        self.description = description
        self.total_number_of_rounds = total_number_of_rounds
        self.ongoing_round = ongoing_round
        self.players = players
        self.status = status
        self.list_of_rounds = list_of_rounds
        self.scores = scores
        self.opponents = opponents
        
        
    def __str__(self):
        return f'{self.name}'