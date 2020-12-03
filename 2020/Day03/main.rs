use std::fs;

fn main() {

    let contents = fs::read_to_string("input.txt").expect("Error");

    let map = contents.lines().collect();

    let result = slop(&map, 3, 1);

    println!("Result: {}", result);

    let slops = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];
    let mut result2 = 1;
    for s in &slops {
        result2 *= slop(&map, s[0], s[1]);
    }

    println!("Result2: {}", result2);
}

fn slop(map: &Vec<&str>, right: usize, down: usize) -> usize {
    let mut x = 0;
    let mut y = 0;
    let mut trees = 0;
    while y < map.len() {
        let path: Vec<char> = map[y].chars().collect();
        if path[x] == '#' {
            trees += 1;
        }
        x += right;
        x %= path.len();
        y += down;
    }
    return trees;
}