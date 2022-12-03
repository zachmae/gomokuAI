/*
** EPITECH PROJECT, 2022
** main.cpp
** File description:
** main
*/

#include <string>
#include <iostream>
#include <cstring>
#include <utility>
#include "gomoku.hpp"


static std::pair<std::size_t, std::size_t> apply(const std::pair<std::string, std::string>& command)
{
    if (command.first == "START")
        return starting(command.second);
    if (command.first == "RECTSTART")
        return recStarting(command.second);
    std::cout << "DEBUG: Need to start the game first" << std::endl;
    return std::make_pair(0, 0);
}

static std::string getCommand(std::string const command)
{
    char *token = std::strtok((char *)command.c_str(), " ");
    if (token == nullptr)
        return "";
    std::string commandName(token);
    return commandName;
}

static std::string getArg(std::string const &input, std::string const &commandName)
{
    if (input == commandName)
        return "";
    std::string arg(input.c_str() + (commandName.size() + 1));
    return arg;
}

int startTheGame(std::size_t sizeX, std::size_t sizeY)
{
    Gomoku gomoku(sizeX, sizeY);
    std::string input;
    std::pair<std::string, std::string> command;

    std::cout << "OK" << std::endl;
    std::getline(std::cin, input);
    command.first = getCommand(input);
    command.second = getArg(input, command.first);
    while (command.first != "END") {
        gomoku.checkCommand(command.first, command.second);
        std::getline(std::cin, input);
        command.first = getCommand(input);
        command.second = getArg(input, command.first);
    }
    return 0;
}

int main()
{
    std::string input;
    std::pair<std::string, std::string> command;

    std::getline(std::cin, input);
    command.first = getCommand(input);
    command.second = getArg(input, command.first);
    while (command.first != "START" && command.first != "RECTSTART" && command.first != "END") {
        std::getline(std::cin, input);
        command.first = getCommand(input);
        command.second = getArg(input, command.first);
    }
    if (command.first == "END")
        return 0;
    std::pair<std::size_t, std::size_t> size = apply(command);
    if (size.first < 5 || size.second < 5)
        return 84;
    if (startTheGame(size.first, size.second) < 0)
        return 84;
    return 0;
}
