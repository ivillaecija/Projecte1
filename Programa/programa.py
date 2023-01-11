import funcions_dades.funcions as funcions

menu00 = "1)Add/Remove/Show Players" + "\n" + "2)Settings" + "\n" + "3)Play Game" + "\n" + "4)Ranking" + "\n" + "5) Reports" + "\n" + "6) Exit"
menu01 = "1)New Human Player" + "\n" + "2)New Boot" + "\n" + "3)Show/Remove Players" + "\n" + "4)Go back"
menu02 = "1)Set Game Players" + "\n" + "2)Set Card's Deck" + "\n" + "3)Set Max Rounds (Default 5 rounds)" + "\n" + "4)Go back"
menu04 = "1)Players With More Earnings" + "\n" + "2)Players With More Games Played" + "\n" + "Players With More Minutes Played" + "\n" + "Go back"

flg_00 = True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False
salir = False

while not salir:
    while flg_00:
        opc = funcions.getOpt(menu00, "Option: ", [1,2,3,4,5,6])
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
        opc = funcions.getOpt(menu01, "Option: ", [1,2,3,4])
        if opc == 1:
            print()
        elif opc == 2:
            print()
        elif opc == 3:
            print()
        elif opc == 4:
            flg_01 = False
            flg_00 = True
    while flg_02:
        opc = funcions.getOpt(menu02, "Option: ", [1, 2, 3, 4])
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
        print()
    while flg_04:
        opc = funcions.getOpt(menu04, "Option: ", [1, 2, 3, 4])
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
        print()
