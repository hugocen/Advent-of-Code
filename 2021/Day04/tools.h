#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<int> getBingoNumbers(string numbers)
{
    const char delim = ',';
    vector<int> bingoNumbers;
    stringstream bingoNumbersStream(numbers);
    string number;

    while (getline(bingoNumbersStream, number, delim))
    {
        bingoNumbers.push_back(stoi(number));
    }

    return bingoNumbers;
}