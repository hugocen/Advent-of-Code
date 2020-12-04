use std::fs;

fn main() {
    let contents = fs::read_to_string("Day1.txt").expect("Error");
    let mut sums = 0;
    let mut sums2 = 0;
    for line in contents.lines() {
        sums += fuel_module(line.parse::<usize>().unwrap());
        sums2 += fuel_module_recursive(line.parse::<i128>().unwrap());
    }
    println!("Result: {}", sums);
    println!("Result2: {}", sums2);
}

fn fuel_module(mass: usize) -> usize {
    return (mass / 3) - 2;
}

fn fuel_module_recursive(mass: i128) -> i128 {
    let fuel =  (mass / 3) - 2;
    if fuel > 0 {
        return fuel + fuel_module_recursive(fuel);
    } else {
        return 0;
    }
}