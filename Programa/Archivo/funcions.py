import dades as dades
import os

#Limpiar pantalla
#Mohamed el Amin

def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


#20 Puntos iniciales a todos los jugadores
#Mohamed el Amin

def resetPoints():
    for key, value in dades.players.items():
        value["points"] = 20

    for clave, valor in dades.players.items():

        print("name:",valor["name"].ljust(8),"human:",str(valor["human"]).ljust(8),"bank:",str(valor["bank"]).ljust(8),
              "initialCard:", valor["initialCard"].ljust(5),"priority:",str(valor["priority"]).ljust(5),
              "type:",str(valor["type"]).ljust(5),"bet:",str(valor["bet"]).ljust(5),"points:",str(valor["points"]).ljust(5),
              "cards:", str(valor["cards"]).ljust(5),"roundPoints:",str(valor["roundPoints"]).ljust(5))


#Insertar datos en el diccionario player_game
#Mohamed el Amin
player_game = {"id_game":
                   {"id_player_1":
                        {"initial_card_id":1, "starting_points":1,"ending_points":1},
                   "id_player_2":
                       {"initial_card_id":2,"starting_points":2, "ending_points":2}
                   }
               }

def fill_player_game(player_game,gameID,*fields):



#GetOpt


def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[]):  # 1)
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
                print("="*65 + "Incorrect option" + "=" *65)
                input("Press enter to continue".center(146))
        except:
            if opc in exceptions:
                return opc
            else:
                print("="*65 + "Incorrect option" + "=" *65)
                input("Press enter to continue".center(146))


#