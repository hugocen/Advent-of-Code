#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
using namespace std;

int part1(vector<tuple<string, int>> instructions)
{
    int depths = 0;
    int distance = 0;
    for (int i = 0; i < instructions.size(); i++)
    {
        string direction = get<0>(instructions[i]);
        int number = get<1>(instructions[i]);

        if (direction == "forward")
        {
            distance += number;
        }
        else if (direction == "down")
        {
            depths += number;
        }
        else if (direction == "up")
        {
            depths -= number;
        }
    }
    return depths * distance;
}

int part2(vector<tuple<string, int>> instructions)
{
    int aim = 0;
    int depths = 0;
    int distance = 0;

    for (int i = 0; i < instructions.size(); i++)
    {
        string direction = get<0>(instructions[i]);
        int number = get<1>(instructions[i]);

        if (direction == "forward")
        {
            distance += number;
            depths += number * aim;
        }
        else if (direction == "down")
        {
            aim += number;
        }
        else if (direction == "up")
        {
            aim -= number;
        }
    }
    return depths * distance;
}

int main(int argc, char *argv[])
{
    const char delim = ' ';

    ifstream inputFile(argv[1]);

    vector<tuple<string, int>> instructions;

    if (inputFile)
    {
        string line;
        while (getline(inputFile, line))
        {
            auto found = line.find(delim);
            string direction = line.substr(0, found);
            string numberString = line.substr(found + 1);

            auto instruction = make_tuple(direction, stoi(numberString));
            instructions.push_back(instruction);
        }
        inputFile.close();
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        return 1;
    }

    int part1Answer = part1(instructions);
    cout << "Part 1 answer: " << part1Answer << endl;

    int part2Answer = part2(instructions);
    cout << "Part 2 answer: " << part2Answer << endl;

    return 0;
}