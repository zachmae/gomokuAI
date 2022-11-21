/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** start
*/

#include "gomoku.hpp"
#include <iostream>

bool Gomoku::start(std::vector<int> command)
{
    int size = 0;

    if (command.size() != 2) {
        std::cout << "ERROR: START Invalid number of arguments" << std::endl;
        return false;
    }
    try {
        size = command.at(0);
        _boardSize.first = size;
        _boardSize.second = size;
        if (_boardSize.first > 0 and _boardSize.second > 0) {
            for (int i = 0; i < _gameBoard.size(); i++) {
                for (int j = 0; j < _gameBoard[i].size(); j++) {
                    _gameBoard[i][j] = _EMPTY;
                }    
            }
            std::cout << "OK" << std::endl;
            return true;
        } else {
            std::cout << "ERROR: START Invalid size (not positive number)" << std::endl;
            return false;
        }
    } catch (std::invalid_argument& e) {
        throw e.what();
        return false;
    }
}


// bool Gomoku::rectStart(std::vector<int> command)
// {
//     // command.at(1).split(',')

//     if (len(size) != 2)
//         std::cout << "ERROR: RECTSTART Invalid number of arguments" << std::endl;
//         return false;
//     try {
//         _boardSize.first = size[0];
//         _boardSize.second = size[1];
//         if (_boardSize.first > 0 and _boardSize.second > 0) {
//             for (int i = 0; i < _gameBoard.size(); i++) {
//                 for (int j = 0; j < _gameBoard[i].size(); j++) {
//                     _gameBoard[i][j] = _EMPTY;
//                 }    
//             }
//             std::cout << "OK" << std::endl;
//             return true;
//         } else {
//             std::cout << "ERROR: RECTSTART Invalid size (not positive number)" << std::endl;
//             return false
//         }
//     } catch (std::invalid_argument& e) {
//         std::cout << "ERROR: RECTSTART Invalid size (not a number)" << std::endl;
//         return false;
//     }
// }