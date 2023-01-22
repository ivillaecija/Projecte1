import random
import funcions_dades.dades
import os
import mysql.connector
import datetime
import time

def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[], borrar_pantalla="no"):  # 1)
    while True:
        print(textOpts)
        opc = input(inputOptText)
        try:
            opc = int(opc)
            if opc in rangeList:
                return opc
            elif opc in exceptions:
                return opc
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                if borrar_pantalla:
                    borrarPantalla()
        except:
            if opc in exceptions:
                return opc
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                if borrar_pantalla:
                    borrarPantalla()

def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def newPlayer(dni="", name="", profile="", human=""):
    funcions_dades.dades.players = {}
    charge_bbdd_players()
    menu_profile = "".ljust(38) + "Select your Profile:" + "\n" + "".ljust(38) + "1)Cautious" + "\n" + "".ljust(
        38) + "2)Moderated" + "\n" + "".ljust(38) + "3)Bold"
    while True:
        borrarPantalla()
        name = input("".ljust(38) + "Name: ")
        if not name.isalpha():
            print("".ljust(38) + "Incorrect name, please, enter a name not empty with only letters")
            input("".ljust(38) + "Enter to continue")
            borrarPantalla()
        else:
            break
    if human == True:
        while True:
            nif = input("".ljust(38) + "Enter NIF: ")
            if not (len(nif) == 9 and nif[:8].isdigit() and nif[8].isalpha() and nif[8].upper() ==
                    funcions_dades.dades.letrasDni[int(nif[:8]) % 23]):
                print("".ljust(38) + "Wrong NIF")
                input("".ljust(38) + "Enter to continue")
                borrarPantalla()
            elif nif.upper() in funcions_dades.dades.players.keys():
                print("".ljust(38) + "NIF {} already exists".format(nif.upper()))
                input("".ljust(38) + "Enter to continue")
                borrarPantalla()
            else:
                nif = nif.upper()
                borrarPantalla()
                break
    elif human == False:
        borrarPantalla()
        nif = str(random.randint(1, 9))
        for i in range(1, 8):
            nif += str(random.randint(1, 9))
        letra = funcions_dades.dades.letrasDni[int(nif) % 23]
        nif = nif + letra
    while True:
        cadena = ("".ljust(38) + "Name:".ljust(10) + name.rjust(20) + "\n" + "".ljust(38) + "DNI:".ljust(
            10) + nif.rjust(20) + "\n")
        opc = getOpt("\n" + cadena + "\n" + menu_profile, "".ljust(38) + "Option: ", [1, 2, 3])
        if opc == 1:
            valor_apuestas = 30
            perfil_apuestas = "Caotiuos"
            break
        elif opc == 2:
            valor_apuestas = 40
            perfil_apuestas = "Normal"
            break
        elif opc == 3:
            valor_apuestas = 50
            perfil_apuestas = "Bold"
            break
    cadena_new_player = ("\n" +
                         "".ljust(38) + "Name:".ljust(10) + name.rjust(20) + "\n" + "".ljust(38) + "DNI:".ljust(
                10) + nif.rjust(20)
                         + "\n" + "".ljust(38) + "Profile:".ljust(10) + perfil_apuestas.rjust(20) + "\n")
    borrarPantalla()
    save_player = getOpt(cadena_new_player, "".ljust(38) + "Is ok ? Y/n: ", [], ["Y", "y", "N", "n"])
    if save_player == "y" or save_player == "Y":
        new_bbdd_player(nif, name, valor_apuestas, human)
        return
    elif save_player == "n" or save_player == "N":
        return

def show_players():
    funcions_dades.dades.players = {}
    charge_bbdd_players()
    borrarPantalla()
    cabecera_show_players = ("*" * 140 + "\n" + "*" * 63 + "Select Players" + "*" * 63 + "\n" + "".ljust(29)
                             + "Boot Players" + "".ljust(29) + "||" + "".ljust(29) + "Human Players" + "".ljust(26)
                             + "\n" + "-" * 140 + "\n" + "ID".ljust(20) + "Name".ljust(25) + "Type".ljust(25) + "||" +
                             " " + "ID".ljust(20) + "Name".ljust(25) + "Type".ljust(22) + "\n" + "*" * 140)
    human_players = []
    boot_players = []
    for player in funcions_dades.dades.players.keys():
        if player not in human_players and funcions_dades.dades.players[player]["human"] == True:
            human_players.append(player)
        elif player not in boot_players and funcions_dades.dades.players[player]["human"] == False:
            boot_players.append(player)

    for pasadas in range(len(human_players) - 1):
        for player in range(len(human_players) - 1 - pasadas):
            if human_players[player] > human_players[player + 1]:
                aux = human_players[player]
                human_players[player] = human_players[player + 1]
                human_players[player + 1] = aux

    for pasadas in range(len(boot_players) - 1):
        for player in range(len(boot_players) - 1 - pasadas):
            if boot_players[player] > boot_players[player + 1]:
                aux = boot_players[player]
                boot_players[player] = boot_players[player + 1]
                boot_players[player + 1] = aux
    while True:
        while True:
            if len(human_players) > len(boot_players):
                boot_players.append("")
            elif len(boot_players) > len(human_players):
                human_players.append("")
            else:
                break

        cadena = ""
        if len(human_players) == 0:
            print(cabecera_show_players)
            return
        else:
            for player in range(len(human_players)):
                cadena += "\n" + boot_players[player].ljust(20)
                if boot_players[player] in funcions_dades.dades.players.keys():
                    cadena += funcions_dades.dades.players[boot_players[player]]["name"].ljust(25)
                    if funcions_dades.dades.players[boot_players[player]]["type"] == 30:
                        cadena += "Caotious".ljust(25) + "|| "
                    elif funcions_dades.dades.players[boot_players[player]]["type"] == 40:
                        cadena += "Normal".ljust(25) + "|| "
                    elif funcions_dades.dades.players[boot_players[player]]["type"] == 50:
                        cadena += "Bold".ljust(25) + "|| "
                else:
                    cadena += "".ljust(50) + "|| "
                cadena += human_players[player].ljust(20)
                if human_players[player] in funcions_dades.dades.players.keys():
                    cadena += funcions_dades.dades.players[human_players[player]]["name"].ljust(25)
                    if funcions_dades.dades.players[human_players[player]]["type"] == 30:
                        cadena += "Caotious".ljust(22)
                    elif funcions_dades.dades.players[human_players[player]]["type"] == 40:
                        cadena += "Normal".ljust(22)
                    elif funcions_dades.dades.players[human_players[player]]["type"] == 50:
                        cadena += "Bold".ljust(22)
                else:
                    cadena += "".ljust(47)
            borrarPantalla()
            cadena += "\n" * 2 + "*" * 140
            print(cabecera_show_players + cadena)
            return

def remove_players():
    funcions_dades.dades.players = {}
    charge_bbdd_players()
    while True:
        human_players = []
        boot_players = []
        for player in funcions_dades.dades.players.keys():
            if player not in human_players and funcions_dades.dades.players[player]["human"] == True:
                human_players.append(player)
            elif player not in boot_players and funcions_dades.dades.players[player]["human"] == False:
                boot_players.append(player)
        show_players()
        remove_player = input("Option ( -id to remove player, -1 to exit):\n".center(140))
        if len(remove_player) != 2 and len(remove_player) != 10:
            print("=" * 63 + "Invalid option" + "=" * 63)
            input("Press enter to continue".center(140))
            borrarPantalla()
        elif remove_player == "-1":
            break
        elif remove_player[0] == "-" and remove_player[1:].upper() in funcions_dades.dades.players.keys():
            remove_bbdd_player(nif=remove_player[1:].upper())

