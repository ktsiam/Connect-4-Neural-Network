CXX      = clang++
LDFLAGS  = -Wall -Wextra -std=c++11 -O3

all : play bitPlay

play:    score4.o  main.cpp
	${CXX} ${LDFLAGS} -o	play	score4.o main.cpp
	
score4.o : score.cpp score.h

bitPlay: bitscore4.o bitmain.cpp 
	${CXX} ${LDFLAGS} -o	bitPlay	score4.o main.cpp

bitscore4.o : bitscore.cpp bitscore.h

clean:
	rm -f play
	rm -f bitPlay
	rm -rf *.dSYM
