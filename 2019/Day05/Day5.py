with open('Day5.txt', 'r') as f:
    data = f.read()
# data = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
data = data.split(',')
data = [int(d) for d in data]

input_num = 5

index = 0 
while True:
    instruction = '%05d' % data[index]
    # print(instruction)
    opcode = int(instruction[3:5])    
    parameter_1_mode = int(instruction[2])
    parameter_2_mode = int(instruction[1])
    # parameter_3_mode = int(instruction[0])
    if opcode != 99:
        if parameter_1_mode:
            parameter_1 = data[index+1]
        else:
            parameter_1 = data[data[index+1]]
        if opcode != 4 and opcode != 3:
            if parameter_2_mode:
                parameter_2 = data[index+2]
            else:
                parameter_2 = data[data[index+2]]
    # if parameter_3_mode:
    #     parameter_3 = data[index+3]
    # else:
    #     parameter_3 = data[data[index+3]]
    if opcode == 1:
        data[data[index+3]] = parameter_1 + parameter_2
        index += 4
    elif opcode == 2:
        data[data[index+3]] = parameter_1 * parameter_2
        index += 4
    elif opcode == 3:
        data[data[index+1]] = input_num
        index += 2
    elif opcode == 4:
        print(parameter_1)
        index += 2
    elif opcode == 5:
        if parameter_1 != 0:
            index = parameter_2
        else:
            index += 3
    elif opcode == 6:
        if parameter_1 == 0:
            index = parameter_2
        else:
            index += 3
    elif opcode == 7:
        if parameter_1 < parameter_2:
            data[data[index+3]] = 1
        else:
            data[data[index+3]] = 0
        index += 4
    elif opcode == 8:
        if parameter_1 == parameter_2:
            data[data[index+3]] = 1
        else:
            data[data[index+3]] = 0
        index += 4
    elif opcode == 99:
        break

