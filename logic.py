
import random
import constants as cons



def merge(line):
   
    n_elements = len(line)
    
    line = [value for value in line if value != 0]
    index = 0
   
    while index < len(line)-1:
        
        if line[index] == line[index+1]:
            line[index] *= 2
            line.pop(index+1)
        
        index += 1
    
    line += [0]*(n_elements-len(line))
    return line


class TwentyFortyEight:
  

    def __init__(self, grid_height, grid_width, offsets):
        self._offsets = offsets
        self._height = grid_height
        self._width = grid_width
        self._grid = None
        self.reset()
        self._initial_tiles = {cons.UP: [(0, col, self._height) for col in range(self._width)],
                               cons.DOWN: [(-1, col, self._height) for col in range(self._width)],
                               cons.LEFT: [(row, 0, self._width) for row in range(self._height)],
                               cons.RIGHT: [(row, -1, self._width) for row in range(self._height)]}

    def reset(self):
        
        self._grid = [[0]*self._width for dummy_i in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        
        return str(self._grid)

    def get_grid_height(self):
        
        return self._height

    def get_grid_width(self):
      
        return self._width

    def move(self, direction):
        
        moved = False
        displacement_vector = list(self._offsets[direction])
        initial_tiles = [list(initial_t) for initial_t in self._initial_tiles[direction]]
        
        for tile_pos in initial_tiles:
            to_merge = []
            for dummy_i in range(tile_pos[2]):
                to_merge += [self.get_tile(tile_pos[0], tile_pos[1])]
                tile_pos[0] += displacement_vector[0]
                tile_pos[1] += displacement_vector[1]
            merged = merge(to_merge)
            merged.reverse()
            for index in range(tile_pos[2]):
                tile_pos[0] -= displacement_vector[0]
                tile_pos[1] -= displacement_vector[1]
                if merged[index] != self.get_tile(tile_pos[0], tile_pos[1]):
                    moved = True
                self.set_tile(tile_pos[0], tile_pos[1], merged[index])
        if moved:
            self.new_tile()

    def new_tile(self):
       
       
        candidate_tiles = []
        for row_index in range(self._height):
            for col_index in range(self._width):
                if self._grid[row_index][col_index] == 0:
                    candidate_tiles += [(row_index, col_index)]
        
        if candidate_tiles:
            tile_pos = random.choice(candidate_tiles)
            tile_row, tile_col = tile_pos[0], tile_pos[1]
            
            tile_value = 2 if random.random() <= 0.9 else 4
            self.set_tile(tile_row, tile_col, tile_value)

    def set_tile(self, row, col, value):
       
        self._grid[row][col] = value

    def get_tile(self, row, col):
        
        return self._grid[row][col]

    def get_game_state(self):
        
        return self._grid
