import numpy as np

with open("Day08/day08_input.txt") as f:
    content = f.read().splitlines()

# Parsing : generating a numpy array
grid = [list(x) for x in content]
grid = [[int(x) for x in l] for l in grid]
grid = np.array(grid)

# Initializing constants
sides = ((grid.shape[0] * 2) + (grid.shape[1] * 2)) - 4     # nb of trees on the sides
visible_trees = sides
nb_rows = grid.shape[0]
nb_columns = grid.shape[1]


## PART ONE

for i in range(1, nb_rows-1):
  for j in range(1, nb_columns-1):
    x = grid[i, j]    # isolating the tree
    # inspecting left, right, top and bottom of the tree :
    from_left = grid[i,:j+1]
    from_right = grid[i,j:]
    from_top = grid[:i+1,j]
    from_bottom = grid[i:,j]
    sections = [from_left, from_right, from_top, from_bottom]

    for section in sections:
      if np.count_nonzero(section == max(section)) == 1:    # only one max allowed
        if x == max(section):
          visible_trees += 1
          break

print("visible trees", visible_trees)


## PART TWO

view_scores = []

for i in range(1, nb_rows-1):
  for j in range(1, nb_columns-1):
    x = grid[i, j]    # isolating the tree
    # inspecting left, right, top and bottom of the tree :
    look_left = grid[i,:j+1][-2::-1]
    look_right = grid[i,j:][1:]
    look_top = grid[:i+1,j][-2::-1]
    look_bottom = grid[i:,j][1:]
    inspections = [look_left, look_right, look_top, look_bottom]

    view_score = 1
    for inspection in inspections:
      trees = 0
      for k in inspection:
        trees += 1
        if k >= x:
          break
      view_score *= trees
    
    view_scores.append(view_score)

print("best view_score", max(view_scores))