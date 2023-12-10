class Pipe:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.main_loop = False
        self.enclosed = False
        self.right = False
        self.down = False
        self.left = False
        self.up = False

    def __repr__(self):
        return f"{self.x} {self.y} {self.shape}"

    def convert_starting_point(self):
        if self.right:
            if self.left:
                self.shape = "-"
            elif self.up:
                self.shape = "L"
            elif self.down:
                self.shape = "F"
        elif self.left:
            if self.up:
                self.shape = "J"
            elif self.down:
                self.shape = "7"
        else:
            self.shape = "|"

    def next(self, previous_x, previous_y):
        if self.shape == "|":
            return self.vertical(previous_x, previous_y)
        elif self.shape == "-":
            return self.horizontal(previous_x, previous_y)
        elif self.shape == "L":
            return self.l_shape(previous_x, previous_y)
        elif self.shape == "J":
            return self.j_shape(previous_x, previous_y)
        elif self.shape == "7":
            return self.seven_shape(previous_x, previous_y)
        elif self.shape == "F":
            return self.f_shape(previous_x, previous_y)
        elif self.shape == "S":
            return self.x, self.y
        else:
            return None

    def vertical(self, x, y):
        if y == self.y - 1:
            return self.x, self.y + 1
        else:
            return self.x, self.y - 1

    def horizontal(self, x, y):
        if x == self.x - 1:
            return self.x + 1, self.y
        else:
            return self.x - 1, self.y

    def l_shape(self, x, y):
        if y == self.y - 1:
            return self.x + 1, self.y
        else:
            return self.x, self.y - 1

    def j_shape(self, x, y):
        if y == self.y - 1:
            return self.x - 1, self.y
        else:
            return self.x, self.y - 1

    def seven_shape(self, x, y):
        if x == self.x - 1:
            return self.x, self.y + 1
        else:
            return self.x - 1, self.y

    def f_shape(self, x, y):
        if x == self.x + 1:
            return self.x, self.y + 1
        else:
            return self.x + 1, self.y
