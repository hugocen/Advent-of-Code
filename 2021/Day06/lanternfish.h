using namespace std;

class Lanternfish
{
public:
    int timer;

    Lanternfish(int initial_timer)
    {
        timer = initial_timer;
    };

    bool tick()
    {
        if (timer > 0)
        {
            timer--;
            return false;
        }
        else
        {
            timer = 6;
            return true;
        }
    };
};
