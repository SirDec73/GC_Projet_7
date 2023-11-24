#Morpion
#Import variable from file
from Test_variable_morpion import *
from Morpion_IA_Move import *
from random import *


autorisation_key_restart:str = ['O','OUI','N','NON']

def Game():
    End: int = 0
    while End == 0:
        #Initialisation Variable
        choices_player1: list = []
        choices_IA: list = []
        pos: list = [1,2,3,4,5,6,7,8,9]
        win: list =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[7,5,3]]
        display: list = [1,2,3,4,5,6,7,8,9]
        End: int = 0
        possibility_win_IA :list = []
        while End == 0:
            # Display of the board
            for i in range(0,3):
                print('|' , display[i+i*2] ,'|' , display[1+i+i*2] ,'|' , display[2+i+i*2] ,'| \n')
            
            #Player 1 Turn
            choice_player1: int = \
            Ask_int ("Tour Joueur 1, Choisissez une position entre 1 a 9 : " , 1 , 9 , pos)
            choices_player1.append(choice_player1)
            display[choice_player1-1] = "X"

            #Verification if the winning condition are met
            End , possibility_win_player = Test_Winner(choices_player1, win,  1)
            if End == 1:
                break

            #Removing from the possible move the player choice
            pos.remove(choice_player1)
            if len(pos) == 0:
                End = 3
                break

            #IA Choice
            choice_IA = Move_IA(possibility_win_player, pos, choices_IA, choices_player1,possibility_win_IA) # add possibility win IA
            choices_IA.append(choice_IA)
            display[choice_IA-1] = "O"
            print("L'IA a choisi la position "+ str(choice_IA))
            
            #Verification if the winning condition are met
            End, possibility_win_IA = Test_Winner(choices_IA, win, 2)
            if End == 2:
                break

            #Removing the player's choice from the available moves
            pos.remove(choice_IA)

        for i in range(0,3):
            print('|' , display[i+i*2] ,'|' , display[1+i+i*2] ,'|' , display[2+i+i*2] ,'| \n')
        if End == 3:
            print('Match Nul !')
        elif End == 1:
            print('Victoire du Joueur')
        else:
            print("Victoire de L'IA")
        
        Restart:str = Ask_Input("Rejouer --> 'O' / 'OUI' | STOP --> 'N' / 'NON' : ",autorisation_key_restart)
        if(Restart.upper() == autorisation_key_restart[0] or Restart.upper() == autorisation_key_restart[1]):
            print('PARTI RELANCEE !')
            End = 0
        else:
            print('À une prochaine fois.')

Game()

#Si envie, donner une option d'utiliser l'IA basique ou avancée
#Verifier que ca ne crash pas si input etrange (lettres et numeros > 9)