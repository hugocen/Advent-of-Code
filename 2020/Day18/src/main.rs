use std::fs;
use std::collections::VecDeque;


fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let mut sum = 0 as isize;

    for line in contents.lines() {
        let mut que = VecDeque::new();

        for i in 0..line.len() {
            let c = line[i..i+1].to_owned();
            match c.as_str() {
                "(" | "+" | "*" => que.push_back(c),
                " " => {},
                ")" => {
                    let new_que = get2left(&mut que);
                    que = new_que;
                },
                _ => que.push_back(c)
            }
        }
        let s = operate2(que, 0);
        sum += s;
    }
    println!("Result: {}", sum);
}

fn get2left (que: &mut VecDeque<String>) -> VecDeque<String> {
    let mut last_left = 0;
    for i in 0..que.len() {
        if que[i] == "(" {
            last_left = i;
        }
    }
    let num = operate2(que.clone(), last_left+1);
    
    let sr = format!("{}", num);
    for _ in 0..(que.len()-last_left) {
        que.pop_back();
    }
    que.push_back(sr);
    return que.clone();
}

fn operate1(que: VecDeque<String>, idx: usize) -> isize {
    let mut num = que[idx].parse::<isize>().unwrap();
    for i in (idx+1..que.len()).step_by(2) {
        let operator = &que[i];
        let num2 = que[i+1].parse::<isize>().unwrap();
        match operator.as_str() {
            "+" => num += num2,
            "*" => num *= num2,
            _ => panic!("error")
        }
    }
    return num;
}

fn operate2(que: VecDeque<String>, idx: usize) -> isize {
    let mut tmp_que: Vec<String> = que.into_iter().collect();
    let vec_que = tmp_que.drain(idx..).collect();
    let new_que = add(vec_que);
    let mut num = new_que[0].parse::<isize>().unwrap();
    for i in (1..new_que.len()).step_by(2) {
        let operator = &new_que[i];
        let num2 = new_que[i+1].parse::<isize>().unwrap();
        match operator.as_str() {
            "*" => num *= num2,
            _ => panic!("error")
        }
    }
    return num;
}

fn add(que: Vec<String>) -> Vec<String> {
    let mut new_que = Vec::new();
    new_que.push(que[0].clone());
    for i in (2..que.len()).step_by(2) {
        if que[i-1] == "+" {
            let n1 = new_que.pop().unwrap();
            let num = n1.parse::<isize>().unwrap() + que[i].parse::<isize>().unwrap();
            let sn = format!("{}", num);
            new_que.push(sn);
        } else {
            new_que.push(que[i-1].clone());
            new_que.push(que[i].clone());
        }
    }
    return new_que;
}