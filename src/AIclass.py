import sys
import math
from board_analyze import calculate_board_value

class ai:

    def __init__(self):
        self.board = []
        self.current_turn = 0
        self.color = 0
        self.time = 0
        self.x = 0
        self.y = 0
        self.sizeX = 0
        self.sizeY = 0
        self.game_info = {}
        self.ALLY = 2
        self.ENEMY = 1
        self.EMPTY = 0

    from protocol import start, turn, begin, board, info, end, about, rectstart, restart, takeback, play

    ## COMMAND PARSER
    def parse_command(self, command):
        print("DEBUG Command Received ", command, flush=True)
        command_list = {"START": self.start,
                    "TURN": self.turn,
                    "BEGIN": self.begin,
                    "BOARD": self.board,
                    "INFO": self.info,
                    "END": self.end,
                    "ABOUT": self.about,
                    "RESTART": self.restart,
                    "RECTSTART": self.rectstart,
                    "TAKEBACK": self.takeback,
                    "PLAY": self.play}
        if (command[0] in command_list):
            return command_list[command[0]](command)
        else:
            print("ERROR Unknown command", flush=True)
            return False

    ## Brain of the AI
    def do_action(self):
        print("DEBUG Turn: ", self.current_turn, flush=True)
        for x in range(self.sizeX):
            print("DEBUG", self.board[x], flush=True)
        res = [[(-1 * math.inf) for x in range(self.sizeY)] for y in range(self.sizeX)]
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if (self.board[x][y] == self.EMPTY):
                    print("DEBUG COORD check", x, y, flush=True)
                    test = list()
                    for v in range(len(self.board)):
                        test.append(self.board[v][:])
                    test[x][y] = self.ALLY
                    res[x][y] = calculate_board_value(test, self.ALLY, self.ENEMY)
        val, x, y = -1 * math.inf, 0, 0
        print("DEBUG ANALYSE", flush=True)
        for x in range(self.sizeX):
            print("DEBUG", res[x], flush=True)
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if (res[i][j] > val):
                    val = res[i][j]
                    x = i
                    y = j
        if val == -1 * math.inf:
            print("SUGGEST 0,0", flush=True)
            return False
        print(str(x) + "," + str(y), flush=True)
        self.board[x][y] = self.ALLY
        return True