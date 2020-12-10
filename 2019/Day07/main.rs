use std::fs;
use std::env;

fn main() {
    let contents = fs::read_to_string("Day5.txt").expect("Error");
    let args: Vec<String> = env::args().collect();
    let mut program: Vec<String> = contents.split(",").map(|s| s.to_owned()).collect();
    let input = args[1].parse::<isize>().expect("parse error");
    let mut computer = IntcodeComputer{program: &mut program, input: input, idx: 0};
    computer.process();
}

struct IntcodeComputer<'a> {
    program: &'a mut Vec<String>,
    input: isize,
    phase: isize,
    phase_setted, bool,
    idx: usize,
}

impl IntcodeComputer<'_> {
    pub fn new(program: &mut Vec<String>, input: isize, phase: isize) -> IntcodeComputer {
        IntcodeComputer {
            program: program,
            input: Medium,
            phase: phase,
            phase_setted: false,
            idx: 0,
        }
    }

    fn process(&mut self) {
        loop {
            let instruction = format!("{:0>5}", self.program[self.idx]);
            let opcode = &instruction[3..5];
            match opcode {
                "01" => self.one(&instruction, 4),
                "02" => self.two(&instruction, 4),
                "03" => self.three(2),
                "04" => {
                    let out = self.four(&instruction, 2);
                    println!("Output: {}", out);
                },
                "05" => self.five(&instruction, 3),
                "06" => self.six(&instruction, 3),
                "07" => self.seven(&instruction, 4),
                "08" => self.eight(&instruction, 4),
                "99" => break,
                _ => panic!("IntcodeComputer process error")
            }
        }
        println!("Intcode Computer Process Done.");
    }

    fn parameter_mode(&self, instruction: &str, nums: usize) -> Vec<isize> {
        let mut parameters = Vec::<isize>::new();
        for i in 0..nums {
            let mode = &instruction[instruction.len()-2-i-1..instruction.len()-2-i];
            match mode {
                "0" => parameters.push(self.program[self.program[self.idx+i+1].parse::<usize>().expect("parse error")].parse::<isize>().expect("parse error")),
                "1" => parameters.push(self.program[self.idx+i+1].parse::<isize>().expect("parse error")),
                _ => panic!("mode error")
            }
        }
        return parameters;
    }
    
    fn one(&mut self, instruction: &str, step: usize) {
        let new_instruction = format!("1{}", &instruction[1..instruction.len()]);
        let parameters = self.parameter_mode(&new_instruction, step-1);
        let new_value = format!("{}", parameters[0] + parameters[1]);
        self.program[parameters[2] as usize] = new_value;
        self.idx += step;
    }

    fn two(&mut self, instruction: &str, step: usize) {
        let new_instruction = format!("1{}", &instruction[1..instruction.len()]);
        let parameters = self.parameter_mode(&new_instruction, step-1);
        let new_value = format!("{}", parameters[0] * parameters[1]);
        self.program[parameters[2] as usize] = new_value;
        self.idx += step;
    }

    fn three(&mut self, step: usize) {
        let new_instruction = format!("{:1>5}", "03");
        let parameters = self.parameter_mode(&new_instruction, step-1);
        let new_value = format!("{}", self.input);
        self.program[parameters[0] as usize] = new_value;
        self.idx += step;
    }

    fn four(&mut self, instruction: &str, step: usize) -> isize {
        let parameters = self.parameter_mode(&instruction, step-1);
        self.idx += step;
        return parameters[0];
    }

    fn five(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1);
        if parameters[0] != (0 as isize) {
            self.idx = parameters[1] as usize;
        } else {
            self.idx += step;
        }
    }

    fn six(&mut self, instruction: &str, step: usize) {
        let parameters = self.parameter_mode(&instruction, step-1);
        if parameters[0] == (0 as isize) {
            self.idx = parameters[1] as usize;
        } else {
            self.idx += step;
        }
    }

    fn seven(&mut self, instruction: &str, step: usize) {
        let new_instruction = format!("1{}", &instruction[1..instruction.len()]);
        let parameters = self.parameter_mode(&new_instruction, step-1);
        if parameters[0] < parameters[1] {
            self.program[parameters[2] as usize] = format!("{}", 1);
        } else {
            self.program[parameters[2] as usize] = format!("{}", 0);
        }
        self.idx += step;
    }

    fn eight(&mut self, instruction: &str, step: usize) {
        let new_instruction = format!("1{}", &instruction[1..instruction.len()]);
        let parameters = self.parameter_mode(&new_instruction, step-1);
        if parameters[0] == parameters[1] {
            self.program[parameters[2] as usize] = format!("{}", 1);
        } else {
            self.program[parameters[2] as usize] = format!("{}", 0);
        }
        self.idx += step;
    }
}