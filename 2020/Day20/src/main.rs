use std::fs;
use std::collections::HashSet;
use colored::*;

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

fn form_pic(order: &mut Vec<Tile>) -> Tile {
    let tile_edge_len = order[0].edge_len - 2;
    let num_of_tile_in_each_edge = (order.len() as f32).sqrt() as usize;
    let pic_edge_len = tile_edge_len * num_of_tile_in_each_edge;
    let mut pic = Vec::new();
    for _ in 0..pic_edge_len {
        pic.push("".to_string());
    }

    for ix in 0..order.len() {
        order[ix].remove_edge();
        for jx in 0..order[ix].tile.len() {
            let idx = (ix / num_of_tile_in_each_edge) * tile_edge_len + jx;
            pic[idx] += &order[ix].tile[jx];
        }
    }
    return Tile::new(pic, 0);
}

fn search(target: &Vec<String>, pic: &Tile, print_to_terminal: bool) -> usize {
    let target_row_len = target.len();
    let target_column_len = target[0].len();
    let pic_row_len = pic.tile.len();
    let pic_column_len = pic.tile[0].len();

    let mut p = Vec::new();
    for i in 0..pic.tile.len() {
        p.push(pic.tile[i].clone().green().to_string());
    }

    let mut count = 0;
    let mut idx_i = pic_row_len as isize - target_row_len as isize + 1;
    if idx_i < 0 {
        idx_i = 0;
    }
    let mut idx_j = pic_column_len as isize - target_column_len as isize + 1;
    if idx_j < 0 {
        idx_j = 0;
    }
    for ix in 0..(idx_i as usize) {
        for jx in 0..(idx_j as usize) {
            let mut valid = true;
            for kx in 0..target_row_len {
                for lx in 0..target_column_len {
                    if &target[kx][lx..lx+1] != " " && &target[kx][lx..lx+1] != &pic.tile[ix+kx][(jx+lx)..(jx+lx+1)] {
                        valid = false;
                    }
                }
            }
            if valid {
                count += 1;

                // For printing
                // for kx in 0..target_row_len {
                //     for lx in 0..target_column_len {
                //         if &target[kx][lx..lx+1] != " " {
                //             let mut new_string = p[ix+kx][0..(jx+lx)].to_owned();
                //             let target = p[ix+kx][(jx+lx)..(jx+lx+1)].to_owned();
                //             new_string += &target.red();
                //             p[ix+kx] = new_string;
                //         }
                //     }
                // }
            }
        }
    }

    if print_to_terminal && count > 0 {
        for i in 0..p.len() {
            println!("{}", p[i]);
        }
    }
    return count;
}

fn search_pic(target: &Vec<String>, pic: Tile, print_to_terminal: bool) -> usize {
    let mut new_pic = pic.clone();
    let mut count = search(target, &new_pic, print_to_terminal);
    if count > 0 {
        return count;
    }

    for _ in 0..3 {
        new_pic.rotate_right();
        count = search(target, &new_pic, print_to_terminal);
        if count > 0 {
            return count;
        }
    }

    new_pic.flip();
    count = search(target, &new_pic, print_to_terminal);
    if count > 0 {
        return count;
    }

    for _ in 0..3 {
        new_pic.rotate_right();
        count = search(target, &new_pic, print_to_terminal);
        if count > 0 {
            return count;
        }
    }

    return 0;
}

fn part2(tiles: Vec<Tile>) -> usize {
    let size = tiles.len();
    let edge_size = (size as f32).sqrt() as usize;
    let mut order = recursion(&mut Vec::new(), HashSet::new(), &tiles, edge_size);
    let pic = form_pic(&mut order);

    let sea_monster = vec![
        "                  # ".to_string(),
        "#    ##    ##    ###".to_string(),
        " #  #  #  #  #  #   ".to_string(),
    ];
    let sea = vec!["#".to_string()];
    let r1 = search_pic(&sea, pic.clone(), false);
    let r2 = search_pic(&sea_monster, pic.clone(), false);
    return r1 - (r2*15);
}

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let mut lines: Vec<String> = contents.lines().map(|l| l.to_owned()).collect();
    let tiles = extract_data(&mut lines);
    let result1 = part1(tiles.clone());
    println!("Result: {}", result1);

    let result2 = part2(tiles.clone());
    println!("Result2: {}", result2);
}
