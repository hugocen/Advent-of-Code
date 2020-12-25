use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let mut blacktiles = HashSet::new();
    let mut lines: Vec<String> = contents.lines().map(|l| l.to_owned()).collect();
    for i in 0..lines.len() {
        let mut x = 0 as isize;
        let mut y = 0 as isize;
        while lines[i].len() > 0 {
            if lines[i].starts_with("se") {
                x += 2;
                y += 3;
                lines[i] = lines[i].strip_prefix("se").unwrap().to_owned();
            } else if lines[i].starts_with("sw") {
                x -= 2;
                y += 3;
                lines[i] = lines[i].strip_prefix("sw").unwrap().to_owned();
            } else if lines[i].starts_with("nw") {
                x -= 2;
                y -= 3;
                lines[i] = lines[i].strip_prefix("nw").unwrap().to_owned();
            } else if lines[i].starts_with("ne") {
                x += 2;
                y -= 3;
                lines[i] = lines[i].strip_prefix("ne").unwrap().to_owned();
            } else if lines[i].starts_with("e") {
                x += 4;
                lines[i] = lines[i].strip_prefix("e").unwrap().to_owned();
            } else if lines[i].starts_with("w") {
                x -= 4;
                lines[i] = lines[i].strip_prefix("w").unwrap().to_owned();
            }
        }
        // println!("{}", lines[i]);
        if blacktiles.contains(&(x, y)) {
            blacktiles.remove(&(x, y));
        } else {
            blacktiles.insert((x, y));
       }
    }
    println!("Result: {}", blacktiles.len());

    for _ in 0..100 {
        let mut newtiles = HashSet::new();
        let mut affectedtiles = HashSet::new();
        affectedtiles = blacktiles.clone();

        let tmp: Vec<(isize, isize)> = blacktiles.clone().into_iter().collect();

        for t in tmp {
            affectedtiles.insert((t.0-4, t.1));
            affectedtiles.insert((t.0+4, t.1));
            affectedtiles.insert((t.0-2, t.1-3));
            affectedtiles.insert((t.0+2, t.1-3));
            affectedtiles.insert((t.0-2, t.1+3));
            affectedtiles.insert((t.0+2, t.1+3));
        }

        let tmp2: Vec<(isize, isize)> = affectedtiles.clone().into_iter().collect();

        for t in tmp2 {
            let mut numneighbors = 0;
            if blacktiles.contains(&(t.0-4, t.1)) {
                numneighbors += 1;
            }
            if blacktiles.contains(&(t.0+4, t.1)) {
                numneighbors += 1;
            }
            if blacktiles.contains(&(t.0-2, t.1-3)) {
                numneighbors += 1;
            }
            if blacktiles.contains(&(t.0+2, t.1-3)) {
                numneighbors += 1;
            }
            if blacktiles.contains(&(t.0-2, t.1+3)) {
                numneighbors += 1;
            }
            if blacktiles.contains(&(t.0+2, t.1+3)) {
                numneighbors += 1;
            }

            if blacktiles.contains(&t) {
                if numneighbors == 1 || numneighbors == 2 {
                    newtiles.insert(t.clone());
                }
            } else {
                if numneighbors == 2 {
                    newtiles.insert(t.clone());
                }
            }
        }
        blacktiles = newtiles.clone();
    }
    println!("Result: {}", blacktiles.len());
}
