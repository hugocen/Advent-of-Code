with open('Day6.txt', 'r') as f:
    data = f.readlines()
data = [d.replace('\n', '') for d in data]

planet = {}

for d in data:
    d = d.split(')')
    planet[d[1]] = d[0]

count = 0
def find_orbit(obj):
    if obj in planet:
        global count
        count += 1
        find_orbit(planet[obj])

for p in planet:
    find_orbit(p)
print(count)

# traveled = []
def oribt_travel(obj, traveled):
    if obj in planet:
        traveled.append(planet[obj])
        oribt_travel(planet[obj], traveled)
    return traveled

you_traveled = oribt_travel('YOU', [])

def travel2target(obj, target, c):
    if obj in planet:        
        if obj != target:
            c += 1       
            c, obj = travel2target(planet[obj], target, c)
    return c, obj

# print(travel2target('YOU', 'MBY', 0))

total_traveled = []
for t in you_traveled:
    r = travel2target('SAN', t, 0)
    # print(r[1], r[0])
    if r[1] != 'SAN':
        total_traveled.append(r[0]+travel2target('YOU', r[1], 0)[0]-2)
print(min(total_traveled))