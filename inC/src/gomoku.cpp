/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** gomoku
*/

#include <iostream>
#include "gomoku.hpp"

void Gomoku::fillCommandList()
{
    commandList["RESTART"] = &Gomoku::restart;
    commandList["BEGIN"] = &Gomoku::begin;
    commandList["TURN"] = &Gomoku::turn;
    commandList["PLAY"] = &Gomoku::play;
    commandList["TAKEBACK"] = &Gomoku::takeBack;
    commandList["BOARD"] = &Gomoku::board;
    commandList["INFO"] = &Gomoku::info;
    commandList["ABOUT"] = &Gomoku::about;
}

Gomoku::Gomoku(std::size_t x, std::size_t y)
    : _EMPTY(0), _ENEMY(1), _ALLY(2), _boardSize(x, y),
    _gameBoard(x, std::vector<uint_fast8_t>(y, _EMPTY))
{
    _currentTurn = 0;
    fillCommandList();
}

bool Gomoku::checkCommand(std::string const &name, std::string const &data)
{
    for (auto &it : commandList) {
        if (it.first == name)
            return (this->*it.second)(data);
    }
    std::cout << "UNKNOWN command" << std::endl;
    return true;
}

int Gomoku::distanceFromMiddle(int x, int y) const
{
    int middleX = _boardSize.first / 2;
    int middleY = _boardSize.second / 2;

    return abs(x - middleX) + abs(y - middleY);
}

