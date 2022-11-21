def start(self, command):
    if len(command) != 2:
        print("ERROR: START Invalid number of arguments", flush=True)
        return False
    try:
        size = int(command[1])
        self.sizeX = size
        self.sizeY = size
        if self.sizeX > 5 and self.sizeY > 5:
            self.board = [[self.EMPTY for x in range(size)] for y in range(size)]
            print("OK", flush=True)
            return True
        else:
            print("ERROR: START Invalid size (not positive number)", flush=True)
            return False
    except Exception as e:
        print("ERROR: START Invalid size (not a number)", e, flush=True)
        return False


def rect_start(self, command):
    size = command[1].split(",")
    if len(size) != 2:
        print("ERROR: RECTSTART Invalid number of arguments", flush=True)
        return False
    try:
        self.sizeX = int(size[0])
        self.sizeY = int(size[1])
        if self.sizeX > 0 and self.sizeY > 0:
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
