use std::fs;

fn main() {
    let contents = fs::read_to_string("Day8.txt").expect("Error");
    let data: Vec<usize> = contents.chars().map(|s| s.to_digit(10).unwrap() as usize).collect();

    let mut min_zeros = usize::MAX;
    let mut result = 0;
    for i in (0..data.len()).step_by(25*6) {
        let mut zeros = 0;
        let mut ones = 0;
        let mut twos = 0;

        for j in 0..25*6 {
            match data[i+j] {
                0 => zeros += 1,
                1 => ones += 1,
                2 => twos += 1,
                _ => panic!("error")
            }
        }
        if min_zeros > zeros {
            min_zeros = zeros;
            result = ones * twos;
        }
    }
    println!("Result: {}", result);

    let mut pic = vec![3; 25*6];
    for i in (0..data.len()).step_by(25*6).rev() {
        for j in 0..25*6 {
            match data[i+j] {
                0 | 1 => pic[j] = data[i+j],
                2 => {},
                _ => panic!("error")
            }
        }
    }
    for i in 0..6 {
        for j in 0..25 {
            match pic[i*25+j] {
                0 => print!(" "),
                1 => print!("█"),
                _ => panic!("error")
            }
        }
        println!();
    }
}
