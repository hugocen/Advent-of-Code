use std::fs;
use std::collections::HashMap;
use itertools::Itertools;
use std::thread;
use std::sync::{Arc, Mutex};

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let mut data = HashMap::new();
    let mut data2 = HashMap::new();
    let mut mask = "".to_owned();
    let mut mask2 = "".to_owned();

    for line in contents.lines() {
        let sen: Vec<&str> = line.split(" = ").collect();
        
        if sen[0] == "mask" {
            // println!("{}", &sen[1]);
            let new_mask = format!("{:X>64}", &sen[1]);
            let new_mask2 = format!("{:0>64}", &sen[1]);
            mask = new_mask.to_owned();
            mask2 = new_mask2.to_owned();
            println!("{}", mask2);
        } else {
            let idx = sen[0][4..sen[0].len()-1].parse::<u64>().expect("parse error");
            let value = sen[1].parse::<u64>().expect("parse error");
            let m_val = bitmask(mask.clone(), value);
            data.insert(idx, m_val);
            let idxs = address_mask(mask2.clone(), idx);
            for id in idxs {
                data2.insert(id, value);
            }
        }
    }
    let mut result = 0;
    for (_, v) in data.iter() {
        result += v; 
    }
    println!("Result: {}", result);

    let mut result2 = 0;
    for (_, v) in data2.iter() {
        result2 += v; 
    }
    println!("Result: {}", result2);
}

fn bitmask(mask: String, value: u64) -> u64 {
    let mask_string: Vec<char> = mask.chars().collect();
    let val_bits = format!("{:b}", value);
    let mut val_string: Vec<char> = format!("{:0>64}", val_bits).chars().collect();
    // println!("{}", mask);
    for i in 0..64 {
        if mask_string[i] != 'X' {
            val_string[i] = mask_string[i];
        }
    }
    let val_masked: String = val_string.into_iter().collect();
    let m_value = u64::from_str_radix(&val_masked, 2).unwrap();
    // println!("{}", m_value);
    return m_value;
}

fn address_mask(mask: String, address: u64) -> Vec<u64> {
    // let mut addresses = Vec::new();
    let mut addresses = Arc::new(Mutex::new(vec![]));
    let mask_string: Vec<char> = mask.chars().collect();
    let address_bits = format!("{:b}", address);
    let mut address_string: Vec<char> = format!("{:0>64}", address_bits).chars().collect();

    let mut floating = 0;

    for i in 0..64 {
        match mask_string[i] {
            'X' => {
                address_string[i] = 'X';
                floating += 1
            },
            '0' => {},
            '1' => address_string[i] = '1',
            _ => panic!("error"),
        }
    }
    let mut nums = vec!['1'; floating];
    nums.resize(floating*2, '0');
    // let perms = nums.iter().permutations(floating);
    let handle =thread::spawn({
        let clone = Arc::clone(&addresses);
        move || {
        let perms = nums.iter().permutations(floating);
        for perm in perms {
        let mut new_address = address_string.clone();
        let mut p = 0;
        for i in 0..64 {
            if new_address[i] == 'X' {
                new_address[i] = perm[p].clone();
                p += 1;
            }
        }
        let addresses_masked: String = new_address.into_iter().collect();
        // println!("{}", addresses_masked);
        let addresses_value = u64::from_str_radix(&addresses_masked, 2).unwrap();
        let mut v = clone.lock().unwrap();
        v.push(addresses_value);
    }}});
    // println!("");

    handle.join().unwrap();

    // return (addresses.lock().unwrap()).unwrap();
    return Arc::try_unwrap(addresses).unwrap().into_inner().unwrap();

}