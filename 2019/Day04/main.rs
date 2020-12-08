use std::fs;

struct Data <'a> {
    nums: &'a str,
    last_n: usize,
    double: bool
}

fn main () {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let inputs: Vec<usize> = contents.split("-").map(|s| s.parse::<usize>().expect("parse error")).collect();
    let data = Data{nums: "", last_n: 0, double: false};
    let result = dfs(data, &inputs);
    println!("Result: {}", result);
}

fn dfs (data: Data, inputs: &Vec<usize>) -> usize {
    if data.nums.len() == 6 {
        let data_num = data.nums.parse::<usize>().expect("parse error");
        if data.double && data_num >= inputs[0] && data_num <= inputs[1] {
            return 1;
        } else {
            return 0;
        }
    } else {
        let mut sums = 0;
        for i in data.last_n..10 {
            let new_nums = format!("{}{}", data.nums, i);
            let mut new_double = data.nums.len()>0 && i==data.last_n;
            if data.double {
                new_double = data.double;
            }
            let new_data = Data {nums: &new_nums, last_n: i, double: new_double};
            sums += dfs(new_data, inputs);
        }
        return sums;
    }
}