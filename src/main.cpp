#include "score4/score4.h"
#include <iostream>

struct Player{
        int choose(Bitboard me, Bitboard you) { return rand()%8; }
};

int GAME_OVER = 0;

int main()
{
        srand(time(NULL));
        for (int i = 0; i < 1000; ++i){
                std::cout << "GAME STARTS\n";
                GAME_OVER = 0;
                BitScoreFour a;
                Player p1, p2;
                
                while (GAME_OVER == 0) {
                        while (!a.play((File)p1.choose(a.get_pos(WHITE), a.get_pos(BLACK))));
                        if (GAME_OVER != 0)
                                break;
                        while (!a.play((File)p2.choose(a.get_pos(BLACK), a.get_pos(WHITE))));
                }
        }

}



/*        while( std::cin >> c )
          if ( c >= 'a' && c <= 'h' )
          a.play((File)(c - 'a'));
*/
