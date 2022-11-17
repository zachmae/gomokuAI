import math

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
                if sizeH > 5: sizeH = 5
                #check vertical
                sizeV = 1
                while y + sizeV < len(board) and board[y + sizeV][x] == sign: sizeV += 1
                if sizeV > 5: sizeV = 5
                #check diagonal up
                sizeDU = 1
                while x + sizeDU < len(board[0]) and y - sizeDU >= 0 and board[y - sizeDU][x + sizeDU] == sign: sizeDU += 1
                if sizeDU > 5: sizeDU = 5
                #check diagonal down
                sizeDD = 1
                while x + sizeDD < len(board[0]) and y + sizeDD < len(board) and board[y + sizeDD][x + sizeDD] == sign: sizeDD += 1
                if sizeDD > 5: sizeDD = 5
                actual = sum([equivalent[sizeH], equivalent[sizeV], equivalent[sizeDU], equivalent[sizeDD]])
                score += actual
    return score

def calculate_board_value(board, ally, enemy):
    ally_score = analyse_board_value(board, ally)
    enemy_score = analyse_board_value(board, enemy)
    return ally_score - enemy_score
