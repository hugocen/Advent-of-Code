#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

#include <iostream>

using namespace std;

const string point_delim = " -> ";
const char coordinate_delim = ',';

vector<int> string_to_coordinates(string point_string)
{
    auto found = point_string.find(coordinate_delim);
    string x = point_string.substr(0, found);
    string y = point_string.substr(found + 1);

    return {stoi(x), stoi(y)};
}

vector<vector<int>> string_to_points(string line)
{
    auto found = line.find(point_delim);
    string point1 = line.substr(0, found);
    string point2 = line.substr(found + point_delim.length());

    return {string_to_coordinates(point1), string_to_coordinates(point2)};
};

int get_max_value(vector<vector<vector<int>>> lines)
{
    int max = 0;
    for (auto line : lines)
    {
        for (auto point : line)
        {
            max = max > point[0] ? max : point[0];
            max = max > point[1] ? max : point[1];
        }
    }
    return max;
}