def show_setting_players():
    cabecera_setting_players = ("".ljust(40) + "*" * 19 + "Actual Players In Game" + "*" * 18 + "".rjust(40))
    if len(funcions_dades.dades.player_game) == 0 or len(funcions_dades.dades.players) == 0:
        print("\n" * 3 + cabecera_setting_players + "\n" + "".ljust(57) + "There is no players in game" + "".ljust(57))
        input("".ljust(61) + "Enter to continue" + "\n")
        borrarPantalla()
        return
    else:
        while True:
            cadena_players_game = ""
            for player in funcions_dades.dades.player_game:
                perfil_apuestas = ""
                if funcions_dades.dades.players[player]["human"]:
                    human_player_game = "Human"
                else:
                    human_player_game = "Boot"
                if funcions_dades.dades.players[player]["type"] == 30:
                    perfil_apuestas = "Caotiuos"
                elif funcions_dades.dades.players[player]["type"] == 40:
                    perfil_apuestas = "Normal"
                elif funcions_dades.dades.players[player]["type"] == 50:
                    perfil_apuestas = "Bold"
                cadena_players_game += "\n" + "".ljust(40) + str(player).ljust(12) + funcions_dades.dades.players[player][
                        "name"].ljust(20) + human_player_game.ljust(10) + perfil_apuestas.ljust(18)

            print("\n" * 3 + cabecera_setting_players + cadena_players_game + "\n")
            input("".ljust(61) + "Enter to continue" + "".ljust(62))
            borrarPantalla()
            return

def settings_players():
    show_setting_players()
    if len(funcions_dades.dades.player_game) == 0 or len(funcions_dades.dades.players) == 0:
        while True:
            show_players()
            opc = input("".ljust(
                20) + "Option (id to add to game, -id to remove player, sh to show actual players in game, -1 to go back:")
            if len(opc) != 2 and len(opc) != 10 and len(opc) != 9:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()
            elif opc == "-1":
                break
            elif opc[0] == "-" and opc[1:].upper() in funcions_dades.dades.player_game:
                funcions_dades.dades.player_game.remove(opc[1:].upper())
                show_setting_players()
            elif opc.upper() in funcions_dades.dades.players.keys():
                if len(funcions_dades.dades.player_game) >= 6:
                    print()
                    print("Maxim number of players in game reached!!".center(140))
                    show_setting_players()
                elif opc.upper() in funcions_dades.dades.player_game:
                    funcions_dades.dades.player_game.remove(opc.upper())
                    funcions_dades.dades.player_game.append(opc.upper())
                    show_setting_players()
                else:
                    funcions_dades.dades.player_game.append(opc.upper())
                    show_setting_players()
            elif opc.lower() == "sh":
                show_setting_players()
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()
    else:
        while True:
            show_players()
            opc = input("".ljust(
                20) + "Option (id to add to game, -id to remove player, sh to show actual players in game, -1 to go back:")
            if len(opc) != 2 and len(opc) != 10 and len(opc) != 9:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()
            elif opc == "-1":
                break
            elif opc[0] == "-" and opc[1:].upper() in funcions_dades.dades.player_game:
                funcions_dades.dades.player_game.remove(opc[1:].upper())
                borrarPantalla()
            elif opc.upper() in funcions_dades.dades.players.keys():
                if len(funcions_dades.dades.player_game) >= 6:
                    print()
                    print("Maxim number of players in game reached!!".center(140))
                    show_setting_players()
                elif opc.upper() in funcions_dades.dades.player_game:
                    funcions_dades.dades.player_game.remove(opc.upper())
                    funcions_dades.dades.player_game.append(opc.upper())
                    show_setting_players()
                else:
                    funcions_dades.dades.player_game.append(opc.upper())
                    show_setting_players()
            elif opc.lower() == "sh":
                show_setting_players()

def settings_decks():
    borrarPantalla()
    menu_decks = "".ljust(47) + "1) ESP - ESP" + "\n" + "".ljust(47) + "2) POK - POK" + "\n" + "".ljust(
        47) + "0) Go back"
    opc = getOpt(menu_decks, "".ljust(47) + "Option: ", [1, 2, 0], borrar_pantalla=True)
    if opc == 0:
        return
    elif opc == 1:
        funcions_dades.dades.deckgame = "ESP"
        funcions_dades.dades.context_game["typo_mazo"] = "ESP"
        print("".ljust(47) + "Established Card Deck ESP, Baraja Española")
        input("".ljust(47) + "Enter to continue")
    elif opc == 2:
        funcions_dades.dades.deckgame = "POK"
        funcions_dades.dades.context_game["typo_mazo"] = "POK"
        print("".ljust(47) + "Established Card Deck POK, Poker Deck")
        input("".ljust(47) + "Enter to continue")

def settings_max_rounds():
    while True:
        borrarPantalla()
        max_rounds = input("".ljust(60) + "Max Rounds: ")
        try:
            max_rounds = int(max_rounds)
            if max_rounds not in range(1, 21):
                print("".ljust(60) + "Max Rounds Has To Be Between 0 and 20")
                input("".ljust(60) + "Enter to continue")
            else:
                funcions_dades.dades.max_rounds = max_rounds
                funcions_dades.dades.context_game["round"] = max_rounds
                print("".ljust(60) + "Established maximum of rounds to {}".format(str(max_rounds)))
                input("".ljust(60) + "Enter to continue")
                break
        except:
            print("".ljust(60) + "Please, enter only numbers")
            input("".ljust(60) + "Enter to continue")

def charge_bbdd_players():
    funcions_dades.dades.players = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from player")
    player = cursor.fetchone()
    while player:
        if player[3] == 0:
            funcions_dades.dades.players[player[0]] = {"name": player[1], "human": False, "bank" :False,"initialCard":"" ,"priority" :0, "type": player[2], "bet": 4, "points": 20, "cards": [], "roundPoints": 0}
            player = cursor.fetchone()
        elif player[3] == 1:
            funcions_dades.dades.players[player[0]] = {"name": player[1], "human": True, "bank" :False,"initialCard":"" ,"priority" :0, "type": player[2], "bet": 4, "points": 20, "cards": [], "roundPoints": 0}
            player = cursor.fetchone()
    cursor.close()
    conexion.close()
    return

def new_bbdd_player(nif, name, valor_apuestas, human):
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("insert into player values ('{}', '{}', {}, {});".format(nif.upper(), name, valor_apuestas, human))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def remove_bbdd_player(nif):
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("delete from player_game_round where player_id like '{}';".format(nif))
    cursor.execute("delete from player_game where player_id like '{}';".format(nif))
    cursor.execute("delete from player where player_id like '{}';".format(nif))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def crear_listas_10_players(direccion=funcions_dades.dades.default):
    funcions_dades.dades.tabla_partida = {}
    numero_dict = 10
    lista = []
    for player in direccion:
        if len(lista) == 10:
            funcions_dades.dades.tabla_partida[str(numero_dict)] = lista
            lista = []
            numero_dict += 10
            lista.append(player)
        else:
            lista.append(player)
            if len(lista) == 10:
                funcions_dades.dades.tabla_partida[str(numero_dict)] = lista
                lista = []
                numero_dict += 10
            else:
                funcions_dades.dades.tabla_partida[str(numero_dict)] = lista

    funcions_dades.dades.tabla_partida[str(numero_dict + 10)] = ""
    return numero_dict

