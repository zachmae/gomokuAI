from math import inf

## i must upgrade this function
def analyse_board_value(board, sign):
    score = 0
    equivalent = [0, 1, 2, 4, 8, inf]
    board_len_x = len(board)
    board_len_y = len(board[0])
    for y in range(board_len_x):
        for x in range(board_len_y):
            if board[y][x] == sign:
                actual = 0
                # check horizontal
                size_h = 1
                for i in range(1, 6):
                    if not (x + i < board_len_y and board[y][x + i] == sign):
                        break
                    size_h = i
                # check vertical
                size_v = 1
                for i in range(1, 6):
                    if not (y + i < board_len_x and board[y + i][x] == sign):
                        break
                    size_v = i
                # check diagonal up
                size_du = 1
                for i in range(1, 6):
                    if not (x + i < board_len_y and y - i >= 0 and board[y - i][x + i] == sign):
                        break
                    size_du = i
                # check diagonal down
                size_dd = 1
                for i in range(1, 6):
                    if not (x + i < board_len_y and y + i < board_len_x and board[y + i][x + i] == sign):
                        break
                    size_dd = i
                actual = sum([equivalent[size_h], equivalent[size_v], equivalent[size_du], equivalent[size_dd]])
                score += actual
    return score

def calculate_board_value(board, ally, enemy):
    ally_score = analyse_board_value(board, ally)
    enemy_score = analyse_board_value(board, enemy)
    return ally_score - enemy_score
