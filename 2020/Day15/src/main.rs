use std::fs;
use std::collections::HashMap;

fn main() {
    let target = 30000000;
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let data: Vec<usize> = contents.split(",").map(|s| s.parse::<usize>().expect("parse error")).collect();
    let mut dic = HashMap::new();
    let mut idx = data.len();
    let mut val = data.last().unwrap().to_owned();
    for i in 0..data.len()-1 {
        dic.insert(data[i], i+1);
    }
    while idx < target {
        // println!("Idx: {}, Result: {}", idx, val);
        let new_val;
        if dic.contains_key(&val) {
            new_val = idx - dic[&val];
            dic.insert(val, idx);

        } else {
            new_val = 0;
            dic.insert(val, idx);
        }
        dic.insert(val, idx);
        val = new_val;
        idx += 1;
    }
    println!("Idx: {}, Result: {}", idx, val);
}
