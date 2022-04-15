class Player:
    
    def __init__(self, id, firstname, last_name, gender):
        self.id = id
        self.first_name = firstname
        self.last_name = last_name
        self.gender = gender
        self.rating = 0

    def __str__(self):
        return f' ID # {self.id} - {self.first_name} ' \
               f'{self.last_name} - Rating # {self.rating}'

    def get_rating(self):
        return self.rating

    def get_name(self):
        return self.last_name

