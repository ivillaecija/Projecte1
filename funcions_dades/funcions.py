import funcions_dades.dades as dades
import random
import os
# Hace falta una funcion que pueda limpiar la pantalla.


def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[]):  # 1)
    while True:
        print(textOpts)
        opc = input(inputOptText)
        borrarPantalla()
        try:
            opc = int(opc)

            if opc in rangeList:
                return opc
            elif opc in exceptions:
                return opc
            else:
                print("="*65 + "Incorrect option" + "=" *65)
                input("Press enter to continue".center(146))
                borrarPantalla()


        except:
            if opc in exceptions:
                return opc
            else:
                print("="*65 + "Incorrect option" + "=" *65)
                input("Press enter to continue".center(146))
                borrarPantalla()


def borrarPantalla():
    if os.name == "posix":
       os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")


def shuffle():  # SHUFFLE CARDS
    mazo = list(dades.cartas[dades.context_game["typo_mazo"]].keys())
    for cards in range(len(mazo)):
        random_position = random.randint(0, len(mazo)) #GENERATE RANDOM PONSITION EACH LOOP
        mazo.insert(random_position,mazo[cards])  # INSERT A CARD S CLONE IN A RANDOM POSITION
        if random_position == (len(mazo)-1):  #DELETE THE OLD CARD
            mazo.pop(random_position)
        else:
            mazo.pop(random_position + 1)
    dades.context_game["mazo"] = mazo
    return mazo


def setGamePriority():  # SET PLAYERS PRIORITY
    players = orderAllPlayers()
    for p in players:
        dades.players[p]["priority"] = players.index(p)
    return players




def checkMinimun2PlayerWithPoints():
    try:
        if len(dades.context_game["players"]) < 2 :  # CHECK MINIMUM 2 PLAYERS
            raise ValueError("Minimum of 2 players needed")
        else:
            for player in dades.context_game["players"]:  # CHECK POINTS
                if dades.players[player]["points"] == 0:
                    raise ValueError("Pleyers with no points")
    except ValueError as e:
        print(e)


def orderAllPlayers():
    deck = shuffle()
    players = dades.context_game["players"]
    for i in players:
        dades.players[i]["initialCard"] = deck[0]  # ASSIGN A CARD TO EACH PLAYER IN THE GAME
        deck.remove(deck[0])  # REMOVE ASSIGNED CARD
    for pasadas in range(len(players) - 1):  # ORDER PLAYERS
        for player in range((len(players) - pasadas) - 1):
            if dades.cartas[dades.context_game["typo_mazo"]][dades.players[players[player]]["initialCard"]][
                "value"] < \
                    dades.cartas[dades.context_game["typo_mazo"]][dades.players[players[player + 1]]["initialCard"]][
                        "value"]:

                players[player], players[player + 1] = players[player + 1], players[player]

            elif (dades.cartas[dades.context_game["typo_mazo"]][dades.players[players[player]]["initialCard"]][
                      "value"] ==  # SAME VALUE, DIFFERENT TYPE
                  dades.cartas[dades.context_game["typo_mazo"]][dades.players[players[player + 1]]["initialCard"]][
                      "value"]) \
                    and (dades.cartas[dades.context_game["typo_mazo"]][dades.players[players[player]]["initialCard"]][
                             "priority"] <
                         dades.cartas[dades.context_game["typo_mazo"]][
                             dades.players[players[player + 1]]["initialCard"]]["priority"]):

                players[player], players[player + 1] = players[player + 1], players[player]

    for player in range(len(players)):
       if dades.players[players[player]]["bank"] == True:
            players.insert(0,players[player])
            if player == (len(players)-1):
                players.pop(player)
            else:
               players.pop(player + 1)
    return players

#Funciones Settings

# def setDeck():
#     opc = getOpt(dades.menu022,"Option")
#
#
# def settings():
#     opc = getOpt(dades.menu02, "Option:",[1,2,3,4])
#     if opc == 1:
#         print("Set Game Players")
#     elif opc == 2:
#         print("Set Card's Deck")
#     elif opc == 3:
#         print("Set Max Rounds")
#     elif opc == 4:
#         dades.flg_02 = False
#         dades.flg_00 = True



# def catch_humans(list_players):
#     humans = []
#     for player in list_players:
#         if dades.players[player]["human"] == True:
#             humans.append(player)
#     return humans

