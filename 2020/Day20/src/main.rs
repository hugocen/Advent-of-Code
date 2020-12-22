use std::fs;
use std::collections::HashSet;

#[derive(PartialEq, Eq, Hash, Clone)]
struct Tile {
    tile: Vec<String>,
    id: usize,
    edge_len: usize
}

impl Tile {
    pub fn new(tile: Vec<String>, id: usize) -> Tile {
        Tile {
            edge_len: tile.len(),
            tile: tile,
            id: id
        }
    }

    fn right_edge(&self) -> String {
        let mut edge = "".to_string();
        for i in 0..self.edge_len {
            let s = &self.tile[i][self.edge_len-1..self.edge_len];
            edge += s;
        }
        return edge;
    }

    fn left_edge(&self) -> String {
        let mut edge = "".to_string();
        for i in 0..self.edge_len {
            let s = &self.tile[i][0..1];
            edge += s;
        }
        return edge;
    }

    fn top_edge(&self) -> String {
        return self.tile[0].clone();
    }

    fn bottom_edge(&self) -> String {
        return self.tile[self.edge_len-1].clone();
    }

    fn rotate_right(&mut self) {
        let mut rotated = Vec::new();
        for ix in 0..self.edge_len {
            let mut tmp = "".to_string();
            for jx in 0..self.edge_len {
                let t = &self.tile[self.edge_len-jx-1][ix..ix+1];
                tmp += t;
            }
            rotated.push(tmp);
        }
        self.tile = rotated;
    }

    fn flip(&mut self) {
        self.tile.reverse();
    }

    fn remove_edge(&mut self) {
        let mut removed = Vec::new();
        for ix in 1..self.edge_len-1 {
            let mut tmp = "".to_string();
            for jx in 1..self.edge_len-1 {
                let t = &self.tile[ix][jx..jx+1];
                tmp += t;
            }
            removed.push(tmp);
        }
        self.tile = removed;
    }
}

fn check(order: Vec<Tile>, tile: &Tile, edge_size: usize) -> bool {
    if (order.len()as isize + 1 - edge_size as isize) > 0 {
        let mut idx = order.len() as isize - edge_size as isize;
        if idx < 0 {
            idx = order.len() as isize + idx;
        }
        if tile.top_edge() != order[idx as usize].bottom_edge() {
            return false;
        }
    }
    if (order.len() + 1) % edge_size != 1 {
        if tile.left_edge() != order[order.len() - 1].right_edge() {
            return false;
        }
    }
    return true;
}

fn recursion(order: &mut Vec<Tile>, visited: HashSet<usize>, tiles: &Vec<Tile>, edge_size: usize) -> Vec<Tile> {
    let mut result = Vec::new();
    if order.len() == tiles.len() {
        return order.to_owned();
    } else {
        for i in 0..tiles.len() {
            if !visited.contains(&tiles[i].id) {

                let mut new_tile = tiles[i].clone();

                let process = |new_tile: &Tile| -> Vec<Tile> {
                    let mut new_order = order.clone();
                    new_order.push(new_tile.clone());
                    let mut new_visited = visited.clone();
                    new_visited.insert(new_tile.id);
                    let rresult = recursion(&mut new_order, new_visited, tiles, edge_size);
                    rresult
                };

                if check(order.clone(), &new_tile, edge_size) {
                    // let mut new_order = order.clone();
                    // new_order.push(new_tile.clone());
                    // let mut new_visited = visited.clone();
                    // new_visited.insert(new_tile.clone());
                    // result = recursion(&mut new_order, new_visited, tiles, edge_size);
                    result = process(&new_tile);
                    if result.len() > 0{
                        return result;
                    }
                }
                
                for _ in 0..3 {
                    new_tile.rotate_right();
                    if check(order.clone(), &new_tile, edge_size) {
                        result = process(&new_tile);
                        if result.len() > 0{
                            return result;
                        }
                    }
                }

                new_tile.flip();
                if check(order.clone(), &new_tile, edge_size) {
                    result = process(&new_tile);
                    if result.len() > 0{
                        return result;
                    }
                }

                for _ in 0..3 {
                    new_tile.rotate_right();
                    if check(order.clone(), &new_tile, edge_size) {
                        result = process(&new_tile);
                        if result.len() > 0{
                            return result;
                        }
                    }
                }
            }
        }
    }
    return result;
}

fn extract_data(lines: &mut Vec<String>) -> Vec<Tile> {
    let mut tiles = Vec::new();
    for i in (0..lines.len()).step_by(12) {
        let id = lines[i].clone().replace("Tile ", "").replace(":", "").parse::<usize>().unwrap();
        let mut tile = Vec::new();
        for j in i+1..i+11 {
            tile.push(lines[j].clone());
        }
        let new_tile = Tile::new(tile, id);
        tiles.push(new_tile);
    }
    return tiles;
}

fn part1(tiles: Vec<Tile>) -> isize {
    let mut result = 1 as isize;
    let size = tiles.len();
    let edge_size = (size as f32).sqrt() as usize;

    let order = recursion(&mut Vec::new(), HashSet::new(), &tiles, edge_size);

    let upper_left = 0;
    let upper_right = edge_size - 1;
    let bottom_left = size - edge_size;
    let bottom_right = size - 1;
    result *= order[upper_left].id as isize;
    result *= order[upper_right].id as isize;
    result *= order[bottom_left].id as isize;
    result *= order[bottom_right].id as isize;
    return result;
}

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let mut lines: Vec<String> = contents.lines().map(|l| l.to_owned()).collect();
    let tiles = extract_data(&mut lines);
    let result1 = part1(tiles);
    println!("Result: {}", result1);
}
