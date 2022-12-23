import numpy as np

with open("Day08/day08_input.txt") as f:
    content = f.read().splitlines()

# Parsing : generating a numpy array
grid = [list(x) for x in content]
grid = [[int(x) for x in l] for l in grid]
grid = np.array(grid)

# Initializing constants
nb_rows = grid.shape[0]
nb_columns = grid.shape[1]
sides = ((nb_rows * 2) + (nb_columns * 2)) - 4     # nb of trees on the sides


## PART ONE

visible_trees = sides

# external trees are excluded from the iterations
# since they're always visible from outside the forest
for i in range(1, nb_rows-1):
  for j in range(1, nb_columns-1):
    x = grid[i, j]    # considering one tree at a time
    from_left = grid[i,:j+1]
    from_right = grid[i,j:]
    from_top = grid[:i+1,j]
    from_bottom = grid[i:,j]
    sections = [from_left, from_right, from_top, from_bottom]

    for section in sections:
      # to be visible from outside the forest, the tree's height has to be the unique max of its section 
      if (np.count_nonzero(section == max(section)) == 1) and (x == max(section)):
        visible_trees += 1
        break

print("visible trees", visible_trees)


## PART TWO

scenic_scores = []

# external trees are excluded from the iterations
# since their scenic_score is always 0
for i in range(1, nb_rows-1):
  for j in range(1, nb_columns-1):
    x = grid[i, j]    # considering one tree at a time
    look_left = grid[i,:j+1][-2::-1]    # iterating backwards
    look_right = grid[i,j:][1:]
    look_top = grid[:i+1,j][-2::-1]     # iterating backwards
    look_bottom = grid[i:,j][1:]
    inspections = [look_left, look_right, look_top, look_bottom]

    scenic_score = 1
    for inspection in inspections:
      trees = 0
      for k in inspection:
        trees += 1
        if k >= x:
          break
      scenic_score *= trees
    
    scenic_scores.append(scenic_score)

print("best scenic score", max(scenic_scores))