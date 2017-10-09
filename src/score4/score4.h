#include <cstdint>

typedef uint64_t Bitboard;

//FILE
enum File { A, B, C, D, E, F, G, H, FILE_NB = 8 };
const Bitboard _FILE[FILE_NB] = { 72340172838076673,   144680345676153346,
             289360691352306692,  578721382704613384,  1157442765409226768,
             2314885530818453536, 4629771061636907072, 9259542123273814144u};

//RANK
enum Rank { ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, RANK_NB = 7 };
const Bitboard _RANK[RANK_NB] = { 255, 65280, 16711680, 4278190080, 1095216660480,
                                  280375465082880, 71776119061217280};

//Color
enum Color { WHITE = 1, BLACK = 0, COLOR_NB = 2};

enum Direction { UP = FILE_NB, RIGHT = -1 };



class BitScoreFour{
public:
        BitScoreFour();
        bool play(File fileIdx);
        void print();
        Bitboard all_pieces();
        void game_over(File, Rank);
        Bitboard get_pos(Color col) { return POS[col]; }
        
private:
        Bitboard POS[COLOR_NB];
        Color color;
};
