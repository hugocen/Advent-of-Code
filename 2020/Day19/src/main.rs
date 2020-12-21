use std::fs;
use std::collections::HashMap;
use regex::Regex;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let lines: Vec<String> = contents.lines().map(|l| l.to_owned()).collect();

    let mut rules = HashMap::new();

    let mut idx = 0;

    while idx < lines.len() {
        if lines[idx] == "" {
            break;
        } else {
            let rule_line: Vec<&str> = lines[idx].split(":").collect();
            let rule_idx = rule_line[0].parse::<usize>().unwrap();
            let rule: Vec<String>;
            if rule_line[1].contains("\"") {
                rule = vec![rule_line[1].trim().replace("\"", "")];
            } else {
                rule = rule_line[1].split_whitespace().map(|w| w.to_owned()).collect();
            }
            rules.insert(rule_idx, rule);
        }
        idx += 1;
    }
    idx += 1;

    let reg_rule = format!(r"^{}$", build_regex(0, &rules));
    let re = Regex::new(&reg_rule).unwrap();

    // println!("{}", reg_rule);

    let mut result = 0;
    let mut messages = Vec::new();
    while idx < lines.len() {
        if re.is_match(&lines[idx]) {
            result += 1;
        }
        messages.push(&lines[idx]);
        idx += 1;
    }
    println!("Result: {}", result);

    let reg_42 = build_regex(42, &rules);
    let reg_32 = build_regex(31, &rules);

    let mut result2 = 0;
    for n in 1..5 {
        let new_regex = format!(r"^({}+{}{{{}}}{}{{{}}})$", reg_42, reg_42, n, reg_32, n);
        let new_re = Regex::new(&new_regex).unwrap();
        for i in 0..messages.len() {
            if new_re.is_match(&messages[i]) {
                result2 += 1;
            }
        }
    }
    println!("Result2: {}", result2);
}

fn build_regex(idx: usize, rules: &HashMap<usize, Vec<String>>) -> String {
    let mut result = "".to_string();
    if rules[&idx][0] == "a" || rules[&idx][0] == "b" {
        result = rules[&idx][0].clone();
        return result;        
    } else {
        result += "(";
        for i in 0..rules[&idx].len() {
            if rules[&idx][i] == "|" {
                result += &rules[&idx][i];
            } else {
                let new_idx = rules[&idx][i].parse::<usize>().unwrap();
                result += &build_regex(new_idx, rules);
            }
        }
        result += ")";
        return result;
    }
}