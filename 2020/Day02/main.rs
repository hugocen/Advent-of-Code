use std::fs;

fn main() {

    let contents = fs::read_to_string("input.txt").expect("Error");

    let lines = contents.lines();

    let mut result = 0;
    let mut result2 = 0;

    for line in lines {
        let data: Vec<&str> = line.split(":").collect();
        let pwd: Vec<char> = data[1].chars().collect();
        let rule: Vec<&str> = data[0].split_whitespace().collect();
        let target: Vec<char> = rule[1].chars().collect();
        let start_end: Vec<usize> = rule[0].split("-").map(|s| s.parse::<usize>().expect("parse error")).collect();
        // println!("start={},end={}", start_end[0], start_end[1]);
        let mut count = 0;
        for c in &pwd { 
            if *c == target[0] {
                count += 1;
            }
        }

        if count >= start_end[0] &&  count <= start_end[1] {
            result += 1;
        }

        if (pwd[start_end[0]] == target[0] || pwd[start_end[1]] == target[0]) && pwd[start_end[0]] != pwd[start_end[1]] {
            result2 += 1;
        }
    }

    println!("Result: {}", result);
    println!("Result2: {}", result2);
}
