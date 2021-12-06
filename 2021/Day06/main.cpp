#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "tools.h"
#include "lanternfish.h"

using namespace std;

unsigned part1(vector<int> initial_timers, int days)
{
    vector<Lanternfish> lanternfishes;

    for (auto initial_timer : initial_timers)
    {
        lanternfishes.push_back(Lanternfish(initial_timer));
    }

    for (int i = 1; i <= days; i++)
    {
        vector<Lanternfish> new_lanternfishes;
        int new_fish_count = 0;
        for (auto &lanternfish : lanternfishes)
        {
            bool new_fish = lanternfish.tick();
            new_lanternfishes.push_back(lanternfish);
            if (new_fish)
            {
                new_fish_count += 1;
            }
        }

        for (size_t i = 0; i < new_fish_count; i++)
        {
            new_lanternfishes.push_back(Lanternfish(8));
        }

        lanternfishes = new_lanternfishes;
    }

    return lanternfishes.size();
};

long int part2(vector<int> initial_timers, int days)
{
    long int lanternfishes[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (auto initial_timer : initial_timers)
    {
        lanternfishes[initial_timer] += 1;
    }

    for (int i = 1; i <= days; i++)
    {
        long int new_lanternfishes[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        for (int j = 1; j < 9; j++)
        {
            new_lanternfishes[j - 1] = lanternfishes[j];
        }
        new_lanternfishes[6] += lanternfishes[0];
        new_lanternfishes[8] = lanternfishes[0];

        for (int j = 0; j < 9; j++)
        {
            lanternfishes[j] = new_lanternfishes[j];
        }
    }

    long int total = 0;
    for (int i = 0; i < 9; i++)
    {
        total += lanternfishes[i];
    }
    return total;
};

int main(int argc, char *argv[])
{
    ifstream inputFile(argv[1]);

    if (inputFile)
    {

        string line;
        getline(inputFile, line);

        inputFile.close();

        auto initial_timers = get_initial_timers(line);

        long int part1Answer = part1(initial_timers, 80);
        cout << "Part 1 answer: " << part1Answer << endl;

        long int part2Answer = part2(initial_timers, 256);
        cout << "Part 2 answer: " << part2Answer << endl;
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        return 1;
    }
}