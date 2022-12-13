# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
import ast
import copy
import functools


class Day13(Base):
    pairs = []

    def preprocess_data(self):
        for i in range(0, len(self.data), 3):
            self.pairs.append([ast.literal_eval(self.data[i]), ast.literal_eval(self.data[i + 1])])

    def compare(self, left_pair, right_pair):
        left_pair = copy.deepcopy(left_pair)
        right_pair = copy.deepcopy(right_pair)
        if len(left_pair) == 0:
            return 1
        if len(right_pair) == 0:
            return -1
        left = left_pair.pop(0)
        right = right_pair.pop(0)
        if isinstance(left, int) and isinstance(right, int):
            if right < left:
                return -1
            elif right > left:
                return 1
            else:
                if len(left_pair) == 0 and len(right_pair) == 0:
                    return 0
        else:
            if isinstance(left, list) and isinstance(right, list):
                result = self.compare(left, right)
                if result != 0:
                    return result
            elif isinstance(left, int):
                result = self.compare([left], right)
                if result != 0:
                    return result
            else:
                result = self.compare(left, [right])
                if result != 0:
                    return result
        return self.compare(left_pair, right_pair)

    def puzzle1(self):
        pairs = copy.deepcopy(self.pairs)
        indices_sum = 0
        for i, pair in enumerate(pairs):
            result = self.compare(pair[0], pair[1])
            if result > 0:
                indices_sum += i + 1
        print(f"What is the sum of the indices of those pairs? {indices_sum}")

    def unpack(self, packets):
        result = []
        for packet in packets:
            if packet == []:
                result.append(-1)
            elif isinstance(packet, list):
                result += self.unpack(packet)
            else:
                result.append(packet)
        return result

    def puzzle2(self):
        pairs = copy.deepcopy(self.pairs)
        divider_packets = [[[2]], [[6]]]
        all_packets = [] + divider_packets
        for pair in pairs:
            all_packets.append(pair[0])
            all_packets.append(pair[1])

        sorted_packets = sorted(all_packets, reverse=True, key=functools.cmp_to_key(self.compare))

        decoder_key = 1

        for i, pair in enumerate(sorted_packets):
            if pair == divider_packets[0] or pair == divider_packets[1]:
                decoder_key *= i + 1
        print(f"What is the decoder key for the distress signal? {decoder_key}")


if __name__ == "__main__":
    obj = Day13()
    obj.run()
