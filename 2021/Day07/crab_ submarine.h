#include <map>

using namespace std;

class CrabSubmarine
{
public:
    map<int, int> step_map;

    CrabSubmarine(){};

    int calculate_fuel(int step)
    {
        if (step == 1)
        {
            return 1;
        }
        else if (step == 0)
        {
            return 0;
        }
        else if (step_map.find(step) != step_map.end())
        {
            return step_map[step];
        }
        else
        {
            int fuel = calculate_fuel(step - 1) + step;
            step_map[step] = fuel;
            return fuel;
        }
    };
};
