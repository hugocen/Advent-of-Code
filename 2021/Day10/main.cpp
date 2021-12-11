#include "../tools/tools.h"
#include "navigation.h"

using namespace std;

int main(int argc, char *argv[])
{
    auto lines = readfile(argv[1]);

    NavigationSubsystem nav(lines);

    cout << "Part 1 answer: " << nav.getCorruptedScore() << endl;

    cout << "Part 2 answer: " << nav.getIncompleteScore() << endl;

    return 0;
};