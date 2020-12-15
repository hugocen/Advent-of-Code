use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let mut data = HashMap::new();
    let mut data2 = HashMap::new();
    let mut mask = "".to_owned();
    let mut mask2 = "".to_owned();

    for line in contents.lines() {
        let sen: Vec<&str> = line.split(" = ").collect();
        
        if sen[0] == "mask" {
            let new_mask = format!("{:X>64}", &sen[1]);
            let new_mask2 = format!("{:0>64}", &sen[1]);
            mask = new_mask.to_owned();
            mask2 = new_mask2.to_owned();
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
    for i in 0..64 {
        if mask_string[i] != 'X' {
            val_string[i] = mask_string[i];
        }
    }
    let val_masked: String = val_string.into_iter().collect();
    let m_value = u64::from_str_radix(&val_masked, 2).unwrap();
    return m_value;
}

fn address_mask(mask: String, address: u64) -> Vec<u64> {
    let mask_string: Vec<char> = mask.chars().collect();
    let address_bits = format!("{:b}", address);
    let mut address_string: Vec<char> = format!("{:0>64}", address_bits).chars().collect();

    for i in 0..64 {
        match mask_string[i] {
            'X' => address_string[i] = 'X',
            '0' => {},
            '1' => address_string[i] = '1',
            _ => panic!("error"),
        }
    }
    return recur_address(address_string, 0);
}

fn recur_address(address: Vec<char>, idx: usize) -> Vec<u64> {
    let mut addresses = Vec::new();
    let mut flag = true;
    for i in idx..address.len() {
        if address[i] == 'X' {
            let mut new_address1 = address.clone();
            new_address1[i] = '1';
            let mut r1 = recur_address(new_address1, i+1);
            addresses.append(&mut r1);

            let mut new_address2 = address.clone();
            new_address2[i] = '0';
            let mut r2 = recur_address(new_address2, i+1);
            addresses.append(&mut r2);
            flag = false;
            break;
        }
    }
    if flag {
        let addresses_masked: String = address.into_iter().collect();
        let addresses_value = u64::from_str_radix(&addresses_masked, 2).unwrap();
        addresses.push(addresses_value);
    }
    return addresses;
}