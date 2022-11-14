import sys
import gomoku

def main():
    gomoku.gomoku()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(84)
    sys.exit(0)