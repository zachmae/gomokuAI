import math


def checkBoard(board, searching):
    sizeY = len(board)
    sizeX = len(board[0])
    max_line = 0
    direction = 0
    pos = (0, 0)
    for y in range(sizeY):
        for x in range(sizeX):
            if board[y][x] == searching:
                # check horizontal
                sizeH = 1
                while x + sizeH < sizeX and board[y][x + sizeH] == searching: sizeH += 1
                # check vertical
                sizeV = 1
                while y + sizeV < sizeY and board[y + sizeV][x] == searching: sizeV += 1
                # check diagonal up
                sizeDU = 1
                while x + sizeDU < sizeX and y - sizeDU >= 0 and board[y - sizeDU][x + sizeDU] == searching: sizeDU += 1
                # check diagonal down
                sizeDD = 1
                while x + sizeDD < sizeX and y + sizeDD < sizeY and board[y + sizeDD][x + sizeDD] == searching:
                    sizeDD += 1
                v = max(max_line, sizeH, sizeV, sizeDU, sizeDD)
                if v != max_line:
                    direction = [max_line, sizeH, sizeV, sizeDU, sizeDD].index(v)
                    max_line = v
                    pos = (x, y)
    return max_line, pos, direction


def analyse_board_value(board, sign):
    score = 0
    equivalent = [0, 1, 2, 4, 8, math.inf]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == sign:
                actual = 0
                # check horizontal
                sizeH = 1
                while x + sizeH < len(board[0]) and board[y][x + sizeH] == sign: sizeH += 1
                # check vertical
                sizeV = 1
                while y + sizeV < len(board) and board[y + sizeV][x] == sign: sizeV += 1
                # check diagonal up
                sizeDU = 1
                while x + sizeDU < len(board[0]) and y - sizeDU >= 0 and board[y - sizeDU][
                    x + sizeDU] == sign: sizeDU += 1
                # check diagonal down
                sizeDD = 1
                while x + sizeDD < len(board[0]) and y + sizeDD < len(board) and board[y + sizeDD][
                    x + sizeDD] == sign: sizeDD += 1
                actual = sum([equivalent[sizeH], equivalent[sizeV], equivalent[sizeDU], equivalent[sizeDD]])
                score += actual
    return score


def calculate_board_value(board, ally, enemy):
    ally_score = analyse_board_value(board, ally)
    print("ally_score", ally_score)
    enemy_score = analyse_board_value(board, enemy)
    print("enemy_score", enemy_score)
    return ally_score - enemy_score


board = [[0, 0, 2, 0, 0, 0],
         [0, 1, 1, 2, 1, 1],
         [0, 0, 1, 2, 2, 0],
         [0, 0, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 0]]
print(calculate_board_value(board, 1, 2))
