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
    players = dades.context_game["players"]
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
    players.append(players[0])
    players.pop(0)
    dades.players[players[-1]]["bank"]=True
    dades.game = players



# def catch_humans(list_players):
#     humans = []
#     for player in list_players:
#         if dades.players[player]["human"] == True:
#             humans.append(player)
#     return humans

def showGameStats(list_id_players):
    players = dades.context_game["players"]
    cadena = ""

    print("Stats of players".center(100, "*") + "\n")

    titles = ["name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints"]
    for pasadas in titles:
        if pasadas in titles:
            cadena += pasadas.ljust(20)
        for datos in list_id_players:
            cartas = ""
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
                if len(dades.players[datos]["cards"]) > 0:
                    for card in dades.players[datos]["cards"]:
                        cartas += card + ";"
                    cadena += str(cartas[0:-1]).ljust(20)
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
            cadena = cadena[0:-1] + "\n"

        else:
            cadena += t.rjust(55) + " ".ljust(6) + str(dades.players[id_player][t]) + "\n"
    return cadena

def setBet(id_player,id_bank):
    while True:
        try:
            bet = input("How many points do you want to bet:")
            if not(bet.isdigit()):
                if bet == "":
                    raise ValueError("Bet can't be empty")
                elif bet[0] == "-" and  bet[1:].isdigit():
                    if int(bet) < 0:
                        raise ValueError("Bet has to be positive!")
                elif "."  in  bet:
                    raise TypeError("Bet can't be float")
                else:
                    raise TypeError("Bet has to be a number!")
            elif int(bet) > int(dades.players[id_player]["points"]):
                raise ValueError("Bet can't be higher than points")
            elif int(bet) > int(dades.players[id_bank]["points"]):
                raise ValueError("Bet can't be higher than bank points")

            return bet
        except TypeError as e:
            print(e)
        except ValueError as e :
            print(e)

def takeCard(id_player):
    dades.players[id_player]["cards"].append(dades.context_game["mazo"][0])
    card_value = dades.cartas[dades.context_game["typo_mazo"]][dades.context_game["mazo"][0]]["realValue"]
    dades.round_player_cards.append(dades.context_game["mazo"][0])
    dades.context_game["mazo"].remove(dades.context_game["mazo"][0])



def orderCard(id_player,auto=False):
    player_cards_value = 0
    dng_cards = 0
    if len(dades.context_game["mazo"]) > 0:
        for ply_card in dades.round_player_cards:  # CALCULATE THE PLAYERS CARD VALUE
            player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][ply_card]["realValue"]
        for card in dades.context_game["mazo"]:  # CALCULATE DANGEROUS CARDS
            if (dades.cartas[dades.context_game["typo_mazo"]][card]["realValue"] + player_cards_value) > 7.5:
                dng_cards += 1

        if (dades.players[id_player]["human"] == True) and (auto == False):
            if len(dades.round_player_cards) >= 1:
                print("Chance of exceed 7.5 == ",round(dng_cards/len(dades.context_game["mazo"])*100),"%"+"\n")
                save = input("Are you sure do you want to order another card? Y/y = Yes, another key = Not")
                if save.lower() == "y":  # SAVE THE CARD IF YES
                    print("The new card is " + dades.cartas[dades.context_game["typo_mazo"]][dades.context_game["mazo"]
                    [0]]["nombre"])
                    takeCard(id_player)
                    player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][dades.round_player_cards[-1]]["realValue"]

                    print("Now you have {} points".format(player_cards_value))  # PRINT CARD VALUE
                else:
                    print("Card not saved")  # Card not saved
            else:
                print("The new card is " + dades.cartas[dades.context_game["typo_mazo"]][dades.context_game["mazo"]
                [0]]["nombre"])
                takeCard(id_player)
                player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][dades.round_player_cards[-1]]["realValue"]

                print("Now you have {} points".format(player_cards_value))  # PRINT CARD VALUE
                input("Enter to continue")
            dades.players[id_player]["roundPoints"] = player_cards_value

        elif (dades.players[id_player]["human"] == False) or (auto == True) :  # BOOT BEHAVIOUR
            if len(dades.round_player_cards) == 0:
                takeCard(id_player)
                player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][dades.round_player_cards[-1]]["realValue"]

            elif len(dades.round_player_cards) >= 1:
                if dades.players[id_player]["type"] == 30:     #30 -> Cautious, 40 -> Moderated, 50 -> Bold
                    if round(dng_cards/len(dades.context_game["mazo"])*100) <= 30:
                        if dades.players[id_player]["points"] > 14:
                            dades.players[id_player]["bet"] = round((dades.players[id_player]["points"]/100)*30)
                        else:
                            dades.players[id_player]["bet"] = 4
                        takeCard(id_player)
                        player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][dades.round_player_cards[-1]]["realValue"]

                    else:
                        dades.flg_game = False
                elif dades.players[id_player]["type"] == 40:
                    if round(dng_cards/len(dades.context_game["mazo"])*100) <= 50:
                        if dades.players[id_player]["points"] > 10:
                            dades.players[id_player]["bet"] = round((dades.players[id_player]["points"]/100)*40)
                        else:
                            dades.players[id_player]["bet"] = 4
                        takeCard(id_player)
                        player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][dades.round_player_cards[-1]]["realValue"]

                    else:
                        dades.flg_game = False

                elif dades.players[id_player]["type"] == 50:
                    if round(dng_cards/len(dades.context_game["mazo"])*100) <= 70:
                        if dades.players[id_player]["points"] > 8:
                            dades.players[id_player]["bet"] = round((dades.players[id_player]["points"]/100)*50)
                        else:
                            dades.players[id_player]["bet"] = 4
                        takeCard(id_player)
                        player_cards_value += dades.cartas[dades.context_game["typo_mazo"]][dades.round_player_cards[-1]]["realValue"]

                    else:
                        dades.flg_game = False
            dades.players[id_player]["roundPoints"] = player_cards_value
    else:
        shuffle()
        print("The deck has been shuffled !")


