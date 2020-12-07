use std::fs;
use regex::Regex;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error");
    let re = Regex::new(r"((\w+)( \w+)( bag))").unwrap();
    let vals = Regex::new(r"(\d)").unwrap();
    let mut dic = HashMap::<&str, HashMap<&str, usize>>::new();

    for line in contents.lines() {
        let bags: Vec<&str> = re.find_iter(line).map(|mat| mat.as_str()).collect();
        let values: Vec<usize> = vals.find_iter(line).map(|mat| mat.as_str().parse::<usize>().expect("parse error")).collect();
        // println!("{:?}", bags);
        dic.entry(bags[0]).or_insert(HashMap::new());
        for i in 1..bags.len() {
            if bags[i] != "no other bag" {
                if !dic[bags[0]].contains_key(bags[i]) {
                    dic.get_mut(bags[0]).unwrap().insert(bags[i], values[i-1]);
                }
            }
        }
    }
    // println!("{:?}", dic);
    let mut result = 0;
    let target = "shiny gold bag";
    let mut path = HashMap::<&str, bool>::new();
    for key in dic.keys() {
        if dfs(key, target, &dic, &mut path) {
            result += 1;
        }
    }
    println!("Result: {}", result);

    println!("Result2: {}", dfs2(target, &dic));
}

fn dfs <'a> (bag: &'a str, target: &str, dic: &HashMap::<&'a str, HashMap<&'a str, usize>>, path: &mut HashMap::<&'a str, bool>) -> bool {
    if dic[bag].contains_key(target) {
        return true;
    } else if path.contains_key(bag) {
        return path[bag];
    } else {
        let mut flag = false;
        for b in dic[bag].keys() {
            if dfs(b, target, dic, path) {
                flag = true;
                break;
            }
        }
        path.insert(bag, flag);
        return flag;
    }
}

fn dfs2 <'a> (bag: &'a str, dic: &HashMap::<&'a str, HashMap<&'a str, usize>>) -> usize {
    let mut sum = 0;
    for (key, val) in dic[bag].iter() {
        sum += val + val*dfs2(key, dic);
    }
    return sum;

}
