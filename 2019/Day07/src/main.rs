use std::fs;
use std::cmp::max;
use itertools::Itertools;

fn main() {
    let contents = fs::read_to_string("Day7.txt").expect("Error");
    let mut program: Vec<String> = contents.split(",").map(|s| s.to_owned()).collect();
    let result1 = amplification_circuit(&mut program, 0..5, false);
    let result2 = amplification_circuit(&mut program, 5..10, true);
    println!("Result1: {}", result1);
    println!("Result2: {}", result2);
}

fn amplification_circuit(controller_software: &mut Vec<String>, range: std::ops::Range<isize>, feedback: bool) -> isize {
    let mut result = 0  as isize;
    let perms = range.permutations(5);
    for perm in perms {
        let mut amplifiers = Vec::<IntcodeComputer>::new();
        let mut input = 0 as isize;
        for phase in perm {
            let mut computer = IntcodeComputer::new(controller_software.clone(), phase);
            if !feedback {
                computer.halt = true;
            }
            amplifiers.push(computer);
        }
        loop {
            for i in 0..5 {
                amplifiers[i].process(input);
                input = amplifiers[i].output.last().unwrap().clone();
            }
            if amplifiers.last().unwrap().halt {
                break;
            }
        }
        result = max(result, amplifiers.last().unwrap().output.last().unwrap().clone());
    }
    return result;
}

struct IntcodeComputer {
    program: Vec<String>,
    input: isize,
    phase: isize,
    phase_setted: bool,
    idx: usize,
    output: Vec<isize>,
    halt: bool
}

impl IntcodeComputer {
    pub fn new(program: Vec<String>, phase: isize) -> IntcodeComputer {
        IntcodeComputer {
            program: program,
            input: 0,
            phase: phase,
            phase_setted: false,
            idx: 0,
            output: Vec::<isize>::new(),
            halt: false
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
                "03" => self.three(2),
                "04" => {
                    let out = self.four(&instruction, 2);
                    self.output.push(out);
                    break;
                },
                "05" => self.five(&instruction, 3),
                "06" => self.six(&instruction, 3),
                "07" => self.seven(&instruction, 4),
                "08" => self.eight(&instruction, 4),
                "99" => {
                    self.halt = true;
                    break;
                }
                _ => panic!("IntcodeComputer process error")
            }
        }
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