def order_by_priority(lista_ids):
    for pasadas in range(len(lista_ids) - 1):  # ORDER PLAYERS
        for player in range((len(lista_ids) - pasadas) - 1):
            if dades.players[lista_ids[player]]["priority"] < dades.players[lista_ids[player+1]]["priority"]:
                lista_ids[player], lista_ids[player + 1] = lista_ids[player + 1], lista_ids[player]
    return lista_ids

def game():

    orderAllPlayers()
    setGamePriority()

    round = 0
    p_winer = False
    bet_ban = False

    g_players = dades.game

    while dades.context_game["round"] != 0:

        eliminate_players = True
        pointer = 0
        candidatos_banka = []

        for id_player in g_players:
            dades.round_player_cards.clear()
            bet_ban = False
            dades.flg_game = True
            while dades.flg_game == True:
                if dades.players[id_player]["roundPoints"] < 7.5:
                    if dades.players[id_player]["human"] == False:
                        orderCard(id_player)
                    else:
                        opc = getOpt(dades.menu03,"Option:",[1,2,3,4,5,6])
                        if opc == 1:
                            print(showPlayerStat(id_player))
                        elif opc == 2:
                            print(showGameStats(dades.game))
                        elif opc == 3:
                            try:
                                if dades.players[id_player]["bank"] == True:  # CANT BET IF ITS THE BANK
                                    raise ValueError("The bank can't bet")
                                elif bet_ban == True:
                                    raise ValueError("Can't bet once a card has been ordered")  # IF ORDERED A CARD CANT BET
                                dades.players[id_player]["bet"] = setBet(id_player,g_players[-1])
                            except ValueError as e:
                                print(e)
                        elif opc == 4:
                            if dades.players[id_player]["roundPoints"] < 7.5:
                                orderCard(id_player)    # ORDER A CARD ACTIVATES BET BAN
                                bet_ban = True
                            else:
                                dades.flg_game = False
                        elif opc == 5:
                            orderCard(id_player, auto=True)
                            if g_players.index(id_player) != len(g_players):
                                print(showGameStats(dades.game))
                        elif opc == 6:
                            if g_players.index(id_player) != len(g_players):
                                print(showGameStats(dades.game))
                            dades.flg_game = False
                else:
                    dades.flg_game = False

        borrarPantalla()

        for i in range(len(g_players)-1):
            p_winer = False
            if dades.players[g_players[i]]["roundPoints"] == 7.5 and dades.players[g_players[-1]]["roundPoints"] != 7.5: # PLAYER 7.5 BANKA NO
                candidatos_banka.append(dades.game[i])
                p_winer = True
            elif dades.players[g_players[i]]["roundPoints"] <= dades.players[g_players[-1]]["roundPoints"] and \
                    (dades.players[g_players[-1]]["roundPoints"] <= 7.5):  #BANKA WINS PLAYER <= 7.5
                print("BG  wins puntuacion < 7.5")
                p_winer = False

            elif dades.players[g_players[i]]["roundPoints"] > dades.players[g_players[-1]]["roundPoints"] and \
                dades.players[g_players[i]]["roundPoints"] <= 7.5:  # PLAYER WINS BANKA < 7.5
                print("BG  loses puntuacion < 7.5")
                p_winer = True

            elif dades.players[g_players[i]]["roundPoints"] > 7.5 and dades.players[g_players[-1]]["roundPoints"] < 7.5:  # BANKA WINS PLAYER OVER 7.5
                print("BG  wins puntuacion_pl > 7.5")
                p_winer = False

            elif dades.players[g_players[i]]["roundPoints"] < 7.5 and dades.players[g_players[-1]]["roundPoints"] > 7.5:  # PLAYER WINS BANKA OVER 7.5
                print("BG  loses puntuacion_bl > 7.5")
                p_winer = True

            if p_winer == True:      # POINTS DISTRIBUTION
                if dades.players[g_players[i]]["roundPoints"] == 7.5 and dades.players[g_players[-1]][
                    "roundPoints"] != 7.5:  # PLAYER 7.5 BANKA NO
                    if (dades.players[g_players[i]]["bet"] * 2) > dades.players[g_players[-1]]["points"]:  # BANKA DOESNT HAVE ENOUGH POINTS
                        dades.players[g_players[i]]["points"] += dades.players[g_players[-1]]["points"]  # ALL POINTS GIVEN TO PLAYER
                        dades.players[g_players[-1]]["points"] = 0  # BANKA ELIMINATED WITH 0 POINTS7
                        print("Player Wins" + "\n" + "Banka is eliminated")
                    else:
                        dades.players[g_players[i]]["points"] += (dades.players[g_players[i]]["bet"] * 2)     # PLAYER WINS AND BANKA HAVE ENOUGH P
                        dades.players[g_players[-1]]["points"] -= (dades.players[g_players[i]]["bet"] * 2)      # CHANGE BANKA
                        candidatos_banka = order_by_priority(candidatos_banka)
                        dades.players[g_players[-1]]["bank"] = False
                        dades.players[candidatos_banka[0]]["bank"] = True
                        g_players = order_by_priority(g_players)
                        g_players.append(candidatos_banka[0])
                        g_players.remove(candidatos_banka[0])
                else:
                    dades.players[g_players[i]]["points"] += dades.players[g_players[i]]["bet"]
                    dades.players[g_players[-1]]["points"] -= dades.players[g_players[i]]["bet"]
            elif p_winer == False:
                dades.players[g_players[-1]]["points"] += dades.players[g_players[i]]["bet"]
                dades.players[g_players[i]]["points"] -= dades.players[g_players[i]]["bet"]

        while eliminate_players:
            print("Pointer {}".format(pointer))
            print(g_players)
            if dades.players[g_players[pointer]]["points"] <= 0:
                if dades.players[g_players[pointer]]["bank"] == True:
                    g_players.remove(g_players[pointer])
                    dades.players[g_players[0]]["bank"] = True
                    g_players.append(g_players[0])
                    g_players.remove(g_players[0])
                else:
                    g_players.remove(g_players[pointer])
            else:
                pointer += 1

            if pointer > len(g_players)-1 :
                eliminate_players = False

        for reset in g_players:
            dades.players[reset]["roundPoints"] = 0
            dades.players[reset]["cards"] = []

        if len(g_players) == 1:
            return g_players[0]
        round += 1
        print(" ROUND {} ".format(round).center(100,"*"))
        print(showGameStats(dades.game))
        dades.context_game["round"] -= 1

    for pasadas in range(len(g_players)-1):
        for winer in range(len(g_players)-1):
            if dades.players[g_players[winer]]["points"] < dades.players[g_players[winer+1]]["points"]:

                dades.players[g_players[winer]]["points"], dades.players[g_players[winer+1]]["points"] = \
                dades.players[g_players[winer+1]]["points"], dades.players[g_players[winer]]["points"]

            elif dades.players[g_players[winer]]["points"] == dades.players[g_players[winer+1]]["points"] and \
                 dades.players[g_players[winer+1]]["bank"] == True:

                dades.players[g_players[winer]]["points"], dades.players[g_players[winer + 1]]["points"] = \
                    dades.players[g_players[winer + 1]]["points"], dades.players[g_players[winer]]["points"]
    return g_players[0]



print(game())