# fmt: off
import sys
sys.path.append('../')
from utils.base import Base
# fmt: on


class Day04(Base):
    pairs = []

    def preprocess_data(self):
        for line in self.data:
            pair = line.split(",")
            seat_assignment = []
            for seat_assign_str in pair:
                seat_assign = seat_assign_str.split("-")
                for i, seat in enumerate(seat_assign):
                    seat_assign[i] = int(seat)
                seat_assignment.append(seat_assign)
            seat_assignment = sorted(
                seat_assignment, key=lambda x: (x[0], -x[1]))
            self.pairs.append(seat_assignment)

    def puzzle1(self):
        fully_contain = 0
        for seat_a, seat_b in self.pairs:
            if seat_b[0] >= seat_a[0] and seat_b[0] <= seat_a[1]:
                if seat_b[1] >= seat_a[0] and seat_b[1] <= seat_a[1]:
                    fully_contain += 1

        print(f"Fully contain seats: {fully_contain}")

    def puzzle2(self):
        overlap = 0
        for seat_a, seat_b in self.pairs:
            if seat_b[0] >= seat_a[0] and seat_b[0] <= seat_a[1]:
                overlap += 1

        print(f"Overlap seats: {overlap}")


if __name__ == "__main__":
    obj = Day04()
    obj.run()