# FUNCIONES PARA LOS RANKINGS
# OPC 1 - EARNINGS
def show_rankings_more_earnings():
    lista_rankings = []
    borrarPantalla()
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from tabla_ranking")
    player = cursor.fetchone()
    while player:
        funcions_dades.dades.tabla_rankings[player[0]] = {"name": player[1], "earnings": int(player[2]), "games": int(player[3]), "minutes": float(player[4])}
        player = cursor.fetchone()
    cursor.close()
    conexion.close()
    cadena = ""
    for player in funcions_dades.dades.tabla_rankings.keys():
        lista_rankings.append(player)

    for pasadas in range(len(lista_rankings) - 1):
        for player in range(len(lista_rankings) - 1 - pasadas):
            if int(funcions_dades.dades.tabla_rankings[lista_rankings[player]]["earnings"]) < int(funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]]["earnings"]):
                aux = funcions_dades.dades.tabla_rankings[lista_rankings[player]]
                funcions_dades.dades.tabla_rankings[lista_rankings[player]] = funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]]
                funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]] = aux
    numero_dict = crear_listas_10_players(direccion=funcions_dades.dades.tabla_rankings.keys())
    return numero_dict
def rankings_more_earnings():
    numero_dict = show_rankings_more_earnings()
    borrarPantalla()
    numero_cadena = 10
    while True:
        if len(funcions_dades.dades.tabla_rankings) > 1:
            cadena = ""
            for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + "".ljust(34) + player.ljust(12) + funcions_dades.dades.tabla_rankings[player][
                    "name"].ljust(22) + \
                          str(funcions_dades.dades.tabla_rankings[player]["earnings"]).rjust(8) + str(
                    funcions_dades.dades.tabla_rankings[player]["games"]).rjust(14) + \
                          str(funcions_dades.dades.tabla_rankings[player]["minutes"]).rjust(16)
            cadena = (funcions_dades.dades.cabecera_rankings + cadena)
            print(cadena)
            if len(funcions_dades.dades.tabla_rankings) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Rankings: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Rankings: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Rankings: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Rankings: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(funcions_dades.dades.cabecera_rankings)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

# OPC 2 - GAMES
def show_rankings_more_games():
    lista_rankings = []
    borrarPantalla()
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from tabla_ranking")
    player = cursor.fetchone()
    while player:
        funcions_dades.dades.tabla_rankings[player[0]] = {"name": player[1], "earnings": int(player[2]),
                                                          "games": int(player[3]), "minutes": float(player[4])}
        player = cursor.fetchone()
    cursor.close()
    conexion.close()
    cadena = ""
    for player in funcions_dades.dades.tabla_rankings.keys():
        lista_rankings.append(player)

    for pasadas in range(len(lista_rankings) - 1):
        for player in range(len(lista_rankings) - 1 - pasadas):
            if int(funcions_dades.dades.tabla_rankings[lista_rankings[player]]["games"]) < int(funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]]["games"]):
                aux = funcions_dades.dades.tabla_rankings[lista_rankings[player]]
                funcions_dades.dades.tabla_rankings[lista_rankings[player]] = funcions_dades.dades.tabla_rankings[
                    lista_rankings[player + 1]]
                funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]] = aux
    numero_dict = crear_listas_10_players(direccion=funcions_dades.dades.tabla_rankings.keys())
    return numero_dict
def rankings_more_games():
    numero_dict = show_rankings_more_games()
    borrarPantalla()
    numero_cadena = 10
    while True:
        if len(funcions_dades.dades.tabla_rankings) > 1:
            cadena = ""
            for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + "".ljust(34) + player.ljust(12) + funcions_dades.dades.tabla_rankings[player][
                    "name"].ljust(22) + \
                          str(funcions_dades.dades.tabla_rankings[player]["earnings"]).rjust(8) + str(
                    funcions_dades.dades.tabla_rankings[player]["games"]).rjust(14) + \
                          str(funcions_dades.dades.tabla_rankings[player]["minutes"]).rjust(16)
            cadena = (funcions_dades.dades.cabecera_rankings + cadena)
            print(cadena)
            if len(funcions_dades.dades.tabla_rankings) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "(+ to repage, exit to go back): ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "(- to repage, exit to go back): ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "(+ to repage, - to repage , exit to go back): ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Rankings: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(funcions_dades.dades.cabecera_rankings)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

# OPC 3 - MINUTES
def show_rankings_more_minutes():
    lista_rankings = []
    borrarPantalla()
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from tabla_ranking")
    player = cursor.fetchone()
    while player:
        funcions_dades.dades.tabla_rankings[player[0]] = {"name": player[1], "earnings": int(player[2]),
                                                          "games": int(player[3]), "minutes": float(player[4])}
        player = cursor.fetchone()
    cursor.close()
    conexion.close()
    cadena = ""
    for player in funcions_dades.dades.tabla_rankings.keys():
        lista_rankings.append(player)

    for pasadas in range(len(lista_rankings) - 1):
        for player in range(len(lista_rankings) - 1 - pasadas):
            if int(funcions_dades.dades.tabla_rankings[lista_rankings[player]]["games"]) < int(
                    funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]]["games"]):
                aux = funcions_dades.dades.tabla_rankings[lista_rankings[player]]
                funcions_dades.dades.tabla_rankings[lista_rankings[player]] = funcions_dades.dades.tabla_rankings[
                    lista_rankings[player + 1]]
                funcions_dades.dades.tabla_rankings[lista_rankings[player + 1]] = aux
    numero_dict = crear_listas_10_players(direccion=funcions_dades.dades.tabla_rankings.keys())
    return numero_dict
def rankings_more_minutes():
    numero_dict = show_rankings_more_minutes()
    borrarPantalla()
    numero_cadena = 10
    while True:
        if len(funcions_dades.dades.tabla_rankings) > 1:
            cadena = ""
            for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + "".ljust(34) + player.ljust(12) + funcions_dades.dades.tabla_rankings[player][
                    "name"].ljust(22) + \
                          str(funcions_dades.dades.tabla_rankings[player]["earnings"]).rjust(8) + str(
                    funcions_dades.dades.tabla_rankings[player]["games"]).rjust(14) + \
                          str(funcions_dades.dades.tabla_rankings[player]["minutes"]).rjust(16)
            cadena = (funcions_dades.dades.cabecera_rankings + cadena)
            print(cadena)
            if len(funcions_dades.dades.tabla_rankings) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "(+ to repage, exit to go back): ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "(- to repage, exit to go back): ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "(+ to repage, - to repage , exit to go back): ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Rankings: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(funcions_dades.dades.cabecera_rankings)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()


# FUNCIONES PARA LOS RECORDS

