import sys

class ai:

    def init(self):
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
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if (self.board[x][y] == self.EMPTY):
                    self.board[x][y] = self.ALLY
                    self.current_turn += 1
                    print(str(x) + "," + str(y), flush=True)
                    return True
        print("SUGGEST 0,0", flush=True)
        return False