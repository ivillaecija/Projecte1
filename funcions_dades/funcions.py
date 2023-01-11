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


for i in dades.players:
    dades.game.append(i)
dades.context_game["typo_mazo"] = "ESP"
dades.players["22225555A"]["bank"] = True

print(setGamePriority())
players=setGamePriority()
for i in players:
    print(i," ",dades.players[i]["priority"])