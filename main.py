from importlib import import_module
from tournament import Tournament
from player import Player

def create_player():
    id = input('id: ')
    first_name = input('name: ')
    return Player(id, first_name, 'lastname', 'm')

if __name__ == '__main__':
    # 1 on cree le tournois
    tournois = Tournament(None,input('Donner le nom du tournoi: '),10,'A tournament')
    # 2 on cree les joueurs
    tournois.players = [create_player(), create_player()]
    # 3 On lance la creation des rounds ou match
    tournois.create_match()
    breakpoint()

