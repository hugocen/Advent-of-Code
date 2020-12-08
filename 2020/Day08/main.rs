use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let result = game_console(contents.lines().collect());
    println!("Result: {}", result.accumulator);
    let result2 = debug(contents.lines().collect());
    println!("Result2: {}", result2);
}

struct Console {
    accumulator: isize,
    idx: isize
}

fn game_console(instructions: Vec<&str>) -> Console {
    let mut program = Console {accumulator: 0, idx: 0};
    let mut set = HashSet::new();

    while !set.contains(&program.idx) && program.idx < instructions.len() as isize {
        let instruction: Vec<&str> = instructions[program.idx as usize].split_whitespace().collect();
        set.insert(program.idx);
        if instruction[0] == "acc" {
            program.accumulator += &instruction[1].parse::<isize>().expect("parse error");
            program.idx += 1;
        } else if instruction[0] == "jmp" {
            program.idx += &instruction[1].parse::<isize>().expect("parse error");
        } else if instruction[0] == "nop" {
            program.idx += 1;
        } 
    }
    return program;
}

fn debug(instructions: Vec<&str>) -> isize {
    for i in 0..instructions.len() {
        let instruction: Vec<&str> = instructions[i].split_whitespace().collect();
        if instruction[0] == "jmp" {
            let result = debug_process(&instructions, i, "nop", instruction[1]);
            if result.idx as usize == instructions.len() {
                return result.accumulator;
            }
        } else if instruction[0] == "nop" {
            let result = debug_process(&instructions, i, "jmp", instruction[1]);
            if result.idx as usize == instructions.len() {
                return result.accumulator;
            }
        }
    }
    return 0 as isize;
}

fn debug_process(instructions: &Vec<&str>, idx: usize, instruct: &str, values: &str) -> Console {
    let mut new_instructions = instructions.clone();
    let new_instruction = format!("{} {}", instruct, values);
    new_instructions[idx] = &new_instruction;
    return game_console(new_instructions);
}