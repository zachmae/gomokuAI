from board_analyze import calculate_board_value
import math
import time

def check_neighbours_one_not_empty(board : list, x : int, y : int):
    board_len_x = len(board)
    board_len_y = len(board[y])
    if (x and board[y][x - 1]):
        # print('DEBUG gauche', flush=True)
        return True
    if (y and board[y - 1][x]):
        # print('DEBUG haut', flush=True)
        return True
    if (board_len_y - 1 != x and board[y][x + 1]):
        # print('DEBUG droite', flush=True)
        return True
    if (board_len_x - 1 != y and board[y + 1][x]):
        # print('DEBUG bas', flush=True)
        return True
    if (x and y and board[y - 1][x - 1]):
        # print('DEBUG diagonal haut gauche', flush=True)
        return True
    if (x and board_len_x - 1 != y and board[y + 1][x - 1]):
        # print('DEBUG diagonal bas gauche', flush=True)
        return True
    if (board_len_y - 1 != x and board_len_x - 1 != y and board[y + 1][x + 1]):
        # print('DEBUG diagonal bas droite', flush=True)
        return True
    if (board_len_y - 1 != x and y and board[y - 1][x + 1]):
        # print('DEBUG diagonal haut droite', flush=True)
        return True
    return False

def minmax(board: list, depth: int, my_turn: bool, ally_sign, enemy_sign):
    if depth == 0:
        return calculate_board_value(board, ally_sign, enemy_sign)
    if my_turn:
        best_score = -math.inf
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0 and check_neighbours_one_not_empty(board, x, y):
                    board[y][x] = ally_sign
                    score = minmax(board, depth - 1, False, ally_sign, enemy_sign)
                    board[y][x] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0 and check_neighbours_one_not_empty(board, x, y):
                    board[y][x] = enemy_sign
                    score = minmax(board, depth - 1, True, ally_sign, enemy_sign)
                    board[y][x] = 0
                    best_score = min(score, best_score)
        return best_score

def alpha_beta_prunning(board: list, depth: int, my_turn: bool, ally_sign, enemy_sign, alpha, beta, timelimit, start_stamp):
    if depth == 0:
        return calculate_board_value(board, ally_sign, enemy_sign)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0 and check_neighbours_one_not_empty(board, x, y):
                board[y][x] = ally_sign if my_turn else enemy_sign
                value = alpha_beta_prunning(board, depth - 1, not my_turn, ally_sign, enemy_sign, alpha, beta, timelimit, start_stamp)
                if my_turn:
                    alpha = max(alpha, value)
                else:
                    beta = min(beta, value)
                board[y][x] = 0
                if alpha >= beta or int(time.time()) * 1000 - start_stamp > timelimit * 0.9:
                    return alpha if my_turn else beta
    return alpha if my_turn else beta
