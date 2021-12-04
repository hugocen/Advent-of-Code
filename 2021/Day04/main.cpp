#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "BingoBoard.h"
#include "tools.h"

using namespace std;

int part1(vector<int> bingoNumbers, vector<BingoBoard> bingoBoards)
{
    bool bingo = false;
    int count = 0;
    while (!bingo)
    {
        for (int i = 0; i < bingoBoards.size(); i++)
        {
            bingoBoards[i].mark(bingoNumbers[count]);
            if (bingoBoards[i].isBingo())
            {
                return bingoBoards[i].unmarkedSum() * bingoNumbers[count];
            }
        }
        count++;
    }

    return -1;
}

int part2(vector<int> bingoNumbers, vector<BingoBoard> bingoBoards)
{
    int count = 0;
    while (bingoBoards.size() > 1)
    {
        vector<BingoBoard> notBingoBoards;
        for (int i = 0; i < bingoBoards.size(); i++)
        {
            bingoBoards[i].mark(bingoNumbers[count]);
            if (!bingoBoards[i].isBingo())
            {
                notBingoBoards.push_back(bingoBoards[i]);
            }
        }
        count++;
        bingoBoards = notBingoBoards;
    }

    BingoBoard lastBoard = bingoBoards[0];

    while (!lastBoard.isBingo())
    {
        lastBoard.mark(bingoNumbers[count]);
        count++;
    }

    return lastBoard.unmarkedSum() * bingoNumbers[count - 1];
}

int main(int argc, char *argv[])
{
    ifstream inputFile(argv[1]);

    if (inputFile)
    {
        string line;
        vector<string> lines;
        while (getline(inputFile, line))
        {
            lines.push_back(line);
        }

        inputFile.close();

        vector<int> bingoNumbers = getBingoNumbers(lines[0]);

        vector<BingoBoard> bingoBoards;

        for (int i = 2; i < lines.size(); i += 6)
        {
            vector<string> bingoBoardStringList;
            for (int j = 0; j < 5; j++)
            {
                bingoBoardStringList.push_back(lines[i + j]);
            }
            BingoBoard newBingoBoard;
            newBingoBoard.set_board(bingoBoardStringList);
            bingoBoards.push_back(newBingoBoard);
        }

        int part1Answer = part1(bingoNumbers, bingoBoards);
        cout << "Part 1 answer: " << part1Answer << endl;

        int part2Answer = part2(bingoNumbers, bingoBoards);
        cout << "Part 2 answer: " << part2Answer << endl;
    }
    else
    {
        cerr << "File could not be opened!\n";
        cerr << "Error: " << strerror(errno);
        return 1;
    }
}