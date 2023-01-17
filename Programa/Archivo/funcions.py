import random
import funcions_dades.dades
import os
import mysql.connector

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
            elif opc[0] == "-" and opc[1:].upper() in funcions_dades.dades.player_game.keys():
                funcions_dades.dades.player_game.pop(opc[1:].upper())
                show_setting_players()
            elif opc.upper() in funcions_dades.dades.players.keys():
                if len(funcions_dades.dades.player_game) >= 6:
                    print()
                    print("Maxim number of players in game reached!!".center(140))
                    show_setting_players()
                else:
                    funcions_dades.dades.player_game[opc.upper()] = {""}
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
            elif opc[0] == "-" and opc[1:].upper() in funcions_dades.dades.player_game.keys():
                funcions_dades.dades.player_game.pop(opc[1:].upper())
                borrarPantalla()
            elif opc.upper() in funcions_dades.dades.players.keys():
                funcions_dades.dades.player_game[opc.upper()] = {""}
                print("hola")
                borrarPantalla()
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
        print("".ljust(47) + "Established Card Deck ESP, Baraja Española")
        input("".ljust(47) + "Enter to continue")
    elif opc == 2:
        funcions_dades.dades.deckgame = "POK"
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
                print("".ljust(60) + "Established maximum of rounds to {}".format(str(max_rounds)))
                input("".ljust(60) + "Enter to continue")
                break
        except:
            print("".ljust(60) + "Please, enter only numbers")
            input("".ljust(60) + "Enter to continue")

def charge_bbdd_players():
    funcions_dades.dades.players = {}
    conexion = mysql.connector.connect(user='root', password='1234', host='localhost', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("select * from player")
    player = cursor.fetchone()
    while player:
        if player[3] == 0:
            funcions_dades.dades.players[player[0]] = {"name": player[1], "human": False, "type": player[2], "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
            player = cursor.fetchone()
        elif player[3] == 1:
            funcions_dades.dades.players[player[0]] = {"name": player[1], "human": True, "type": player[2], "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
            player = cursor.fetchone()
    cursor.close()
    conexion.close()
    return

def new_bbdd_player(nif, name, valor_apuestas, human):
    conexion = mysql.connector.connect(user='root', password='1234', host='localhost', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("insert into player values ('{}', '{}', {}, {});".format(nif.upper(), name, valor_apuestas, human))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def remove_bbdd_player(nif):
    conexion = mysql.connector.connect(user='root', password='1234', host='localhost', database='projecte1', port='3306')
    cursor = conexion.cursor()
    cursor.execute("delete from player_round_game where player_id like '{}';".format(nif))
    cursor.execute("delete from player_game where player_id like '{}';".format(nif))
    cursor.execute("delete from player where player_id like '{}';".format(nif))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def crear_listas_10_players():
    numero_dict = 10
    lista = []
    for player in funcions_dades.dades.tabla_rankings.keys():
        if len(lista) == 10:
            funcions_dades.dades.tabla_partida[str(numero_dict)] = lista
            lista = []
            numero_dict += 10
            lista.append(player)
        else:
            lista.append(player)
            funcions_dades.dades.tabla_partida[str(numero_dict)] = lista


    funcions_dades.dades.tabla_partida[str(numero_dict + 10)] = ""
    print(str(funcions_dades.dades.tabla_partida))
    return numero_dict

crear_listas_10_players()

def show_rankings_more_earnings():
    lista_rankings = []
    borrarPantalla()
    conexion = mysql.connector.connect(user='root', password='1234', host='localhost', database='projecte1', port='3306')
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
    numero_dict = crear_listas_10_players()
    return numero_dict

def show_rankings_more_games():
    lista_rankings = []
    borrarPantalla()
    conexion = mysql.connector.connect(user='root', password='1234', host='localhost', database='projecte1',
                                       port='3306')
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
    numero_dict = crear_listas_10_players()
    return numero_dict

def show_rankings_more_minutes():
    lista_rankings = []
    borrarPantalla()
    conexion = mysql.connector.connect(user='root', password='1234', host='localhost', database='projecte1',
                                       port='3306')
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
    numero_dict = crear_listas_10_players()
    return numero_dict

def rankings_more_earnings():
    numero_dict = show_rankings_more_earnings()
    borrarPantalla()
    numero_cadena = 10
    while True:
        cadena = ""
        for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
            cadena += "\n" + "".ljust(34) + player.ljust(12) + funcions_dades.dades.tabla_rankings[player][
                "name"].ljust(22) + \
                      str(funcions_dades.dades.tabla_rankings[player]["earnings"]).rjust(8) + str(
                funcions_dades.dades.tabla_rankings[player]["games"]).rjust(14) + \
                      str(funcions_dades.dades.tabla_rankings[player]["minutes"]).rjust(16)
        cadena = (funcions_dades.dades.cabecera_rankings + cadena)
        print(cadena)
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

def rankings_more_games():
    numero_dict = show_rankings_more_games()
    borrarPantalla()
    numero_cadena = 10
    while True:
        cadena = ""
        for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
            cadena += "\n" + "".ljust(34) + player.ljust(12) + funcions_dades.dades.tabla_rankings[player][
                "name"].ljust(22) + \
                      str(funcions_dades.dades.tabla_rankings[player]["earnings"]).rjust(8) + str(
                funcions_dades.dades.tabla_rankings[player]["games"]).rjust(14) + \
                      str(funcions_dades.dades.tabla_rankings[player]["minutes"]).rjust(16)
        cadena = (funcions_dades.dades.cabecera_rankings + cadena)
        print(cadena)
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

def rankings_more_minutes():
    numero_dict = show_rankings_more_minutes()
    borrarPantalla()
    numero_cadena = 10
    while True:
        cadena = ""
        for player in funcions_dades.dades.tabla_partida[str(numero_cadena)]:
            cadena += "\n" + "".ljust(34) + player.ljust(12) + funcions_dades.dades.tabla_rankings[player][
                "name"].ljust(22) + \
                      str(funcions_dades.dades.tabla_rankings[player]["earnings"]).rjust(8) + str(
                funcions_dades.dades.tabla_rankings[player]["games"]).rjust(14) + \
                      str(funcions_dades.dades.tabla_rankings[player]["minutes"]).rjust(16)
        cadena = (funcions_dades.dades.cabecera_rankings + cadena)
        print(cadena)
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
