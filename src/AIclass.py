import sys

ALLY = 2
ENEMY = 1
EMPTY = 0

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

    ## protocol
    def start(self, size):
        try:
            self.sizeX = int(size)
            self.sizeY = int(size)
            if (type(self.sizeX) == int and self.sizeX >= 0 and type(self.sizeY) == int and self.sizeY >= 0):
                self.board = [[EMPTY for x in range(size)] for y in range(size)]
                print("OK", flush=True)
                return True
            else:
                print("ERROR Invalid size (not positive number)", flush=True)
                return False
        except:
            print("ERROR Invalid size (not a number)", flush=True)
            return False

    def turn(self, pos: str):
        try:
            x, y = map(int, pos.split(','))
            if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY):
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
        ALLY = 1
        ENEMY = 2
        EMPTY = 0
        return self.do_action()
    
    def board(self):
        try:
            line = ""
            while (line != "DONE"):
                line = input()
                content = line.split(",")
                x = int(content[0])
                y = int(content[1])
                tile = int(content[2])
                if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY or tile not in [EMPTY, ALLY, ENEMY]):
                    print("ERROR Invalid board", flush=True)
                    return False
                board[int(content[0])][int(content[1])] = int(content[2])
            return self.do_action()
        except:
            print("ERROR Invalid board", flush=True)
            return False

    def info(self, info):
        self.game_info[info[0]] = info[1]
    
    def end(self):
        pass
    
    def about(self):
        print("name=\"Gomoku\", version=\"1.0\", author=\"Gomoku\", country=\"France\"", flush=True)

    def rectstart(self, size):
        try:
            info = size.split(",")
            self.sizeX = int(info[0])
            self.sizeY = int(info[1])
            if (type(self.sizeX) == int and self.sizeX >= 0 and type(self.sizeY) == int and self.sizeY >= 0):
                self.board = [[EMPTY for x in range(sizeY)] for y in range(sizeX)]
                print("OK", flush=True)
                return True
            else:
                print("ERROR Invalid size (not positive number)", flush=True)
                return False
        except:
            print("ERROR Invalid size (not a number)", flush=True)
            return False

    def restart(self):
        self.board = [[EMPTY for x in range(self.sizeX)] for y in range(self.sizeY)]
        self.current_turn = 0
        self.color = 0
        self.time = 0
        self.x = 0
        self.y = 0
        self.game_info = {}
        print("OK", flush=True)
    
    def takeback(self, pos):
        try:
            x, y = map(int, pos.split(','))
            if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY):
                print("ERROR Invalid position (out of board)", flush=True)
                return False
            else:
                self.board[x][y] = EMPTY
                self.current_turn -= 1
                print("OK", flush=True)
                return True
        except:
            print("ERROR Invalid position (not a number)", flush=True)
            return False
        
    def play(self, pos):
        try:
            x, y = map(int, pos.split(','))
            if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY):
                print("ERROR Invalid position (out of board)", flush=True)
                return False
            elif (self.board[x][y] != EMPTY):
                print("ERROR Invalid position (already taken)", flush=True)
                return False
            self.board[x][y] = ALLY
            self.current_turn += 1
            print(str(x) + "," + str(y), flush=True)    
            return True
        except:
            print("ERROR Invalid position (not a number)", flush=True)
            return False


    ## Brain of the AI    
    def do_action(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if (self.board[x][y] == EMPTY):
                    self.board[x][y] = ALLY
                    self.current_turn += 1
                    print(str(x) + "," + str(y), flush=True)
                    return True
        print("SUGGEST 0,0", flush=True)
        return False