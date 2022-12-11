# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on


class Day09(Base):
    moves = []

    def preprocess_data(self):
        for line in self.data:
            instruction = line.split(" ")
            self.moves.append((instruction[0], int(instruction[1])))

    @staticmethod
    def check_touching(head, tail):
        vertical = abs(head[1] - tail[1])
        horizontal = abs(head[0] - tail[0])
        touched = vertical <= 1 and horizontal <= 1
        go_diagonal = vertical + horizontal > 2
        return touched, go_diagonal

    @staticmethod
    def tail_follow_straight(head, tail):
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
        elif head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
        return tail

    @staticmethod
    def tail_follow_diagonal(head, tail):
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
        return tail

    @staticmethod
    def move(point, instruction):
        match instruction[0]:
            case "R":
                point[0] += 1
            case "L":
                point[0] -= 1
            case "U":
                point[1] += 1
            case "D":
                point[1] -= 1
        return point

    def puzzle1(self):
        head = [0, 0]
        tail = [0, 0]
        tail_walked = set()
        tail_walked.add(tuple(tail))
        for move in self.moves:
            for _ in range(move[1]):
                head = self.move(head, move)
                touched, go_diagonal = self.check_touching(head, tail)
                if not touched:
                    if go_diagonal:
                        tail = self.tail_follow_diagonal(head, tail)
                    else:
                        tail = self.tail_follow_straight(head, tail)
                tail_walked.add(tuple(tail))

        print(f"How many positions does the tail of the rope visit at least once? {len(tail_walked)}")

    def puzzle2(self):
        rope = [[0, 0] for _ in range(10)]
        tail_walked = set()
        tail_walked.add(tuple(rope[-1]))
        for move in self.moves:
            for _ in range(move[1]):
                rope[0] = self.move(rope[0], move)
                for i in range(1, len(rope)):
                    touched, go_diagonal = self.check_touching(rope[i - 1], rope[i])
                    if not touched:
                        if go_diagonal:
                            rope[i] = self.tail_follow_diagonal(rope[i - 1], rope[i])
                        else:
                            rope[i] = self.tail_follow_straight(rope[i - 1], rope[i])
                tail_walked.add(tuple(rope[-1]))

        print(f"How many positions does the tail of the rope visit at least once? {len(tail_walked)}")


if __name__ == "__main__":
    obj = Day09()
    obj.run()
