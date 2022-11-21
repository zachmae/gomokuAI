from AIclass import Ai


def gomoku():
    my_ai = Ai()
    command = ["NULL"]

    while command:
        command = input().split()
        if len(command) == 1 and command[0] == "END":
            return 0
        my_ai.parse_command(command)
    return 84
