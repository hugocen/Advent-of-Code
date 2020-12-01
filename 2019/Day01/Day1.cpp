#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main(void)
{
    fstream  file ;
    string line;
    int total_fuel = 0;
    int need_fuel;
    file.open("Day1.txt", ios::in);
    while ( getline (file,line) )
    {
        need_fuel = (stoi(line))/3-2;
	while (need_fuel > 0)
	{
	        total_fuel += need_fuel;
		need_fuel = need_fuel/3-2; 
	}
    }
    file.close();
    cout << total_fuel << '\n';
    
    return 0;
}
