def board(self, plateau):
    try:
        line = ""
        while line != "DONE":
            line = input()
            content = line.split(",")
            x = int(content[0])
            y = int(content[1])
            tile = int(content[2])
            if x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY or tile not in [self.EMPTY, self.ALLY, self.ENEMY]:
                print("ERROR: BOARD Invalid board (out of board or not in ally empty enemy)", flush=True)
                return False
            plateau[int(content[0])][int(content[1])] = int(content[2])
            return self.do_action()
    except Exception as e:
        print("ERROR: BOARD Invalid board (except)", e, flush=True)
        return False


def info(self, command):
    if len(command) != 3:
        print("ERROR: INFO Invalid info (no parameter)", flush=True)
        return False
    information = command[1:]
    self.game_info[information[0]] = information[1]


def about(self, command):
    print("name=\"Gomoku\", version=\"1.0\", author=\"Gomoku\", country=\"France\"", flush=True)