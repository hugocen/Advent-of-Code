#ifndef SEGMENTS_H
#define SEGMENTS_H

#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include "../tools/tools.h"

using namespace std;

class segment
{
public:
    map<string, string> map_values;
    string numbers[10];

    segment(string input);

    void sort_value(vector<string>);
    void set_map();

    string get_value(string);
};

segment::segment(string input)
{
    vector<string> input_values = spilt_string_by_delim(input, ' ');
    for (int i = 0; i < 10; i++)
    {
        sort(input_values[i].begin(), input_values[i].end());
    }

    sort_value(input_values);

    set_map();
}

void segment::sort_value(vector<string> input_values)
{
    // get 1 4 7 8
    for (auto value : input_values)
    {
        if (value.length() == 2)
        {
            numbers[1] = value;
        }
        else if (value.length() == 3)
        {
            numbers[7] = value;
        }
        else if (value.length() == 4)
        {
            numbers[4] = value;
        }
        else if (value.length() == 7)
        {
            numbers[8] = value;
        }
    }

    // get 3
    for (auto value : input_values)
    {
        if (value.length() == 5)
        {
            if (check_string_contain(value, numbers[1]))
            {
                numbers[3] = value;
                break;
            }
        }
    }

    // get 6 9 0
    for (auto value : input_values)
    {
        if (value.length() == 6)
        {
            if (check_string_contain(value, numbers[3]))
            {
                numbers[9] = value;
            }
            else if (check_string_contain(value, numbers[7]))
            {
                numbers[0] = value;
            }
            else
            {
                numbers[6] = value;
            }
        }
    }

    // get 5
    for (auto value : input_values)
    {
        if (value.length() == 5)
        {
            if (check_string_contain(numbers[6], value))
            {
                numbers[5] = value;
                break;
            }
        }
    }

    // get 2
    for (auto value : input_values)
    {
        if (value.length() == 5)
        {
            if (value != numbers[3] && value != numbers[5])
            {
                numbers[2] = value;
                break;
            }
        }
    }
}

void segment::set_map()
{
    for (int i = 0; i < 10; i++)
    {
        map_values[numbers[i]] = to_string(i);
    }
}

string segment::get_value(string input)
{
    return map_values[input];
}

#endif
