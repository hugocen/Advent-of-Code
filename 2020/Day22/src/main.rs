use std::fs;
use std::collections::VecDeque;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let lines: Vec<&str> = contents.lines().collect();
    let mut idx = 1;
    let mut player1 = VecDeque::new();
    while lines[idx] != "" {
        let n = lines[idx].parse::<usize>().unwrap();
        player1.push_back(n);
        idx += 1;
    }
    let mut nplayer1 = player1.clone();
    idx += 2;
    let mut player2 = VecDeque::new();
    while idx < lines.len() {
        let n = lines[idx].parse::<usize>().unwrap();
        player2.push_back(n);
        idx += 1;
    }
    let mut nplayer2 = player2.clone();


    while player1.len() > 0 && player2.len() > 0 {
        let n1 = player1.pop_front().unwrap();
        let n2 = player2.pop_front().unwrap();
        if n1 > n2 {
            player1.push_back(n1);
            player1.push_back(n2);
        } else {
            player2.push_back(n2);
            player2.push_back(n1);
        }
    }

    let mut result1 = 0;

    let result_player:VecDeque<usize>;

    if player1.len() > player2.len() {
        result_player = player1;
    } else {
        result_player = player2;
    }

    for i in 0..result_player.len() {
        result1 += (result_player.len()-i) * result_player[i];
    }

    println!("Result: {:?}", result1);

    let r = recursive(&mut nplayer1, &mut nplayer2);

    let mut result2 = 0;
    for i in 0..r.1.len() {
        result2 += (r.1.len()-i) * r.1[i];
    }
    println!("Result2: {:?}", result2);
}


fn recursive(player1: &mut VecDeque<usize>, player2: &mut VecDeque<usize>) -> (bool, VecDeque<usize>) {
    let mut path = HashSet::new();
    while player1.len() > 0 && player2.len() > 0 {
        if path.contains(&(player1.clone(), player2.clone())) {
            return (true, player1.clone())
        }
        path.insert((player1.clone(), player2.clone()));
        let n1 = player1.pop_front().unwrap();
        let n2 = player2.pop_front().unwrap();

        if n1 <= player1.len() && n2 <= player2.len() {
            let nplayer1: VecDeque<usize> = player1.clone().drain(0..n1).collect();
            let nplayer2: VecDeque<usize> = player2.clone().drain(0..n2).collect();
            let r = recursive(&mut nplayer1.clone(), &mut nplayer2.clone());
            if r.0 {
                player1.push_back(n1);
                player1.push_back(n2);
            } else {
                player2.push_back(n2);
                player2.push_back(n1);
            }
        } else {
            if n1 > n2 {
                player1.push_back(n1);
                player1.push_back(n2);
            } else {
                player2.push_back(n2);
                player2.push_back(n1);
            }
        }
    }
    if player1.len() != 0 {
        return (true, player1.clone());

    } else {
        return (false, player2.clone());
    }
}
