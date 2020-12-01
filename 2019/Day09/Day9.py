class amplifier(object):
    def __init__(self, phase):
        with open('Day9.txt', 'r') as f:
            self.data = f.read()
        # self.data = """109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"""
        # self.data = """1102,34915192,34915192,7,4,7,99,0"""
        # self.data = """104,1125899906842624,99"""
        self.data = self.data.split(',').copy()
        self.data = [int(d.replace('\n', '')) for d in self.data]
        extent = [0]*(len(self.data)*99)
        # self.data.append(0)
        self.data.extend(extent)
        # print(self.data)
        self.index = 0
        self.inputs = [phase]
        self.last_output = 0
        self.relative_base = 0

    def incode_computer(self):
        while True:
            # print(self.data[self.index])
            instruction = '%05d' % self.data[self.index]
            # print(instruction)
            opcode = int(instruction[3:5])    
            parameter_1_mode = int(instruction[2])
            parameter_2_mode = int(instruction[1])
            parameter_3_mode = int(instruction[0])
            if opcode != 99:
                if parameter_1_mode == 1 and opcode != 3:
                    parameter_1 = self.data[self.index + 1]
                elif parameter_1_mode == 2 and opcode != 3:
                    parameter_1 = self.data[self.data[self.index + 1] + self.relative_base]                
                elif opcode == 3 and parameter_1_mode == 2:
                    parameter_1 = self.data[self.index + 1] + self.relative_base
                elif opcode == 3 and parameter_1_mode != 2:
                    parameter_1 = self.data[self.index + 1]
                else:
                    parameter_1 = self.data[self.data[self.index + 1]]
                    
                if opcode != 4 and opcode != 3 and opcode != 9:
                    if parameter_2_mode == 1:
                        parameter_2 = self.data[self.index + 2]
                    elif parameter_2_mode == 2:
                        parameter_2 = self.data[self.data[self.index + 2] + self.relative_base]
                    else:
                        parameter_2 = self.data[self.data[self.index + 2]]
            if parameter_3_mode == 2:
                parameter_3 = self.data[self.index+3] + self.relative_base
            else:
                parameter_3 = self.data[self.index+3]
            if opcode == 1:
                self.data[parameter_3] = parameter_1 + parameter_2
                self.index += 4
            elif opcode == 2:
                self.data[parameter_3] = parameter_1 * parameter_2
                self.index += 4
            elif opcode == 3:
                # TODO
                if len(self.inputs) != 0:
                    self.data[parameter_1] = self.inputs.pop(0)
                else:
                    return 'wait'
                self.index += 2
            elif opcode == 4:
                self.index += 2
                self.last_output = parameter_1
                # if parameter_1 != 0:
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
                    self.data[parameter_3] = 1
                else:
                    self.data[parameter_3] = 0
                self.index += 4
            elif opcode == 8:
                if parameter_1 == parameter_2:
                    self.data[parameter_3] = 1
                else:
                    self.data[parameter_3] = 0
                self.index += 4
            elif opcode == 9:
                self.relative_base += parameter_1
                self.index += 2
            elif opcode == 99:
                self.index += 1
                return None

a = amplifier(2)
while True:
    r = a.incode_computer()
    print(r)
    if not r:
        break
