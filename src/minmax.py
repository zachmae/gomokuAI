from board_analyze import calculate_board_value
import math

def minmax(board: list, depth: int, my_turn: bool, ally_sign, enemy_sign):
    if depth == 0:
        return calculate_board_value(board, ally_sign, enemy_sign)
    if my_turn:
        best_score = -math.inf
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    board[y][x] = ally_sign
                    score = minmax(board, depth - 1, False, ally_sign, enemy_sign)
                    board[y][x] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    board[y][x] = enemy_sign
                    score = minmax(board, depth - 1, True, ally_sign, enemy_sign)
                    board[y][x] = 0
                    best_score = min(score, best_score)
        return best_score
