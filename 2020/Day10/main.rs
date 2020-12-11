use std::fs;

fn main() {
    let contents = fs::read_to_string("Inputs.txt").expect("Error");
    let mut adapters: Vec<i128> = contents.split_whitespace().map(|s| s.parse::<i128>().expect("parse error")).collect();
    adapters.sort();
    let mut jolts = 0 as i128;
    let mut idx = 0;
    let mut one_jolt = 0;
    let mut three_jolt = 0;

    while idx < adapters.len() {
        let difference = adapters[idx] - jolts;
        match difference {
            1 => one_jolt += 1,
            2 => {},
            3 => three_jolt += 1,
            _ => {
                println!("Adapters not supported!");
                break;
            }
        }
        jolts = adapters[idx];
        idx += 1;
    }
    // count your own device
    three_jolt += 1;

    let result = one_jolt * three_jolt;
    println!("Result: {}", result);
    let result2 = dp(&adapters);
    println!("Result2: {}", result2);
}

fn dp(adapters: &Vec<i128>) -> i128 {
    let mut adapters_clone = adapters.clone();
    adapters_clone.insert(0, 0);
    let mut dp_adapters = vec![0 as i128; adapters_clone.len()];
    dp_adapters[0] = 1;
    for i in 1..dp_adapters.len() {
        let mut sum = 0;
        let mut idx = (i as isize) - 3;
        if idx < 0 {
            idx = 0;
        }
        for j in idx as usize..i {
            if (adapters_clone[i] - adapters_clone[j]) <= 3 {
                sum += dp_adapters[j];
            }
        }
        dp_adapters[i] = sum;
    }
    return dp_adapters[dp_adapters.len()-1]
}