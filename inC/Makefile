##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## Makefile
##

CXX			=	g++

NAME		= 	pbrain-gomoku-ai

SRC			=	src/gomoku.cpp			\
                src/main.cpp			\
                src/minmax.cpp			\
                src/start.cpp			\
                src/boardAnalyze.cpp	\
                src/commands/extra.cpp	\
                src/commands/move.cpp	\
                src/commands/restart.cpp

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

re: fclean all

.PHONY: all debug clean fclean