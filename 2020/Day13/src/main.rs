use std::fs;
use ring_algorithm::chinese_remainder_theorem;


fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let lines: Vec<&str> = contents.lines().collect();
    let target = lines[0].parse::<i128>().expect("parse error");
    let buses: Vec<&str> = lines[1].split(",").collect();
    let mut min_wait = i128::MAX;
    let mut result = 0;

    for i in 0..(buses.len()) {
        if buses[i] != "x" {
            let bus_id = buses[i].parse::<i128>().expect("parse error");
            let wait = bus_id - (target % bus_id);
            if wait < min_wait {
                min_wait = wait;
                result = wait * bus_id;
            }
        }        
    }
    println!("Result: {}", result);

    let mut new_buses = Vec::<i128>::new();
    let mut waits = Vec::<i128>::new();

    for i in 0..(buses.len()) {
        if buses[i] != "x" {
            let bus_id = buses[i].parse::<i128>().expect("parse error");
            new_buses.push(bus_id);
            waits.push((i as i128)*-1);
        }
    }
    let result2 = chinese_remainder_theorem::<i128>(&waits, &new_buses).unwrap();

    println!("Result2: {}", result2);
}
