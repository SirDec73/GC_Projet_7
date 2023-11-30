# Morpion
from Test_variable_morpion import *
from Morpion_IA_Move import *
from random import *
import time
autorisation_key_restart:str = ['Y','YES','N','NO']

def Game():
    End: int = 0
    while End == 0:
        
        # Def Variable
        choices_player1: list = []
        choices_IA: list = []
        pos: list[int] = []
        display: list[int] = []
        
        # Game width
        grid_width = Ask_int('choose the size of the grid (between 3 and 10,000): ', 3, 10000)
        align = Ask_int ( "choose the number of alignment to win between 3 and " + str(grid_width) + ": " , 3, grid_width)

        # Alignment required to win. (Predetermined)
        # Create a Table for possible moves
        for i in range (0,grid_width**2): 
            pos.append(int(i+1)) # Adds them to the possible options to select when playing
        
        # Create a similar table as the one before, but for the display (for changing the display value in the future)
        for i in range (0,grid_width**2):
            display.append(str(i+1))
        
        
        #Display of the board for a better visual all along the game
        End: int = 0
        possibility_win_IA :list = []
        
        while End == 0:
            space_1:str = ''
            space_2:str = ''
            #Display of the board for a better visual all along the game
            for i in range(0,grid_width):
                for j in range(0,grid_width):
                    if (j+i*grid_width) >= 0 and (j+i*grid_width) < 9 :
                        space_1 = ' '
                        space_2 = ' '
                    elif j+i*grid_width >= 9 and j+i*grid_width <= 98:
                        space_1 = ' '
                        space_2 = ''
                    else:
                        space_1 = ''
                        space_2 = ''
                    if (j < grid_width-1):
                        print('|' , space_1 + display[j+i*grid_width] + space_2 ,'|', end ='')
                    else:
                        print('|' , space_1 + display[j+i*grid_width] + space_2 ,'|')
            
            # Player 1 Turn
            choice_player1: int = \
            Ask_int ("Your turn, choose a position between 1 and " + str(grid_width**2) + ": " , 1 , grid_width**2, pos)
            
            choices_player1.append(choice_player1)
            display[choice_player1-1] = "X"
            
            # Fix for display purposes
            if choice_player1 >= 10:
                display[choice_player1-1] += " "
            
            # Verify if the player winning condition is met

            End , possibility_win_player = Test_Winner(choice_player1,choices_player1, 1, align, grid_width)
            

            if End == 1:
                break

            # Removing from the possible move the player choice
            pos.remove(int(choice_player1))
            
            # If grid is full and nobody won = game over
            if len(pos) == 0:
                End = 3
                break

            # IA Choice
            choice_IA = Get_Move_IA(possibility_win_player, pos, choices_IA, choices_player1,possibility_win_IA, grid_width) # add possibility win IA
            choices_IA.append(choice_IA)

            display[choice_IA-1] = "O"
            
            # For display purposes
            if choice_IA >= 10:
                display[choice_IA-1] += " "
            
            print("Computer choose "+ str(choice_IA))
            
            # Verify if the AI winning condition is met
            print("Testing ...")
            start = time.time()
            End, possibility_win_IA = Test_Winner(choice_IA,choices_IA, 2, align, grid_width , possibility_win_IA)
            end = time.time()
            print("Done in " + str(end - start))
            if End == 2:
                break

            #Removing the player's choice from the available moves
            pos.remove(choice_IA)
            if len(pos) == 0:
                End = 3
                break
            #Reset the possibilities of winning for the AI if the previous attempt have failed
            for i in possibility_win_IA:
                counter = 0
                for j in i:
                    if j in choices_player1 or j in choices_IA:
                        counter += 1
                if counter == align:
                    possibility_win_IA.remove(i)

        # Final grid display (After you lost/won)
        for i in range(0,grid_width):
            for j in range(0,grid_width):
                if (j+i*grid_width) >= 0 and (j+i*grid_width) < 9 :
                    space_1 = ' '
                    space_2 = ' '
                elif j+i*grid_width >= 9 and j+i*grid_width <= 98:
                    space_1 = ' '
                    space_2 = ''
                else:
                    space_1 = ''
                    space_2 = ''
                if (j < grid_width-1):
                    print('|' , space_1 + display[j+i*grid_width] + space_2 ,'|', end ='')
                else:
                    print('|' , space_1 + display[j+i*grid_width] + space_2 ,'|')

        Winner = ['You Win !', "You Lose...", 'That a Draw !']
        print(Winner[End - 1])
        
        # Restart the game
        Restart:str = Ask_Input("Retry --> 'Y' / 'YES' | STOP --> 'N' / 'NO' : ",autorisation_key_restart)
        if(Restart.upper() == autorisation_key_restart[0] or Restart.upper() == autorisation_key_restart[1]):
            print('Game Restarted !')
            End = 0
        else:
            print('See you next time')
Game()