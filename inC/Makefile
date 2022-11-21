##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## Makefile
##

CXX			=	g++

NAME		= 	pbrain-gomoku-ai

MAIN		=	src/main.cpp

SRC			=	src/gomoku.cpp		\
				src/start.cpp		\
				src/move.cpp		\
				src/main.cpp

OBJ			=	$(SRC:.cpp=.o)

CPPFLAGS	=	-I include/

CXXFLAGS	=	-Wall -Wextra -O3


all: $(NAME)

$(NAME): $(OBJ)
	$(CXX) -o $(NAME) $(OBJ)

debug:CXXFLAGS+=-g3
debug: re

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

.PHONY: all debug clean fclean