# 1 CARTAS INICIALES MAS REPETIDAS POR PLAYER
def bbdd_initial_card_most_repeated():
    funcions_dades.dades.initial_card_most_repeated = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from initial_card_most_repeated_player;")
    player = cursor.fetchone()
    while player:
        funcions_dades.dades.initial_card_most_repeated[str(player[0])] = {"palo": player[1], "card": player[2], "repeticions": player[3], "games": player[4]}
        player = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def initial_card_most_repeated():
    borrarPantalla()
    bbdd_initial_card_most_repeated()
    menu = "".ljust(42) + "*"*61 + "\n" + "".ljust(42) + "ID Player".ljust(12) + "Stick".ljust(15) + "Card".ljust(7) + "Repetitions".ljust(15) + "Games Played".ljust(15) + "\n" + "".ljust(42) + "*"*61
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.initial_card_most_repeated.keys())
    while True:
        if len(funcions_dades.dades.initial_card_most_repeated) > 1:
            cadena = ""
            for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + player.rjust(51) + "".ljust(3) + funcions_dades.dades.initial_card_most_repeated[player]["palo"].ljust(15) + \
                    str(funcions_dades.dades.initial_card_most_repeated[player]["card"].rjust(4)) + "".ljust(3) + \
                    str(funcions_dades.dades.initial_card_most_repeated[player]["repeticions"]).rjust(11) + \
                    str(funcions_dades.dades.initial_card_most_repeated[player]["games"]).rjust(16)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.initial_card_most_repeated) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

# 2 APUESTA MAS ALTA
def bbdd_highest_bet_game():
    funcions_dades.dades.highest_bet = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from apuesta_mas_alta;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.highest_bet[game[1]] = {"player": game[0], "bet": game[2]}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def highest_bet_game():
    borrarPantalla()
    menu = "".ljust(42) + "*"*50 + "\n" + "".ljust(45) + "ID Game".ljust(12) + "ID Player".ljust(28) + "Max Bet" + "\n" + "".ljust(42) + "*"*50
    bbdd_highest_bet_game()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.highest_bet.keys())
    while True:
        if len(funcions_dades.dades.highest_bet) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + "".ljust(5) + funcions_dades.dades.highest_bet[game][
                    "player"].ljust(28) + str(funcions_dades.dades.highest_bet[game]["bet"]).rjust(7)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.highest_bet) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()


# 3 APUESTA MAS BAJA
def bbdd_lowest_bet_game():
    funcions_dades.dades.lowest_bet = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from apuesta_mas_baja;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.lowest_bet[game[1]] = {"player": game[0], "bet": game[2]}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def lowest_bet_game():
    borrarPantalla()
    menu = "".ljust(42) + "*"*50 + "\n" + "".ljust(45) + "ID Game".ljust(12) + "ID Player".ljust(28) + "Min Bet" + "\n" + "".ljust(42) + "*"*50
    bbdd_lowest_bet_game()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.lowest_bet.keys())
    while True:
        if len(funcions_dades.dades.lowest_bet) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + "".ljust(5) + funcions_dades.dades.lowest_bet[game][
                    "player"].ljust(28) + str(funcions_dades.dades.lowest_bet[game]["bet"]).rjust(7)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.lowest_bet) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

# 4 PORCENTAJE DE VICTORIAS DE CADA JUGADOR EN CADA PARTIDA
def bbdd_perc_round_won_player_game():
    funcions_dades.dades.lowest_bet = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123',host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from porcentaje_rondas_ganadas_player;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.percentatge_round_won_player[str(game[0])] = {"player": game[1], "rounds": game[2], "avg_bet": game[3], "wrounds": game[4], "percwon": game[5]}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def perc_round_won_player_game():
    borrarPantalla()
    bbdd_perc_round_won_player_game()
    menu = "".ljust(19) + "*"*101 + "\n" + "".ljust(20) + "ID Game".ljust(12) + "ID Player".ljust(25) + "Rounds".ljust(12) + \
           "Average Bet".ljust(16) + "Winned Rouds".ljust(19) + "Percentatge Won" + "\n" + "".ljust(19) + "*"*101
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.percentatge_round_won_player.keys())
    while True:
        if len(funcions_dades.dades.percentatge_round_won_player) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + game.rjust(27) + funcions_dades.dades.percentatge_round_won_player[game]["player"].rjust(14) + \
                    str(funcions_dades.dades.percentatge_round_won_player[game]["rounds"]).rjust(22) + \
                    str(funcions_dades.dades.percentatge_round_won_player[game]["avg_bet"]).rjust(17) + \
                    str(funcions_dades.dades.percentatge_round_won_player[game]["wrounds"]).rjust(17) + \
                    str(funcions_dades.dades.percentatge_round_won_player[game]["percwon"]).rjust(22)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.percentatge_round_won_player) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

# 5 VICTORIAS BOTS
def bbdd_bot_wins():
    funcions_dades.dades.games_won_bots = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from victorias_bots;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.games_won_bots[str(game[0])] = {"points": game[1]}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def bot_wins():
    borrarPantalla()
    menu = "".ljust(42) + "*" * 28 + "\n" + "".ljust(45) + "ID Game".ljust(15) + "Points Won" + "\n" + "".ljust(42) + "*" * 28
    bbdd_bot_wins()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.games_won_bots.keys())
    while True:
        if len(funcions_dades.dades.games_won_bots) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + str(funcions_dades.dades.games_won_bots[game]["points"]).rjust(
                    18)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.games_won_bots) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()


# 6 RONDAS GANADAS BANCA
def bbdd_rounds_win_bank():
    funcions_dades.dades.bank_round_wins = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from rondas_ganadas_banca;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.bank_round_wins[str(game[0])] = {"rounds": game[1]}
        game = cursor.fetchone()
    return
def rounds_win_bank():
    borrarPantalla()
    menu = "".ljust(42) + "*" * 28 + "\n" + "".ljust(45) + "ID Game".ljust(15) + "Rounds Won" + "\n" + "".ljust(
        42) + "*" * 28
    bbdd_rounds_win_bank()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.bank_round_wins.keys())
    while True:
        if len(funcions_dades.dades.bank_round_wins) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + str(funcions_dades.dades.bank_round_wins[game]["rounds"]).rjust(
                    18)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.bank_round_wins) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()


# 7 USUARIOS QUE HAN SIDO BANCA
def bbdd_users_bank():
    funcions_dades.dades.number_bank_users_game = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from usuarios_banca_partida;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.number_bank_users_game[str(game[0])] = {"users": game[1]}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def users_bank():
    borrarPantalla()
    menu = "\n" + "".ljust(42) + "*"*40 + "\n" + "".ljust(45) + "ID Game" + "Users who have been bank".rjust(30) + "\n" + "".ljust(42) + "*"*40
    bbdd_users_bank()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.number_bank_users_game.keys())
    while True:
        if len(funcions_dades.dades.number_bank_users_game) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + str(funcions_dades.dades.number_bank_users_game[game]["users"]).rjust(30)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.number_bank_users_game) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()


# 8 APUESTA MEDIA POR PARTIDA
def bbdd_average_bet_game():
    funcions_dades.dades.average_bet_game = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123',host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from apuesta_media_partida;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.average_bet_game[str(game[0])] = {"bet": str(game[1])}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def average_bet_game():
    borrarPantalla()
    menu = "\n" + "".ljust(42) + "*"*28 + "\n" + "".ljust(45) + "ID Game" + "Average Bet".rjust(18) + "\n" + "".ljust(42) + "*"*28
    bbdd_average_bet_game()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.average_bet_game.keys())
    while True:
        if len(funcions_dades.dades.average_bet_game) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + funcions_dades.dades.average_bet_game[game]["bet"].rjust(18)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.average_bet_game) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

