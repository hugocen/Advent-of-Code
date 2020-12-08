use std::fs;
use std::collections::HashMap;
use std::cmp::min;

struct Point {
    x: isize,
    y: isize,
    step: isize,
    result: isize,
    result2: isize
}

fn main() {
    let contents = fs::read_to_string("Day3.txt").expect("Error");
    let mut path_a = HashMap::new();
    let dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]];
    let mut line_a = true;
    let mut point = Point {x: 0, y: 0, step: 0, result: isize::MAX, result2: isize::MAX};

    for line in contents.lines() {
        for direction in line.split(",") {
            if &direction[0..1] == "U" {
                point = walk(point, 0, direction, &dirs, &mut path_a, line_a);
            } else if &direction[0..1] == "D" {
                point = walk(point, 1, direction, &dirs, &mut path_a, line_a);
            } else if &direction[0..1] == "L" {
                point = walk(point, 2, direction, &dirs, &mut path_a, line_a);
            } else if &direction[0..1] == "R" {
                point = walk(point, 3, direction, &dirs, &mut path_a, line_a);
            }
        }
        if line_a {
            line_a = false;
            point.x = 0;
            point.y = 0;
            point.step = 0;
        }
    }
    println!("Result: {}", point.result);
    println!("Result2: {}", point.result2);
}

fn walk <'a> (mut point: Point, dir: usize, direction: &'a str, dirs: &'a[[isize; 2]; 4], path: &mut HashMap::<(isize, isize), isize>, line_a: bool) -> Point {
    let length = direction[1..direction.len()].parse::<isize>().expect("parse error");
    for _ in 0..length {
        point.x += dirs[dir][0];
        point.y += dirs[dir][1];
        point.step += 1;
        if line_a {
            path.insert((point.x, point.y), point.step);
        } else if path.contains_key(&(point.x, point.y)) {
            point.result = min(point.result, point.x.abs() + point.y.abs());
            point.result2 = min(point.result2, path[&(point.x, point.y)]+point.step);
        }
    }
    return point;
}