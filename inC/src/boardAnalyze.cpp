/*
** EPITECH PROJECT, 2022
** boardAnalyze.cpp
** File description:
** boardAnalyze
*/

#include "gomoku.hpp"

int Gomoku::checkDiagonalUp(int x, int y, uint_fast8_t sign, uint_fast8_t counterSign)
{
    int equivalent[6] = {0, 1, 2, 4, 8, INF};
    int multiplier = 0;
    int sizeDu = 1;

    if (x != _boardSize.first - 1 && y > 0 && _gameBoard[x + 1][y - 1] == _EMPTY)
        multiplier += 1;
    for (int i = 1; i < 6; ++i) {
        sizeDu = i;
        if (x - i < 0 || y + i >= _boardSize.second || _gameBoard[x - i][y + i] != sign)
            break;
    }
    if (x - sizeDu >= 0 && y + sizeDu < _boardSize.second && _gameBoard[x - sizeDu][y + sizeDu] != counterSign)
        multiplier += 1;
    if (x + 1 < _boardSize.first && y > 0 && _gameBoard[x + 1][y - 1] == sign)
        multiplier = 0;
    if (equivalent[sizeDu] == INF)
        return INF;
    return equivalent[sizeDu] * multiplier;

}

int Gomoku::checkDiagonalDown(int x, int y, uint_fast8_t sign, uint_fast8_t counterSign)
{
    int equivalent[6] = {0, 1, 2, 4, 8, INF};
    int multiplier = 0;
    int sizeDd = 1;

    if (x > 0 && y > 0 && _gameBoard[x - 1][y - 1] == _EMPTY)
        multiplier += 1;
    for (int i = 1; i < 6; ++i) {
        sizeDd = i;
        if (x + i >= _boardSize.first || y + i >= _boardSize.second || _gameBoard[x + i][y + i] != sign)
            break;
    }
    if (x + sizeDd < _boardSize.first && y + sizeDd < _boardSize.second && _gameBoard[x + sizeDd][y + sizeDd] != counterSign)
        multiplier += 1;
    if (x > 0 && y > 0 && _gameBoard[x - 1][y - 1] == sign)
        multiplier = 0;
    if (equivalent[sizeDd] == INF)
        return INF;
    return equivalent[sizeDd] * multiplier;
}

int Gomoku::checkVertical(int x, int y, uint_fast8_t sign, uint_fast8_t counterSign)
{
    int equivalent[6] = {0, 1, 2, 4, 8, INF};
    int multiplier = 0;
    int sizeV = 1;

    if (x > 0 && _gameBoard[x - 1][y] == _EMPTY)
        multiplier += 1;
    for (int i = 1; i < 6; ++i) {
        sizeV = i;
        if (x + i >= _boardSize.first || _gameBoard[x + i][y] != sign)
            break;
    }
    if (x + sizeV < _boardSize.first && _gameBoard[x + sizeV][y] != counterSign)
        multiplier += 1;
    if (x > 0 && _gameBoard[x - 1][y] == sign)
        multiplier = 0;
    if (equivalent[sizeV] == INF)
        return INF;
    return equivalent[sizeV] * multiplier;
}

int Gomoku::checkHorizontal(int x, int y, uint_fast8_t sign, uint_fast8_t counterSign)
{
    int equivalent[6] = {0, 1, 2, 4, 8, INF};
    int multiplier = 0;
    int sizeH = 1;

    if (y > 0 && _gameBoard[x][y - 1] == _EMPTY)
        multiplier += 1;
    for (int i = 1; i < 6; ++i) {
        sizeH = i;
        if (y + i >= _boardSize.second || _gameBoard[x][y + i] != sign)
            break;
    }
    if (y + sizeH < _boardSize.second && _gameBoard[x][y + sizeH] != counterSign)
        multiplier += 1;
    if (y > 0 && _gameBoard[x][y - 1] == sign)
        multiplier = 0;
    if (equivalent[sizeH] == INF)
        return INF;
    return equivalent[sizeH] * multiplier;
}

int Gomoku::analyseBoardValue(uint_fast8_t sign, uint_fast8_t counterSign)
{
    int score = 0;

    for (int x = 0; x < _boardSize.first; ++x) {
        for (int y = 0; y < _boardSize.second; ++y) {
            if (_gameBoard[x][y] == sign) {
                score += checkHorizontal(x, y, sign, counterSign);
                score += checkVertical(x, y, sign, counterSign);
                score += checkDiagonalUp(x, y, sign, counterSign);
                score += checkDiagonalDown(x, y, sign, counterSign);
            }
        }
    }
    return score;
}

int Gomoku::calculateBoardValue()
{
    int allyScore = analyseBoardValue(_ALLY, _ENEMY);
    int enemyScore = analyseBoardValue(_ENEMY, _ALLY);
    return allyScore - enemyScore;
}
