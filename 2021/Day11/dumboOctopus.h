#include <vector>
#include <string>

using namespace std;

class DumboOctopus
{
private:
    vector<vector<int>> Octopuses;
    int countFlashes();
    void chargeEnergy();
    void chargeNeighbors(int x, int y);
    int step();
    bool checkSynchronize();

public:
    DumboOctopus(vector<string> input);
    int steps(int s);
    void print();
    int getSynchronized();
};

DumboOctopus::DumboOctopus(vector<string> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        vector<int> row;
        for (int j = 0; j < input[i].size(); j++)
        {
            row.push_back(input[i][j] - '0');
        }
        Octopuses.push_back(row);
    }
};

void DumboOctopus::print()
{
    for (int i = 0; i < this->Octopuses.size(); i++)
    {
        for (int j = 0; j < this->Octopuses[i].size(); j++)
        {
            cout << this->Octopuses[i][j];
        }
        cout << endl;
    }
};

void DumboOctopus::chargeEnergy()
{
    for (int i = 0; i < this->Octopuses.size(); i++)
    {
        vector<int> row;
        for (int j = 0; j < this->Octopuses[i].size(); j++)
        {
            this->Octopuses[i][j] += 1;
        }
    }
};

void DumboOctopus::chargeNeighbors(int x, int y)
{
    if (x > 0 && this->Octopuses[x - 1][y] != 0)
    {
        this->Octopuses[x - 1][y] += 1;
    }
    if (x < this->Octopuses.size() - 1 && this->Octopuses[x + 1][y] != 0)
    {
        this->Octopuses[x + 1][y] += 1;
    }
    if (x > 0 && y > 0 && this->Octopuses[x - 1][y - 1] != 0)
    {
        this->Octopuses[x - 1][y - 1] += 1;
    }
    if (x > 0 && y < this->Octopuses[x].size() - 1 && this->Octopuses[x - 1][y + 1] != 0)
    {
        this->Octopuses[x - 1][y + 1] += 1;
    }
    if (x < this->Octopuses.size() - 1 && y > 0 && this->Octopuses[x + 1][y - 1] != 0)
    {
        this->Octopuses[x + 1][y - 1] += 1;
    }
    if (x < this->Octopuses.size() - 1 && y < this->Octopuses[x].size() - 1 && this->Octopuses[x + 1][y + 1] != 0)
    {
        this->Octopuses[x + 1][y + 1] += 1;
    }
    if (y > 0 && this->Octopuses[x][y - 1] != 0)
    {
        this->Octopuses[x][y - 1] += 1;
    }
    if (y < this->Octopuses[x].size() - 1 && this->Octopuses[x][y + 1] != 0)
    {
        this->Octopuses[x][y + 1] += 1;
    }
};

int DumboOctopus::countFlashes()
{
    int flashes = 0;
    for (int i = 0; i < this->Octopuses.size(); i++)
    {
        for (int j = 0; j < this->Octopuses[i].size(); j++)
        {
            if (this->Octopuses[i][j] > 9)
            {
                flashes++;
                this->chargeNeighbors(i, j);
                this->Octopuses[i][j] = 0;
            }
        }
    }
    return flashes;
};

int DumboOctopus::step()
{
    this->chargeEnergy();
    int flashes = 0;
    while (true)
    {
        int flash = this->countFlashes();
        if (flash == 0)
        {
            break;
        }
        flashes += flash;
    }

    return flashes;
};

int DumboOctopus::steps(int s)
{
    int flashes = 0;
    for (int i = 0; i < s; i++)
    {
        int flash = this->step();
        flashes += flash;
    }
    return flashes;
};

bool DumboOctopus::checkSynchronize()
{
    for (int i = 0; i < this->Octopuses.size(); i++)
    {
        for (int j = 0; j < this->Octopuses[i].size(); j++)
        {
            if (this->Octopuses[i][j] != 0)
            {
                return false;
            }
        }
    }
    return true;
};

int DumboOctopus::getSynchronized()
{
    int s = 0;
    while (!this->checkSynchronize())
    {
        this->step();
        s++;
    }
    return s;
};