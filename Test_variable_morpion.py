# Test Variable
def Ask_int(message:str, min:int = 1, max:int = 9, pos:list=[]):
    while True:

        try:
            Verif:int = int(input(message))

            if (Verif >= min and Verif <= max):    
                if (Verif in pos):
                    return Verif
            
            print('Rappel des possibilité: ',pos)
            print('Rappel des bornes min et max : [',min,',',max,']')
            
        except ValueError:
            print('ERROR')

def Ask_Input(message:str, sAuthorized: list):
    
    while True:

        Verif:str = input(message)
        if (Verif.upper() in sAuthorized):
            return Verif
        print('Entrée non valide')

def Test_Winner(player_list: list = [], Win_list: list = [],num_player:int = 0):

    Winner:int = 0
    posibility_win =[]
    for y in Win_list:
        counter:int = 0
        for x in player_list :
            if x in y :
                counter += 1
                if counter == 2:
                    posibility_win.append(y)
                if counter >= 3:
                    Winner = num_player
                    return int(Winner), list(posibility_win)
    return int(Winner) , list(posibility_win)