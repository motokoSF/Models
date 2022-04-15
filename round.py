


class Round:

    round_num = None
    matches = None
 
    def __init__(Self, round_num, matches = None):

        Self.name = f"Round {round_num}"
        Self.round_num = round_num
        
        if matches:
            Self.matches = matches
            
    def __str__(Self):
        return f'{Self.name}'

 