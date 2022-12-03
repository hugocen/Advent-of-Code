# fmt: off
import sys
sys.path.append('../')
from utils import io
# fmt: on


Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"

Win = "Win"
Draw = "Draw"
Lose = "Lose"

opponent_map = {
    "A": Rock,
    "B": Paper,
    "C": Scissors
}

mine_map = {
    "X": Rock,
    "Y": Paper,
    "Z": Scissors
}

result_map = {
    "X": Lose,
    "Y": Draw,
    "Z": Win
}


def rock_paper_scissors(mine, opponent):
    if mine == Rock:
        if opponent == Rock:
            return 1 + 3
        elif opponent == Paper:
            return 1 + 0
        else:
            return 1 + 6
    elif mine == Paper:
        if opponent == Rock:
            return 2 + 6
        elif opponent == Paper:
            return 2 + 3
        else:
            return 2 + 0
    else:
        if opponent == Rock:
            return 3 + 0
        elif opponent == Paper:
            return 3 + 6
        else:
            return 3 + 3


def rock_paper_scissors_result(result, opponent):
    if result == Lose:
        if opponent == Rock:
            return 0 + 3
        elif opponent == Paper:
            return 0 + 1
        else:
            return 0 + 2
    elif result == Draw:
        if opponent == Rock:
            return 3 + 1
        elif opponent == Paper:
            return 3 + 2
        else:
            return 3 + 3
    else:
        if opponent == Rock:
            return 6 + 2
        elif opponent == Paper:
            return 6 + 3
        else:
            return 6 + 1


def puzzle1(input_file_path):
    data = io.get_data(input_file_path)
    scores = 0
    for line in data:
        opponent = opponent_map[line[0]]
        mine = mine_map[line[2]]
        scores += rock_paper_scissors(mine, opponent)

    print(f"Total Score: {scores}")


def puzzle2(input_file_path):
    data = io.get_data(input_file_path)
    scores = 0
    for line in data:
        opponent = opponent_map[line[0]]
        result = result_map[line[2]]
        scores += rock_paper_scissors_result(result, opponent)

    print(f"Total Score: {scores}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("no inputs")
    input_file_path = sys.argv[1]
    puzzle1(input_file_path)
    puzzle2(input_file_path)
