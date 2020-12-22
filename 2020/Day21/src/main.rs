use std::fs;
use std::collections::{HashMap, HashSet};
use std::iter::FromIterator;

fn main() {
    let mut dic = HashMap::<String, HashSet<String>>::new();
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    for line in contents.lines() {
        let data: Vec<&str> = line.split(" (contains ").collect();
        let allerg: Vec<String> = data[1].replace(")", "").split(", ").map(|s| s.to_owned()).collect();
        let ingred: Vec<String> = data[0].split_whitespace().map(|s| s.to_owned()).collect();
        for i in 0..allerg.len() {
            let target_set = HashSet::<String>::from_iter(ingred.clone());

            let mut new_set: HashSet<String>;

            if dic.contains_key(&allerg[i]) {
                let tmp = dic.get(&allerg[i]).unwrap().clone();
                new_set = HashSet::new();
                for k in &tmp {
                    if target_set.contains(k) && tmp.contains(k) {
                        new_set.insert(k.to_owned());
                    }
                }
            } else {
                new_set = target_set;
            }
            dic.insert(allerg[i].clone(), new_set);
        }
    }
    let mut f = HashSet::new();
    for k in dic.values() {
        f = f.union(k).map(|s| s.to_owned()).collect::<HashSet<String>>();
    }
    println!("{:?}", dic);
    println!("{:?}", f);
    

    let mut result1 = 0;
    for line in contents.lines() {
        let data: Vec<&str> = line.split(" (contains ").collect();
        let ingred = data[0].split_whitespace().map(|s| s.to_owned());
        let ingred_set = HashSet::<String>::from_iter(ingred);
        let mut dif = HashSet::new();
        for k in &ingred_set {
            if !f.contains(k) {
                dif.insert(k);
            }
        }

        result1 += dif.len();
    }
    println!("Result: {}", result1);

    let mut new_dic = HashMap::new();
    let mut single_item = HashSet::new();

    let ttd = dic.clone();
    for (key, val) in ttd.iter() {
        if val.len() == 1 {
            new_dic.insert(key.to_owned(), val.clone());
            for v in val.iter() {
                single_item.insert(v.to_owned());
            }
        }
    }

    loop {
        let td = dic.clone();
        let mut tmp_dic = dic.clone();
        for (key, val) in td.iter() {
            let mut tmp = HashSet::new();
            for v in val.iter() {
                if !single_item.contains(v) {
                    tmp.insert(v.to_owned());
                }
            }

            tmp_dic.insert(key.to_owned(), tmp.clone());

            if tmp.len() == 1 {
                for v in tmp.clone().iter() {
                    single_item.insert(v.to_owned());
                }
                new_dic.insert(key.to_owned(), tmp);
            }
        }
        let mut sums = 0;
        let ttmp_d = tmp_dic.clone();
        for v in ttmp_d.values() {
            sums += v.len();
        }
        dic = tmp_dic;
        if sums == 0 {
            break;
        }
    }
    let mut rr: Vec<(String, HashSet<String>)> = new_dic.into_iter().collect();
    rr.sort_by(|a, b| a.0.cmp(&b.0));
    let mut result2 = String::new();

    for r in rr {
        for t in r.1 {
            result2 += &t;
        }
        result2 += ","
    }
    result2 = result2[0..(result2.len()-1)].to_string();
    println!("Result2: {}", result2);
}
