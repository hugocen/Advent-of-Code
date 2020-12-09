use std::fs;
use std::cmp;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let data: Vec<isize> = contents.split_whitespace().map(|s| s.parse::<isize>().expect("parse error")).collect();
    let mut set = HashSet::new();
    let preamble = 25;
    let mut index = preamble;
    let mut flag = false;
    let result1;

    loop {
        for i in (index-preamble)..index {
            let rest = data[index] - data[i];
            if set.contains(&rest) {
                index += 1;
                set.clear();
                flag = true;
                break;
            } else {
                set.insert(&data[i]);
            }
        }
        if !flag {
            result1 = &data[index];
            break;
        } else {
            flag = false;
        }
    }
    println!("Result: {}", result1);

    for i in 0..data.len() {
        let mut sum = 0;
        let mut min = isize::MAX;
        let mut max = isize::MIN;
        for j in i..data.len() {
            sum += data[j];
            min = cmp::min(min, data[j]);
            max = cmp::max(max, data[j]);
            if &sum == result1 {
                println!("Result2: {}", min+max);
            } else if &sum > result1 {
                break;
            }
        }
    }
}