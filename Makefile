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

ifeq ($(OS), Windows_NT)
$(NAME): setup
	python3.10 -m PyInstaller --onefile $(MAIN) --distpath . -n pbrain-gomoku-ai
else
$(NAME): setup
	cp $(MAIN) ./$(NAME)
endif

ifeq ($(OS), Windows_NT)
setup:
	echo "Windows"
#	@echo "Installing requirements..."
#	@if (python3.10 -c "import PyInstaller" 2> $null); then \
#		echo "PyInstaller already installed"; \
#	else \
#		echo "Installing PyInstaller..."; \
#		pip3 install PyInstaller >> $null; \
#	fi
else
setup:
	@echo "Installing requirements..."
	@if (python3.10 -c "import PyInstaller" 2> /dev/null); then \
		echo "PyInstaller already installed"; \
	else \
		echo "Installing PyInstaller..."; \
		pip3 install PyInstaller; \
	fi
endif

ifeq ($(OS), Windows_NT)
clean:
	rm .\build
	rm .\pbrain-gomoku-ai.spec

fclean: clean
	rm .\pbrain-gomoku-ai.exe
else
clean:
	$(RM) -r __pycache__

fclean: clean
	$(RM) $(NAME)
endif

re: fclean all

.PHONY: all setup clean fclean re