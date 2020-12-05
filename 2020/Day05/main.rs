use std::fs;
use std::cmp;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error");

    let mut max = 0;

    let mut seats = [[false; 8]; 128];

    for line in contents.lines() {
        let seat = decode(line);
        max = cmp::max(seat.id, max);
        seats[seat.row][seat.seat] = true;
    }

    println!("Result: {}", max);

    for i in 0..seats.len() {
        for j in 0..seats[i].len() {
            if !seats[i][j] {
                println!("Row: {} Seat: {} ID: {}", i, j, i*8+j);
            }
        }
    }
}

struct Place {
    start: usize,
    end: usize
}

struct Seat {
    row: usize,
    seat: usize,
    id: usize
}

fn decode(passe: &str) -> Seat {
    let partitions: Vec<char> = passe.chars().collect();
    let mut row = Place {start: 0, end: 127};
    for i in 0..7 {
        if partitions[i] == 'F' {
            row = binary_part(row, false);
        } else {
            row = binary_part(row, true);
        }
    }

    let mut seat = Place {start: 0, end: 7};

    for i in 7..10 {
        if partitions[i] == 'L' {
            seat = binary_part(seat, false);
        } else {
            seat = binary_part(seat, true);
        }
    }
    // println!("Row: {}, Seat: {}", row.start, seat.start);
    return Seat{row:row.start, seat: seat.start, id: row.start * 8 + seat.start}
}

fn binary_part(place: Place, upper:bool) -> Place {
    if upper {
        return Place {start: (place.start + place.end) / 2 + 1, end: place.end};
    } else {
        return Place {start: place.start, end: (place.start + place.end) / 2};
    }
}