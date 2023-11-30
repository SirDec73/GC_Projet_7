# Test Variable
def Ask_int(message:str, min:int = 1, max:int = 1, pos:list=[]):
    while True:

        try:
            Verif:int = int(input(message))
            if (Verif >= min and Verif <= max):   
                if (Verif in pos):
                    return Verif
                else:
                    return Verif
            print('Choice already taken or out of range')
            print('Reminder of the min and max terminals: [',min,',',max,']')
        except ValueError:
            print('ERROR')

def Ask_Input(message:str, sAuthorized: list[str]):
    
    while True:
        Verif:str = input(message)
        if (Verif.upper() in sAuthorized):
            return Verif
        print('Invalid enter')

# Verify winning conditions for player and AI
def Test_Winner(last_position:int , choices_list:list[int] = [] , num_player:int = 0 , align:int=0 , grid_width:int=0, possibility_win_IA:list[list[int]] = None):
    win:list[list[int]]=[]
    # Banned numbers
    StopValueRow:list[int] =[]
    StopValueCol:list[int] =[]
    Stop_value_for_diago:list[int]=[]
    Stop_value_for_diago2:list[int]=[]
    for i in range(1,grid_width+1):
        Stop = grid_width * i + 1 # Left border
        Stop_value_for_diago2.append(Stop)
        Stop = grid_width * i # Right border
        StopValueRow.append(Stop)
        Stop_value_for_diago.append(Stop)
        
        Stop = grid_width**2+grid_width - i # Bottom border
        StopValueRow.append(Stop)
        StopValueCol.append(Stop)
        Stop_value_for_diago.append(Stop)

    # Creating for possible winning columns
    start_col = last_position - grid_width*(align+1)
    for i in range(1,align+1):
        add_col_win_list: list =[]
        for j in range(1,align+1):
            ValueCol = grid_width*j + start_col + i*grid_width
            add_col_win_list.append(ValueCol)
            if ValueCol <= 0 or ValueCol in StopValueCol or ValueCol > grid_width**2:
                break
        if len(add_col_win_list) == align:
            win.append(add_col_win_list)

    # Creating for possible winning lines
    start_row = last_position - align
    for i in range(1,align+1):
        add_row_win_list: list =[]
        for j in range(0,align):
            ValueRow = start_row + j + i
            add_row_win_list.append(ValueRow)
            if ValueRow <= 0 or ValueRow in StopValueRow or ValueRow > grid_width**2:
                break
        if len(add_row_win_list) == align:
            win.append(add_row_win_list)

    # Creating for possible winning diagonals left -> right
    start_diag:int = last_position-(grid_width+1)*(align-1)
    for i in range (0,align):
        add_diag_win_list: list =[]
        for j in range(0,align):
            ValueDiag = start_diag + grid_width*j + j + (grid_width+1)*i
            add_diag_win_list.append(ValueDiag)
            if ValueDiag <= 0 or ValueDiag in Stop_value_for_diago or ValueDiag > grid_width**2:
                break
        if len(add_diag_win_list) == align:
            win.append(add_diag_win_list)

    # Creating for possible winning diagonals right -> left
    start_diag:int = last_position-(grid_width-1)*(align-1)
    for i in range (0,align):
        add_diag2_win_list: list =[]
        if start_diag >= align:
            for j in range(0,align):
                ValueDiag2 = start_diag + grid_width*j - j + (grid_width-1)*i
                add_diag2_win_list.append(ValueDiag2)
                if ValueDiag2 <= 0 or ValueDiag2 in Stop_value_for_diago2 or ValueDiag2 > grid_width**2:
                    break

        if len(add_diag2_win_list) == align:
            win.append(add_diag2_win_list)

    exception:int = 0 # exception when you need to align 4 or more
    if align >= 4:
        exception = 1
    Winner:int = 0
    if num_player == 1:
        possibility_win:list[list[int]] = []
    elif num_player == 2:
        possibility_win:list[list[int]] = possibility_win_IA

    for y in win:  # y = each win possibility
        counter:int = 0
        for each_entry in choices_list :
            if each_entry in y :
                counter += 1 # Count how many cases the player/IA have
                if counter >= align-1-exception: # If the table is larger than the amount you need to win
                    possibility_win.append(y)
                if counter >= align:
                    Winner = num_player
                    return int(Winner), list(possibility_win)
    return int(Winner) , list(possibility_win)