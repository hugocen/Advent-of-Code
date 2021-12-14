#include "polymerization.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    auto equipment = Polymerization(argv[1]);

    cout << "Part 1 answer: " << equipment.steps(10) << endl;

    equipment = Polymerization(argv[1]);

    cout << "Part 2 answer: " << equipment.steps(40) << endl;

    return 0;
};