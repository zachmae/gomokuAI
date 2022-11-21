from math import inf
from board_analyze import calculate_board_value
from minmax import minmax


class Ai:

    def __init__(self):
        self.game_board = []
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

    from commands.extra import board, info, about
    from commands.start import start, rect_start, restart
    from commands.move import begin, turn, play, take_back

    ## COMMAND PARSER
    def parse_command(self, command):
        print("MESSAGE Command Received ", command, flush=True)
        command_list = {"START": self.start,
                        "TURN": self.turn,
                        "BEGIN": self.begin,
                        "BOARD": self.board,
                        "INFO": self.info,
                        "ABOUT": self.about,
                        "RESTART": self.restart,
                        "RECTSTART": self.rect_start,
                        "TAKEBACK": self.take_back,
                        "PLAY": self.play}
        if command[0] in command_list:
            return command_list[command[0]](command)
        else:
            print("ERROR Unknown command", flush=True)
            return False

    ## Brain of the AI
    def do_minmax(self):
        best_value = -inf
        best_move = (0, 0)
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if (self.game_board[x][y] == self.EMPTY):
                    self.game_board[x][y] = self.ALLY
                    value = minmax(self.game_board, 2,True, self.ALLY, self.ENEMY)
                    self.game_board[x][y] = self.EMPTY
                    if (value > best_value):
                        best_value = value
                        best_move = (x, y)
        print(str(best_move[0]) + "," + str(best_move[1]), flush=True)
        self.game_board[best_move[0]][best_move[1]] = self.ALLY
        return True

    ## Brain of the AI
    def do_action(self):
        print("DEBUG Turn: ", self.current_turn, flush=True)
        for x in range(self.sizeX):
            print("DEBUG", self.game_board[x], flush=True)
        res = [[(-1 * inf) for x in range(self.sizeY)] for y in range(self.sizeX)]
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if self.game_board[x][y] == self.EMPTY:
                    print("DEBUG COORD check", x, y, flush=True)
                    test = list()
                    for v in range(len(self.game_board)):
                        test.append(self.game_board[v][:])
                    test[x][y] = self.ALLY
                    res[x][y] = calculate_board_value(test, self.ALLY, self.ENEMY)
        val, x, y = -1 * inf, 0, 0
        print("DEBUG ANALYSE", flush=True)
        for x in range(self.sizeX):
            print("DEBUG", res[x], flush=True)
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if res[i][j] > val:
                    val = res[i][j]
                    x = i
                    y = j
        if val == -1 * inf:
            print("SUGGEST 0,0", flush=True)
            return False
        print(str(x) + "," + str(y), flush=True)
        self.game_board[x][y] = self.ALLY
        return True