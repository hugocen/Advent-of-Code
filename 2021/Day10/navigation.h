#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

class NavigationSubsystem
{
private:
    vector<string> lines;
    vector<char> checkCorrupted(string line);
    map<char, char> char_match = {
        {')', '('},
        {']', '['},
        {'}', '{'},
        {'>', '<'},
    };
    map<char, int> corrupted_score = {
        {')', 3},
        {']', 57},
        {'}', 1197},
        {'>', 25137},
    };
    map<char, long int> incomplete_score = {
        {'(', 1},
        {'[', 2},
        {'{', 3},
        {'<', 4},
    };
    long int calc_incomplete_score(string line);

public:
    NavigationSubsystem(vector<string> input);
    void print();
    int getCorruptedScore();
    long int getIncompleteScore();
};

NavigationSubsystem::NavigationSubsystem(vector<string> input)
{
    this->lines = input;
};

void NavigationSubsystem::print()
{
    for (int i = 0; i < lines.size(); i++)
    {
        cout << lines[i] << endl;
    }
};

vector<char> NavigationSubsystem::checkCorrupted(string line)
{
    vector<char> stack;
    for (auto c : line)
    {
        if (this->char_match.find(c) == char_match.end())
        {
            stack.push_back(c);
        }
        else
        {
            if (this->char_match[c] != stack.back())
            {
                vector<char> temp{c};
                return temp;
            }
            else
            {
                stack.pop_back();
            }
        }
    }
    return stack;
};

int NavigationSubsystem::getCorruptedScore()
{
    int score = 0;
    for (int i = 0; i < lines.size(); i++)
    {
        vector<char> stack = this->checkCorrupted(lines[i]);
        if (stack.size() == 1)
        {
            score += this->corrupted_score[stack[0]];
        }
    }
    return score;
};

long int NavigationSubsystem::calc_incomplete_score(string line)
{
    long int score = 0;
    vector<char> stack = this->checkCorrupted(line);
    if (stack.size() <= 1)
    {
        return 0;
    }
    for (int i = stack.size() - 1; i >= 0; i--)
    {
        score = ((score * 5) + this->incomplete_score[stack[i]]);
    }
    return score;
};

long int NavigationSubsystem::getIncompleteScore()
{
    vector<long int> scores;
    for (int i = 0; i < lines.size(); i++)
    {
        long int score = this->calc_incomplete_score(lines[i]);
        if (score != 0)
        {
            scores.push_back(score);
        }
    }
    sort(scores.begin(), scores.end());
    return scores[scores.size() / 2];
};