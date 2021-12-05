#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "map.h"
#include "tools.h"

using namespace std;

int part1(vector<string> linesString)
{
    vector<vector<vector<int>>> lines;

    for (int i = 0; i < linesString.size(); i++)
    {
        auto points = string_to_points(linesString[i]);
        lines.push_back(points);
    }

    int max_value = get_max_value(lines);

    Map map(max_value);

    map.add_lines(lines);

    return map.sum_overlap();
}

int part2(vector<string> linesString)
{
    vector<vector<vector<int>>> lines;

    for (int i = 0; i < linesString.size(); i++)
    {
        auto points = string_to_points(linesString[i]);
        lines.push_back(points);
    }

    int max_value = get_max_value(lines);

    Map map(max_value);

    map.add_lines(lines);
    map.add_diagonal_lines(lines);

    return map.sum_overlap();
}

int main(int argc, char *argv[])
{
    ifstream inputFile(argv[1]);

    if (inputFile)
    {
        vector<string> lines;

        string line;
        while (getline(inputFile, line))
        {
            lines.push_back(line);
        }
        inputFile.close();

        int part1Answer = part1(lines);
        cout << "Part 1 answer: " << part1Answer << endl;

        int part2Answer = part2(lines);
        cout << "Part 2 answer: " << part2Answer << endl;
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        return 1;
    }
}
