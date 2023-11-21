#Plus ou moins

# Add library

from random import*

# Array Value

autorisation_key_restart:list = ['O','OUI','N','NON']

# Test Variable

def Ask_int(message:str, min:int = 1, max:int = 100):
    while True:
            try:
                Verif:int = int(input(message))

                if (Verif < min or Verif > max):
                    print('Rappel des bornes min et max : [',min,',',max,']')

                else:
                    break

            except ValueError:
                print('ERROR')

    return Verif

def Ask_Input(message:str, sAuthorized: list):

    while True:

        Verif:str = input(message)
        if (Verif.upper() in sAuthorized):
            return Verif

# Start Game
def Game():
    Play:bool = True
    while Play == True:

        # Ask for maximun number

        choix_range:int = Ask_int("fixez le nombre maximum devinable (de 1 à 100): ")

        # Get random number

        num_rand:int = randint(1,choix_range)

        # Ask for maximun try

        essai:int = Ask_int("combien d'essaie te donne tu (de 1 à 8) ? ",1,8)

        # Ask for a number | Verification choice number

        while essai > 0:

            choix:int = Ask_int("Choix du nombre : ",1,choix_range)

            essai -= 1

            if choix < num_rand :
                print('C est plus')
            elif choix > num_rand :
                print('C est moins')
            else:
                print('Bien Joué')
                break

            print('Il vous reste ' + str(essai) + ' Tentative')

            if essai == 0 :
                print('PERDU')
                break
        Play=False
        Restart()
        break

# End Game | Ask for restart
def Restart():
    Restart:bool = Ask_Input("Rejouer --> 'O' / 'OUI' | STOP --> 'N' / 'NON' : ",autorisation_key_restart)
    if(Restart.upper() == autorisation_key_restart[0] or Restart.upper() == autorisation_key_restart[1]):
        print('PARTI RELANCER !')
        Game()
    else:
        print('À une prochaine fois.')

Game()