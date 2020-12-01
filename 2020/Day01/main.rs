use std::fs;
use std::collections::HashSet;

fn main() {
    let target: i32 = 2020;

    let mut dic = HashSet::<i32>::new();

    let contents = fs::read_to_string("input.txt").expect("Error");

    let vec: Vec<i32> = contents.split_whitespace().map(|s| s.parse::<i32>().expect("parse error")).collect();

    // let mut result = Vec::<i32>::new();

    let mut sums: i32 = 1;

    // for (pos, n) in vec.iter().enumerate() {
    for i in 0..vec.len() {
        let left = target - vec[i];
        if dic.contains(&left) {
            sums = sums * vec[i];
            sums = sums * left;
        }
        dic.insert(vec[i]);
    }

    println!("{}", sums);

    let mut ndic = HashSet::<i32>::new();
    let mut result = HashSet::new();

    let mut nsums: i128 = 1;
    for i in 0..vec.len() {
        for j in (i+1)..vec.len() {
            // println!("i = {} and j = {}", i, j);
            let left = target - vec[i] - vec[j];
            if ndic.contains(&left) {
                if !result.contains(&vec[i]) {
                    nsums = nsums * vec[i] as i128;
                    result.insert(vec[i]);
                }
                if !result.contains(&vec[j]) {
                    nsums = nsums * vec[j] as i128;
                    result.insert(vec[j]);
                }
                if !result.contains(&left) {
                    nsums = nsums * left as i128;
                    result.insert(left);
                }
            }
            ndic.insert(vec[j]);
        }
        ndic.insert(vec[i]);
    }

    println!("{}", nsums);
}