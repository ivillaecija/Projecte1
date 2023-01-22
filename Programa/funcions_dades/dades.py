import funcions_dades.dades

letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
             "J", "Z", "S", "Q", "V", "H", "L", "L", "C", "K", "E"]

cartas = {"ESP":{
"O01": { "nombre" : "As de Oros" , "value" : 1, "priority" : 4, "realValue" : 1},
"O02": { "nombre" : "Dos de Oros" , "value" : 2, "priority" : 4, "realValue" : 2},
"O03": { "nombre" : "Tres de Oros" , "value" : 3, "priority" : 4, "realValue" : 3},
"O04":{"nombre" : "Cuatro de Oros" , "value" : 4, "priority" : 4, "realValue" : 4},
"O05":{"nombre" : "Cinco de Oros" , "value" : 5, "priority" : 4, "realValue" : 5},
"O06":{"nombre" : "Seis de Oros" , "value" : 6, "priority" : 4, "realValue" : 6},
"O07":{"nombre" : "Siete de Oros" , "value" : 7, "priority" : 4, "realValue" : 7},
"O08":{"nombre" : "Ocho de Oros" , "value" : 8, "priority" : 4, "realValue" : 0.5},
"O09":{"nombre" : "Nueve de Oros" , "value" : 9, "priority" : 4, "realValue" : 0.5},
"O10":{"nombre" : "Diez de Oros" , "value" : 10, "priority" : 4, "realValue" : 0.5},
"O11":{"nombre" : "Once de Oros" , "value" : 11, "priority" : 4, "realValue" : 0.5},
"O12":{"nombre" : "Doce de Oros" , "value" : 12, "priority" : 4, "realValue" : 0.5},

"E01": { "nombre" : "As de Espadas" , "value" : 1, "priority" : 3, "realValue" : 1},
"E02": { "nombre" : "Dos de Espadas" , "value" : 2, "priority" : 3, "realValue" : 2},
"E03": { "nombre" : "Tres de Espadas" , "value" : 3, "priority" : 3, "realValue" : 3},
"E04":{"nombre" : "Cuatro de Espadas" , "value" : 4, "priority" : 3, "realValue" : 4},
"E05":{"nombre" : "Cinco de Espadas" , "value" : 5, "priority" : 3, "realValue" : 5},
"E06":{"nombre" : "Seis de Espadas" , "value" : 6, "priority" : 3, "realValue" : 6},
"E07":{"nombre" : "Siete de Espadas" , "value" : 7, "priority" : 3, "realValue" : 7},
"E08":{"nombre" : "Ocho de Espadas" , "value" : 8, "priority" : 3, "realValue" : 0.5},
"E09":{"nombre" : "Nueve de Espadas" , "value" : 9, "priority" : 3, "realValue" : 0.5},
"E10":{"nombre" : "Diez de Espadas" , "value" : 10, "priority" : 3, "realValue" : 0.5},
"E11":{"nombre" : "Once de Espadas" , "value" : 11, "priority" : 3, "realValue" : 0.5},
"E12":{"nombre" : "Doce de Espadas" , "value" : 12, "priority" : 3, "realValue" : 0.5},

"C01": { "nombre" : "As de Copas" , "value" : 1, "priority" : 2, "realValue" : 1},
"C02": { "nombre" : "Dos de Copas" , "value" : 2, "priority" : 2, "realValue" : 2},
"C03": { "nombre" : "Tres de Copas" , "value" : 3, "priority" : 2, "realValue" : 3},
"C04":{"nombre" : "Cuatro de Copas" , "value" : 4, "priority" : 2, "realValue" : 4},
"C05":{"nombre" : "Cinco de Copas" , "value" : 5, "priority" : 2, "realValue" : 5},
"C06":{"nombre" : "Seis de Copas" , "value" : 6, "priority" : 2, "realValue" : 6},
"C07":{"nombre" : "Siete de Copas" , "value" : 7, "priority" : 2, "realValue" : 7},
"C08":{"nombre" : "Ocho de Copas" , "value" : 8, "priority" : 2, "realValue" : 0.5},
"C09":{"nombre" : "Nueve de Copas" , "value" : 9, "priority" : 2, "realValue" : 0.5},
"C10":{"nombre" : "Diez de Copas" , "value" : 10, "priority" : 2, "realValue" : 0.5},
"C11":{"nombre" : "Once de Copas" , "value" : 11, "priority" : 2, "realValue" : 0.5},
"C12":{"nombre" : "Doce de Copas" , "value" : 12, "priority" : 2, "realValue" : 0.5},

"B01": { "nombre" : "As de Bastos" , "value" : 1, "priority" : 1, "realValue" : 1},
"B02": { "nombre" : "Dos de Bastos" , "value" : 2, "priority" : 1, "realValue" : 2},
"B03": { "nombre" : "Tres de Bastos" , "value" : 3, "priority" : 1, "realValue" : 3},
"B04":{"nombre" : "Cuatro de Bastos" , "value" : 4, "priority" : 1, "realValue" : 4},
"B05":{"nombre" : "Cinco de Bastos" , "value" : 5, "priority" : 1, "realValue" : 5},
"B06":{"nombre" : "Seis de Bastos" , "value" : 6, "priority" : 1, "realValue" : 6},
"B07":{"nombre" : "Siete de Bastos" , "value" : 7, "priority" : 1, "realValue" : 7},
"B08":{"nombre" : "Ocho de Bastos" , "value" : 8, "priority" : 1, "realValue" : 0.5},
"B09":{"nombre" : "Nueve de Bastos" , "value" : 9, "priority" : 1, "realValue" : 0.5},
"B10":{"nombre" : "Diez de Bastos" , "value" : 10, "priority" : 1, "realValue" : 0.5},
"B11":{"nombre" : "Once de Bastos" , "value" : 11, "priority" : 1, "realValue" : 0.5},
"B12":{"nombre" : "Doce de Bastos" , "value" : 12, "priority" : 1, "realValue" : 0.5},
},"POK":{
"D01":{"nombre" : "As de Diamantes" , "value" : 1, "priority" : 4, "realValue" : 1},
"D02":{"nombre" : "Dos de Diamantes" , "value" : 2, "priority" : 4, "realValue" : 2},
"D03":{"nombre" : "Tres de Diamantes" , "value" : 3, "priority" : 4, "realValue" : 3},
"D04":{"nombre" : "Cuatro de Diamantes" , "value" : 4, "priority" : 4, "realValue" : 4},
"D05":{"nombre" : "Cinco de Diamantes" , "value" : 5, "priority" : 4, "realValue" : 5},
"D06":{"nombre" : "Seis de Diamantes" , "value" : 6, "priority" : 4, "realValue" : 6},
"D07":{"nombre" : "Siete de Diamantes" , "value" : 7, "priority" : 4, "realValue" : 7},
"D08":{"nombre" : "Ocho de Diamantes" , "value" : 8, "priority" : 4, "realValue" : 0.5},
"D09":{"nombre" : "Nueve de Diamantes" , "value" : 9, "priority" : 4, "realValue" : 0.5},
"D10":{"nombre" : "Diez de Diamantes" , "value" : 10, "priority" : 4, "realValue" : 0.5},
"D11":{"nombre" : "Jota de Diamantes" , "value" : 11, "priority" : 4, "realValue" : 0.5},
"D12":{"nombre" : "Reina de Diamantes" , "value" : 12, "priority" : 4, "realValue" : 0.5},
"D13":{"nombre" : "Rey de Diamantes" , "value" : 13, "priority" : 4, "realValue" : 0.5},

"P01":{"nombre" : "As de Picas" , "value" : 1, "priority" : 3, "realValue" : 1},
"P02":{"nombre" : "Dos de Picas" , "value" : 2, "priority" : 3, "realValue" : 2},
"P03":{"nombre" : "Tres de Picas" , "value" : 3, "priority" : 3, "realValue" : 3},
"P04":{"nombre" : "Cuatro de Picas" , "value" : 4, "priority" : 3, "realValue" : 4},
"P05":{"nombre" : "Cinco de Picas" , "value" : 5, "priority" : 3, "realValue" : 5},
"P06":{"nombre" : "Seis de Picas" , "value" : 6, "priority" : 3, "realValue" : 6},
"P07":{"nombre" : "Siete de Picas" , "value" : 7, "priority" : 3, "realValue" : 7},
"P08":{"nombre" : "Ocho de Picas" , "value" : 8, "priority" : 3, "realValue" : 0.5},
"P09":{"nombre" : "Nueve de Picas" , "value" : 9, "priority" : 3, "realValue" : 0.5},
"P10":{"nombre" : "Diez de Picas" , "value" : 10, "priority" : 3, "realValue" : 0.5},
"P11":{"nombre" : "Jota de Picas" , "value" : 11, "priority" : 3, "realValue" : 0.5},
"P12":{"nombre" : "Reina de Picas" , "value" : 12, "priority" : 3, "realValue" : 0.5},
"P13":{"nombre" : "Rey de Picas" , "value" : 13, "priority" : 3, "realValue" : 0.5},

"C01":{"nombre" : "As de Corazones" , "value" : 1, "priority" : 2, "realValue" : 1},
"C02":{"nombre" : "Dos de Corazones" , "value" : 2, "priority" : 2, "realValue" : 2},
"C03":{"nombre" : "Tres de Corazones" , "value" : 3, "priority" : 2, "realValue" : 3},
"C04":{"nombre" : "Cuatro de Corazones" , "value" : 4, "priority" : 2, "realValue" : 4},
"C05":{"nombre" : "Cinco de Corazones" , "value" : 5, "priority" : 2, "realValue" : 5},
"C06":{"nombre" : "Seis de Corazones" , "value" : 6, "priority" : 2, "realValue" : 6},
"C07":{"nombre" : "Siete de Corazones" , "value" : 7, "priority" : 2, "realValue" : 7},
"C08":{"nombre" : "Ocho de Corazones" , "value" : 8, "priority" : 2, "realValue" : 0.5},
"C09":{"nombre" : "Nueve de Corazones" , "value" : 9, "priority" : 2, "realValue" : 0.5},
"C10":{"nombre" : "Diez de Corazones" , "value" : 10, "priority" : 2, "realValue" : 0.5},
"C11":{"nombre" : "Jota de Corazones" , "value" : 11, "priority" : 2, "realValue" : 0.5},
"C12":{"nombre" : "Reina de Corazones" , "value" : 12, "priority" : 2, "realValue" : 0.5},
"C13":{"nombre" : "Rey de Corazones" , "value" : 13, "priority" : 2, "realValue" : 0.5},

"T01":{"nombre" : "As de Treboles" , "value" : 1, "priority" : 1, "realValue" : 1},
"T02":{"nombre" : "Dos de Treboles" , "value" : 2, "priority" : 1, "realValue" : 2},
"T03":{"nombre" : "Tres de Treboles" , "value" : 3, "priority" : 1, "realValue" : 3},
"T04":{"nombre" : "Cuatro de Treboles" , "value" : 4, "priority" : 1, "realValue" : 4},
"T05":{"nombre" : "Cinco de Treboles" , "value" : 5, "priority" : 1, "realValue" : 5},
"T06":{"nombre" : "Seis de Treboles" , "value" : 6, "priority" : 1, "realValue" : 6},
"T07":{"nombre" : "Siete de Treboles" , "value" : 7, "priority" : 1, "realValue" : 7},
"T08":{"nombre" : "Ocho de Treboles" , "value" : 8, "priority" : 1, "realValue" : 0.5},
"T09":{"nombre" : "Nueve de Treboles" , "value" : 9, "priority" : 1, "realValue" : 0.5},
"T10":{"nombre" : "Diez de Treboles" , "value" : 10, "priority" : 1, "realValue" : 0.5},
"T11":{"nombre" : "Jota de Treboles" , "value" : 11, "priority" : 1, "realValue" : 0.5},
"T12":{"nombre" : "Reina de Treboles" , "value" : 12, "priority" : 1, "realValue" : 0.5},
"T13":{"nombre" : "Rey de Treboles" , "value" : 13, "priority" : 1, "realValue" : 0.5},
}}
menu03 = "".ljust(60) + "1)View Stats"+"\n"+ "".ljust(60) + "2)View Game Stats" + "\n"+ "".ljust(60) + "3)Set Bet" +"\n"+ "".ljust(60) + "4)Order Card" + "\n"+\
         "".ljust(60) + "5)Automatic Play" + "\n" + "".ljust(60) + "6)Stand"
players = {}
game = []
mazo = []
human_players = []
round_player_cards = []
max_rounds = 5
context_game = {"players":game,"typo_mazo":"ESP","mazo":mazo,"round": max_rounds}

deckgame = ""
cardgame = []
player_game = []
player_game_round = {}

cabecera_rankings = "".ljust(34) + "*"*72 + "\n" + "".ljust(34) + "Player ID".ljust(12) + "Name".ljust(22) + "Earnings".ljust(10) + \
                    "Games Played".ljust(14) + "Minutes Played" + "\n" + "".ljust(34) + "*"*72

tabla_rankings = {}
tabla_partida = {}
default = []
initial_card_most_repeated = {}
highest_bet = {}
lowest_bet = {}
percentatge_round_won_player = {}
games_won_bots = {}
bank_round_wins = {}
number_bank_users_game = {}
average_bet_game = {}
average_first_round_game = {}
average_last_round_game = {}

flg_game = True

