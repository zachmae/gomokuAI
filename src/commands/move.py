def begin(self, command):
    self.ALLY = 1
    self.ENEMY = 2
    self.EMPTY = 0
    return self.do_minmax()


def turn(self, command):
    pos = command[1]
    try:
        x, y = map(int, pos.split(','))
        if x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY:
            print("ERROR: TURN Invalid position (out of board)", flush=True)
            return False
        elif self.game_board[x][y] != self.EMPTY:
            print("ERROR: TURN Invalid position (already taken)", x, y, pos[x][y], flush=True)
            return False
        else:
            self.game_board[x][y] = self.ENEMY
            self.current_turn += 1
            return self.do_minmax()
    except Exception as e:
        print("ERROR: TURN Invalid position (not a number)", e, flush=True)
        return False


def play(self, command):
    pos = command[1:]
    try:
        x, y = map(int, pos.split(','))
        print("DEBUG", x, y, flush=True)
        if x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY:
            print("ERROR: PLAY Invalid position (out of board)", flush=True)
            return False
        elif self.game_board[x][y] != self.EMPTY:
            print("ERROR: PLAY Invalid position (already taken)", flush=True)
            return False
        self.game_board[x][y] = self.ALLY
        self.current_turn += 1
        print(str(x) + "," + str(y), flush=True)
        return True
    except Exception as e:
        print("ERROR: PLAY Invalid position (not a number)", e, flush=True)
        return False


def take_back(self, command):
    pos = command[1:]
    try:
        x, y = map(int, pos.split(','))
        if x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY:
            print("ERROR: TAKEBACK Invalid position (out of board)", flush=True)
            return False
        else:
            self.game_board[x][y] = self.EMPTY
            self.current_turn -= 1
            print("OK", flush=True)
            return True
    except Exception as e:
        print("ERROR: TAKEBACK Invalid position (not a number)", e, flush=True)
        return False
