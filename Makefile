CXX      = clang++
CXXFLAGS = -std=c++11 -Wall -Wextra -pedantic #-Weverything #-O3
LDFLAGS  = 


play: score4.o main.o 
	${CXX} ${CXXFLAGS} ${LDFLAGS} -o	play	./src/objects/score4.o ./src/objects/main.o


score4.o: ./src/score4/score4.cpp
	${CXX} ${CXXFLAGS} -c -o ./src/objects/score4.o ./src/score4/score4.cpp

main.o: ./src/main.cpp
	${CXX} ${CXXFLAGS} -c -o ./src/objects/main.o ./src/main.cpp
clean:
	rm -f play
	rm -f ./src/objects/*
	rm -rf *.dSYM
