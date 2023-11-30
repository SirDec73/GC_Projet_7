#Plus ou moins

# Add library

from random import*
from Test_variable import*

# Array Value

autorisation_key_restart:list = ['O','OUI','N','NON']


# Start Game
def Game():
    Play:bool = True
    while Play == True:

        # Ask for maximun number

        choix_range:int = Ask_int("fixez le nombre maximum devinable (de 1 à 100): ")

        # Get random number

        num_rand:int = randint(1,choix_range)

        # Ask for maximun try

        essai:int = Ask_int("combien d'essais te donnes tu (de 1 à 8) ? ",1,8)

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

    # End Game | Ask for restart
    Restart:bool = Ask_Input("Rejouer --> 'O' / 'OUI' | STOP --> 'N' / 'NON' : ",autorisation_key_restart)
    if(Restart.upper() == autorisation_key_restart[0] or Restart.upper() == autorisation_key_restart[1]):
        print('PARTIE RELANCEE !')
        Play=True
    else:
        print('À une prochaine fois.')

Game()