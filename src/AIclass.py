ALLY = 1
ENEMY = -1
EMPTY = 0

class ai:
    def __init__(self):
        self.board = []
        self.turn = 0
        self.color = 0
        self.time = 0
        self.x = 0
        self.y = 0
        self.size = 0

    ## protocol
    def start(self, size):
        self.size = size
        if (type(size) == int and size >= 0):
            self.board = [[EMPTY for x in range(size)] for y in range(size)]
            print("OK", flush=True)
            return True
        else:
            print("ERROR Invalid size (not positive number)", flush=True)
            return False

    def turn(self, pos):
        try:
            x, y = map(int, pos.split(','))
            if (x < 0 or y < 0 or x >= self.size or y >= self.size):
                print("ERROR Invalid position (out of board)", flush=True)
                return False
            elif (self.board[x][y] != EMPTY):
                print("ERROR Invalid position (already taken)", flush=True)
                return False
            else:
                self.board[x][y] = self.color
                self.turn += 1
                print("OK", flush=True)
                return True
        except:
            print("ERROR Invalid position (not a number)", flush=True)
            return False


    ## Brain of the AI    
    def do_action(self):
        while True:
            print("im the AI, its my turn")
            continue
