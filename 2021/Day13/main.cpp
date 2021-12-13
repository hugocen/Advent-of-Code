#include "manual.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    auto manual = ThermalCameraManual(argv[1]);

    cout << "Part 1 answer: " << manual.fold(1) << endl;

    manual = ThermalCameraManual(argv[1]);

    cout << "Part 2 answer: " << manual.folds() << endl;
    manual.print();

    return 0;
};