use std::fs;
use std::cmp::min;

fn main() {
    let contents = fs::read_to_string("Inputs.txt").expect("Error");
    let mut map: Vec<Vec<char>> = contents.split_whitespace().map(|s| s.chars().collect::<Vec<_>>()).collect();

    fn check(i: usize, j: usize, ni: isize, nj: isize, map: &Vec<Vec<char>>) -> usize {
        if ni >= 0 && nj >= 0 && ni < map.len() as isize && nj < map[0].len() as isize && !(ni == i as isize && nj == j as isize){
            if map[ni as usize][nj as usize] == '#' {
                return 1;
            } else if map[ni as usize][nj as usize] == 'L'{
                return 2;
            } else {
                return 0;
            }
        } else {
            return 0;
        }
    }

    loop {
        let mut new_map = vec![vec![' '; map[0].len()]; map.len()];
        for i in 0..map.len() {
            for j in 0..map[0].len() {
                new_map[i][j] = map[i][j];
                let mut occupied = 0;
                for nj in j as isize-1..(j+2) as isize {
                    for ni in i as isize-1..(i+2) as isize {
                        if check(i, j, ni, nj, &map) == 1 {
                            occupied += 1;
                        }
                    }
                }
                if map[i][j] == 'L' && occupied == 0 {
                    new_map[i][j] = '#';
                } else if map[i][j] == '#' && occupied >= 4 {
                    new_map[i][j] = 'L';
                }
            }
        }
        if new_map == map {
            break;
        } else {
            map = new_map;
        }
    }
    let mut occupied = 0;
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            if map[i][j] == '#' {
                occupied += 1;
            }
        }
    }
    println!("Result: {}", occupied);

    // --------------------------------Part 2---------------------------------------------

    map = contents.split_whitespace().map(|s| s.chars().collect::<Vec<_>>()).collect();

    loop {
        let mut new_map = vec![vec![' '; map[0].len()]; map.len()];
        for i in 0..map.len() {
            for j in 0..map[0].len() {
                new_map[i][j] = map[i][j];
                let mut occupied = 0;
                // left
                for ni in (0..i).rev() {
                    let c = check(i, j, ni as isize, j as isize, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // right
                for ni in i+1..map.len() {
                    let c = check(i, j, ni as isize, j as isize, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // up
                for nj in (0..j).rev() {
                    let c = check(i, j, i as isize, nj as isize, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // down
                for nj in j+1..map[0].len() {
                    let c = check(i, j, i as isize, nj as isize, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // left up 
                for n in 1..min(i+1, j+1) {
                    let c = check(i, j, i as isize-n as isize, j as isize-n as isize, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // right up
                for n in 1..min(map.len()as isize-i as isize+1, j as isize+1) {
                    let c = check(i, j, i as isize+n, j as isize-n, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // left down
                for n in 1..min(i as isize+1, map[0].len()as isize-j as isize+1) {
                    let c = check(i, j, i as isize-n, j as isize+n, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }
                // right down
                for n in 1..min(map.len()as isize-i as isize+1, map[0].len()as isize-j as isize+1) {
                    let c = check(i, j, i as isize+n, j as isize+n, &map);
                    if c == 1 {
                        occupied += 1;
                        break;
                    } else if c == 2 {
                        break;
                    }
                }

                if map[i][j] == 'L' && occupied == 0 {
                    new_map[i][j] = '#';
                } else if map[i][j] == '#' && occupied >= 5 {
                    new_map[i][j] = 'L';
                }
            }
        }
        if new_map == map {
            break;
        } else {
            map = new_map;
        }
    }
    let mut occupied = 0;
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            if map[i][j] == '#' {
                occupied += 1;
            }
        }
    }
    println!("Result: {}", occupied);
}
