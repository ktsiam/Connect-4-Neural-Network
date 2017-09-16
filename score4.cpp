#include "score4.h"
#include <iostream>
#include <cassert>
Score4::Score4()
{
        for ( int r = 0; r < ROW_NB; ++r )
                for ( int c = 0; c < COL_NB; ++c )
                        board[r][c] = EMPTY;
        for ( int c = 0; c < COL_NB; ++c)
                board[ROW_NB][c] = 3;

        moveCount = 0;
        turn = R_TURN;
        print();
}

void Score4::print()
{
        for ( int r = 0; r < ROW_NB; ++r )
                for ( int c = 0; c < COL_NB; ++c )
                        std::cout << (int)board[r][c] 
                                  << " \n"[!(c+1-COL_NB)];
}

void Score4::play( small move )
{
        assert( move < COL_NB && move >= 0 && !board[0][move] );

        small *piece = &board[0][move];
        while( !*(piece+COL_NB) )
                piece += COL_NB;
        
        *piece = turn ? RED : BLACK;
        print();
        game_over();
        turn = turn ? B_TURN : R_TURN;

        moveCount ++ ;

}

void Score4::game_over()
{
        if ( moveCount == SQ_NB ) 
                std::cout << "DRAW" << std::endl;
        else if ( wins() ){
                std::cout << (turn == R_TURN ?"RED WINS\n":"BLACK WINS\n"); 
                exit(0);
        }
}

bool Score4::wins(){
        for ( int r = 0; r < ROW_NB; ++r) {
                for ( int c = 0; c < 5; ++c) {
                        if ( board[r][c] && board[r][c] == board[r][c+1]
                                 && board[r][c] == board[r][c+2] 
                             && board[r][c] == board[r][c+3])
                                return 1;
                }
        }

        for ( int c = 0; c < COL_NB; ++c) {
                for ( int r = 0; r < 5; ++c) {
                        if ( board[r][c] && board[r][c] == board[r][c+1]
                                 && board[r][c] == board[r][c+2] 
                             && board[r][c] == board[r][c+3])
                                return 1;
                }
        }


        for ( int r = 0; r < ROW_NB; ++r) {
                for ( int c = 0; c < 5; ++c) {
                        if ( board[r][c] && board[r][c] == board[r][c+1]
                                 && board[r][c] == board[r][c+2] 
                             && board[r][c] == board[r][c+3])
                                return 1;
                }
        }
        
}
