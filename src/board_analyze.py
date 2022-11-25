from math import inf



def analyse_board_value(board, sign, counter_sign):
    score = 0
    equivalent = [0, 1, 2, 4, 8, inf]
    board_len_x = len(board[0])
    board_len_y = len(board)
    try:
        for y in range(board_len_x):
            for x in range(board_len_y):
                if board[x][y] == sign:
                    # check horizontal
                    multiplier = 0
                    size_h = 1
                    if (y and board[x][y - 1] not in  [counter_sign, sign]):
                        multiplier += 1
                    for i in range(1, 6):
                        size_h = i
                        if (y + i >= board_len_x or board[x][y + i] != sign):
                            break
                    if (y + size_h < board_len_x and board[x][y + size_h] != counter_sign):
                        multiplier += 1
                    if (y and board[x][y - 1] ==  sign):
                        multiplier = 0
                    if equivalent[size_h] == inf:
                        return inf
                    score += equivalent[size_h] * multiplier
                    # check vertical
                    multiplier = 0
                    size_v = 1
                    if (x and board[x - 1][y] not in  [counter_sign, sign]):
                        multiplier += 1
                    for i in range(1, 6):
                        size_v = i
                        if (x + i >= board_len_y or board[x + i][y] != sign):
                            break
                    if (x + size_v < board_len_y and board[x + size_v][y] != counter_sign):
                        multiplier += 1
                    if (x and board[x - 1][y] ==  sign):
                        multiplier = 0
                    if equivalent[size_v] == inf:
                        return inf
                    score += equivalent[size_v] * multiplier
                    # check diagonal up
                    multiplier = 0
                    size_du = 1
                    if (x != board_len_y - 1 and y and board[x + 1][y - 1] not in [counter_sign, sign]):
                        multiplier += 1
                    for i in range(1, 6):
                        size_du = i
                        if (x - i < 0 or y + i >= board_len_x or board[x - i][y + i] != sign):
                            break
                    if (x - size_du >= 0 and y + size_du < board_len_x and board[x - size_du][y + size_du] != counter_sign):
                        multiplier += 1
                    if (x != board_len_y - 1 and y and board[x + 1][y - 1] == sign):
                        multiplier = 0
                    if equivalent[size_du] == inf:
                        return inf
                    score += equivalent[size_du] * multiplier
                    # check diagonal down
                    multiplier = 0
                    size_dd = 1
                    if (x and y and board[x - 1][y - 1] not in [counter_sign, sign]):
                        multiplier += 1
                    for i in range(1, 6):
                        size_dd = i
                        if (x + i >= board_len_y or y + i >= board_len_x or board[x + i][y + i] != sign):
                            break
                    if (x + size_dd < board_len_y and y + size_dd < board_len_x and board[x + size_dd][y + size_dd] != counter_sign):
                        multiplier += 1
                    if (x and y and board[x - 1][y - 1] == sign):
                        multiplier = 0
                    if equivalent[size_dd] == inf:
                        return inf
                    score += equivalent[size_dd] * multiplier
    except Exception as e:
        print(f"ERROR error = {e}", flush=True)
    return score

def calculate_board_value(board, ally, enemy):
    ally_score = analyse_board_value(board, ally, enemy)
    enemy_score = analyse_board_value(board, enemy, ally)
    return ally_score - enemy_score
