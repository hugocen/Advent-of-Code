use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let mut dic = HashMap::<char, usize>::new();
    let mut people = 0;
    let mut result = 0;
    let mut result2 = 0;
    for line in contents.lines() {
        if line == "" {
            result += dic.len();
            for (_, val) in dic.iter() {
                if *val == people {
                    result2 += 1;
                }
            }
            dic.clear();
            people = 0;
        }
        else {
            people += 1;
            let ans: Vec<char> = line.chars().collect();
            for c in &ans {
                dic.insert(*c, dic.get(c).cloned().unwrap_or(0)+1);
            }
        }
    }    
    result += dic.len();
    for (_, val) in dic.iter() {
        if *val == people {
            result2 += 1;
        }
    }
    println!("Result: {}", result);
    println!("Result2: {}", result2);
}