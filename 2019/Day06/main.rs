use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("Day6.txt").expect("Error");
    let mut orbits = HashMap::new();
    for line in contents.lines() {
        let planets: Vec<&str> = line.split(")").collect();
        orbits.insert(planets[1], planets[0]);
    }

    let mut result = 0;
    for planet in orbits.keys() {
        result += dfs(planet, &orbits)
    }
    println!("Result: {}", result);

    let mut result2 = 0;
    let mut idx = "YOU":
    let mut step = 0;
    while you_idx != "COM" {
        idx = orbits[idx];
        idx.insert(idx, step);
        step += 1;
    }
    step = 0;
    idx = "SAN";
    loop {
        if you_path.contains_key(idx) {
            result2 = step + you_path[idx];
            break;
        } else {
            idx = orbits[idx];
            step += 1;
        }
    }
    println!("Result2: {}", result2);
}

fn dfs(planet: &str, orbits: &HashMap::<&str, &str>) -> usize {
    let mut n = 0;
    if orbits.contains_key(planet) {
        n = dfs(orbits[planet], &orbits) + 1;
    }
    return n;
}
