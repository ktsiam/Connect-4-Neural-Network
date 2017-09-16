#include <cstdint>
#define small int8_t

const small ROW_NB = 6;
const small COL_NB = 7;
const small SQ_NB  = 42;
enum Color : small{
        EMPTY, RED, BLACK
};

enum Turn : int{
        B_TURN, R_TURN
};

class Score4{
        
public:

        Score4();
        void play(small move);
        
        
public:
        small board[ROW_NB+1][COL_NB];
        small moveCount;
        Turn  turn;
        
        void game_over();
        void print();
        bool wins();
};

