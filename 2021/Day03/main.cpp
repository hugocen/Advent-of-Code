#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int part1(vector<string> &diagnosticReport)
{
    vector<int> oneCounts;
    for (int i = 0; i < diagnosticReport[0].length(); i++)
    {
        if (diagnosticReport[0][i] == '1')
        {
            oneCounts.push_back(1);
        }
        else
        {
            oneCounts.push_back(0);
        }
    }

    for (int i = 1; i < diagnosticReport.size(); i++)
    {
        for (int j = 0; j < diagnosticReport[i].length(); j++)
        {
            if (diagnosticReport[i][j] == '1')
            {
                oneCounts[j]++;
            }
        }
    }

    string gamma = "";
    string epsilon = "";

    for (int i = 0; i < oneCounts.size(); i++)
    {
        if (oneCounts[i] > diagnosticReport.size() / 2)
        {
            gamma.append("1");
            epsilon.append("0");
        }
        else
        {
            gamma.append("0");
            epsilon.append("1");
        }
    }

    return stoi(gamma, nullptr, 2) * stoi(epsilon, nullptr, 2);
}

vector<string> criteriaFilter(vector<string> &diagnosticReport, int pos, bool findMax)
{
    int count = 0;
    bool flag = false;
    vector<string> filteredReport;

    pos = pos % diagnosticReport[0].length();

    for (int i = 0; i < diagnosticReport.size(); i++)
    {
        if (diagnosticReport[i][pos] == '1')
        {
            count++;
        }
    }

    if (findMax && (count >= (diagnosticReport.size() - count)))
    {
        flag = true;
    }
    else if (!findMax && (count < (diagnosticReport.size() - count)))
    {
        flag = true;
    }

    if (flag)
    {
        for (int i = 0; i < diagnosticReport.size(); i++)
        {
            if (diagnosticReport[i][pos] == '1')
            {
                filteredReport.push_back(diagnosticReport[i]);
            }
        }
    }
    else
    {
        for (int i = 0; i < diagnosticReport.size(); i++)
        {
            if (diagnosticReport[i][pos] == '0')
            {
                filteredReport.push_back(diagnosticReport[i]);
            }
        }
    }

    if (filteredReport.size() == 1)
    {
        return filteredReport;
    }
    else
    {
        return criteriaFilter(filteredReport, pos + 1, findMax);
    }
}

int part2(vector<string> &diagnosticReport)
{
    vector<string> oxygenGeneratorRating = criteriaFilter(diagnosticReport, 0, true);
    vector<string> co2ScrubberRating = criteriaFilter(diagnosticReport, 0, false);
    return stoi(oxygenGeneratorRating[0], nullptr, 2) * stoi(co2ScrubberRating[0], nullptr, 2);
}

int main(int argc, char *argv[])
{
    ifstream inputFile(argv[1]);

    vector<string> diagnosticReport;

    if (inputFile)
    {
        string line;
        while (getline(inputFile, line))
        {
            diagnosticReport.push_back(line);
        }
        inputFile.close();
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        return 1;
    }

    int part1Answer = part1(diagnosticReport);
    cout << "Part 1 answer: " << part1Answer << endl;

    int part2Answer = part2(diagnosticReport);
    cout << "Part 2 answer: " << part2Answer << endl;

    return 0;
}