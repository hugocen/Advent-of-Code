#include <vector>
#include <stdlib.h>
#include <map>
#include "../tools/tools.h"
#include "crab_ submarine.h"

using namespace std;

int part1(vector<int> positions)
{
    sort(positions.begin(), positions.end());

    int idx = positions.size() / 2;

    int fuel = 0;

    for (auto pos : positions)
    {
        fuel += labs(pos - positions[idx]);
    }

    return fuel;
}

int part2(vector<int> positions)
{
    CrabSubmarine csub;

    sort(positions.begin(), positions.end());

    int farthest = max_value(positions);

    long long int min_fuel = 0;

    for (auto pos : positions)
    {
        min_fuel += csub.calculate_fuel(pos);
    }

    for (int i = 1; i <= farthest; i++)
    {
        int fuel = 0;
        for (auto pos : positions)
        {
            fuel += csub.calculate_fuel(labs(pos - i));
        }
        if (fuel < min_fuel)
        {
            min_fuel = fuel;
        }
    }
    return min_fuel;
}

int main(int argc, char *argv[])
{
    auto lines = readfile(argv[1]);

    vector<string> stringPositions = spilt_string_by_delim(lines[0], ',');

    vector<int> positions;

    for (auto string_pos : stringPositions)
    {
        positions.push_back(stoi(string_pos));
    }

    int part1Answer = part1(positions);
    cout << "Part 1 answer: " << part1Answer << endl;

    int part2Answer = part2(positions);
    cout << "Part 2 answer: " << part2Answer << endl;
}