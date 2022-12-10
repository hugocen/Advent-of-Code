# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
# pylint: disable=missing-class-docstring,missing-function-docstring


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parrent=None):
        self.child_directory = {}
        self.files = []
        self.name = name
        self.parent_dir = parrent

    def add_file(self, file_name, size):
        self.files.append(File(file_name, size))

    def add_directory(self, name, parent):
        new_directory = Directory(name, parent)
        self.child_directory[name] = new_directory

    def get_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size

        for _, child_dir in self.child_directory.items():
            child_dir_size = child_dir.get_total_size()
            total_size += child_dir_size

        print(f"Dir: {self.name}, size: {total_size}")
        return total_size

    def get_puzzle_result(self, at_most_size):
        total_size = 0
        result = 0
        for file in self.files:
            total_size += file.size

        for _, child_dir in self.child_directory.items():
            child_dir_size, child_dir_result = child_dir.get_puzzle_result(at_most_size)
            total_size += child_dir_size
            result += child_dir_result

        if total_size <= at_most_size:
            result += total_size
        return total_size, result

    def get_all_dir_sizes(self):
        total_size = 0
        all_sizes = []
        for file in self.files:
            total_size += file.size
        for _, child_dir in self.child_directory.items():
            child_dir_size, child_dir_sizs = child_dir.get_all_dir_sizes()
            total_size += child_dir_size
            all_sizes += child_dir_sizs
        all_sizes.append(total_size)
        return total_size, all_sizes


class Day07(Base):
    root_dir = None

    def preprocess_data(self):
        self.root_dir = Directory("/")
        current_dir = self.root_dir
        for line in self.data[1:]:
            if line.startswith("$ cd"):
                target_dir = line.replace("$ cd ", "")
                if target_dir == "..":
                    current_dir = current_dir.parent_dir
                else:
                    current_dir = current_dir.child_directory[target_dir]
            elif line == "$ ls":
                continue
            else:
                if line.startswith("dir"):
                    target_dir = line.replace("dir ", "")
                    current_dir.add_directory(target_dir, current_dir)
                else:
                    current_file = line.split(" ")
                    current_dir.add_file(current_file[1], int(current_file[0]))

    def puzzle1(self):
        # root_dir.get_total_size()
        _, result = self.root_dir.get_puzzle_result(100000)
        print(f"Sum of the total sizes of those directories: {result}")

    def puzzle2(self):
        root_size, all_dir_sizes = self.root_dir.get_all_dir_sizes()
        all_dir_sizes.sort()
        free_space = 70000000 - root_size
        need_for_update = 30000000 - free_space
        for size in all_dir_sizes:
            if size >= need_for_update:
                print(
                    f"The smallest directory that, if deleted, would free up enough space on the filesystem to run the update: {size}"
                )
                return


if __name__ == "__main__":
    obj = Day07()
    obj.run()
