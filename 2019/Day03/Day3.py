with open('Day3.txt', 'r') as f:
    data = f.readlines()

line1 = data[0].replace('\n', '').split(',')
line2 = data[1].split(',')


# Part 1
def walk(pos, direction, step, traveled):
    for _ in range(1, step+1):
        pos[direction[0]] += direction[1]
        traveled.append((pos[0], pos[1]))
    return traveled, pos

def travel(line):
    line_travel_points = []
    pos = [0, 0]
    for l in line:
        if l[0] == 'R':
            line_travel_points, pos = walk(pos, [1,1], int(l[1:]), line_travel_points)
        elif l[0] == 'L':
            line_travel_points, pos = walk(pos, [1,-1], int(l[1:]), line_travel_points)
        elif l[0] == 'U':
            line_travel_points, pos = walk(pos, [0,1], int(l[1:]), line_travel_points)
        elif l[0] == 'D':
            line_travel_points, pos = walk(pos, [0,-1], int(l[1:]), line_travel_points)
    return line_travel_points

line1_traveled = set(travel(line1))
line2_traveled = set(travel(line2))

intersection_points = line1_traveled.intersection(line2_traveled)

min_dist = float('inf')
for point in intersection_points:
    dist = abs(point[0]) + abs(point[1])
    if dist < min_dist:
        min_dist = dist
print(min_dist)

# Part 2
def walk_to(pos, direction, step, point):
    for s in range(1, step+1):
        # print(pos)
        pos[direction[0]] += direction[1]
        if pos == point:
            return True, s, pos
    return False, step, pos

def travel_to(line, point):
    pos = [0, 0]
    steps = 0
    for l in line:
        if l[0] == 'R':
            end, s, pos = walk_to(pos, [1,1], int(l[1:]), point)
        elif l[0] == 'L':
            end, s, pos = walk_to(pos, [1,-1], int(l[1:]), point)
        elif l[0] == 'U':
            end, s, pos = walk_to(pos, [0,1], int(l[1:]), point)
        elif l[0] == 'D':
            end, s, pos = walk_to(pos, [0,-1], int(l[1:]), point)
        steps += s
        if end:
            return steps

min_dist = float('inf')
for point in intersection_points:
    p = [point[0], point[1]]
    dist = travel_to(line1, p) + travel_to(line2, p)
    if dist < min_dist:
        min_dist = dist
print(min_dist)