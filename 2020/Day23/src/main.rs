use std::fs;

#[derive(PartialEq, Debug)]
pub struct Node {
    val: usize,
    next: Option<Box<Node>>
}

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");

    let target_run = 10;

    let data: Vec<usize> = contents.chars().map(|c| c.to_digit(10).unwrap() as usize).collect();
    let root = Node{val: data[0], next: None};
    let mut node = root;
    for i in 1..data.len() {
        let mut new_node = Box::new(Node{val: data[i], next: None});
        node.next = Some(new_node);
        node = new_node.assume_init();
    }
}
