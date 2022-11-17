def start(self, command):
    size = int(command[1])
    try:
        self.sizeX = int(size)
        self.sizeY = int(size)
        if (type(self.sizeX) == int and self.sizeX > 0 and type(self.sizeY) == int and self.sizeY > 0):
            self.board = [[self.EMPTY for x in range(size)] for y in range(size)]
            print("OK", flush=True)
            return True
        else:
            print("ERROR: START Invalid size (not positive number)", flush=True)
            return False
    except Exception as e:
        print("ERROR: START Invalid size (not a number)", e, flush=True)
        return False

def turn(self, command):
    pos = command[1]
    try:
        x, y = map(int, pos.split(','))
        if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY):
            print("ERROR: TURN Invalid position (out of board)", flush=True)
            return False
        elif (self.board[x][y] != self.EMPTY):
            print("ERROR: TURN Invalid position (already taken)", x, y, board[x][y], flush=True)
            return False
        else:
            self.board[x][y] = self.ENEMY
            self.current_turn += 1
            return self.do_action()
    except Exception as e:
        print("ERROR: TURN Invalid position (not a number)", e, flush=True)
        return False

def begin(self, command):
    self.ALLY = 1
    self.ENEMY = 2
    self.EMPTY = 0
    return self.do_action()

def board(self, board):
    try:
        line = ""
        while (line != "DONE"):
            line = input()
            content = line.split(",")
            x = int(content[0])
            y = int(content[1])
            tile = int(content[2])
            if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY or tile not in [self.EMPTY, self.ALLY, self.ENEMY]):
                print("ERROR: BOARD Invalid board (out of board or not in ally empty enemy)", flush=True)
                return False
            board[int(content[0])][int(content[1])] = int(content[2])
            return self.do_action()
    except Exception as e:
        print("ERROR: BOARD Invalid board (except)", e, flush=True)
        return False

def info(self, command):
    if len(command) != 3:
        print("ERROR: INFO Invalid info (no parameter)", flush=True)
        return False
    info = command[1:]
    self.game_info[info[0]] = info[1]

def end(self, command):
    pass

def about(self, command):
    print("name=\"Gomoku\", version=\"1.0\", author=\"Gomoku\", country=\"France\"", flush=True)

def rectstart(self, command):
    size = command[1:]
    try:
        info = size.split(",")
        self.sizeX = int(info[0])
        self.sizeY = int(info[1])
        if (type(self.sizeX) == int and self.sizeX > 0 and type(self.sizeY) == int and self.sizeY > 0):
            self.board = [[self.EMPTY for x in range(self.sizeY)] for y in range(self.sizeX)]
            print("OK", flush=True)
            return True
        else:
            print("ERROR: RECTSTART Invalid size (not positive number)", flush=True)
            return False
    except Exception as e:
        print("ERROR: RECTSTART Invalid size (not a number)", e, flush=True)
        return False

def restart(self, command):
    self.board = [[self.EMPTY for x in range(self.sizeX)] for y in range(self.sizeY)]
    self.current_turn = 0
    self.color = 0
    self.time = 0
    self.x = 0
    self.y = 0
    self.game_info = {}
    print("OK", flush=True)

def takeback(self, command):
    pos = command[1:]
    try:
        x, y = map(int, pos.split(','))
        if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY):
            print("ERROR: TAKEBACK Invalid position (out of board)", flush=True)
            return False
        else:
            self.board[x][y] = self.EMPTY
            self.current_turn -= 1
            print("OK", flush=True)
            return True
    except Exception as e:
        print("ERROR: TAKEBACK Invalid position (not a number)", e, flush=True)
        return False

def play(self, command):
    pos = command[1:]
    try:
        x, y = map(int, pos.split(','))
        print("DEBUG", x, y, flush=True)
        if (x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY):
            print("ERROR: PLAY Invalid position (out of board)", flush=True)
            return False
        elif (self.board[x][y] != self.EMPTY):
            print("ERROR: PLAY Invalid position (already taken)", flush=True)
            return False
        self.board[x][y] = self.ALLY
        self.current_turn += 1
        print(str(x) + "," + str(y), flush=True)    
        return True
    except Exception as e:
            print("ERROR: PLAY Invalid position (not a number)", e, flush=True)
            return False