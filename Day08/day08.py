import numpy as np

with open("Day08/day08_input.txt") as f:
    content = f.read().splitlines()

# Parsing
# Generating a numpy array
grid = [list(x) for x in content]
grid = [[int(x) for x in l] for l in grid]
grid = np.array(grid)

# Initializing constants
sides = ((grid.shape[0] * 2) + (grid.shape[1] * 2)) - 4
visible_trees = sides
nb_rows = grid.shape[0]
nb_columns = grid.shape[1]

for i in range(1, nb_rows-1):
  for j in range(1, nb_columns-1):
    x = grid[i, j]    # isolating the tree
    # inspecting left, right, top and bottom of the tree
    z_row_left = grid[i,:j+1]
    z_row_right = grid[i,j:nb_columns]
    z_column_top = grid[:i+1,j]
    z_column_bottom = grid[i:nb_rows,j]
    sections = [z_row_left, z_row_right, z_column_top, z_column_bottom]

    for section in sections:
      if np.count_nonzero(section == max(section)) == 1:    # only one max allowed
        if x == max(section):
          visible_trees += 1
          break

print(visible_trees)