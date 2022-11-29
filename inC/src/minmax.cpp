/*
** EPITECH PROJECT, 2022
** minmax.cpp
** File description:
** minmax
*/

#include <limits>
#include <iostream>
#include "gomoku.hpp"

bool Gomoku::lunchMinmax()
{
    int moveValue = 0;
    int bestValue = -INF;
    std::pair<int, int> bestMove = std::make_pair(0, 0);

    for (int x = 0; x < _boardSize.first; x++) {
        for (int y = 0; y < _boardSize.second; y++) {
            if (_gameBoard[x][y] == _EMPTY) {
                _gameBoard[x][y] = _ALLY;
                moveValue = minmax(0, false);
                _gameBoard[x][y] = _EMPTY;
                if (moveValue > bestValue || (moveValue == bestValue && distanceFromMiddle(x, y) < distanceFromMiddle(bestMove.first, bestMove.second))) {
                    bestMove.first = x;
                    bestMove.second = y;
                    bestValue = moveValue;
                }
            }
        }
    }
    _gameBoard[bestMove.first][bestMove.second] = _ALLY;
    std::cout << bestMove.first << "," << bestMove.second << std::endl;
    //std::cout << "MESSAGE: " << bestMove.first << " " << bestMove.second << std::endl;
    return true;
}

bool Gomoku::checkNeighboursOneNotEmpty(int x, int y)
{
    if ((x && _gameBoard[x - 1][y]) || (y && _gameBoard[x][y - 1]))
        return true;
    if (x + 1 <= _boardSize.first && _gameBoard[x + 1][y])
        return true;
    if (y + 1 <= _boardSize.second && _gameBoard[x][y + 1])
        return true;
    if (x && y && _gameBoard[x - 1][y - 1])
        return true;
    if (y && x + 1 <= _boardSize.first && _gameBoard[x + 1][y - 1])
        return true;
    if (x + 1 > _boardSize.first && y + 1 > _boardSize.second && _gameBoard[x + 1][y + 1])
        return true;
    if (x && y + 1 > _boardSize.second && _gameBoard[x - 1][y + 1])
        return true;
    return false;
}

bool Gomoku::minmax(int depth, bool myTurn)
{
    int bestScore = (myTurn) ? (-INF) : (INF);
    int score = 0;

    if (depth == 0)
        return calculateBoardValue();
    for (int x = 0; x < _boardSize.first; x++) {
        for (int y = 0; y < _boardSize.second; y++) {
            if (_gameBoard[x][y] == _EMPTY && checkNeighboursOneNotEmpty(x, y)) {
                _gameBoard[x][y] = (myTurn) ? (_ALLY) : (_ENEMY);
                score = minmax(depth - 1, false);
                _gameBoard[x][y] = _EMPTY;
                bestScore = (myTurn) ? (std::max(score, bestScore))
                                      : (std::min(score, bestScore));
            }
        }
    }
    return bestScore;
}

bool Gomoku::alphaBetaPruning(int depth, bool myTurn, int alpha, int beta)
{
    int bestScore = (myTurn) ? (-INF) : (INF);

    if (depth == 0)
        return calculateBoardValue();
    for (int x = 0; x < _boardSize.first; x++) {
        for (int y = 0; y < _boardSize.second; y++) {
            if (_gameBoard[x][y] == _EMPTY && checkNeighboursOneNotEmpty(x, y)) {
                _gameBoard[x][y] = (myTurn) ? (_ALLY) : (_ENEMY);
                alpha = alphaBetaPruning(depth - 1, !myTurn, alpha, beta);
                _gameBoard[x][y] = _EMPTY;
                if (myTurn)
                    alpha = std::max(alpha, bestScore);
                else
                    beta = std::min(beta, bestScore);
                if (alpha >= beta)
                    break;
            }
        }
    }
    return (myTurn) ? (alpha) : (beta);
}
