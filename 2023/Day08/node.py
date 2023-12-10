class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.name} {self.left} {self.right}"

    def go_left(self):
        return self.left

    def go_right(self):
        return self.right
