import sys

ALLY = 1
ENEMY = -1
EMPTY = 0

class ai:
    def __init__(self):
        self.board = []
        self.current_turn = 0
        self.color = 0
        self.time = 0
        self.x = 0
        self.y = 0
        self.size = 0
        self.game_info = {}

    ## protocol
    def start(self, size):
        self.size = int(size)
        if (type(self.size) == int and self.size >= 0):
            self.board = [[EMPTY for x in range(size)] for y in range(size)]
            print("OK", flush=True)
            return True
        else:
            print("ERROR Invalid size (not positive number)", flush=True)
            return False

    def turn(self, pos: str):
        try:
            x, y = map(int, pos.split(','))
            if (x < 0 or y < 0 or x >= self.size or y >= self.size):
                print("ERROR Invalid position (out of board)", flush=True)
                return False
            elif (self.board[x][y] != EMPTY):
                print("ERROR Invalid position (already taken)", flush=True)
                return False
            else:
                self.board[x][y] = ENEMY
                self.current_turn += 1
                return self.do_action()
        except:
            print("ERROR Invalid position (not a number)", flush=True)
            return False

    def begin(self):
        self.do_action()
    
    def board(self):
        while (input() != "DONE"):
            pass
        return self.do_action()

    def info(self, info):
        self.game_info[info[0]] = info[1]
    
    def end(self):
        pass
    
    def about(self):
        print("name=\"Gomoku\", version=\"1.0\", author=\"Gomoku\", country=\"France\"")

    ## Brain of the AI    
    def do_action(self):
        for x in range(self.size):
            for y in range(self.size):
                if (self.board[x][y] == EMPTY):
                    self.board[x][y] = ALLY
                    self.current_turn += 1
                    print(str(x) + "," + str(y), flush=True)
                    return True
        print("ERROR No more space", flush=True)
        return False