/*
** EPITECH PROJECT, 2022
** start.cpp
** File description:
** start
*/

#include <string>
#include <utility>
#include <stdexcept>
#include <iostream>
#include <cstring>
#include "gomoku.hpp"

std::pair<std::size_t, std::size_t> recStarting(std::string const &arg)
{
    std::size_t sizeX;
    std::size_t sizeY;
    char *token = std::strtok((char *)arg.c_str(), ",");
    std::string strSizeX((token == nullptr) ? "" : token);
    if (strSizeX.empty() || strSizeX == arg)
        return std::make_pair(0, 0);
    std::string strSizeY(arg.c_str() + (strSizeX.size() + 1));

    try {
        sizeX = std::stoul(strSizeX);
        sizeY = std::stoul(strSizeY);
    } catch (std::invalid_argument& e) {
        std::cerr << "ERROR: START Invalid size (not a number)" << std::endl;
        return std::make_pair(0, 0);
    }
    return std::make_pair(sizeX, sizeY);
}

std::pair<std::size_t, std::size_t> starting(std::string const &arg)
{
    std::size_t size = 0;

    try {
        size = std::stoul(arg);
    } catch (std::invalid_argument& e) {
        std::cerr << "ERROR: START Invalid size (not a number)" << std::endl;
        return std::make_pair(0, 0);
    }
    return std::make_pair(size, size);
}
