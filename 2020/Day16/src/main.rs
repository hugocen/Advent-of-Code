use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let lines: Vec<&str> = contents.lines().collect();
    let mut valid_fields = HashSet::new();
    let mut class_fields = Vec::new();
    let mut idx = 0;
    while lines[idx] != "" {
        let field: Vec<&str> = lines[idx].split(": ").collect();
        let vals: Vec<&str> = field[1].split(" or ").collect();
        let mut class = HashSet::new();
        for v in vals {
            let n: Vec<usize> = v.split("-").map(|s| s.parse::<usize>().expect("parse error")).collect();
            for step in n[0]..n[1]+1 {
                valid_fields.insert(step);
                class.insert(step);
            }
        }
        class_fields.push(class);
        idx += 1;
    }

    idx += 2;
    let my_ticket: Vec<usize> = lines[idx].split(",").map(|s| s.parse::<usize>().expect("parse error")).collect();

    let mut valid_ticket = Vec::new();

    idx += 3;
    let mut result = 0;
    while idx < lines.len() {
        let ticket: Vec<usize> = lines[idx].split(",").map(|s| s.parse::<usize>().expect("parse error")).collect();
        let mut flag = true;
        for i in 0..ticket.len() {
            if !valid_fields.contains(&ticket[i]) {
                result += ticket[i];
                flag = false;
            }
        }
        if flag {
            valid_ticket.push(ticket);
        }
        idx += 1;
    }
    println!("Result: {}", result);

    let new_path = Vec::new();

    dfs(&valid_ticket, &class_fields, new_path, &my_ticket);

}

fn dfs(valid_ticket: &Vec<Vec<usize>>, class_fields: &Vec<HashSet<usize>>, path: Vec<usize>, my_ticket: &Vec<usize>) -> bool {
    if path.len() == class_fields.len() {
        let mut result2 = 1;
            for i in 0..path.len() {
                if path[i] < 6 {
                    result2 *= my_ticket[i];
                }
            } 
            println!("Result2: {}", result2);
            return true;
    } else {
        for i in 0..class_fields.len() {
            if !path.contains(&i) {
                let mut flag = true;
                for j in 0..valid_ticket.len() {
                    if !class_fields[i].contains(&valid_ticket[j][path.len()]) {
                        flag = false;
                        break;
                    }
                }
                if flag {
                    let mut new_path = path.clone();
                    new_path.push(i);
                    if dfs(valid_ticket, class_fields, new_path, my_ticket) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}