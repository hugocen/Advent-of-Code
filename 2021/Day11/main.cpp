#include "../tools/tools.h"
#include "dumboOctopus.h"

using namespace std;

int main(int argc, char *argv[])
{
    auto lines = readfile(argv[1]);

    auto octopuses = DumboOctopus(lines);

    cout << "Part 1 answer: " << octopuses.steps(100) << endl;

    octopuses = DumboOctopus(lines);

    cout << "Part 2 answer: " << octopuses.getSynchronized() << endl;

    return 0;
};