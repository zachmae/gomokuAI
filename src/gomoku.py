from AIclass import ai
import sys

def gomoku():
    my_ai = ai()
    command = ["INIT", "YES"]

    while command[0] != "END":
        command = input().split()
        my_ai.parse_command(command)
    return 0