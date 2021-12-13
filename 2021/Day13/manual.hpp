#include <string>
#include <vector>
#include <tuple>
#include "../tools/tools.h"

using namespace std;

class ThermalCameraManual
{
private:
    int width;
    int height;
    vector<vector<bool>> map;
    vector<tuple<char, int>> instructions;
    int setupMap(vector<string> lines);
    void getInstructions(vector<string> lines, int start);
    void initMap();
    void placeDots(vector<vector<int>> dots);
    void foldX(int distance);
    void foldY(int distance);
    int getTotalDots();

public:
    ThermalCameraManual(string input_file);
    void print();
    int fold(int step);
    int folds();
};

ThermalCameraManual::ThermalCameraManual(string input_file)
{
    vector<string> lines = readfile(input_file);

    int idx = this->setupMap(lines);

    idx += 1;
    getInstructions(lines, idx);
};

int ThermalCameraManual::setupMap(vector<string> lines)
{
    vector<vector<int>> dots;
    vector<int> xs;
    vector<int> ys;

    int idx = 0;
    for (; idx < lines.size(); idx++)
    {
        if (lines[idx] == "")
        {
            break;
        }
        vector<string> coord = split_string_two_part(lines[idx], ',');
        vector<int> dot{stoi(coord[0]), stoi(coord[1])};
        xs.push_back(dot[0]);
        ys.push_back(dot[1]);
        dots.push_back(dot);
    }

    this->width = max_value(xs) + 1;
    this->height = max_value(ys) + 1;

    this->initMap();
    this->placeDots(dots);

    return idx;
}

void ThermalCameraManual::getInstructions(vector<string> lines, int start)
{
    for (int idx = start; idx < lines.size(); idx++)
    {
        if (lines[idx].find('x') != string::npos)
        {
            size_t found = lines[idx].find('x');
            this->instructions.push_back(make_tuple('x', stoi(lines[idx].substr(found + 2))));
        }
        else
        {
            size_t found = lines[idx].find('y');
            this->instructions.push_back(make_tuple('y', stoi(lines[idx].substr(found + 2))));
        }
    }
}

void ThermalCameraManual::initMap()
{
    for (int i = 0; i < this->height; i++)
    {
        vector<bool> row;
        for (int j = 0; j < this->width; j++)
        {
            row.push_back(false);
        }
        this->map.push_back(row);
    }
};

void ThermalCameraManual::placeDots(vector<vector<int>> dots)
{
    for (int i = 0; i < dots.size(); i++)
    {
        this->map[dots[i][1]][dots[i][0]] = true;
    }
};

void ThermalCameraManual::print()
{
    for (int i = 0; i < this->height; i++)
    {
        for (int j = 0; j < this->width; j++)
        {
            if (this->map[i][j])
            {
                cout << "#";
            }
            else
            {
                cout << ".";
            }
        }
        cout << endl;
    }
};

void ThermalCameraManual::foldX(int distance)
{
    vector<vector<bool>> new_map;
    for (int i = 0; i < this->height; i++)
    {
        vector<bool> row;
        for (int j = 0; j < distance; j++)
        {
            row.push_back(this->map[i][j]);
        }

        for (int j = distance + 1; j < this->width; j++)
        {
            int new_j = distance - (j - distance);
            if (this->map[i][j])
            {
                row[new_j] = true;
            }
        }
        new_map.push_back(row);
    }
    this->map = new_map;
    this->width = distance;
};

void ThermalCameraManual::foldY(int distance)
{
    vector<vector<bool>> new_map;
    for (int i = 0; i < distance; i++)
    {
        vector<bool> row;
        for (int j = 0; j < this->width; j++)
        {
            row.push_back(this->map[i][j]);
        }
        new_map.push_back(row);
    }

    for (int i = distance + 1; i < this->height; i++)
    {
        vector<bool> row;
        for (int j = 0; j < this->width; j++)
        {
            int new_i = distance - (i - distance);
            if (this->map[i][j])
            {
                new_map[new_i][j] = true;
            }
        }
    }
    this->map = new_map;
    this->height = distance;
};

int ThermalCameraManual::getTotalDots()
{
    int total = 0;
    for (int i = 0; i < this->height; i++)
    {
        for (int j = 0; j < this->width; j++)
        {
            if (this->map[i][j])
            {
                total++;
            }
        }
    }
    return total;
};

int ThermalCameraManual::folds()
{
    for (int i = 0; i < this->instructions.size(); i++)
    {
        char direction = get<0>(this->instructions[i]);
        int distance = get<1>(this->instructions[i]);
        if (direction == 'x')
        {
            this->foldX(distance);
        }
        else
        {
            this->foldY(distance);
        }
    }
    return this->getTotalDots();
};

int ThermalCameraManual::fold(int step)
{
    for (int i = 0; i < step; i++)
    {
        char direction = get<0>(this->instructions[i]);
        int distance = get<1>(this->instructions[i]);
        if (direction == 'x')
        {
            this->foldX(distance);
        }
        else
        {
            this->foldY(distance);
        }
    }
    return this->getTotalDots();
};