use std::fs;
use std::collections::HashMap;

macro_rules! hashmap {
    ($( $key: expr => $val: expr ),*) => {{
         let mut map = HashMap::new();
         $( map.insert($key, $val); )*
         map
    }}
}

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let right_dir = hashmap![
        "W" => "N",
        "N" => "E",
        "E" => "S",
        "S" => "W"
    ];
    let left_dir = hashmap![
        "W" => "S",
        "S" => "E",
        "E" => "N",
        "N" => "W"
    ];
    let mut current_dir = "E";
    let mut x = 0 as isize;
    let mut y = 0 as isize;
    for line in contents.lines() {
        let mut diraction = &line[0..1];
        let value = &line[1..line.len()].parse::<isize>().expect("parse error");
        match diraction {
            "F" => diraction = current_dir,
            "E" | "W" | "S" | "N" | "L" | "R" => {},
            _ => panic!("error"),
        }
        match diraction {
            "E" => {
                x += value;
                // current_dir = "E";
            },
            "W" => {
                x -= value;
                // current_dir = "W";
            },
            "S" => {
                y -= value;
                // current_dir = "S";
            },
            "N" => {
                y += value;
                // current_dir = "N";
            },
            "L" => {
                let mut nv = value.clone();
                while nv != 0 {
                    current_dir = left_dir[current_dir];
                    nv -= 90;
                }
            },
            "R" => {
                let mut nv = value.clone();
                while nv != 0 {
                    current_dir = right_dir[current_dir];
                    nv -= 90;
                }
            },
            _ => panic!("error"),
        }
    }
    let result = x.abs() + y.abs();
    println!("Result: {}", result);

    x = 0 as isize;
    y = 0 as isize;

    let mut wx = 10 as isize;
    let mut wy = 1 as isize;

    for line in contents.lines() {
        let diraction = &line[0..1];
        let value = &line[1..line.len()].parse::<isize>().expect("parse error");

        match diraction {
            "F" => {
                x += value * wx;
                y += value * wy;
            },
            "E" => {
                wx += value;
            },
            "W" => {
                wx -= value;
            },
            "S" => {
                wy -= value;
            },
            "N" => {
                wy += value;
            },
            "L" => {
                let nv = value.clone() % 360;
                match nv {
                    90 => {
                        let n_wx = wy*-1;
                        let n_wy = wx*1;
                        wy = n_wy;
                        wx = n_wx;
                    },
                    180 => {
                        wx *= -1;
                        wy *= -1;
                    },
                    270 => {
                        let n_wx = wy*1;
                        let n_wy = wx*-1;
                        wy = n_wy;
                        wx = n_wx;
                    },
                    _ => panic!("error"),
                }
            },
            "R" => {
                let nv = value.clone() % 360;
                match nv {
                    90 => {
                        let n_wx = wy*1;
                        let n_wy = wx*-1;
                        wy = n_wy;
                        wx = n_wx;
                    },
                    180 => {
                        wx *= -1;
                        wy *= -1;
                    },
                    270 => {
                        let n_wx = wy*-1;
                        let n_wy = wx*1;
                        wy = n_wy;
                        wx = n_wx;
                    },
                    _ => panic!("error"),
                }
            },
            _ => panic!("error"),
        }
    }
    let result2 = x.abs() + y.abs();
    println!("Result2: {}", result2);
}

