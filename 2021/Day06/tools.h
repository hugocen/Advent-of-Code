#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<int> get_initial_timers(string input)
{
    vector<int> timers;
    const char delim = ',';

    stringstream ss(input);

    string token;

    while (getline(ss, token, delim))
    {
        if (token == " " || token == "")
            continue;
        timers.push_back(stoi(token));
    }

    return timers;
};