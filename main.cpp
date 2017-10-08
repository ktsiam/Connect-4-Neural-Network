#include "score4.h"
#include <iostream>

int main()
{
        BitScoreFour a;
        a.print();
        char c;
        while( std::cin >> c )
                if ( c >= 'a' && c <= 'h' )
                        a.play((File)(c - 'a'));
}
