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
        elif command[0] == "ABOUT":
            my_ai.about()
        elif command[0] == "RESTART":
            my_ai.restart()
        elif command[0] == "RECTSTART":
            my_ai.rectstart(command[1:])
        elif command[0] == "TAKEBACK":
            my_ai.takeback(command[1:])
        elif command[0] == "PLAY":
            my_ai.play(command[1])
        else:
            print("ERROR Invalid command", flush=True)
    return 0