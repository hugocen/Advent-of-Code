import sys
sys.path.append('../')
from utils import io

def puzzle1(input_file_path):
    data = io.get_data(input_file_path)
    max_calories = float("-inf")
    carrying = 0
    for line in data:
        if line == "\n":
            carrying = 0
            continue
        carrying += int(line)
        max_calories = max(max_calories, carrying)
    
    print(f"The Elf carrying the most calories carries: {max_calories}")

def puzzle2(input_file_path):
    data = io.get_data(input_file_path)
    calories = []
    carrying = 0
    for line in data:
        if line == "\n":
            calories.append(carrying)
            carrying = 0
            continue
        carrying += int(line)
    calories.append(carrying)
    calories.sort()

    top3sums = calories[-1] + calories[-2] + calories[-3]

    print(f"Top 3 Elfs carrying the most calories carries sums: {top3sums}")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("no inputs")
    input_file_path = sys.argv[1]
    puzzle1(input_file_path)
    puzzle2(input_file_path)