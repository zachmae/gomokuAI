from AIclass import ai
import sys

def gomoku():
    my_ai = ai()
    while True:
        command = input().split()
        if command[0] == "START":
            my_ai.start(int(command[1]))
        elif command[0] == "TURN":
            my_ai.turn(str(command[1]))
        elif command[0] == "BEGIN":
            my_ai.begin()
        elif command[0] == "BOARD":
            my_ai.board()
        elif command[0] == "INFO":
            my_ai.info(command[1:])
        elif command[0] == "END":
            my_ai.end()
            break