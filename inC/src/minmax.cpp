/*
** EPITECH PROJECT, 2022
** minmax.cpp
** File description:
** minmax
*/

#include <iostream>
#include "gomoku.hpp"

bool Gomoku::lunchMinmax()
{
    int bestValue = -INF;
    int moveValue = 0;
    std::pair<int, int> bestMove = std::make_pair(0, 0);

    for (int x = 0; x < _boardSize.first; x++) {
        for (int y = 0; y < _boardSize.second; y++) {
            if (_gameBoard[x][y] == _EMPTY) {
                _gameBoard[x][y] = _ALLY;
                moveValue = alphaBetaPruning(1, false, -INF, INF);//minmax(1, false);
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
    return true;
}

bool Gomoku::checkNeighboursOneNotEmpty(int x, int y)
{
    if (y > 0 && _gameBoard[x][y - 1])
        return true;
    if (x > 0 && _gameBoard[x - 1][y])
        return true;
    if (_boardSize.second - 1 != y && _gameBoard[x][y + 1])
        return true;
    if (_boardSize.first - 1 != x && _gameBoard[x + 1][y])
        return true;
    if (y > 0 && x > 0 && _gameBoard[x - 1][y - 1])
        return true;
    if (y > 0 && _boardSize.first - 1 != x && _gameBoard[x + 1][y - 1])
        return true;
    if (_boardSize.second - 1 != y && _boardSize.first - 1 != x && _gameBoard[x + 1][y + 1])
        return true;
    if (_boardSize.second - 1 != y && x > 0 && _gameBoard[x - 1][y + 1])
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

int Gomoku::alphaBetaPruning(int depth, bool myTurn, int alpha, int beta)
{
    if (depth == 0)
        return calculateBoardValue();
    for (int x = 0; x < _boardSize.first; x++) {
        for (int y = 0; y < _boardSize.second; y++) {
            if (_gameBoard[x][y] == _EMPTY && checkNeighboursOneNotEmpty(x, y)) {
                _gameBoard[x][y] = (myTurn) ? (_ALLY) : (_ENEMY);
                if (myTurn)
                    alpha = std::max(alpha, alphaBetaPruning(depth - 1, false, alpha, beta));
                else
                    beta = std::min(beta, alphaBetaPruning(depth - 1, true, alpha, beta));
                _gameBoard[x][y] = _EMPTY;
                if (alpha >= beta)
                    break;
            }
        }
    }
    return (myTurn) ? (alpha) : (beta);
}
