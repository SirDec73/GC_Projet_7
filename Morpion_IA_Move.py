from random import*
def Move_IA(player_posibility_win: list, pos: list, choices_IA: list, choices_player1: list, possibility_win_IA :list):
# position : list

# Verification if IA can WIN
    for position in possibility_win_IA:
        win: int = 0
        for x in choices_player1:
            if x in position:
                win +=1
        if win == 0:
            for nb in position:
                if nb not in choices_IA:
                    return nb
# If Player got Win condition : Try to block it
    for position in player_posibility_win: 
        safe: int = 0
        for x in choices_IA:
            if x in position:
                safe +=1
        if safe == 0:
            for nb in position:
                if nb not in choices_player1:
                    return nb
    return choice(pos)