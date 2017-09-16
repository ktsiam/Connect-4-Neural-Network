CXX      = clang++
LDFLAGS  = -Wall -Wextra -std=c++11 -Werror

play:	score4.cpp main.cpp
	${CXX} ${LDFLAGS} -o	play	score4.cpp main.cpp

clean:
	rm -f play
