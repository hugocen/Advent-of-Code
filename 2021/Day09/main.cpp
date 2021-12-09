#include <stdlib.h>
#include <vector>
#include <string>
#include <iostream>
#include "../tools/tools.h"
#include "heightmap.h"

using namespace std;

int part1(vector<string> input)
{
    Heightmap hm(input);
    return hm.get_risk_level();
}

int part2(vector<string> input)
{
    Heightmap hm(input);
    auto basins = hm.find_basins();
    return basins[0] * basins[1] * basins[2];
}

int main(int argc, char *argv[])
{
    auto lines = readfile(argv[1]);

    int part1Answer = part1(lines);
    cout << "Part 1 answer: " << part1Answer << endl;

    int part2Answer = part2(lines);
    cout << "Part 2 answer: " << part2Answer << endl;

    return 0;
}