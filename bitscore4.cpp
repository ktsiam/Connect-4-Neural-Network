#include "bitscore4.h"
#include <iostream>
#include <cassert>


BitScoreFour::BitScoreFour()
{
        POS[WHITE] = 0;
        POS[BLACK] = 0;
        color      = WHITE;
}

void BitScoreFour::play(File file)
{
        Bitboard pieces = all_pieces();

        //add element
        int rank;
        for (rank = ONE; rank != RANK_NB; ++rank){
                Bitboard square = _FILE[file] & _RANK[rank];
                if ( !(pieces & square) ){
                        POS[color] |= square;
                        break;
                }
        }
        assert( rank != RANK_NB );

        //check if game_over
        game_over(file, (Rank)rank);

        //swap color
        color = color ? BLACK : WHITE;
        print();
                
}

Bitboard BitScoreFour::all_pieces()
{
        return POS[WHITE] | POS[BLACK];
}

void BitScoreFour::print()
{        
        Bitboard pieces = all_pieces();

        std::cout << ( color ? "WHITE TO MOVE\n":"BLACK TO MOVE\n");

        for (int r = 6; r >= 0; --r){
        std::cout << r+1 << " ";

                for (int f = 0; f < 8; ++f){
                        Bitboard square = _FILE[f] & _RANK[r];
                        if ( pieces & square )
                                std::cout << "xo"
                                        [(bool)(POS[WHITE] & square)]
                                          << " ";
                        else
                                std::cout << "_ ";
                }                 
                std::cout << "\n";
        }
        std::cout << "  A B C D E F G H\n\n";
}

void BitScoreFour::game_over(File file, Rank rank)
{
        if ( !~all_pieces() ){
                std::cout << "DRAW!" << std::endl;
                exit(0);
        }

        //rows
        int winCount(0);
        for (int f = file+1; f != FILE_NB; ++f)
                if ( POS[color] & _FILE[f] & _RANK[rank] )
                        winCount++;
                else
                        break;
                 
        for (int f = file-1; f >= A; --f)
                if ( POS[color] & _FILE[f] & _RANK[rank] )
                        winCount++;
                else
                        break;
       
        if ( winCount >= 3 )
                std::cout << (color?"WHITE":"BLACK") << " WON!\n";

        //columns
        winCount = 0;
        for (int r = rank+1; r != RANK_NB; ++r)
                if ( POS[color] & _FILE[file] & _RANK[r] )
                        winCount++;
                else
                        break;
        
        for (int r = rank-1; r >= ONE; --r)
                if ( POS[color] & _FILE[file] & _RANK[r] )
                        winCount++;
                else
                        break;
        
        if ( winCount >= 3 )
                std::cout << (color?"WHITE":"BLACK") << " WON!\n";
        
        // \ diagonals
        winCount = 0;

        for (int f = file+1, r = rank-1; f < FILE_NB && r >= ONE; ++f,--r)
                if ( POS[color] & _FILE[f] & _RANK[r] )
                        winCount++;
                else
                        break;        

        for (int f = file-1, r = rank+1;f >= A && r < RANK_NB ;--f,++r)
                if ( POS[color] & _FILE[f] & _RANK[r] )
                        winCount++;
                else
                        break;
        
        if ( winCount >= 3 )
                std::cout << (color?"WHITE":"BLACK") << " WON!\n";

        // / diagonals 
        winCount = 0;
        for (int f = file+1, r = rank+1; f < FILE_NB && r < RANK_NB; ++f,++r){
                if ( POS[color] & _FILE[f] & _RANK[r] )
                        winCount++;
                else
                        break;        
        
        for (int f = file-1, r = rank-1;f >= A && r >= ONE; --f,--r)
                if ( POS[color] & _FILE[f] & _RANK[r] )
                        winCount++;
                else
                        break;        
        
        if ( winCount >= 3 )
                std::cout << (color?"WHITE":"BLACK") << " WON!\n";
}
