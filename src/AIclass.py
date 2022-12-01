from math import inf
from board_analyze import calculate_board_value
from minmax import minmax, alpha_beta_prunning
import time

def get_5_by_5_board_centered_on(board, x, y):
    board_len_x = len(board)
    board_len_y = len(board[0])
    new_board = []
    for i in range(-2, 3):
        new_board.append([])
        for j in range(-2, 3):
            if (x + i < 0 or x + i >= board_len_x or y + j < 0 or y + j >= board_len_y):
                new_board[i + 2].append(0)
            else:
                new_board[i + 2].append(board[x + i][y + j])
    return new_board

def distance_from_middle(x, y, board):
    middle_x = len(board[0]) // 2
    middle_y = len(board) // 2
    return abs(x - middle_x) + abs(y - middle_y)

class Ai:

    def __init__(self):
        self.game_board = []
        self.current_turn = 0
        self.sizeX = 0
        self.sizeY = 0
        self.game_info = {}
        self.ALLY = 2
        self.ENEMY = 1
        self.EMPTY = 0

    from commands.extra import board, info, about, display
    from commands.start import start, rect_start, restart
    from commands.move import begin, turn, play, take_back

    ## COMMAND PARSER
    def parse_command(self, command):
        print(f"MESSAGE Command Received {command}", flush=True)
        command_list = {"START": self.start,
                        "TURN": self.turn,
                        "BEGIN": self.begin,
                        "BOARD": self.board,
                        "INFO": self.info,
                        "ABOUT": self.about,
                        "RESTART": self.restart,
                        "RECTSTART": self.rect_start,
                        "TAKEBACK": self.take_back,
                        "PLAY": self.play,
                        "DISPLAY": self.display}
        if command[0] in command_list:
            return command_list[command[0]](command)
        else:
            print("ERROR Unknown command", flush=True)
            return False

    ## Brain of the AI
    def do_minmax(self):
        CURRENT_TIME = int(time.time() * 1000)
        printed = False
        best_value = -inf
        set_move = False
        best_move = (len(self.game_board[0]) // 2, len(self.game_board) // 2)
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if (self.game_board[x][y] == self.EMPTY):
                    closest = get_5_by_5_board_centered_on(self.game_board, x, y)
                    c = 0
                    for i in closest:
                        if (any([self.ALLY, self.ENEMY]) in i):
                            c += 1
                    if (c):
                        self.game_board[x][y] = self.ALLY
                        value = alpha_beta_prunning(self.game_board, 1, False, self.ALLY, self.ENEMY, -inf, inf, int(self.game_info["timeout_turn"]), CURRENT_TIME)
                        self.game_board[x][y] = self.EMPTY
                        if (value > best_value or (value == best_value and distance_from_middle(x, y, self.game_board) < distance_from_middle(best_move[0], best_move[1], self.game_board)) or set_move == False):
                            best_value = value
                            best_move = (x, y)
                            set_move = True
        if (set_move == False):
            print("MESSAGE No move found", flush=True)
        print(f"{best_move[0]},{best_move[1]}", flush=True)
        self.game_board[best_move[0]][best_move[1]] = self.ALLY
        return True
