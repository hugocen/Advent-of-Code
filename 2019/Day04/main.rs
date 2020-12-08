use std::fs;

struct Data <'a> {
    nums: &'a str,
    last_n: usize,
    duplicate: usize,
    double: bool
}

fn main () {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let inputs: Vec<usize> = contents.split("-").map(|s| s.parse::<usize>().expect("parse error")).collect();
    let data = Data{nums: "", last_n: 0, duplicate: 0, double: false};
    let result = dfs(data, &inputs, false);
    println!("Result: {}", result);
    let data2 = Data{nums: "", last_n: 0, duplicate: 0, double: false};
    let result2 = dfs(data2, &inputs, true);
    println!("Result2: {}", result2);

}

fn dfs (data: Data, inputs: &Vec<usize>, p2: bool) -> usize {
    if data.nums.len() == 6 {
        let data_num = data.nums.parse::<usize>().expect("parse error");
        if data.double && data_num >= inputs[0] && data_num <= inputs[1] {
            return 1;
        } else {
            if p2 && data_num >= inputs[0] && data_num <= inputs[1] {
                if data.duplicate == 2 {
                    return 1;
                } else {
                    return 0;
                }
            } else {
                return 0;
            }
        }
    } else {
        let mut sums = 0;
        for i in data.last_n..10 {
            let new_nums = format!("{}{}", data.nums, i);
            let mut new_double = data.double;
            let mut new_duplicate = data.duplicate;
            if p2 {
                if i != data.last_n {
                    if data.duplicate == 2 {
                        new_double = true;
                    }
                    new_duplicate = 1;

                } else {
                    new_duplicate += 1;
                }
            } else {
                if !data.double {
                    new_double = data.nums.len()>0 && i==data.last_n;
                }
            }
            let new_data = Data {nums: &new_nums, last_n: i, duplicate: new_duplicate, double: new_double};
            sums += dfs(new_data, inputs, p2);
        }
        return sums;
    }
}