/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** start
*/

#include "gomoku.hpp"
#include <iostream>
#include <ranges>

bool Gomoku::begin(std::vector<int> command)
{
    _ENEMY = 2;
    _ALLY = 1;
}

/*bool Gomoku::turn(std::vector<int> command)
{
    std::pair<int, int> pos;

    if (command.size() < 2) {
        std::cout << "ERROR TURN command invalid" << std::endl;
        return false;
    }
    auto split = command | std::ranges::views::split(' ')
    std::views::split(command, ',');
}*/

// def turn(self, command):
//     pos = command[1]
//     try:
//         x, y = map(int, pos.split(','))

//         if x < 0 or y < 0 or x >= self.sizeX or y >= self.sizeY:
//             print("ERROR: TURN Invalid position (out of board)", flush=True)
//             return False
//         elif self.game_board[x][y] != self.EMPTY:
//             print("ERROR: TURN Invalid position (already taken)", x, y, pos[x][y], flush=True)
//             return False
//         else:
//             self.game_board[x][y] = self.ENEMY
//             self.current_turn += 1
//             return self.do_minmax()
//     except Exception as e:
//         print("ERROR: TURN Invalid position (not a number)", e, flush=True)
//         return False
