#include <fstream>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;

int main(void)
{
    fstream  file ;
    string line;
    
    for (int noun=0;noun<100;noun++)
    {
        for (int verb=0;verb<100;verb++)
        {
            vector <int> data;
            file.open("Day2.txt", ios::in);
            getline(file, line);
            file.close();
            char char_array[line.length() + 1];
            strcpy(char_array, line.c_str());
            const char *delim = ",";
            char *token = strtok(char_array, delim);
            while (token != NULL)
            {
                data.push_back(atoi(token));
                token = strtok (NULL, delim);
            }
            data[1] = noun;
            data[2] = verb;
            int index = 0;
            while (data[index] != 99)
            {
                if (data[index] == 1)
                {
                    data[data[index+3]] = data[data[index+1]] + data[data[index+2]];
                }
                else if (data[index] == 2)
                {
                    data[data[index+3]] = data[data[index+1]] * data[data[index+2]];
                }
                index += 4;
            }
            // cout << data[0] << "\n";
            if (data[0] == 19690720)
            {
                cout << (100 * noun + verb) << "\n";
                break;
                break;
            }
        }
    }
    return 0;
}
