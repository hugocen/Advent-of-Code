#include <vector>
#include <string>
#include <tuple>
#include <algorithm>
#include <map>
#include "../tools/tools.h"

using namespace std;

class Polymerization
{
private:
    string polymerTemplate;
    vector<vector<string>> insertions;
    map<string, unsigned long long> patterns;
    unsigned long long getScore();

public:
    Polymerization(string filePath);
    unsigned long long steps(int steps);
    void print();
    void step();
};

Polymerization::Polymerization(string filePath)
{
    vector<string> lines = readfile(filePath);
    this->polymerTemplate = lines[0];

    for (int i = 2; i < lines.size(); i++)
    {
        vector<string> split = split_string_two_part(lines[i], " -> ");
        vector<string> insert{split[0], split[1]};
        this->insertions.push_back(insert);
    }

    for (int i = 0; i < polymerTemplate.length() - 1; i++)
    {
        this->patterns[polymerTemplate.substr(i, 2)]++;
    }
};

void Polymerization::print()
{
    cout << "Polymerization:" << polymerTemplate << endl;
    for (auto &insert : this->insertions)
    {
        cout << insert[0] << " -> " << insert[1] << endl;
    }
};

unsigned long long Polymerization::steps(int steps)
{
    for (int i = 0; i < steps; i++)
    {
        this->step();
    }
    return this->getScore();
};

void Polymerization::step()
{
    vector<tuple<string, unsigned long long>> newPatterns;
    for (auto insert : this->insertions)
    {
        if (this->patterns.find(insert[0]) != this->patterns.end() && this->patterns[insert[0]] > 0)
        {
            newPatterns.push_back(make_tuple(insert[0].substr(0, 1) + insert[1], this->patterns[insert[0]]));
            newPatterns.push_back(make_tuple(insert[1] + insert[0].substr(1, 1), this->patterns[insert[0]]));
            this->patterns[insert[0]] = 0;
        }
    }
    for (auto &pattern : newPatterns)
    {
        this->patterns[get<0>(pattern)] += get<1>(pattern);
    }
};

unsigned long long Polymerization::getScore()
{
    map<char, unsigned long long> occurs;
    for (auto pattern : this->patterns)
    {
        occurs[pattern.first[0]] += pattern.second;
        occurs[pattern.first[1]] += pattern.second;
    }
    occurs[this->polymerTemplate[0]]--;
    occurs[this->polymerTemplate[this->polymerTemplate.length() - 1]]--;
    for (auto &occur : occurs)
    {
        occur.second /= 2;
    }
    occurs[this->polymerTemplate[0]]++;
    occurs[this->polymerTemplate[this->polymerTemplate.length() - 1]]++;
    vector<unsigned long long> scores;
    for (auto &occur : occurs)
    {
        scores.push_back(occur.second);
    }
    sort(scores.begin(), scores.end());

    return scores[scores.size() - 1] - scores[0];
};