with open('Day2.txt', 'r') as f:
    data = f.read()
data = data.split(',')
data = [int(d) for d in data]

data[1] = 12
data[2] = 2

# Part 1
index = 0 
while data[index] != 99:
    if data[index] == 1:
        data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
    elif data[index] == 2:
        data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
    index += 4

print(data[0])

# Part 2
for noun in range(100):
    for verb in range(100):
        with open('Day2.txt', 'r') as f:
            data = f.read()
        data = data.split(',')
        data = [int(d) for d in data]
        data[1] = noun
        data[2] = verb
        index = 0 
        while data[index] != 99:
            if data[index] == 1:
                data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
            elif data[index] == 2:
                data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
            index += 4
        if data[0] == 19690720:
            print(100 * noun + verb)
            break
