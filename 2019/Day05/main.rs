use std::fs;

fn main() {
    let contents = fs::read_to_string("Day5.txt").expect("Error");
    let mut input: Vec<String> = contents.split(",").map(|s| s.to_owned()).collect();
    let mut computer = IntcodeComputer{program: &mut input, input: 1 as isize, idx: 0};
    computer.process();
    // let result = intcode_computer(&mut initialed_input);
    // println!("Result: {}", result);
}

struct IntcodeComputer<'a> {
    program: &'a mut Vec<String>,
    input: isize,
    idx: usize,
    // outputs: &'a mut Vec<isize>
}

impl IntcodeComputer<'_> {
    fn process(&mut self) {
        loop {
            let instruction = format!("{:0>5}", self.program[self.idx]);
            // println!("instruction: {}", instruction);
            let opcode = &instruction[3..5];
            // println!("opcode: {}, idx: {}, instruction:{}", opcode, self.idx, self.program[self.idx]);
            match opcode {
                "01" => self.one(&instruction, 4),
                "02" => self.two(&instruction, 4),
                "03" => self.three(2),
                "04" => {
                    let out = self.four(&instruction, 2);
                    println!("Output: {}", out);
                    // self.outputs.push(out);
                },
                "99" => break,
                _ => panic!("IntcodeComputer process error")
            }
        }
    }

    fn parameter_mode(&self, instruction: &str, nums: usize) -> Vec<isize> {
        let mut parameters = Vec::<isize>::new();
        // println!("instruction: {}", instruction);
        for i in 0..nums {
            let mode = &instruction[instruction.len()-2-i-1..instruction.len()-2-i];
            // println!("para idx: {}", self.idx+i+1);
            // println!("mode: {}", mode);
            // println!("parameter: {}", self.program[self.idx+i+1]);
            // println!("parse parameter: {}", self.program[self.idx+i+1].parse::<isize>().expect("parse error"));
            // println!("parse parameter2: {}", self.program[self.program[self.idx+i+1].parse::<usize>().expect("parse error")].parse::<isize>().expect("parse error"));
            match mode {
                "0" => parameters.push(self.program[self.program[self.idx+i+1].parse::<usize>().expect("parse error")].parse::<isize>().expect("parse error")),
                "1" => parameters.push(self.program[self.idx+i+1].parse::<isize>().expect("parse error")),
                _ => panic!("mode error")
            }
        }
        // println!("{:?}", parameters);
        return parameters;
    }
    
    fn one(&mut self, instruction: &str, step: usize) {
        let new_instruction = format!("1{}", &instruction[1..instruction.len()]);
        let parameters = self.parameter_mode(&new_instruction, 3);
        let new_value = format!("{}", parameters[0] + parameters[1]);
        // println!("new_value: {}, parameters[2]: {}", &new_value, parameters[2]);
        self.program[parameters[2] as usize] = new_value;
        self.idx += step;
    }

    fn two(&mut self, instruction: &str, step: usize) {
        let new_instruction = format!("1{}", &instruction[1..instruction.len()]);
        let parameters = self.parameter_mode(&new_instruction, 3);
        let new_value = format!("{}", parameters[0] * parameters[1]);
        // println!("new_value: {}, parameters[2]: {}", &new_value, parameters[2]);
        self.program[parameters[2] as usize] = new_value;
        self.idx += step;
    }

    fn three(&mut self, step: usize) {
        let new_instruction = format!("{:1>5}", "03");
        let parameters = self.parameter_mode(&new_instruction, 1);
        let new_value = format!("{}", self.input);
        self.program[parameters[0] as usize] = new_value;
        self.idx += step;
    }

    fn four(&mut self, instruction: &str, step: usize) -> isize {
        let parameters = self.parameter_mode(&instruction, 1);
        self.idx += step;
        return parameters[0];
    }
}