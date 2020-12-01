with open('Day1.txt', 'r') as f:
    data = f.read()
data = data.split('\n')
data = [int(d) for d in data]

# Part 1
total_fuel = 0
for d in data:
    need_fuel = int(d // 3.0)-2
    total_fuel += need_fuel
        
print(total_fuel)

# Part 2
total_fuel = 0
for d in data:
    need_fuel = int(d // 3.0)-2
    while need_fuel > 0:
        total_fuel += need_fuel
        need_fuel = int(need_fuel // 3.0)-2
        
print(total_fuel)

