use std::fs;
use regex::Regex;
use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let re = Regex::new(r"((\w+)( \w+)( bag))").unwrap();
    let mut dic = HashMap::<&str, HashSet<&str>>::new();

    for line in contents.lines() {
        let bags: Vec<&str> = re.find_iter(line).map(|mat| mat.as_str()).collect();
        // println!("{:?}", bags);
        dic.entry(bags[0]).or_insert(HashSet::new());
        for i in 1..bags.len() {
            if bags[i] != "no other bag" {
                if !dic[bags[0]].contains(bags[i]) {
                    dic.get_mut(bags[0]).unwrap().insert(bags[i]);
                }
            }
        }
    }
    // println!("{:?}", dic);
    let mut result = 0;
    let target = "shiny gold bag";
    let mut path = HashMap::<&str, bool>::new();
    for key in dic.keys() {
        if dfs(key, target, &dic, &path) {
            result += 1;
        }
    }
    println!("Result: {}", result);
}

fn dfs(bag: &str, target: &str, dic: &HashMap::<&str, HashSet<&str>>, path: &HashMap::<&str, bool>) -> bool {
    if dic[bag].contains(target) {
        return true;
    } else if path.contains_key(bag) {
        return path[bag];
    } else {
        let mut flag = false;
        for b in dic[bag].iter() {
            if dfs(b, target, dic, path) {
                flag = true;
                break;
            }
        }
        path.insert(bag, flag);
        return flag;
    }
}

trait Process {
    fn process(&mut self, file: &str);
    fn dfs(&self, bag: &str, target: &str, dic: &HashMap::<&str, HashSet<&str>>, path: &HashMap::<&str, bool>) -> bool;
}

struct Luggages <'a> {
    dic: &'a mut HashMap::<&'a str, HashSet<&'a str>>,
    path: &'a mut HashMap::<&'a str, &'a bool>
}

impl <'a, Luggages: Process> Process for Luggages {
    fn process (&mut self, file: &str) {
        let contents = fs::read_to_string("input.txt").expect("Error");
        let re = Regex::new(r"((\w+)( \w+)( bag))").unwrap();

        for line in contents.lines() {
            let bags: Vec<&str> = re.find_iter(line).map(|mat| mat.as_str()).collect();
            // println!("{:?}", bags);
            self.dic.entry(bags[0]).or_insert(HashSet::new());
            for i in 1..bags.len() {
                if bags[i] != "no other bag" {
                    if !dic[bags[0]].contains(bags[i]) {
                        dic.get_mut(bags[0]).unwrap().insert(bags[i]);
                    }
                }
            }
        }

    }
    fn dfs(&self, bag: &str, target: &str, dic: &HashMap::<&str, HashSet<&str>>, path: &HashMap::<&str, bool>) {
        return 
    }
}