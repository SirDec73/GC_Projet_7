# Pierre Feuille Ciseaux

# Add library
from random import*
from Test_variable import*

# Initialitisation Score

score_P1=0
score_AI=0

# Array Value
Symbole:str =['Pierre','Feuille','Ciseaux']
autorisation_key_restart:str = ['O','OUI','N','NON']
list_egal: list = [[1,1],[2,2],[3,3]]
list_loose: list = [[1,2],[2,3],[3,1]]
list_win: list = [[1,3],[3,2],[2,1]]

# Start Game
def Game():
    Play: bool = True
    while Play == True:

        # Initialitisation Score

        score_P1=0
        score_AI=0

        while score_P1 !=3 and score_AI !=3: 
            
            # Ask for number (player/IA)

            choice_player:int = Ask_int('1 -> Pierre | 2 -> Feuille | 3 -> Ciseaux : ',1,3)
            choice_player -=1
            choice_AI:int = randint(1,3)
            choice_AI -=1
            print('Tu as choisi ' , Symbole[choice_player] , ' et l\'ordinateur a choisi ', Symbole[choice_AI])

            # Who win the round

            results: list[list[str]] = \
            [
                ["Egalité", "Defaite", "Victoire"],
                ["Victoire", "Egalité", "Défaite"],
                ["Défaite", "Victoire", "Egalité"],
            ]

            Add_score: list[list[function]] = \
            [
                [[0,0], [0,1], [1,0]],
                [[1,0], [0,0], [0,1]],
                [[0,1], [1,0], [0,0]],
            ]
            
            print(results[choice_player][choice_AI])

            addUser, addAI = Add_score[choice_player][choice_AI]
            score_P1 += addUser
            score_AI += addAI

            print('Score : Player --> ' , score_P1 , ' | IA --> ' , score_AI)

        #Who win the game
        
        final_result: list[str]= \
            [
                "Vous avez Perdu la partie", "Vous avez Gagné la partie"
            ]

        result_player: int = score_P1//3

        print(final_result[result_player])

        Play=False

        # Ask for Restart

        Restart:str = Ask_Input("Rejouer --> 'O' / 'OUI' | STOP --> 'N' / 'NON' : ",autorisation_key_restart)

        if(Restart.upper() == autorisation_key_restart[0] or Restart.upper() == autorisation_key_restart[1]):
            print('PARTIE RELANCEE !')
            Play = True
        else:
            print('À une prochaine fois.')

Game()