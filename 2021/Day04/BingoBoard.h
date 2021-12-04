#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

class BingoBoard
{
public:
    vector<vector<int>> board;
    vector<vector<bool>> marked;

    void set_board(vector<string> &bingoList)
    {
        const char delim = ' ';
        for (int i = 0; i < bingoList.size(); i++)
        {
            vector<int> row;
            vector<bool> marks;

            stringstream bingoListStream(bingoList[i]);
            string token;

            while (getline(bingoListStream, token, delim))
            {
                if (token == " " || token == "")
                    continue;
                row.push_back(stoi(token));
                marks.push_back(false);
            }
            board.push_back(row);
            marked.push_back(marks);
        }
    };

    void print()
    {
        cout << "Board size:" << board.size() << endl;
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[i].size(); j++)
            {
                cout << board[i][j] << " ";
            }
            cout << "length: " << board[i].size() << endl;
        }
    };

    void mark(int target)
    {
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[i].size(); j++)
            {
                if (board[i][j] == target)
                {
                    marked[i][j] = true;
                }
            }
        }
    };

    bool isBingo()
    {
        for (int i = 0; i < board.size(); i++)
        {
            bool flag = true;
            for (int j = 0; j < board[i].size(); j++)
            {
                if (marked[i][j] == false)
                {
                    flag = false;
                }
            }
            if (flag == true)
            {
                return true;
            }
        }

        for (int i = 0; i < board[0].size(); i++)
        {
            bool flag = true;
            for (int j = 0; j < board.size(); j++)
            {
                if (marked[j][i] == false)
                {
                    flag = false;
                }
            }
            if (flag == true)
            {
                return true;
            }
        }

        return false;
    };

    int unmarkedSum()
    {
        int sum = 0;
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[i].size(); j++)
            {
                if (marked[i][j] == false)
                {
                    sum += board[i][j];
                }
            }
        }
        return sum;
    };
};
