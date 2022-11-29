/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** start
*/

#include "gomoku.hpp"

bool Gomoku::restart(std::string const &data)
{
    _currentTurn = 0;
    _color = 0;
    _time = 0;
    _positions = std::make_pair(0, 0);
    _gameBoard = std::vector<std::vector<uint_fast8_t>>(_boardSize.first, std::vector<uint_fast8_t>(_boardSize.second, _EMPTY));
    _EMPTY = 0;
    _ENEMY = 1;
    _ALLY = 2;
    return true;
}