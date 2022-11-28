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
    #include <functional>

std::pair<std::size_t, std::size_t> starting(std::string const &arg);
std::pair<std::size_t, std::size_t> recStarting(std::string const &arg);

class Gomoku;


typedef bool (Gomoku::*fun)(std::string const &);

class Gomoku {

    public:
        Gomoku(std::size_t x = 20, std::size_t y = 20);
        ~Gomoku() = default;

        // START
        bool restart(std::string const &data);

        // MOVE
        bool begin(std::string const &data);
        bool turn(std::string const &data);
        bool play(std::string const &data);
        bool takeBack(std::string const &data);

        // EXTRA
        bool board(std::string const &data);
        bool info(std::string const &data);
        bool about(std::string const &data);


        bool checkCommand(std::string const &name, std::string const &data);

        int analyseBoardValue(uint_fast8_t sign, uint_fast8_t counterSign);

        bool checkNeighboursOneNotEmpty(int x, int y);

        bool lunchMinmax();

        int distanceFromMiddle(int x, int y) const;

        bool minmax(int depth, bool myTurn);
        int calculateBoardValue();

        bool alphaBetaPruning(int depth, bool myTurn, int alpha, int beta);
    private:

        uint_fast8_t _EMPTY;
        uint_fast8_t _ENEMY;
        uint_fast8_t _ALLY;

        std::pair<int, int> _boardSize;
        std::vector<std::vector<uint_fast8_t>> _gameBoard;
        std::pair<int, int> _positions;

        std::unordered_map<std::string, fun> commandList;
        void fillCommandList();

        int _currentTurn;
        int _color;
        int _time;
};

#endif /* !Gomoku_HPP_ */
