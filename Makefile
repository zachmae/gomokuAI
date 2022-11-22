##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## Makefile

CP 			= 	-cp -r
MV 			= 	-mv
EXEC 		=	-chmod +x

NAME			=	pbrain-gomoku-ai

REQUIREMENTS	=	requirements.txt

MAIN			=	src/main.py
SRC = $(MAIN) \
	  src/AIclass.py \
	  src/board_analyze.py \
	  src/gomoku.py \
	  src/minmax.py \
	  src/commands

all: $(NAME)

$(NAME):
	$(CP) $(SRC) .
	$(MV) main.py $(NAME)
	$(EXEC) $(NAME)


clean:
	rm -rf ./build
	$(RM) ./pbrain-gomoku-ai.spec
	$(RM) -r __pycache__

fclean: clean
	$(RM) $(NAME)
	rm -rf AIclass.py board_analyze.py gomoku.py commands minmax.py main.py

re: fclean all

.PHONY: all setup clean fclean re