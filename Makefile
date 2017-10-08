CXX      = clang++
CXXFLAGS = -std=c++11 #-Weverything #-O3
LDFLAGS  = -Wall -Wextra 


play: ./objects/score4.o ./objects/main.o 
	${CXX} ${CXXFLAGS} ${LDFLAGS} -o	play	./objects/score4.o ./objects/main.o


./objects/score4.o: ./score4/score4.cpp
	${CXX} ${CXXFLAGS} -c -o ./objects/score4.o ./score4/score4.cpp

./objects/main.o: main.cpp
	${CXX} ${CXXFLAGS} -c -o ./objects/main.o ./main.cpp
clean:
	rm -f play
	rm -f ./objects/*
	rm -rf *.dSYM
