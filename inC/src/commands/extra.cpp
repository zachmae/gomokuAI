/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** Gomoku
*/

#include <iostream>
#include "gomoku.hpp"

bool Gomoku::board(const std::string &data)
{
    return true;
}

bool Gomoku::about(std::string const &data)
{
    std::cout << R"(name="Gomoku", version="1.0", author="Gomoku", country="France")" << std::endl;
    return true;
}

bool Gomoku::info(std::string const &data)
{
    return true;
}



/*def board(self, plateau):
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
        return self.do_minmax()
    except Exception as e:
        print("ERROR: BOARD Invalid board (except)", e, flush=True)
        return False*/
