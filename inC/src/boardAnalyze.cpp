/*
** EPITECH PROJECT, 2022
** boardAnalyze.cpp
** File description:
** boardAnalyze
*/

#include "gomoku.hpp"
#include <limits>

int Gomoku::analyseBoardValue(uint_fast8_t sign, uint_fast8_t counterSign)
{
    int score = 0;
    int inf = std::numeric_limits<int>::infinity();
    int equivalent[6] = {0, 1, 2, 4, 8, inf};
    int multiplier = 0;
    int sizeH = 0;
    int sizeV = 0;
    int sizeDu = 0;
    int sizeDd = 0;

    for (int x = 0; x < _boardSize.first; ++x) {
        for (int y = 0; y < _boardSize.second; ++y) {
            if (_gameBoard[x][y] == sign) {
                /// Check horizontal
                multiplier = 0;
                sizeH = 1;
                if (y > 0 && _gameBoard[x][y - 1] == _EMPTY)
                    multiplier += 1;
                for (int i = 1; i < 6; ++i) {
                    sizeH = i;
                    if (y + i >= _boardSize.second || _gameBoard[x][y] != sign)
                        break;
                }
                if (y + sizeH < _boardSize.second || _gameBoard[x][y + sizeH] != counterSign)
                    multiplier += 1;
                if (y > 0 && _gameBoard[x][y - 1] == sign)
                    multiplier = 0;
                if (equivalent[sizeH] == inf)
                    return inf;
                score += equivalent[sizeH] * multiplier;
                /// Check vertical
                multiplier = 0;
                sizeV = 1;
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
                if (equivalent[sizeV] == inf)
                    return inf;
                score += equivalent[sizeV] * multiplier;
                /// Check diagonal up
                multiplier = 0;
                sizeDu = 1;
                if (x + 1 > _boardSize.first && y > 0 && _gameBoard[x + 1][y - 1] == _EMPTY)
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
                if (equivalent[sizeDu] == inf)
                    return inf;
                score += equivalent[sizeDu] * multiplier;
                /// Check diagonal down
                multiplier = 0;
                sizeDd = 1;
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
                if (equivalent[sizeDd] == inf)
                    return inf;
                score += equivalent[sizeDd] * multiplier;
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