# 9 APUESTA MEDIA PRIMERA RONDA
def bbdd_average_bet_first_round():
    funcions_dades.dades.average_first_round_game = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123',host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from apuesta_media_ronda1;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.average_first_round_game[str(game[0])] = {"bet": str(game[1])}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def average_bet_first_round():
    borrarPantalla()
    menu = "\n" + "".ljust(42) + "*"*28 + "\n" + "".ljust(45) + "ID Game" + "Average Bet".rjust(18) + "\n" + "".ljust(42) + "*"*28
    bbdd_average_bet_first_round()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.average_first_round_game.keys())
    while True:
        if len(funcions_dades.dades.average_first_round_game) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + funcions_dades.dades.average_first_round_game[game]["bet"].rjust(18)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.average_first_round_game) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

#10 APUESTA MEDIA ULTIMA RONDA
def bbdd_average_bet_last_round():
    funcions_dades.dades.average_last_round_game = {}
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123',host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from apuesta_media_ultima_ronda;")
    game = cursor.fetchone()
    while game:
        funcions_dades.dades.average_last_round_game[str(game[0])] = {"bet": str(game[1])}
        game = cursor.fetchone()
    cursor.close()
    conexion.close()
    return
def average_bet_last_round():
    borrarPantalla()
    menu = "\n" + "".ljust(42) + "*"*28 + "\n" + "".ljust(45) + "ID Game" + "Average Bet".rjust(18) + "\n" + "".ljust(42) + "*"*28
    bbdd_average_bet_last_round()
    numero_cadena = 10
    numero_dict = crear_listas_10_players(funcions_dades.dades.average_last_round_game.keys())
    while True:
        if len(funcions_dades.dades.average_last_round_game) > 1:
            cadena = ""
            for game in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
                cadena += "\n" + str(game).rjust(52) + funcions_dades.dades.average_last_round_game[game]["bet"].rjust(18)
            cadena = (menu + cadena)
            print(cadena)
            if len(funcions_dades.dades.average_last_round_game) > 10:
                if numero_cadena == 10:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                elif numero_cadena == numero_dict:
                    opc = input("\n" + "".ljust(42) + "- to go back, exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
                else:
                    opc = input("\n" + "".ljust(42) + "+ to go ahead, - to go back , exit to go Reports: ")
                    if opc.lower() == "exit":
                        break
                    elif opc == "+":
                        numero_cadena += 10
                        borrarPantalla()
                    elif opc == "-":
                        numero_cadena -= 10
                        borrarPantalla()
                    else:
                        print("=" * 63 + "Invalid option" + "=" * 63)
                        input("Press enter to continue".center(140))
                        borrarPantalla()
            else:
                opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
                if opc.lower() == "exit":
                    break
                else:
                    print("=" * 63 + "Invalid option" + "=" * 63)
                    input("Press enter to continue".center(140))
                    borrarPantalla()
        else:
            print(menu)
            opc = input("\n" + "".ljust(42) + "exit to go Reports: ")
            if opc.lower() == "exit":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()

def shuffle():  # SHUFFLE CARDS
    mazo = list(funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]].keys())
    for cards in range(len(mazo)):
        random_position = random.randint(0, len(mazo)) #GENERATE RANDOM PONSITION EACH LOOP
        mazo.insert(random_position,mazo[cards])  # INSERT A CARD S CLONE IN A RANDOM POSITION
        if random_position == (len(mazo)-1):  #DELETE THE OLD CARD
            mazo.pop(random_position)
        else:
            mazo.pop(random_position + 1)
    funcions_dades.dades.context_game["mazo"] = mazo
    return mazo


def setGamePriority():  # SET PLAYERS PRIORITY
    players = funcions_dades.dades.context_game["players"]
    for p in players:
        funcions_dades.dades.players[p]["priority"] = players.index(p)
    return players

def orderAllPlayers():
    for player in funcions_dades.dades.players.keys():
        funcions_dades.dades.players[player]["bank"] = False
    funcions_dades.dades.game = funcions_dades.dades.player_game
    funcions_dades.dades.context_game["players"] = funcions_dades.dades.game
    players = funcions_dades.dades.context_game["players"]
    deck = shuffle()
    for i in players:
        funcions_dades.dades.players[i]["initialCard"] = deck[0]  # ASSIGN A CARD TO EACH PLAYER IN THE GAME
        deck.remove(deck[0])  # REMOVE ASSIGNED CARD

    for pasadas in range(len(players) - 1):  # ORDER PLAYERS
        for player in range((len(players) - pasadas) - 1):
            if funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.players[players[player]]["initialCard"]][
                "value"] < \
                    funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.players[players[player + 1]]["initialCard"]][
                        "value"]:

                players[player], players[player + 1] = players[player + 1], players[player]

            elif (funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.players[players[player]]["initialCard"]][
                      "value"] ==  # SAME VALUE, DIFFERENT TYPE
                  funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.players[players[player + 1]]["initialCard"]][
                      "value"]) \
                    and (funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.players[players[player]]["initialCard"]][
                             "priority"] <
                         funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][
                             funcions_dades.dades.players[players[player + 1]]["initialCard"]]["priority"]):

                players[player], players[player + 1] = players[player + 1], players[player]
    players.append(players[0])
    players.pop(0)
    funcions_dades.dades.players[players[-1]]["bank"]=True
    funcions_dades.dades.game = players



# def catch_humans(list_players):
#     humans = []
#     for player in list_players:
#         if funcions_dades.dades.players[player]["human"] == True:
#             humans.append(player)
#     return humans

def showGameStats(list_id_players):
    players = funcions_dades.dades.context_game["players"]
    cadena = ""
    titles = ["name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints"]
    for pasadas in titles:
        if pasadas in titles:
            cadena += pasadas.ljust(20)
        for datos in list_id_players:
            cartas = ""
            if pasadas == "name":
                cadena += str(funcions_dades.dades.players[datos]["name"]).ljust(20)
            elif pasadas == "type":
                cadena += str(funcions_dades.dades.players[datos]["type"]).ljust(20)
            elif pasadas == "human":
                cadena += str(funcions_dades.dades.players[datos]["human"]).ljust(20)
            elif pasadas == "bank":
                cadena += str(funcions_dades.dades.players[datos]["bank"]).ljust(20)
            elif pasadas == "initialCard":
                cadena += str(funcions_dades.dades.players[datos]["initialCard"]).ljust(20)
            elif pasadas == "priority":
                cadena += str(funcions_dades.dades.players[datos]["priority"]).ljust(20)
            elif pasadas == "bet":
                cadena += str(funcions_dades.dades.players[datos]["bet"]).ljust(20)
            elif pasadas == "points":
                cadena += str(funcions_dades.dades.players[datos]["points"]).ljust(20)
            elif pasadas == "cards" :
                if len(funcions_dades.dades.players[datos]["cards"]) > 0:
                    for card in funcions_dades.dades.players[datos]["cards"]:
                        cartas += card + ";"
                    cadena += str(cartas[0:-1]).ljust(20)
            elif pasadas == "roundPoints":
                cadena += str(funcions_dades.dades.players[datos]["roundPoints"]).ljust(20)
        cadena += "\n"
    return cadena

