/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** Gomoku
*/

#include <iostream>
#include "gomoku.hpp"

static std::vector<std::string> strToVector(std::string const &str, char delim)
{
    std::vector<std::string> result;
    std::string tmp;

    for (auto &it : str) {
        if (it == delim) {
            result.push_back(tmp);
            tmp.clear();
        } else {
            tmp += it;
        }
    }
    result.push_back(tmp);
    return result;
}

std::vector<int> Gomoku::getContent(const std::string &line) const
{
    int x = 0;
    int y = 0;
    int tile = 0;
    std::vector<std::string> content = strToVector(line, ',');

    if (content.size() != 3) {
        std::cout << "ERROR: Invalid board data" << std::endl;
        return {};
    }
    try {
        x = std::stoi(content[0]);
        y = std::stoi(content[1]);
        tile = std::stoi(content[2]);
    } catch (std::exception &e) {
        std::cout << "ERROR BOARD x,y or tile isn't a number" << std::endl;
        return {};
    }
    if (x < 0 || y < 0 || x >= _boardSize.first || y >= _boardSize.second || (tile != 1 && tile != 2)) {
        std::cout << "ERROR BOARD Invalid board (out of board or not in ally empty enemy)" << std::endl;
        return {};
    }
    return {x, y, tile};
}

bool Gomoku::board([[maybe_unused]] const std::string &data)
{
    std::string line;
    std::vector<int> content;

    std::getline(std::cin, line);
    while (line != "DONE") {
        content = getContent(line);
        if (content.empty())
            return false;
        ++_currentTurn;
        _gameBoard[content[0]][content[1]] = (content[2] == 1) ? _ALLY : _ENEMY;
        std::getline(std::cin, line);
    }
    ++_currentTurn;
    return lunchMinmax();
}

bool Gomoku::about([[maybe_unused]] std::string const &data)
{
    std::cout << R"(name="Gomoku", version="2.0", author="Gomoku", country="France")" << std::endl;
    return true;
}

bool Gomoku::info([[maybe_unused]] std::string const &data)
{
    return true;
}