def showGameStats(list_id_players):
    players = dades.context_game["players"]
    cadena = ""
    if len(players) == 1:
        print("Stats of {}".format(dades.players[list_id_players]["name"]).center(100, "*"))
    else:
        print("Stats of players".center(100, "*") + "\n")

    titles = ["name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints"]
    for pasadas in titles:
        if pasadas in titles:
            cadena += pasadas.ljust(20)
        for datos in list_id_players:
            if pasadas == "name":
                cadena += str(dades.players[datos]["name"]).ljust(20)
            elif pasadas == "type":
                cadena += str(dades.players[datos]["type"]).ljust(20)
            elif pasadas == "human":
                cadena += str(dades.players[datos]["human"]).ljust(20)
            elif pasadas == "bank":
                cadena += str(dades.players[datos]["bank"]).ljust(20)
            elif pasadas == "initialCard":
                cadena += str(dades.players[datos]["initialCard"]).ljust(20)
            elif pasadas == "priority":
                cadena += str(dades.players[datos]["priority"]).ljust(20)
            elif pasadas == "bet":
                cadena += str(dades.players[datos]["bet"]).ljust(20)
            elif pasadas == "points":
                cadena += str(dades.players[datos]["points"]).ljust(20)
            elif pasadas == "cards" :
                cadena += str(dades.players[datos]["cards"]).ljust(20)
            elif pasadas == "roundPoints":
                cadena += str(dades.players[datos]["roundPoints"]).ljust(20)
        cadena += "\n"
    return cadena

def showPlayerStat(id_player):
    titles = ["name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints"]
    cadena = ""
    for t in titles:
        if t == "cards":
            cadena += t.rjust(55) + " ".ljust(5)
            for card in dades.players[id_player]["cards"]:
                cadena += card + ";"
            cadena = cadena[0:-1]

        else:
            cadena += t.rjust(55) + " ".ljust(5) + str(dades.players[id_player][t]) + "\n"
    return cadena

def setBet(id_player):
    while True:
        try:
            bet = input("How many points do you want to bet:")
            if not(bet.isdigit()):
                if bet == "":
                    raise ValueError("Bet can't be empty")
                elif bet[0] == "-" and  bet[1:].isdigit():
                    if int(bet) < 0:
                        raise ValueError("Bet has to be positive!")
                else:
                    raise TypeError("Bet has to be a number!")
            dades.players[id_player]["bet"] = bet
        except TypeError as e:
            print(e)
        except ValueError as e :
            print(e)

def takeCard(id_player):
    dades.players[id_player]["cards"].append(dades.context_game["mazo"][0])
    card_value = dades.cartas[dades.context_game["typo_mazo"]][dades.context_game["mazo"][0]]["realValue"]
    dades.context_game["mazo"].remove(dades.context_game["mazo"][0])
    return card_value


def orderCard(id_player,auto=False):
    player_cards_value = 0
    dng_cards = 0

    for ply_card in dades.players[id_player]["cards"]:  # CALCULATE THE PLAYERS CARD VALUE
        player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][ply_card]["realValue"]
    for card in dades.context_game["mazo"]:  # CALCULATE DANGEROUS CARDS
        if (dades.cartas[dades.context_game["typo_mazo"]][card]["realValue"] + player_cards_value) > 7.5:
            dng_cards += 1

    if (dades.players[id_player]["human"] == True) and (auto == False):
        if len(dades.players[id_player]["cards"]) >= 1:
            print("Chance of exceed 7.5 == ",round(dng_cards/len(dades.context_game["mazo"])*100,1),"%"+"\n")
            save = input("Are you sure do you want to order another card? Y/y = Yes, another key = Not")
            if save.lower() == "y":  # SAVE THE CARD IF YES
                print("The new card is " + dades.cartas[dades.context_game["typo_mazo"]][dades.context_game["mazo"]
                [0]]["nombre"])
                player_cards_value += takeCard(id_player)
                print("Now you have {} points".format(player_cards_value))  # PRINT CARD VALUE
            else:
                print("Card not saved")  # Card not saved
        else:
            print("The new card is " + dades.cartas[dades.context_game["typo_mazo"]][dades.context_game["mazo"]
            [0]]["nombre"])
            player_cards_value += takeCard(id_player)
            print("Now you have {} points".format(player_cards_value))  # PRINT CARD VALUE

        input("Enter to continue")
    elif (dades.players[id_player]["human"] == False) or (auto == True) :  # BOOT BEHAVIOUR
        if len(dades.players[id_player]["cards"]) == 0:
            player_cards_value += takeCard(id_player)

        if len(dades.players[id_player]["cards"]) >= 1:
            if dades.players[id_player]["type"] == 30:     #30 -> Cautious, 40 -> Moderated, 50 -> Bold
                if round(dng_cards/len(dades.context_game["mazo"])*100,1) <= 30:
                    player_cards_value += takeCard(id_player)
            elif dades.players[id_player]["type"] == 40:
                if round(dng_cards/len(dades.context_game["mazo"])*100,1) <= 50:
                    player_cards_value += takeCard(id_player)
            elif dades.players[id_player]["type"] == 50:
                if round(dng_cards/len(dades.context_game["mazo"])*100,1) <= 70:
                    player_cards_value += takeCard(id_player)
            print(player_cards_value)


shuffle()
orderCard("11115555A", auto=True)
