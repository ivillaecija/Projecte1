import funcions_dades.dades
import funcions_dades.funcions as funcions

menu00 = "".ljust(55) + "1)Add/Remove/Show Players"+ "\n" + "".ljust(55) + "2)Settings" + "\n" + "".ljust(55) + "3)Play Game" + "\n" + "".ljust(55) + "4)Ranking" + "\n" + "".ljust(55) + "5)Reports" + "\n" + "".ljust(55) + "6)Exit"
menu01 = "".ljust(55) + "1)New Human Player" + "\n" + "".ljust(55) + "2)New Boot" + "\n" + "".ljust(55) + "3)Show/Remove Players"+ "\n" + "".ljust(55) + "4)Go back"
menu02 = "".ljust(55) + "1)Set Game Players" + "\n" + "".ljust(55) + "2)Set Card's Deck" + "\n" + "".ljust(55) + "3)Set Max Rounds (Default 5 rounds)" + "\n" + "".ljust(55) + "4)Go back"
menu04 = "".ljust(55) + "1)Players With More Earnings" + "\n" + "".ljust(55) + "2)Players With More Games Played" + "\n" + "".ljust(55) + "3)Players With More Minutes Played" + "\n" + "".ljust(55) + "4)Go back"
menu05 = "".ljust(42) + "1)  Initial card more repeated by each user" + "\n" + "".ljust(46) + "only users who have played a minimum of 3 games." + \
         "\n" + "".ljust(42) + "2)  Player who makes the highest bet per game" + "\n" + "".ljust(46) + "find the round with the highest bet." + \
         "\n" + "".ljust(42) + "3)  Player who makes the lowest bet per game." + "\n" + "".ljust(42) + "4)  Percentage of rounds won per player in each game" + \
         "\n" + "".ljust(46) + "(%), as well as their average bet for the game." + "\n" + "".ljust(42) + "5)  List of games won by Bots." + \
         "\n" + "".ljust(42) + "6)  Rounds won by the bank in each game." + "\n" + "".ljust(42) + "7)  Number of users have been the bank in each game." + \
         "\n" + "".ljust(42) + "8)  Average bet per game." + "\n" + "".ljust(42) + "9)  Average bet of the first round of each game." + \
         "\n" + "".ljust(42) + "10) Average bet of the last round of each game." + "\n" + "".ljust(42) + "11) Go back"

flg_00 = True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False
salir = False

while not salir:
    while flg_00:
        funcions.borrarPantalla()
        opc = funcions.getOpt(menu00, "".ljust(55) + "Option: ", [1,2,3,4,5,6])
        if opc == 1:
            flg_00 = False
            flg_01 = True
        elif opc == 2:
            flg_00 = False
            flg_02 = True
        elif opc == 3:
            flg_00 = False
            flg_03 = True
        elif opc == 4:
            flg_00 = False
            flg_04 = True
        elif opc == 5:
            flg_00 = False
            flg_05 = True
        elif opc == 6:
            flg_00 = False
            salir = True
    while flg_01:
        funcions.borrarPantalla()
        opc = funcions.getOpt(menu01, "".ljust(55) + "Option: ", [1,2,3,4])
        if opc == 1:
            newplayer = funcions.newPlayer(human=True)
        elif opc == 2:
            newplayer = funcions.newPlayer(human=False)
        elif opc == 3:
            remove_player = funcions.show_remove_players()
        elif opc == 4:
            flg_01 = False
            flg_00 = True
    while flg_02:
        funcions.borrarPantalla()
        opc = funcions.getOpt(menu02, "".ljust(55) + "Option: ", [1, 2, 3, 4])
        if opc == 1:
            print()
        elif opc == 2:
            print()
        elif opc == 3:
            print()
        elif opc == 4:
            flg_02 = False
            flg_00 = True
    while flg_03:
        funcions.borrarPantalla()
        input()
        flg_03 = False
        flg_00 = True
    while flg_04:
        funcions.borrarPantalla()
        opc = funcions.getOpt(menu04, "".ljust(55) + "Option: ", [1, 2, 3, 4])
        if opc == 1:
            print()
        elif opc == 2:
            print()
        elif opc == 3:
            print()
        elif opc == 4:
            flg_04 = False
            flg_00 = True
    while flg_05:
        funcions.borrarPantalla()
        opc = funcions.getOpt(menu05, "".ljust(42) + "Option: ", [1,2,3,4,5,6,7,8,9,10,11])
        if opc == 1:
            print()
        elif opc == 2:
            print()
        elif opc == 3:
            print()
        elif opc == 4:
            print()
        elif opc == 5:
            print()
        elif opc == 6:
            print()
        elif opc == 7:
            print()
        elif opc == 8:
            print()
        elif opc == 9:
            print()
        elif opc == 10:
            print()
        elif opc == 11:
            flg_05 = False
            flg_00 = True

