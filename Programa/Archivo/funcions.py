import random

import funcions_dades.dades
import os


def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[], borrar_pantalla = "no"):  # 1)
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
        except:
            if opc in exceptions:
                return opc
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))


def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def newPlayer(dni="", name="", profile="", human=""):
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
        nif = str(random.randint(1,9))
        for i in range(1, 8):
            nif += str(random.randint(1, 9))
        letra = funcions_dades.dades.letrasDni[int(nif) % 23]
        nif = nif + letra
    while True:
        cadena = ("".ljust(38) + "Name:".ljust(10) + name.rjust(20) + "\n" + "".ljust(38) + "DNI:".ljust(10) + nif.rjust(20) + "\n")
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
            "".ljust(38) + "Name:".ljust(10) + name.rjust(20) + "\n" + "".ljust(38) + "DNI:".ljust(10) + nif.rjust(20)
            + "\n" + "".ljust(38) + "Profile:".ljust(10) + perfil_apuestas.rjust(20) + "\n")
    borrarPantalla()
    save_player = getOpt(cadena_new_player, "".ljust(38) + "Is ok ? Y/n: ", [], ["Y", "y", "N", "n"])
    if save_player == "y" or save_player == "Y":
        funcions_dades.dades.players[nif.upper()] = {"name": name, "human": human, "bank": False, "initialCard": "",
                                                     "priority": 0, "type": valor_apuestas, "bet": 4, "points": 0,
                                                     "cards": [], "roundPoints": 0}
    elif save_player == "n" or save_player == "N":
        return


def show_remove_players():
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
            if human_players[player] > human_players[player+1]:
                aux = human_players[player]
                human_players[player] = human_players[player+1]
                human_players[player+1] = aux

    for pasadas in range(len(boot_players) - 1):
        for player in range(len(boot_players) - 1 - pasadas):
            if boot_players[player] > boot_players[player+1]:
                aux = boot_players[player]
                boot_players[player] = boot_players[player+1]
                boot_players[player+1] = aux
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
            remove_player = input("Option ( -id to remove player, -1 to exit):\n".center(140))
            if remove_player == "-1":
                break
            else:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()
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
            remove_player = input("Option ( -id to remove player, -1 to exit):\n".center(140))
            if len(remove_player) != 2 and len(remove_player) != 10:
                print("=" * 63 + "Invalid option" + "=" * 63)
                input("Press enter to continue".center(140))
                borrarPantalla()
            elif remove_player == "-1":
                break
            elif remove_player[0] == "-" and remove_player[1:].upper() in funcions_dades.dades.players.keys():
                funcions_dades.dades.players.pop(remove_player[1:].upper())
                if remove_player[1:].upper() in human_players:
                    human_players.remove(remove_player[1:].upper())
                elif remove_player[1:].upper() in boot_players:
                    boot_players.remove(remove_player[1:].upper())
                borrarPantalla()

