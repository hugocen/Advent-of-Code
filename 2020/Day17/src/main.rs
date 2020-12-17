use std::fs;

fn main() {
    let contents = fs::read_to_string("inputs.txt").expect("Error");
    let data: Vec<Vec<char>> = contents.lines().map(|l| l.chars().collect()).collect();
    let mut conway_cubes_3d = ConwayCubes3D::new(30);
    conway_cubes_3d.initial(data.clone());
    for _ in 0..6 {
        conway_cubes_3d.simulate();
    }
    println!("Result: {}", conway_cubes_3d.count_result());

    let mut conway_cubes_4d = ConwayCubes4D::new(30);
    conway_cubes_4d.initial(data.clone());
    for _ in 0..6 {
        conway_cubes_4d.simulate();
    }
    println!("Result2: {}", conway_cubes_4d.count_result());
}


struct ConwayCubes3D {
    size: usize,
    space: Vec<Vec<Vec<char>>>
}

impl ConwayCubes3D {
    pub fn new(size: usize) -> ConwayCubes3D {
        ConwayCubes3D {
            size: size,
            space: vec![vec![vec!['.'; size]; size]; size]
        }
    }

    pub fn initial(&mut self, data: Vec<Vec<char>>) {
        let mid = (self.size / 2) - (data.len() / 2);
        for i in 0..data.len() {
            for j in 0..data[0].len() {
                self.space[mid+i][mid+j][mid] = data[i][j];
            }
        }
    }

    pub fn simulate(&mut self) {
        let mut new_space = vec![vec![vec!['.'; self.size]; self.size]; self.size];

        for i in 1..self.space.len()-1 {
            for j in 1..self.space[i].len()-1 {
                for k in 1..self.space[i][j].len()-1 {
                    let actives = self.check_actives(i, j, k);
                    if self.space[i][j][k] == '#' && (actives == 2 || actives == 3) {
                        new_space[i][j][k] = '#';
                    } else if self.space[i][j][k] == '.' && actives == 3 {
                        new_space[i][j][k] = '#';
                    }
                }
            }
        }
        self.space = new_space;
    }
    fn check_actives(&self, si: usize, sj: usize, sk: usize) -> usize {
        let mut actives = 0;
        for i in si-1..si+2 {
            for j in sj-1..sj+2 {
                for k in sk-1..sk+2 {
                    if !(i == si && j == sj && k == sk) && self.space[i][j][k] == '#' {
                        actives += 1;
                    }
                }
            }
        }
        return actives;
    }
    fn count_result(&self) -> usize {
        let mut result = 0;
        for i in 0..self.space.len() {
            for j in 0..self.space[i].len() {
                for k in 0..self.space[i][j].len() {
                    if self.space[i][j][k] == '#' {
                        result += 1;
                    }
                }
            }
        }
        return result;
    }
}

struct ConwayCubes4D {
    size: usize,
    space: Vec<Vec<Vec<Vec<char>>>>
}

impl ConwayCubes4D {
    pub fn new(size: usize) -> ConwayCubes4D {
        ConwayCubes4D {
            size: size,
            space: vec![vec![vec![vec!['.'; size]; size]; size]; size]
        }
    }

    pub fn initial(&mut self, data: Vec<Vec<char>>) {
        let mid = (self.size / 2) - (data.len() / 2);
        for i in 0..data.len() {
            for j in 0..data[0].len() {
                self.space[mid+i][mid+j][mid][mid] = data[i][j];
            }
        }
    }

    pub fn simulate(&mut self) {
        let mut new_space = vec![vec![vec![vec!['.'; self.size]; self.size]; self.size]; self.size];

        for i in 1..self.space.len()-1 {
            for j in 1..self.space[i].len()-1 {
                for k in 1..self.space[i][j].len()-1 {
                    for l in 1..self.space[i][j][k].len()-1 {
                        let actives = self.check_actives(i, j, k, l);
                        if self.space[i][j][k][l] == '#' && (actives == 2 || actives == 3) {
                            new_space[i][j][k][l] = '#';
                        } else if self.space[i][j][k][l] == '.' && actives == 3 {
                            new_space[i][j][k][l] = '#';
                        }
                    }
                }
            }
        }
        self.space = new_space;
    }
    fn check_actives(&self, si: usize, sj: usize, sk: usize, sl: usize) -> usize {
        let mut actives = 0;
        for i in si-1..si+2 {
            for j in sj-1..sj+2 {
                for k in sk-1..sk+2 {
                    for l in sl-1..sl+2 {
                        if !(i == si && j == sj && k == sk && l == sl) && self.space[i][j][k][l] == '#' {
                            actives += 1;
                        }
                    }
                }
            }
        }
        return actives;
    }
    fn count_result(&self) -> usize {
        let mut result = 0;
        for i in 0..self.space.len() {
            for j in 0..self.space[i].len() {
                for k in 0..self.space[i][j].len() {
                    for l in 0..self.space[i][j][k].len() {
                        if self.space[i][j][k][l] == '#' {
                            result += 1;
                        }
                    }
                }
            }
        }
        return result;
    }
}