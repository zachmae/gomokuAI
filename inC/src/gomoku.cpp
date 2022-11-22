/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** gomoku
*/

#include "gomoku.hpp"

Gomoku::Gomoku()
{
    _currentTurn = 0;
    _color = 0;
    _time = 0;
    _EMPTY = 0;
    _ENEMY = 1;
    _ALLY = 2;
    fillCommandList();
}

void Gomoku::fillCommandList()
{
    commandList.insert(std::make_pair<std::string, fun>("START", &Gomoku::start));
    commandList.insert(std::make_pair<std::string, fun>("RECTSTART", &Gomoku::rectStart));
    commandList.insert(std::make_pair<std::string, fun>("RESTART", &Gomoku::restart));
    commandList.insert(std::make_pair<std::string, fun>("BEGIN", &Gomoku::begin));
    commandList.insert(std::make_pair<std::string, fun>("TURN", &Gomoku::turn));
    commandList.insert(std::make_pair<std::string, fun>("PLAY", &Gomoku::play));
    commandList.insert(std::make_pair<std::string, fun>("TAKEBACK", &Gomoku::takeBack));
    commandList.insert(std::make_pair<std::string, fun>("BOARD", &Gomoku::board));
    commandList.insert(std::make_pair<std::string, fun>("INFO", &Gomoku::info));
    commandList.insert(std::make_pair<std::string, fun>("ABOUT", &Gomoku::about));
}