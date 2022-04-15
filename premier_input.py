
from match import Match
from player import Player
from round import Round


id = input("veuillez entrer votre ID: ")
firstname= input("veuillez entrer votre prénon: ")
lastname = input("veuillez entrer votre nom: ")
gender = input ("Genre du joueur (m masculin, f feminin) : ")
player_1 = Player(id,firstname,lastname, gender)
print(player_1)







player_1 = Player(1, "max", "Coh", "M")
print(player_1)
player_2 = Player(2, "albin", "Cap", "M")
print(player_2)
player_3 = Player(3, "alan", "avr", "M")
print(player_3)
player_4 = Player(4, "till", "DeR", "M")
print(player_4)
f_match = Match(player_1.id, player_2.id)
print(f_match)

round = Round("premier_tour","1")
print(round)  


      