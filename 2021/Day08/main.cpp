#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include "../tools/tools.h"
#include "segments.h"

using namespace std;

int part1(vector<string> input)
{
    int result = 0;

    for (auto line : input)
    {
        vector<string> values = split_string_two_part(line, '|');
        vector<string> output_values = spilt_string_by_delim(values[1], ' ');
        for (auto value : output_values)
        {
            if (value.length() == 2 || value.length() == 3 || value.length() == 4 || value.length() == 7)
            {
                result++;
            }
        }
    }
    return result;
}

int part2(vector<string> input)
{
    int result = 0;

    for (auto line : input)
    {
        vector<string> values = split_string_two_part(line, '|');
        vector<string> output_values = spilt_string_by_delim(values[1], ' ');

        segment seg(values[0]);

        string output_value = "";
        for (auto value : output_values)
        {
            sort(value.begin(), value.end());
            output_value += seg.get_value(value);
        }
        result += stoi(output_value);
    }
    return result;
}

int main(int argc, char *argv[])
{
    auto lines = readfile(argv[1]);

    int part1Answer = part1(lines);
    cout << "Part 1 answer: " << part1Answer << endl;

    int part2Answer = part2(lines);
    cout << "Part 2 answer: " << part2Answer << endl;

    return 0;
}