def showPlayerStat(id_player):
    titles = ["name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints"]
    cadena = ""
    for t in titles:
        if t == "cards":
            cadena += "\n" + "".ljust(60) + t.ljust(15)
            for card in funcions_dades.dades.players[id_player]["cards"]:
                cadena += card + ";"
            cadena = cadena[0:-1]

        else:
            cadena += "\n" + "".ljust(60) + t.ljust(15) + str(funcions_dades.dades.players[id_player][t])
    return cadena

def setBet(id_player,id_bank):
    while True:
        try:
            bet = input("".ljust(60) + "How many points do you want to bet:")
            if not(bet.isdigit()):
                if bet == "":
                    raise ValueError("Bet can't be empty")
                elif not bet > 0:
                    raise ValueError("")
                elif bet[0] == "-" and  bet[1:].isdigit():
                    if int(bet) < 0:
                        raise ValueError("Bet has to be positive!")
                elif "."  in  bet:
                    raise TypeError("Bet can't be float")
                else:
                    raise TypeError("Bet has to be a number!")
            elif int(bet) > int(funcions_dades.dades.players[id_player]["points"]):
                raise ValueError("Bet can't be higher than points")
            elif int(bet) > int(funcions_dades.dades.players[id_bank]["points"]):
                raise ValueError("Bet can't be higher than bank points")
            return bet
        except TypeError as e:
            print("".ljust(60) + str(e))
        except ValueError as e :
            print("".ljust(60) + str(e))

def takeCard(id_player):
    funcions_dades.dades.players[id_player]["cards"].append(funcions_dades.dades.context_game["mazo"][0])
    card_value = funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.context_game["mazo"][0]]["realValue"]
    funcions_dades.dades.round_player_cards.append(funcions_dades.dades.context_game["mazo"][0])
    funcions_dades.dades.context_game["mazo"].remove(funcions_dades.dades.context_game["mazo"][0])



def orderCard(id_player,auto=False):
    player_cards_value = 0
    dng_cards = 0
    if len(funcions_dades.dades.context_game["mazo"]) > 0:
        for ply_card in funcions_dades.dades.round_player_cards:  # CALCULATE THE PLAYERS CARD VALUE
            player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][ply_card]["realValue"]
        for card in funcions_dades.dades.context_game["mazo"]:  # CALCULATE DANGEROUS CARDS
            if (funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][card]["realValue"] + player_cards_value) > 7.5:
                dng_cards += 1

        if (funcions_dades.dades.players[id_player]["human"] == True) and (auto == False):
            if len(funcions_dades.dades.round_player_cards) >= 1:
                print("".ljust(60) + "Chance of exceed 7.5 == ",round(dng_cards/len(funcions_dades.dades.context_game["mazo"])*100),"%"+"\n")
                save = input("".ljust(60) + "Are you sure do you want to order another card? Y/y = Yes, another key = Not")
                if save.lower() == "y":  # SAVE THE CARD IF YES
                    print("".ljust(60) + "The new card is " + funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.context_game["mazo"]
                    [0]]["nombre"])
                    takeCard(id_player)
                    player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.round_player_cards[-1]]["realValue"]

                    print("".ljust(60) + "Now you have {} points".format(player_cards_value))  # PRINT CARD VALUE
                else:
                    print("".ljust(60) + "Card not saved")  # Card not saved
            else:
                print("".ljust(60) + "The new card is " + funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.context_game["mazo"]
                [0]]["nombre"])
                takeCard(id_player)
                player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.round_player_cards[-1]]["realValue"]

                print("".ljust(60) + "Now you have {} points".format(player_cards_value))  # PRINT CARD VALUE
                input("".ljust(60) + "Enter to continue")
            funcions_dades.dades.players[id_player]["roundPoints"] = player_cards_value

        elif (funcions_dades.dades.players[id_player]["human"] == False) or (auto == True) :  # BOOT BEHAVIOUR
            if len(funcions_dades.dades.round_player_cards) == 0:
                takeCard(id_player)
                player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.round_player_cards[-1]]["realValue"]

            elif len(funcions_dades.dades.round_player_cards) >= 1:
                if funcions_dades.dades.players[id_player]["type"] == 30:     #30 -> Cautious, 40 -> Moderated, 50 -> Bold
                    if round(dng_cards/len(funcions_dades.dades.context_game["mazo"])*100) <= 30:
                        if funcions_dades.dades.players[id_player]["points"] > 14:
                            funcions_dades.dades.players[id_player]["bet"] = round((funcions_dades.dades.players[id_player]["points"]/100)*30)
                        else:
                            funcions_dades.dades.players[id_player]["bet"] = funcions_dades.dades.players[id_player]["points"]
                        takeCard(id_player)
                        player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.round_player_cards[-1]]["realValue"]

                    else:
                        funcions_dades.dades.flg_game = False
                elif funcions_dades.dades.players[id_player]["type"] == 40:
                    if round(dng_cards/len(funcions_dades.dades.context_game["mazo"])*100) <= 50:
                        if funcions_dades.dades.players[id_player]["points"] > 10:
                            funcions_dades.dades.players[id_player]["bet"] = round((funcions_dades.dades.players[id_player]["points"]/100)*40)
                        else:
                            funcions_dades.dades.players[id_player]["bet"] = funcions_dades.dades.players[id_player]["points"]
                        takeCard(id_player)
                        player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.round_player_cards[-1]]["realValue"]

                    else:
                        funcions_dades.dades.flg_game = False

                elif funcions_dades.dades.players[id_player]["type"] == 50:
                    if round(dng_cards/len(funcions_dades.dades.context_game["mazo"])*100) <= 70:
                        if funcions_dades.dades.players[id_player]["points"] > 8:
                            funcions_dades.dades.players[id_player]["bet"] = round((funcions_dades.dades.players[id_player]["points"]/100)*50)
                        else:
                            funcions_dades.dades.players[id_player]["bet"] = funcions_dades.dades.players[id_player]["points"]
                        takeCard(id_player)
                        player_cards_value += funcions_dades.dades.cartas[funcions_dades.dades.context_game["typo_mazo"]][funcions_dades.dades.round_player_cards[-1]]["realValue"]

                    else:
                        funcions_dades.dades.flg_game = False
            funcions_dades.dades.players[id_player]["roundPoints"] = player_cards_value
    else:
        shuffle()
        print("".ljust(60) + "The deck has been shuffled !")


def order_by_priority(lista_ids):
    for pasadas in range(len(lista_ids) - 1):  # ORDER PLAYERS
        for player in range((len(lista_ids) - pasadas) - 1):
            if funcions_dades.dades.players[lista_ids[player]]["priority"] < funcions_dades.dades.players[lista_ids[player+1]]["priority"]:
                lista_ids[player], lista_ids[player + 1] = lista_ids[player + 1], lista_ids[player]
    return lista_ids

def bbdd_cardgame():
    funcions_dades.dades.cardgame = []
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123',
                                       host='projecte1.mysql.database.azure.com',
                                       database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from cardgame")
    cardgame = cursor.fetchone()
    while cardgame:
        funcions_dades.dades.cardgame.append(cardgame[0])
        cardgame = cursor.fetchone()
    cursor.close()
    conexion.close()

