use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let mut valids = 0;
    let mut fields = 0;
    let mut cid = false;
    for line in contents.lines() {
        if line == "" {
            if fields == 8 {
                valids += 1;
            } else if fields == 7 && !cid {
                valids += 1;
            }
            fields = 0;
            cid = false;
        } else {
            for part in line.split_whitespace() {
                let field: Vec<&str> = part.split(":").collect();
                if field[0] == "cid" {
                    cid = true;
                }
                if valid(&field[0], &field[1]) {
                    fields += 1;
                }
            }
        }
    }
    if fields == 8 {
        valids += 1;
    } else if fields == 7 && !cid {
        valids += 1;
    }
    println!("Valids: {}", valids);
}

fn valid(field: &str, value: &str) -> bool{
    // println!("field: {}, value: {}", field, value);
    if field == "cid" {
        return true;
    } else if field == "byr" {
        let num = value.parse::<usize>().unwrap();
        return num >= 1920 && num <= 2002;
    } else if field == "iyr" {
        let num = value.parse::<usize>().unwrap();
        return num >= 2010 && num <= 2020;
    } else if field == "eyr" {
        let num = value.parse::<usize>().unwrap();
        return num >= 2020 && num <= 2030;
    } else if field == "hgt" {
        let unit = &value[value.len()-2..];        
        if unit =="cm" {
            let num =  &value[..value.len()-2].parse::<usize>().unwrap();
            return num >= &150 && num <= &193;
        } else if unit =="in" {
            let num =  &value[..value.len()-2].parse::<usize>().unwrap();
            return num >= &59 && num <= &76;
        } else {
            return false;
        }
    } else if field == "hcl" {
        return &value.chars().nth(0).unwrap() == &'#' && value.len() == 7;
    } else if field == "ecl" {
        return value == "amb" || value == "blu" || value == "brn" || value == "gry" || value == "grn" || value == "hzl" || value == "oth";
    } else if field == "pid" {
        return value.len() == 9;
    }
    return false;
}