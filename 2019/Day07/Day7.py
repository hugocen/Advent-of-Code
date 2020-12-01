from itertools import permutations 

# print(list(permutations([0,1,2,3,4], 5)))
class amplifier(object):
    def __init__(self, phase):
        with open('Day7.txt', 'r') as f:
            self.data = f.read()
        # self.data = """3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
        #               -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
        #               53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"""
        # self.data = """3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
        #                 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"""
        self.data = self.data.split(',').copy()
        self.data = [int(d.replace('\n', '')) for d in self.data]
        self.index = 0
        self.inputs = [phase]
        self.last_output = 0

    def incode_computer(self):
        while True:
            instruction = '%05d' % self.data[self.index]
            # print(instruction)
            opcode = int(instruction[3:5])    
            parameter_1_mode = int(instruction[2])
            parameter_2_mode = int(instruction[1])
            # parameter_3_mode = int(instruction[0])
            if opcode != 99:
                if parameter_1_mode:
                    parameter_1 = self.data[self.index+1]
                else:
                    parameter_1 = self.data[self.data[self.index+1]]
                if opcode != 4 and opcode != 3:
                    if parameter_2_mode:
                        parameter_2 = self.data[self.index+2]
                    else:
                        parameter_2 = self.data[self.data[self.index+2]]
            # if parameter_3_mode:
            #     parameter_3 = data[self.index+3]
            # else:
            #     parameter_3 = data[data[self.index+3]]
            if opcode == 1:
                self.data[self.data[self.index+3]] = parameter_1 + parameter_2
                self.index += 4
            elif opcode == 2:
                self.data[self.data[self.index+3]] = parameter_1 * parameter_2
                self.index += 4
            elif opcode == 3:
                # TODO
                if len(self.inputs) != 0:
                    self.data[self.data[self.index+1]] = self.inputs.pop(0)
                else:
                    return 'wait'
                self.index += 2
            elif opcode == 4:
                self.index += 2
                self.last_output = parameter_1
                if parameter_1 != 0:
                    return(parameter_1)
            elif opcode == 5:
                if parameter_1 != 0:
                    self.index = parameter_2
                else:
                    self.index += 3
            elif opcode == 6:
                if parameter_1 == 0:
                    self.index = parameter_2
                else:
                    self.index += 3
            elif opcode == 7:
                if parameter_1 < parameter_2:
                    self.data[self.data[self.index+3]] = 1
                else:
                    self.data[self.data[self.index+3]] = 0
                self.index += 4
            elif opcode == 8:
                if parameter_1 == parameter_2:
                    self.data[self.data[self.index+3]] = 1
                else:
                    self.data[self.data[self.index+3]] = 0
                self.index += 4
            elif opcode == 99:
                self.index += 1
                return None



total_signals = []
for comb in list(permutations([5,6,7,8,9], 5)):
    signals = []
    # comb = [9,7,8,5,6]
    # comb = [9,8,7,6,5]
    # print(comb)
    amplifiers = [amplifier(c) for c in comb]
    amplifiers[0].inputs.append(0)
    i = 0
    while True:
        # print(i, amplifiers[i].inputs)
        signals.append(amplifiers[i].inputs[-1])
        r = amplifiers[i].incode_computer()
        i += 1
        i %= 5
        if r != 'wait' and  r != None:
            amplifiers[i].inputs.append(r)
        elif r == 'wait':
            amplifiers[i].inputs.append(amplifiers[i-1].last_output)
        elif r == None:
            break
    total_signals.append(signals[-1])
print(max(total_signals))
