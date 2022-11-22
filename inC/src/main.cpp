/*
** EPITECH PROJECT, 2022
** main.cpp
** File description:
** main
*/

#include <string>
#include <iostream>
#include <ranges>
#include "gomoku.hpp"

bool parserCommand(std::string const &command)
{
    Gomoku gomoku;

    auto split = command | std::ranges::views::split(' ');
    // parse command and call the right function
    //std::vector<std::string> commandList = std::views::split(command, ' ');
}

int main()
{
    std::string command;

    std::cin >> command;
    while (command != "END") {
        std::cin >> command;
    }
    return 0;
}