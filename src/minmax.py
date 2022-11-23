from board_analyze import calculate_board_value
import math

def check_neighbours_one_not_empty(board : list, x : int, y : int):
    if (x and board[y][x - 1]):
        print('DEBUG gauche', flush=True)
        return True
    if (y and board[y - 1][x]):
        print('DEBUG haut', flush=True)
        return True
    if (len(board[y]) - 1 != x and board[y][x + 1]):
        print('DEBUG droite', flush=True)
        return True
    if (len(board) - 1 != y and board[y + 1][x]):
        print('DEBUG bas', flush=True)
        return True
    if (x and y and board[y - 1][x - 1]):
        print('DEBUG diagonal haut gauche', flush=True)
        return True
    if (x and len(board) - 1 != y and board[y + 1][x - 1]):
        print('DEBUG diagonal bas gauche', flush=True)
        return True
    if (len(board[y]) - 1 != x and len(board) - 1 != y and board[y + 1][x + 1]):
        print('DEBUG diagonal bas droite', flush=True)
        return True
    if (len(board[y]) - 1 != x and y and board[y - 1][x + 1]):
        print('DEBUG diagonal haut droite', flush=True)
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

def alpha_beta_prunning(board: list, depth: int, my_turn: bool, ally_sign, enemy_sign, alpha, beta):
    if depth == 0:
        return calculate_board_value(board, ally_sign, enemy_sign)
    if my_turn:
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0 and check_neighbours_one_not_empty(board, x, y):
                    board[y][x] = ally_sign
                    alpha = max(alpha, alpha_beta_prunning(board, depth - 1, False, ally_sign, enemy_sign, alpha, beta))
                    board[y][x] = 0
                    if alpha >= beta:
                        break
        return alpha
    else:
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0 and check_neighbours_one_not_empty(board, x, y):
                    board[y][x] = enemy_sign
                    beta = min(beta, alpha_beta_prunning(board, depth - 1, True, ally_sign, enemy_sign, alpha, beta))
                    board[y][x] = 0
                    if alpha >= beta:
                        break
        return beta
