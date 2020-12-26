use std::fs;
use std::collections::{HashSet, HashMap};

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let lines: Vec<isize> = contents.lines().map(|s| s.parse::<isize>().unwrap()).collect();
    let card_pkey = lines[0].clone();
    let door_pkey = lines[1].clone();
    guessing(card_pkey, door_pkey);
}

fn process(subject_number: isize, loop_size: isize) -> isize {
    let mut val = 1;
    for _ in 0..loop_size {
        val *= subject_number;
        val %= 20201227;
    }
    return val;
}

fn guessloop(pkey: isize, subject_number: isize) -> isize {
    let mut loop_size = 1 as isize;
    let mut val = 1;
    // let mut loop_seen = HashSet::new();
    loop {
        val *= subject_number;
        val %= 20201227;
        // println!("key: {}", key);
        if val == pkey {
            return loop_size;
        }
        loop_size += 1;
    }
}

fn guessing(card_pkey: isize, door_pkey: isize) {
    let subject_number = 7 as isize;
    let cardloop;
    let doorloop;
    
    cardloop = guessloop(card_pkey, subject_number);
    println!("card's loop: {}", cardloop);
    doorloop = guessloop(door_pkey, subject_number);
    println!("door's loop: {}", doorloop);

    println!("subject number: {}, card's loop: {}, door's loop: {}", subject_number, cardloop, doorloop);


    let result = process(card_pkey, doorloop);
    println!("Encryption Key: {}", result);
    let result = process(door_pkey, cardloop);
    println!("Encryption Key: {}", result);
}