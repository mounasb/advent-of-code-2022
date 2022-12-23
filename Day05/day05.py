import re

with open("Day05/day05_input.txt") as f:
    content = f.read().splitlines()

# PART ONE
# Couldn't find a proper way to parse the initial input... -_-

stacks = {1: ['L', 'N', 'W', 'T', 'D'],
          2: ['C', 'P', 'H'],
          3: ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
          4: ['C', 'W', 'S', 'N', 'T', 'Q', 'L'],
          5: ['P', 'H', 'C', 'N'],
          6: ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
          7: ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
          8: ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
          9: ['W', 'G', 'D', 'N', 'P', 'L']
         }

moves = content[10:]
moves = [[int(char) for char in re.findall("\d+", move)] for move in moves]

for move in moves:
    nb_crates, first_stack_nb, second_stack_nb = move
    for i in range(nb_crates):
        crate = stacks[first_stack_nb].pop()
        stacks[second_stack_nb].append(crate)

stack_tops = ''
for value in stacks.values():
    stack_tops += value[-1]

print(stack_tops)