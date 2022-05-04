from importlib import import_module
from match import Match
from tournament import Tournament
from player import Player


def create_player(id):
    
    first_name = input('name: ')
    return Player(id, first_name, 'lastname', 'm')


players =[]

if __name__ == '__main__':
    # 1 on cree le tournois
    #tournois = Tournament(input('Donner le nom du tournoi: '))
    # 2 on cree les joueurs
    #tournois.players = [create_player(), create_player()]
  
    i = 0
    while True:
        reponse =  input("ajouter un joueur O/N: ")
        if reponse == "O":
            nouv_joueur = create_player(i)
            players.append(nouv_joueur)
            i = i+1
        if len(players) in [2,4,6]:
             r = input("Finis d'ajouter des joueurs?: O/N")
             if r == "O":
                break

        if len(players) == 8:
            break
        if reponse == 'N':

            break
    
       
    match = Match()
    match.set_score(players[0].id,players[1].id)
    print(match)
        

    # 3 On lance la creation des rounds ou match
    #tournois.create_first_match()
    # maintenant on peut creer les autre match jusqua la fin du tournois
    # for in ....
    #tournois.create_other_match()
