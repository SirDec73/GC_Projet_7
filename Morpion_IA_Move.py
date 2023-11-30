from random import*
def Get_Move_IA(player_possibility_win: list[list[int]], pos: list[int], choices_IA: list[int], choices_player1: list[int], possibility_win_IA :list[list[int]], grid_width:int=0 ):
# position : list

# Verify if IA can win
    for position in possibility_win_IA:
        Block_IA: int = 0
        for x in choices_player1:
            if x in position:
                Block_IA +=1
        if Block_IA == 0:
            for nb in position:
                if nb not in choices_IA:
                    if nb <= grid_width**2:
                        return nb

# If Player got Win condition : Try to block it
    for position in player_possibility_win:
        safe: int = 0
        for x in choices_IA:
            if x in position:
                safe +=1
        if safe == 0:
            for nb in position:
                if nb not in choices_player1:
                    if nb <= grid_width**2:
                        final_choose = nb
            return final_choose
# If IA can't win or block : random move
    return choice(pos)