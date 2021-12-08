#ifndef TOOLS_H
#define TOOLS_H

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

vector<string> readfile(string filename)
{
    ifstream inputFile(filename);
    vector<string> lines;

    if (inputFile)
    {
        string line;
        while (getline(inputFile, line))
        {
            lines.push_back(line);
        }
        inputFile.close();
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        exit(1);
    }
    return lines;
}

vector<string> spilt_string_by_delim(string input, char delim)
{
    vector<string> result;

    stringstream ss(input);

    string token;

    while (getline(ss, token, delim))
    {
        if (token == " " || token == "")
            continue;
        result.push_back(token);
    }

    return result;
};

int max_value(vector<int> input)
{
    int max = 0;
    for (int i = 0; i < input.size(); i++)
    {
        if (input[i] > max)
            max = input[i];
    }
    return max;
}

vector<string> split_string_two_part(string input, char delim)
{
    vector<string> result;

    string token;

    auto found = input.find(delim);

    result.push_back(input.substr(0, found));
    result.push_back(input.substr(found + 1));

    return result;
};

bool check_string_contain(string input, string target)
{
    for (int i = 0; i < target.length(); i++)
    {
        if (input.find(target[i]) == string::npos)
        {
            return false;
        }
    }
    return true;
}

#endif
