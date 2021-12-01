#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int part1(vector<int> &depths)
{
    int depthIncreased = 0;
    for (int i = 1; i < depths.size(); i++)
    {
        if (depths[i] > depths[i - 1])
        {
            depthIncreased++;
        }
    }

    return depthIncreased;
}

int part2(vector<int> &depths)
{
    vector<int> depthsSlideWindow;
    for (int i = 0; i < depths.size(); i++)
    {
        int windowSum = 0;
        for (int j = 0; j < 3; j++)
        {
            int index = i - j;
            if (index < 0)
            {
                index = depths.size() + index;
            }
            windowSum += depths[index];
        }
        depthsSlideWindow.push_back(windowSum);
    }

    return part1(depthsSlideWindow);
}

int main(int argc, char *argv[])
{
    ifstream inputFile(argv[1]);

    vector<int> depths;

    if (inputFile)
    {
        string line;
        while (getline(inputFile, line))
        {
            depths.push_back(stoi(line));
        }
        inputFile.close();
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        return 1;
    }

    int part1Answer = part1(depths);
    cout << "Part 1 answer: " << part1Answer << endl;

    int part2Answer = part2(depths);
    cout << "Part 2 answer: " << part2Answer << endl;

    return 0;
}
