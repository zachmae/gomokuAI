# GOMOKU #

GOMOKU is an Epitech third year project that consist of the implementation of an AI for gomoku board game.
I've accomplished this project with my team mate [Ines](https://github.com/Happinesseuh) and [Erwan](https://github.com/ErwanC7).

This consisit of an implementation of the Minimax algorithm with alpha-beta pruning and a heuristic function in python.

We followed the piskvork protocol to communicate with the game engine used by the AI.

We also won EPITECH PARIS 2023 gomoku tournament in which our AI faced the one made by other students.

## Prerequies ##
*you will have to installed python 3:*

and to generate the binary you will need to install pyinstaller:
```
    pip install pyinstaller
```
or
```
    pip install -r requirements.txt
```

## Installation and Usage ##

You can generate the binary by running this command from the root of the project:
```
    pyinstaller --onefile --noconsole --name gomoku src/main.py
```
or use the powershell script:
```
    ./generate_binary.ps1
```

then you can test the binary in piskvork on this [link](https://sourceforge.net/projects/piskvork/)

## Contributors ##

This game has been done in the context of an Epitech project.</br>
Here is the developer team (you can join us by mail):

- Zacharie LAWSON - zacharie.lawson@epitech.eu
- Erwan CARIOU - erwan1.cariou@epitech.eu
- Ines MAAROUFI - ines.maaroufi@epitech.eu
