#!/usr/bin/env python3

import sys
import gomoku


def main():
    return gomoku.gomoku()


if __name__ == '__main__':
    try:
        if main() != 0:
            sys.exit(84)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(84)
    sys.exit(0)
