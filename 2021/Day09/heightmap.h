#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

class Heightmap
{
public:
    int height;
    int width;
    vector<vector<int>> map;
    Heightmap(vector<string> input);
    void print();

    vector<int> get_low_points();
    bool is_low_point(int point, vector<int> neighbors);
    int get_risk_level();

    set<string> seen_points;
    vector<int> find_basins();
    string get_coordinate(int i, int j);
    int search_basin(int i, int j);
};

Heightmap::Heightmap(vector<string> input)
{
    this->height = input.size();
    this->width = input[0].size();

    for (int i = 0; i < height; i++)
    {
        vector<int> row;
        for (int j = 0; j < width; j++)
        {
            row.push_back(input[i][j] - '0');
        }
        this->map.push_back(row);
    }
}

void Heightmap::print()
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            cout << map[i][j] << " ";
        }
        cout << endl;
    }
}

vector<int> Heightmap::get_low_points()
{
    vector<int> low_points;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            vector<int> neighbors;
            if (i > 0)
            {
                neighbors.push_back(map[i - 1][j]);
            }
            if (j > 0)
            {
                neighbors.push_back(map[i][j - 1]);
            }
            if (i < height - 1)
            {
                neighbors.push_back(map[i + 1][j]);
            }
            if (j < width - 1)
            {
                neighbors.push_back(map[i][j + 1]);
            }
            if (this->is_low_point(map[i][j], neighbors))
            {
                low_points.push_back(map[i][j]);
            }
        }
    }
    return low_points;
}

bool Heightmap::is_low_point(int point, vector<int> neighbors)
{
    for (auto neighbor : neighbors)
    {
        if (point >= neighbor)
        {
            return false;
        }
    }
    return true;
}

int Heightmap::get_risk_level()
{
    int risk_level = 0;
    auto low_points = this->get_low_points();
    for (auto low_point : low_points)
    {
        risk_level += low_point + 1;
    }
    return risk_level;
}

vector<int> Heightmap::find_basins()
{
    vector<int> basins;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int basin = this->search_basin(i, j);
            if (basin > 0)
            {
                basins.push_back(basin);
            }
        }
    }
    sort(basins.begin(), basins.end(), greater<>());
    return basins;
}

string Heightmap::get_coordinate(int i, int j)
{
    return to_string(i) + "," + to_string(j);
}

int Heightmap::search_basin(int i, int j)
{
    int basin = 0;
    string coord = this->get_coordinate(i, j);
    if (this->seen_points.find(coord) != this->seen_points.end())
    {
        return 0;
    }
    this->seen_points.insert(coord);
    if (this->map[i][j] == 9)
    {
        return 0;
    }

    if (i > 0)
    {
        basin += this->search_basin(i - 1, j);
    }
    if (j > 0)
    {
        basin += this->search_basin(i, j - 1);
    }
    if (i < height - 1)
    {
        basin += this->search_basin(i + 1, j);
    }
    if (j < width - 1)
    {
        basin += this->search_basin(i, j + 1);
    }
    return basin + 1;
}