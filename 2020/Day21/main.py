with open("inputs.txt", "r") as f:
    input_list = f.readlines()

d = {}
for i in input_list:
    allerg = i.split(" (contains ")[1][:-1].replace(")", "").split(", ")
    ingred = i.split(" (contains ")[0].split(" ")
    for a in allerg:
        s = d.get(a, False)
        if s:
            s &= set(ingred)
            d[a] = s
        else:
            d[a] = set(ingred)
f = set()
for i in d.values():
    f |= i
p1 = 0
print(d)
print(f)

for i in input_list:
    ingred = set(i.split(" (contains ")[0].split(" "))
    p1 += len(ingred - f)

print(f"Solution to Part 1 is {p1}")
new_dict = {}
for k, v in d.items():
    if len(v) == 1:
        single_item = v
        new_dict[k] = v

while True:
    new_set = set()
    for k, v in d.items():
        d[k] = v - single_item
        if len(d[k]) == 1:
            new_set |= d[k]
            new_dict[k] = d[k]
    if sum([len(i) for i in (list(d.values()))]) == 0:
        break
    single_item = new_set
p2 = ",".join([i[1].pop() for i in sorted(list(new_dict.items()))])

print(f"Solution for Part2 is {p2}")