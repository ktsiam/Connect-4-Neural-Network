CXX      = clang++
LDFLAGS  = -Wall -Wextra -std=c++11 -O3

play: score4.cpp score4.h main.cpp 
	${CXX} ${LDFLAGS} -o	play	score4.cpp main.cpp

clean:
	rm -f play
	rm -f *o
	rm -rf *.dSYM