def game():
    fecha_inicio = "{} {}".format(datetime.datetime.now().date(), time.strftime("%H:%M:%S"))
    bbdd_cardgame()
    actual_cardgame = funcions_dades.dades.cardgame[-1] + 1
    for player in funcions_dades.dades.players.keys():
        funcions_dades.dades.players[player]["points"] = 20
    player_game_round = {}
    orderAllPlayers()
    setGamePriority()
    funcions_dades.dades.context_game["round"] = funcions_dades.dades.max_rounds
    round = 0
    p_winer = False
    bet_ban = False
    puntos_iniciales = {}
    for player in funcions_dades.dades.player_game:
        puntos_iniciales[player] = {"points": funcions_dades.dades.players[player]["points"], "initialCard": ""}
    g_players = funcions_dades.dades.game
    while funcions_dades.dades.context_game["round"] > 0:
        eliminate_players = True
        pointer = 0
        candidatos_banka = []
        player_game_round[round + 1] = {}
        for id_player in g_players:
            cabecera_turn = "*" * 58 + " Round {} , Turn of {} ".format(round, funcions_dades.dades.players[id_player]["name"]) + "*" * 55 + "\n"
            funcions_dades.dades.round_player_cards.clear()
            bet_ban = False
            funcions_dades.dades.flg_game = True
            player_game_round[round + 1][id_player] = {"is_bank": funcions_dades.dades.players[id_player]["bank"],
                                                        "bet_points": "", "cards_value": "",
                                                        "starting_round_points": funcions_dades.dades.players[id_player][
                                                            "points"], "ending_round_points": ""}
            while funcions_dades.dades.flg_game == True:
                if funcions_dades.dades.players[id_player]["roundPoints"] < 7.5:
                    if funcions_dades.dades.players[id_player]["human"] == False:
                        orderCard(id_player)
                        player_game_round[round + 1][id_player]["bet_points"] = funcions_dades.dades.players[id_player]["bet"]
                        player_game_round[round + 1][id_player]["cards_value"] = funcions_dades.dades.players[id_player]["roundPoints"]
                    else:
                        print("*"*140)
                        print(cabecera_turn)
                        opc = getOpt(funcions_dades.dades.menu03, "\n" + "".ljust(60) + "Option: ",[1,2,3,4,5,6])
                        if opc == 1:
                            borrarPantalla()
                            print("*"*140)
                            print("*"*63 + "Stats of {}".format(funcions_dades.dades.players[id_player]["name"]) + "*"*61)
                            print(showPlayerStat(id_player))
                            input("\n" + "".ljust(60) + "Enter to continue")
                            borrarPantalla()
                        elif opc == 2:
                            borrarPantalla()
                            print("*"*140)
                            print(cabecera_turn + "\n")
                            print(showGameStats(funcions_dades.dades.game))
                            input("\n" + "".ljust(60) + "Enter to continue")
                            borrarPantalla()
                        elif opc == 3:
                            try:
                                if funcions_dades.dades.players[id_player]["bank"] == True:  # CANT BET IF ITS THE BANK
                                    raise ValueError("".ljust(60) + "You're not allowed to change the bet if you're de bank")
                                elif bet_ban == True:
                                    raise ValueError("Can't bet once a card has been ordered")  # IF ORDERED A CARD CANT BET
                                funcions_dades.dades.players[id_player]["bet"] = setBet(id_player,g_players[-1])
                                borrarPantalla()
                            except ValueError as e:
                                print(e)
                                input("".ljust(60) + "Enter to continue")
                                borrarPantalla()
                        elif opc == 4:
                            if funcions_dades.dades.players[id_player]["roundPoints"] < 7.5:
                                print("".ljust(60) + "Order Card")
                                orderCard(id_player)    # ORDER A CARD ACTIVATES BET BAN
                                bet_ban = True
                                borrarPantalla()
                            else:
                                funcions_dades.dades.flg_game = False
                        elif opc == 5:
                            orderCard(id_player, auto=True)
                            if g_players.index(id_player) != len(g_players):
                                borrarPantalla()
                                print("*" * 140)
                                print(cabecera_turn)
                                print()
                                print(showGameStats(funcions_dades.dades.game))
                                input("".ljust(60) + "Enter to continue")
                                borrarPantalla()
                        elif opc == 6:
                            if g_players.index(id_player) != len(g_players):
                                borrarPantalla()
                            player_game_round[round + 1][id_player]["bet_points"] = funcions_dades.dades.players[id_player]["bet"]
                            player_game_round[round + 1][id_player]["cards_value"] = funcions_dades.dades.players[id_player]["roundPoints"]
                            funcions_dades.dades.flg_game = False
                else:
                    player_game_round[round + 1][id_player]["bet_points"] = funcions_dades.dades.players[id_player]["bet"]
                    player_game_round[round + 1][id_player]["cards_value"] = funcions_dades.dades.players[id_player]["roundPoints"]
                    funcions_dades.dades.flg_game = False
        borrarPantalla()

        for i in range(len(g_players)-1):
            p_winer = False
            if funcions_dades.dades.players[g_players[i]]["roundPoints"] == 7.5 and funcions_dades.dades.players[g_players[-1]]["roundPoints"] != 7.5: # PLAYER 7.5 BANKA NO
                candidatos_banka.append(funcions_dades.dades.game[i])
                p_winer = True
            elif funcions_dades.dades.players[g_players[i]]["roundPoints"] <= funcions_dades.dades.players[g_players[-1]]["roundPoints"] and \
                    (funcions_dades.dades.players[g_players[-1]]["roundPoints"] <= 7.5):  #BANKA WINS PLAYER <= 7.5
                print("BG  wins puntuacion < 7.5")
                p_winer = False

            elif funcions_dades.dades.players[g_players[i]]["roundPoints"] > funcions_dades.dades.players[g_players[-1]]["roundPoints"] and \
                funcions_dades.dades.players[g_players[i]]["roundPoints"] <= 7.5:  # PLAYER WINS BANKA < 7.5
                print("BG  loses puntuacion < 7.5")
                p_winer = True

            elif funcions_dades.dades.players[g_players[i]]["roundPoints"] > 7.5 and funcions_dades.dades.players[g_players[-1]]["roundPoints"] < 7.5:  # BANKA WINS PLAYER OVER 7.5
                print("BG  wins puntuacion_pl > 7.5")
                p_winer = False

            elif funcions_dades.dades.players[g_players[i]]["roundPoints"] < 7.5 and funcions_dades.dades.players[g_players[-1]]["roundPoints"] > 7.5:  # PLAYER WINS BANKA OVER 7.5
                print("BG  loses puntuacion_bl > 7.5")
                p_winer = True

            if p_winer == True:      # POINTS DISTRIBUTION
                if funcions_dades.dades.players[g_players[i]]["roundPoints"] == 7.5 and funcions_dades.dades.players[g_players[-1]][
                    "roundPoints"] != 7.5:  # PLAYER 7.5 BANKA NO
                    if (funcions_dades.dades.players[g_players[i]]["bet"] * 2) > funcions_dades.dades.players[g_players[-1]]["points"]:  # BANKA DOESNT HAVE ENOUGH POINTS
                        funcions_dades.dades.players[g_players[i]]["points"] += funcions_dades.dades.players[g_players[-1]]["points"]  # ALL POINTS GIVEN TO PLAYER
                        funcions_dades.dades.players[g_players[-1]]["points"] = 0  # BANKA ELIMINATED WITH 0 POINTS7
                        print("Player Wins" + "\n" + "Banka is eliminated")
                    else:
                        funcions_dades.dades.players[g_players[i]]["points"] += (funcions_dades.dades.players[g_players[i]]["bet"] * 2)     # PLAYER WINS AND BANKA HAVE ENOUGH P
                        funcions_dades.dades.players[g_players[-1]]["points"] -= (funcions_dades.dades.players[g_players[i]]["bet"] * 2)      # CHANGE BANKA
                        candidatos_banka = order_by_priority(candidatos_banka)
                        funcions_dades.dades.players[g_players[-1]]["bank"] = False
                        funcions_dades.dades.players[candidatos_banka[0]]["bank"] = True
                        g_players = order_by_priority(g_players)
                        g_players.append(candidatos_banka[0])
                        g_players.remove(candidatos_banka[0])
                else:
                    funcions_dades.dades.players[g_players[i]]["points"] += int(funcions_dades.dades.players[g_players[i]]["bet"])
                    funcions_dades.dades.players[g_players[-1]]["points"] -= int(funcions_dades.dades.players[g_players[i]]["bet"])
            elif p_winer == False:
                funcions_dades.dades.players[g_players[-1]]["points"] += int(funcions_dades.dades.players[g_players[i]]["bet"])
                funcions_dades.dades.players[g_players[i]]["points"] -= int(funcions_dades.dades.players[g_players[i]]["bet"])

        while eliminate_players:
            if funcions_dades.dades.players[g_players[pointer]]["points"] <= 0:
                if funcions_dades.dades.players[g_players[pointer]]["bank"] == True:
                    g_players.remove(g_players[pointer])
                    funcions_dades.dades.players[g_players[0]]["bank"] = True
                    g_players.append(g_players[0])
                    g_players.remove(g_players[0])
                else:
                    g_players.remove(g_players[pointer])
            else:
                pointer += 1

            if pointer > len(g_players)-1 :
                eliminate_players = False

        for reset in g_players:
            funcions_dades.dades.players[reset]["roundPoints"] = 0
            funcions_dades.dades.players[reset]["cards"] = []
        for player in player_game_round[round + 1].keys():
            player_game_round[round + 1][player]["ending_round_points"] = funcions_dades.dades.players[player]["points"]
        if len(g_players) == 1:
            borrarPantalla()
            conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
            cursor = conexion.cursor()
            # CARDGAME DATABASE INSERT
            fecha_actual = "{} {}".format(datetime.datetime.now().date(), time.strftime("%H:%M:%S"))
            cursor.execute("insert into cardgame values ({}, {}, {}, '{}', '{}', '{}');".format(actual_cardgame, len(funcions_dades.dades.player_game), round, fecha_inicio, fecha_actual, funcions_dades.dades.deckgame))
            # PLAYER_GAME DATABASE INSERT
            for player in funcions_dades.dades.player_game:
                cursor.execute("insert into player_game values ({}, '{}', '{}', {}, {});".format(actual_cardgame, player, puntos_iniciales[player]["initialCard"], puntos_iniciales[player]["points"], funcions_dades.dades.players[player]["points"]))
            # PLAYER_GAME_ROUND DATABASE INSERT
            for game_round in player_game_round.keys():
                for player in player_game_round[game_round]:
                    if player_game_round[game_round][player]["is_bank"] is True:
                        player_game_round[game_round][player]["bet_points"] = 0
                    cursor.execute("insert into player_game_round values ({}, {}, '{}', {}, {}, {}, {}, {});".format(actual_cardgame, game_round, player, player_game_round[game_round][player]["is_bank"], player_game_round[game_round][player]["bet_points"], player_game_round[game_round][player]["cards_value"], player_game_round[game_round][player]["starting_round_points"], player_game_round[game_round][player]["ending_round_points"]))
            conexion.commit()
            cursor.close()
            conexion.close()
            return g_players[0]
        borrarPantalla()
        print("*"*59 + " STATS AFTER ROUND {} ".format(str(round)) + "*"*59)
        print("*"*140)
        print()
        print(showGameStats(funcions_dades.dades.game))

        exit = input("".ljust(60) + "Enter to continue or exit to leave the game: ")  # LEAVE THE GAME
        if exit == "exit":
            funcions_dades.dades.context_game["round"] = 0
        if round == 0:
            for player in funcions_dades.dades.player_game:
                puntos_iniciales[player]["initialCard"] = funcions_dades.dades.players[player]["initialCard"]
        round += 1
        funcions_dades.dades.context_game["round"] -= 1
        borrarPantalla()
    for pasadas in range(len(g_players)-1):
        for winer in range(len(g_players)-1):
            if funcions_dades.dades.players[g_players[winer]]["points"] < funcions_dades.dades.players[g_players[winer+1]]["points"]:

                g_players[winer], g_players[winer+1] = \
                g_players[winer+1], g_players[winer]

            elif funcions_dades.dades.players[g_players[winer]]["points"] == funcions_dades.dades.players[g_players[winer+1]]["points"] and \
                 funcions_dades.dades.players[g_players[winer+1]]["bank"] == True:

                g_players[winer], g_players[winer + 1] = \
                g_players[winer + 1], g_players[winer]
    borrarPantalla()
    conexion = mysql.connector.connect(user='projecte1_root', password='Setimig123', host='projecte1.mysql.database.azure.com', database='projecte1', port='3306')
    cursor = conexion.cursor()
    # CARDGAME DATABASE INSERT
    fecha_actual = "{} {}".format(datetime.datetime.now().date(), time.strftime("%H:%M:%S"))
    cursor.execute("insert into cardgame values ({}, {}, {}, '{}', '{}', '{}');".format(actual_cardgame, len(funcions_dades.dades.player_game), round,
                                                                                fecha_inicio, fecha_actual, funcions_dades.dades.deckgame))
    # PLAYER_GAME DATABASE INSERT
    for player in funcions_dades.dades.player_game:
        cursor.execute("insert into player_game values ({}, '{}', '{}', {}, {});".format(actual_cardgame, player, puntos_iniciales[player]["initialCard"],
                                                                                puntos_iniciales[player]["points"], funcions_dades.dades.players[player]["points"]))
    # PLAYER_GAME_ROUND DATABASE INSERT
    for game_round in player_game_round.keys():
        for player in player_game_round[game_round]:
            if player_game_round[game_round][player]["is_bank"] is True:
                player_game_round[game_round][player]["bet_points"] = 0
            cursor.execute("insert into player_game_round values ({}, {}, '{}', {}, {}, {}, {}, {});".format(actual_cardgame, game_round,
                                                                                                    player, player_game_round[game_round][player]["is_bank"],
                                                                                                    player_game_round[game_round][player]["bet_points"],
                                                                                                    player_game_round[game_round][player]["cards_value"],
                                                                                                    player_game_round[game_round][player]["starting_round_points"],
                                                                                                    player_game_round[game_round][player]["ending_round_points"]))
    conexion.commit()
    cursor.close()
    conexion.close()
    return g_players[0]
