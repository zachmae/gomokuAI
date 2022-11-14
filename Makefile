##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## Makefile

NAME			=	pbrain-gomoku-ai

REQUIREMENTS	=	requirements.txt

MAIN			=	src/main.py

# Useless by now
SRC				=	src/gomoku.py	\
					src/AIclass.py

all: $(NAME)

setup:
	@echo "Installing requirements..."
	@if (python3.10 -c "import PyInstaller" 2> /dev/null); then \
		echo "PyInstaller already installed"; \
	else \
		echo "Installing PyInstaller..."; \
		pip3 install PyInstaller; \
	fi

$(NAME): setup
	python3.10 -m PyInstaller --onefile $(MAIN) --distpath . -n $(NAME)



clean:
	rm -rf ./build
	$(RM) ./pbrain-gomoku-ai.spec
	$(RM) -r __pycache__

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all setup clean fclean re