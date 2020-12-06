use std::fs;

fn main() {
    let contents = fs::read_to_string("Day2.txt").expect("Error");
    let input: Vec<usize> = contents.split(",").map(|s| s.parse::<usize>().expect("parse error")).collect();
    let mut initialed_input = initial(&mut input.clone(), 12, 2);
    let result = intcode_computer(&mut initialed_input);
    println!("Result: {}", result);

    'outer: for noun in 0..100 {
        '_inner: for verb in 0..100 {
            let mut initialed = initial(&mut input.clone(), noun, verb);
            if intcode_computer(&mut initialed) == 19690720 {
                println!("Result2: {}", 100 * noun + verb);
                break 'outer;
            }
        }
    }

}

fn intcode_computer(program: &mut Vec<usize>) -> usize {
    let mut pos = 0;
    while program[pos] != 99 {
        let dest = program[pos+3];
        if program[pos] == 1 {
            program[dest] = program[program[pos+1]] + program[program[pos+2]];
        } else if program[pos] == 2 {
            program[dest] = program[program[pos+1]] * program[program[pos+2]];
        }
        pos += 4;
    }
    return program[0];
}

fn initial (program: &mut Vec<usize>, noun: usize, verb: usize) -> Vec<usize> {
    program[1] = noun;
    program[2] = verb;
    return program.to_vec();
}