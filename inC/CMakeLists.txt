cmake_minimum_required(VERSION 3.17)
project(pbrain-gomoku-ai)

set(CMAKE_BUILD_TYPE Release)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED 11)

if(CMAKE_COMPILER_IS_GNUCXX)
    add_compile_options(-Wall -Wextra -O3 -g3)
endif(CMAKE_COMPILER_IS_GNUCXX)

if (WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /O2")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG "./")
endif(WIN32)

include_directories(include/)

set(COMMAND_SRC
        src/commands/start.cpp
        src/commands/move.cpp
        src/commands/extra.cpp)

add_executable(${PROJECT_NAME}
        src/main.cpp
        src/gomoku.cpp
        src/start.cpp
        src/minmax.cpp
        src/boardAnalyze.cpp
        ${COMMAND_SRC}
)