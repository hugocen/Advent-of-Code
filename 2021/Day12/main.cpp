#include "../tools/tools.h"
#include "subterranean.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    auto lines = readfile(argv[1]);

    auto system = SubterraneanSystem(lines);

    cout << "Part 1 answer: " << system.getNumberOfPaths(1) << endl;

    cout << "Part 2 answer: " << system.getNumberOfPaths(2) << endl;

    return 0;
};