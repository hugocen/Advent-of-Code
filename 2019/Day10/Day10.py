import math
with open('Day10.txt', 'r') as f:
    data = f.read()
data = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""
data = [list(d) for d in data.split('\n')]
# print(data)
stars = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            stars.append([j, i])
# print(stars)

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def detect(tar, target):
    for t in stars:
        if t != tar and t != target:
            # if is_between(tar, t, target):
            #     return False
            if math.atan2(target[1]-tar[1], target[0]-tar[0]) == math.atan2(t[1]-tar[1], t[0]-tar[0]):
                if is_between(tar, t, target):
                    return False
            # if (tar[0] * (target[1] - t[1]) + target[0] * (t[1] - tar[1]) + t[0] * (tar[1] - target[1])) == 0:
            #     if (t[0]-tar[0]) < (target[0]-tar[0]) or (t[1]-tar[1]) < (target[1]-tar[1]):
            #         if (((t[0]-tar[0]) + (target[0]-tar[0])) ==  (target[0]-t[0])) and (((t[1]-tar[1]) + (target[1]-tar[1])) ==  (target[1]-t[1])):
            #             return False
    return True

max_detected = 0
for star in stars:
    detected = 0
    for s in stars:
        if s != star:
            if detect(star, s):
                detected += 1
    # print(star, detected)
    if detected > max_detected:
        max_detected = detected

print(len(stars))
print(max_detected)