/*
** EPITECH PROJECT, 2022
** B-AIA-500-PAR-5-1-gomoku-zacharie.lawson
** File description:
** Gomoku
*/

#ifndef Gomoku_HPP_
    #define Gomoku_HPP_

    #include <utility>
    #include <vector>
    #include <cstdint>
    #include <map>
    #include <string>

class Gomoku;

typedef bool (Gomoku::*fun)(std::vector<int>);

class Gomoku {

    public:
        Gomoku();
        ~Gomoku() = default;

        // START
        bool start(std::vector<int>);
        bool rectStart(std::vector<int> command);
        bool restart(std::vector<int> command);

        // MOVE
        bool begin(std::vector<int> command);
        bool turn(std::vector<int> command);
        bool play(std::vector<int> command);
        bool takeBack(std::vector<int> command);

        // EXTRA
        bool board(std::vector<int> command);
        bool info(std::vector<int> command);
        bool about(std::vector<int> command);

    private:
        std::vector<std::vector<int_fast8_t>> _gameBoard;

        std::map<std::string, fun> commandList;

        void fillCommandList();

        int _currentTurn;
        int _color;
        int _time;

        std::pair <int, int> _positions;
        std::pair <int, int> _boardSize;

        int_fast8_t _EMPTY;
        int_fast8_t _ENEMY;
        int_fast8_t _ALLY;
};

#endif /* !Gomoku_HPP_ */
