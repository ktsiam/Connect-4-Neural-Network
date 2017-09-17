#include "bitscore4.h"
#include <iostream>

int main()
{
        BitScoreFour a;
        a.print();
        char c;
        while(std::cin >> c)                
                a.play((File)(c - 'a'));
}
