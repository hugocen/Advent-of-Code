# fmt: off
import sys
sys.path.append('../')
from utils import io
# fmt: on


def get_duplicate(items):
    dics = []
    for item in items:
        dics.append(set(item))
    result = ""
    for key in dics[0]:
        flag = True
        for dic in dics[1:]:
            if key not in dic:
                flag = False
        if flag:
            result += key
    return result


def get_priority(item):
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return ord(item) - 64 + 26


def puzzle1(input_file_path):
    data = io.get_data(input_file_path)
    sum_priorities = 0
    for line in data:
        line = line.replace("\n", "")
        middle = len(line) // 2
        item1 = line[:middle]
        item2 = line[middle:]
        duplicated = get_duplicate([item1, item2])
        for item in duplicated:
            sum_priorities += get_priority(item)
    print(f"Total priorities: {sum_priorities}")


def puzzle2(input_file_path):
    data = io.get_data(input_file_path)
    sum_priorities = 0
    rucksacks = []
    for line in data:
        line = line.replace("\n", "")
        rucksacks.append(line)
    for i in range(0, len(rucksacks), 3):
        duplicated = get_duplicate(
            [rucksacks[i], rucksacks[i+1], rucksacks[i+2]])
        for item in duplicated:
            sum_priorities += get_priority(item)
    print(f"Total priorities: {sum_priorities}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("no inputs")
    input_file_path = sys.argv[1]
    puzzle1(input_file_path)
    puzzle2(input_file_path)
