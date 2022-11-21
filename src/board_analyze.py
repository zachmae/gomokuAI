from math import inf


def analyse_board_value(board, sign):
    score = 0
    equivalent = [0, 1, 2, 4, 8, inf]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == sign:
                actual = 0
                # check horizontal
                size_h = 1
                while x + size_h < len(board[0]) and board[y][x + size_h] == sign: size_h += 1
                if size_h > 5: size_h = 5
                # check vertical
                sie_v = 1
                while y + sie_v < len(board) and board[y + sie_v][x] == sign: sie_v += 1
                if sie_v > 5: sie_v = 5
                # check diagonal up
                size_du = 1
                while x + size_du < len(board[0]) and y - size_du >= 0 and board[y - size_du][x + size_du] == sign: size_du += 1
                if size_du > 5: size_du = 5
                # check diagonal down
                size_dd = 1
                while x + size_dd < len(board[0]) and y + size_dd < len(board) and board[y + size_dd][x + size_dd] == sign: size_dd += 1
                if size_dd > 5: size_dd = 5
                actual = sum([equivalent[size_h], equivalent[sie_v], equivalent[size_du], equivalent[size_dd]])
                score += actual
    return score


def calculate_board_value(board, ally, enemy):
    ally_score = analyse_board_value(board, ally)
    enemy_score = analyse_board_value(board, enemy)
    return ally_score - enemy_score
