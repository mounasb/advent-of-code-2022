import re

## PART ONE

with open("Day04/day04_input.txt") as f:
    sections = f.read().splitlines()

for i in range(len(sections)):
    numbers = re.findall("\d+", sections[i])
    sections[i] = [int(number) for number in numbers]

full_overlap_count = 0
for a, b, c, d in sections:
    # if one assignment fully contains the other
    full_overlap_condition = (a >= c and b <= d) or (c >= a and d <= b)
    if full_overlap_condition:
        full_overlap_count += 1

print(full_overlap_count)
print(10 * "-")


## PART TWO

overlap_count = 0
for a, b, c, d in sections:
    # if two assignments overlap
    overlap_condition = b >= c and a <= d
    if overlap_condition:
        overlap_count += 1

print(overlap_count)