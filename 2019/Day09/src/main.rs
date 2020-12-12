use std::fs;

fn main() {
    let contents = fs::read_to_string("Day9.txt").expect("Error");
    let program: Vec<String> = contents.split(",").map(|s| s.to_owned()).collect();
    let mut computer = IntcodeComputer::new(program.clone(), 1);
    computer.phase_setted = true;
    computer.process(1);
    println!("Result: {}", computer.output.last().unwrap());

    let mut computer2 = IntcodeComputer::new(program.clone(), 1);
    computer2.phase_setted = true;
    computer2.process(2);
    println!("Result: {}", computer2.output.last().unwrap());
}

struct IntcodeComputer {
    program: Vec<String>,
    input: isize,
    phase: isize,
    phase_setted: bool,
    idx: usize,
    output: Vec<i128>,
    halt: bool,
    relative_base: i128
}

impl IntcodeComputer {
    pub fn new(program: Vec<String>, phase: isize) -> IntcodeComputer {
        let mut new_program = program.clone();
        new_program.resize(program.len()*100, "0".to_string());
        IntcodeComputer {
            program: new_program,
            input: 0,
            phase: phase,
            phase_setted: false,
            idx: 0,
            output: Vec::<i128>::new(),
            halt: false,
            relative_base: 0
        }
    }

    fn process(&mut self, input: isize) {
        self.input = input;
        loop {
            let instruction = format!("{:0>5}", self.program[self.idx]);
            let opcode = &instruction[3..5];
            match opcode {
                "01" => self.one(&instruction, 4),
                "02" => self.two(&instruction, 4),
                "03" => self.three(&instruction, 2),
                "04" => {
                    let out = self.four(&instruction, 2);
                    self.output.push(out);
                    break;
                },
                "05" => self.five(&instruction, 3),
                "06" => self.six(&instruction, 3),
                "07" => self.seven(&instruction, 4),
                "08" => self.eight(&instruction, 4),
                "09" => self.nine(&instruction, 2),
                "99" => {
                    self.halt = true;
                    break;
                }
                _ => panic!("IntcodeComputer process error")
            }
        }
    }

    fn parameter_mode(&self, instruction: &str, nums: usize, write: bool) -> Vec<i128> {
        let mut parameters = Vec::<i128>::new();
        for i in 0..nums {
            let mut mode = &instruction[instruction.len()-2-i-1..instruction.len()-2-i];
            if write && i == nums-1 && mode == "0" {
                mode = "1";
            } else if write && i == nums-1 && mode == "2" {
                mode = "3";
            } 
            match mode {
                "0" => parameters.push(self.program[self.program[self.idx+i+1].parse::<i128>().expect("parse error") as usize].parse::<i128>().expect("parse error")),
                "1" => parameters.push(self.program[self.idx+i+1].parse::<i128>().expect("parse error")),
                "2" => parameters.push(self.program[(self.program[self.idx+i+1].parse::<i128>().expect("parse error")+self.relative_base) as usize].parse::<i128>().expect("parse error")),
                "3" => parameters.push(self.program[self.idx+i+1].parse::<i128>().expect("parse error")+self.relative_base),
                _ => panic!("mode error")
            }
        }
        return parameters;
    }
    
    fn one(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, true);
        let new_value = format!("{}", parameters[0] + parameters[1]);
        self.program[parameters[2] as usize] = new_value;
        self.idx += step;
    }

    fn two(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, true);
        let new_value = format!("{}", parameters[0] * parameters[1]);
        self.program[parameters[2] as usize] = new_value;
        self.idx += step;
    }

    fn three(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, true);
        let new_value;
        if self.phase_setted {
            new_value = format!("{}", self.input);
        } else {
            new_value = format!("{}", self.phase);
            self.phase_setted = true;
        }
        self.program[parameters[0] as usize] = new_value;
        self.idx += step;
    }

    fn four(&mut self, instruction: &str, step: usize) -> i128 {
        let parameters = self.parameter_mode(&instruction, step-1, false);
        self.idx += step;
        return parameters[0];
    }

    fn five(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, false);
        if parameters[0] != (0 as i128) {
            self.idx = parameters[1] as usize;
        } else {
            self.idx += step;
        }
    }

    fn six(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, false);
        if parameters[0] == (0 as i128) {
            self.idx = parameters[1] as usize;
        } else {
            self.idx += step;
        }
    }

    fn seven(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, true);
        if parameters[0] < parameters[1] {
            self.program[parameters[2] as usize] = format!("{}", 1);
        } else {
            self.program[parameters[2] as usize] = format!("{}", 0);
        }
        self.idx += step;
    }

    fn eight(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, true);
        if parameters[0] == parameters[1] {
            self.program[parameters[2] as usize] = format!("{}", 1);
        } else {
            self.program[parameters[2] as usize] = format!("{}", 0);
        }
        self.idx += step;
    }

    fn nine(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1, false);
        self.relative_base += parameters[0];
        self.idx += step;
    }
}