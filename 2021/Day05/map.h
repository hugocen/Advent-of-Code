#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

class Map
{
public:
    int map_size;
    vector<vector<int>> map;

    Map(int size)
    {
        map_size = size + 1;
        map = vector<vector<int>>(map_size, vector<int>(map_size, 0));
    };

    void print()
    {
        for (int i = 0; i < map_size; i++)
        {
            for (int j = 0; j < map_size; j++)
            {
                if (map[i][j] == 0)
                {
                    cout << ".";
                }
                else
                {
                    cout << map[i][j];
                }
            }
            cout << endl;
        }
    };

    bool check_horizontal_or_vertical_line(vector<int> x_coordinates, vector<int> y_coordinates)
    {
        return (x_coordinates[0] == x_coordinates[1] || y_coordinates[0] == y_coordinates[1]);
    };

    void add_line(vector<vector<int>> points)
    {
        vector<int> point1 = points[0];
        vector<int> point2 = points[1];

        vector<int> x_coordinates = {point1[0], point2[0]};
        vector<int> y_coordinates = {point1[1], point2[1]};

        if (!check_horizontal_or_vertical_line(x_coordinates, y_coordinates))
        {
            return;
        }

        sort(x_coordinates.begin(), x_coordinates.end());
        sort(y_coordinates.begin(), y_coordinates.end());

        for (int i = y_coordinates[0]; i <= y_coordinates[1]; i++)
        {
            for (int j = x_coordinates[0]; j <= x_coordinates[1]; j++)
            {
                map[i][j] += 1;
            }
        }
    };

    void add_lines(vector<vector<vector<int>>> lines)
    {
        for (int i = 0; i < lines.size(); i++)
        {
            add_line(lines[i]);
        }
    };

    int sum_overlap()
    {
        int sum = 0;
        for (int i = 0; i < map_size; i++)
        {
            for (int j = 0; j < map_size; j++)
            {
                if (map[i][j] > 1)
                {
                    sum += 1;
                }
            }
        }
        return sum;
    };

    bool check_diagonal_line(vector<int> x_coordinates, vector<int> y_coordinates)
    {
        return (abs(x_coordinates[0] - x_coordinates[1]) == abs(y_coordinates[0] - y_coordinates[1]));
    };

    void add_diagonal_line(vector<vector<int>> points)
    {
        vector<int> point1 = points[0];
        vector<int> point2 = points[1];

        vector<int> x_coordinates = {point1[0], point2[0]};
        vector<int> y_coordinates = {point1[1], point2[1]};

        if (!check_diagonal_line(x_coordinates, y_coordinates))
        {
            return;
        }

        if (x_coordinates[0] > x_coordinates[1])
        {
            swap(x_coordinates[0], x_coordinates[1]);
            swap(y_coordinates[0], y_coordinates[1]);
        }

        int diff = abs(x_coordinates[1] - x_coordinates[0]);

        for (int i = 0; i <= diff; i++)
        {
            if (y_coordinates[0] < y_coordinates[1])
            {
                map[y_coordinates[0] + i][x_coordinates[0] + i] += 1;
            }
            else
            {
                map[y_coordinates[0] - i][x_coordinates[0] + i] += 1;
            }
        }
    };

    void add_diagonal_lines(vector<vector<vector<int>>> lines)
    {
        for (int i = 0; i < lines.size(); i++)
        {
            add_diagonal_line(lines[i]);
        }
    };
};
