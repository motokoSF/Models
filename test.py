from player import Player

def get_player(player):
    id = input("veuillez entrer votre ID: ")
    firstname= input("veuillez entrer votre prénon: ")
    lastname = input("veuillez entrer votre nom: ")
    gender = input ("Genre du joueur (m masculin, f feminin) : ")
    player = Player(id,firstname,lastname, gender)
    return print(player)


player_1 = get_player()