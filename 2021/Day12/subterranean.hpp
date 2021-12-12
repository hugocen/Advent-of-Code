#include <vector>
#include <string>
#include <map>
#include "../tools/tools.h"

using namespace std;

class SubterraneanSystem
{
private:
    map<string, vector<string>> twoWayNap;
    bool isBigCave(string cave);
    int walk(string cave, map<string, int> visited, int visitLimit);

public:
    SubterraneanSystem(vector<string> input);
    void printMap();
    int getNumberOfPaths(int visitLimit);
};

SubterraneanSystem::SubterraneanSystem(vector<string> input)
{
    for (auto &line : input)
    {
        vector<string> split = split_string_two_part(line, '-');
        this->twoWayNap[split[0]].push_back(split[1]);
        this->twoWayNap[split[1]].push_back(split[0]);
    }
};

void SubterraneanSystem::printMap()
{
    for (auto &key : this->twoWayNap)
    {
        cout << key.first << ": ";
        for (auto &value : key.second)
        {
            cout << value << " ";
        }
        cout << endl;
    }
};

bool SubterraneanSystem::isBigCave(string cave)
{
    return isupper(cave[0]);
};

int SubterraneanSystem::getNumberOfPaths(int visitLimit)
{
    int numberOfPaths = 0;
    for (auto cave : this->twoWayNap["start"])
    {
        numberOfPaths += walk(cave, map<string, int>{{"start", 1}}, visitLimit);
    }
    return numberOfPaths;
};

int SubterraneanSystem::walk(string cave, map<string, int> visited, int visitLimit)
{
    if (cave == "end")
    {
        // for (auto &key : visited)
        // {
        //     cout << key.first << ": " << key.second << " ";
        // }
        // cout << endl;
        return 1;
    }
    if (!this->isBigCave(cave) && visited.find(cave) != visited.end())
    {
        if (cave == "start")
        {
            return 0;
        }
        for (auto &key : visited)
        {
            if (key.second >= visitLimit)
            {
                return 0;
            }
        }
        visited[cave]++;
    }
    else
    {
        visited[cave] = 1;
    }

    int numberOfPaths = 0;

    for (auto nextCave : this->twoWayNap[cave])
    {
        numberOfPaths += this->walk(nextCave, visited, visitLimit);
    }
    return numberOfPaths;
};
