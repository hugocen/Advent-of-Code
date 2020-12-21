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
        let edge = self.tile[0].clone();
        return edge;
    }

    fn bottom_edge(&self) -> String {
        let edge = self.tile[self.edge_len-1].clone();
        return edge;
    }

    fn rotate_right(&mut self) {
        let mut rotated = Vec::new();
        for ix in 0..self.edge_len {
            let mut tmp = "".to_string();
            for jx in 0..self.edge_len {
                let t = &self.tile[self.edge_len-jx-1..self.edge_len-jx][ix];
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

fn check(order: Vec<Tile>, tile: Tile, edge_size: usize) -> bool {
    if (order.len() + 1 - edge_size) > 0 {
        if tile.top_edge() != order[order.len() - edge_size].bottom_edge() {
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

fn recursion(order: &Vec<Tile>, visited: HashSet<Tile>, tiles: Vec<Tile>, edge_size: usize) -> Vec<Tile> {
    
    let mut result = Vec::new();
    if order.len() == tiles.len() {
        return order.to_owned();
    } else {
        for i in 0..tiles.len() {
            if !visited.contains(&tiles[i]) {

                let mut new_tile = tiles[i].clone();

                // let process = {
                //     let mut new_order = order.clone();
                //     new_order.push(new_tile);
                //     let mut new_visited = visited.clone();
                //     new_visited.insert(new_tile);
                //     result = recursion(new_order, new_visited, tiles, edge_size);
                //     if result.len() > 0{
                //         return result;
                //     }
                // };

                if check(order.clone(), new_tile, edge_size) {
                    let mut new_order = order.clone();
                    new_order.push(new_tile);
                    let mut new_visited = visited.clone();
                    new_visited.insert(new_tile);
                    result = recursion(&new_order, new_visited, tiles, edge_size);
                    if result.len() > 0{
                        return result;
                    }
                }
                
                for _ in 0..3 {
                    new_tile.rotate_right();
                    if check(order.clone(), new_tile, edge_size) {
                        let mut new_order = order.clone();
                        new_order.push(new_tile);
                        let mut new_visited = visited.clone();
                        new_visited.insert(new_tile);
                        result = recursion(&new_order, new_visited, tiles, edge_size);
                        if result.len() > 0{
                            return result;
                        }
                    }
                }

                new_tile.flip();
                if check(order.clone(), new_tile, edge_size) {
                    let mut new_order = order.clone();
                    new_order.push(new_tile);
                    let mut new_visited = visited.clone();
                    new_visited.insert(new_tile);
                    result = recursion(&new_order, new_visited, tiles, edge_size);
                    if result.len() > 0{
                        return result;
                    }
                }

                for _ in 0..3 {
                    new_tile.rotate_right();
                    if check(order.clone(), new_tile, edge_size) {
                        let mut new_order = order.clone();
                        new_order.push(new_tile);
                        let mut new_visited = visited.clone();
                        new_visited.insert(new_tile);
                        result = recursion(&new_order, new_visited, tiles, edge_size);
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



fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let lines: Vec<String> = contents.lines().map(|l| l.to_owned()).collect();
}
