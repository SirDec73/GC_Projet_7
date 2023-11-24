# Test Variable
def Ask_int(message:str, min:int = 1, max:int = 3):
    while True:

        try:
            Verif:int = int(input(message))

            if (Verif >= min and Verif <= max):    
                return Verif
            
            print('Rapel des bornes min et max : [',min,',',max,']')
            
        except ValueError:
            print('ERROR')


def Ask_Input(message:str, sAuthorized: list):
    
    while True:

        Verif:str = input(message)
        if (Verif.upper() in sAuthorized):
            return Verif
        print('Entré non valide')
