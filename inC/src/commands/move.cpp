/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** start
*/

#include "gomoku.hpp"
#include <iostream>
#include <cstring>

static std::pair<int, int> getPos(std::string const &str)
{
    char *token = std::strtok((char *)str.c_str(), ",");
    std::string strX((token == nullptr || std::string(token) == str) ? "" : token);
    if (strX.empty())
        return std::make_pair(-1, -1);
    std::string strY(str.c_str() + (strX.size() + 1));

    try {
        return std::make_pair(std::stoi(strX), std::stoi(strY));
    } catch (std::invalid_argument &e) {
        return std::make_pair(-1, -1);
    }
}

bool Gomoku::begin([[maybe_unused]] std::string const &data)
{
    _ALLY = 1;
    _ENEMY = 2;
    _currentTurn += 1;
    return lunchMinmax();
}

bool Gomoku::turn(std::string const &data)
{
    std::pair<int, int> pos = getPos(data);

    if (pos.first == -1 || pos.second == -1) {
        std::cout << "ERROR: TURN position must be a number" << std::endl;
        return false;
    }
    if (pos.first >= _boardSize.first || pos.second >= _boardSize.second) {
        std::cout << "ERROR: TURN position is out of range" << std::endl;
        return false;
    }
    if (_gameBoard[pos.first][pos.second] != _EMPTY) {
        std::cout << "ERROR: TURN position is already taken" << std::endl;
        return false;
    }
    ++_currentTurn;
    _gameBoard[pos.first][pos.second] = _ENEMY;
    ++_currentTurn;
    return lunchMinmax();
}

bool Gomoku::play(std::string const &data)
{
    std::pair<int, int> pos = getPos(data);

    if (pos.first == -1 || pos.second == -1) {
        std::cout << "ERROR: PLAY position must be a number" << std::endl;
        return false;
    }
    if (pos.first >= _boardSize.first || pos.second >= _boardSize.second) {
        std::cout << "ERROR: PLAY position is out of range" << std::endl;
        return false;
    }
    if (_gameBoard[pos.first][pos.second] != _EMPTY) {
        std::cout << "ERROR: PLAY position is already taken" << std::endl;
        return false;
    }
    _gameBoard[pos.first][pos.second] = _ALLY;
    _currentTurn++;
    std::cout << pos.first << "," << pos.second << std::endl;
    return true;
}

bool Gomoku::takeBack(std::string const &data)
{
    std::pair<int, int> pos = getPos(data);

    if (pos.first == -1 || pos.second == -1) {
        std::cout << "ERROR: TAKEBACK position must be a number" << std::endl;
        return false;
    }
    if (pos.first >= _boardSize.first || pos.second >= _boardSize.second) {
        std::cout << "ERROR: TAKEBACK position is out of range" << std::endl;
        return false;
    }
    if (_gameBoard[pos.first][pos.second] == _EMPTY) {
        std::cout << "ERROR: TAKEBACK position is already empty" << std::endl;
        return false;
    }
    _gameBoard[pos.first][pos.second] = _EMPTY;
    _currentTurn--;
    std::cout << "OK" << std::endl;
    return true;
}
