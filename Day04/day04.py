import re

## PART ONE

with open("Day04/day04_input.txt") as f:
    sections = f.read().splitlines()

for i in range(len(sections)):
    numbers = re.findall("\d+", sections[i])
    sections[i] = [int(number) for number in numbers]

full_overlap_count = 0
for a, b, c, d in sections:
    full_overlap_condition = (a >= c and b <= d) or (c >= a and d <= b)
    if full_overlap_condition:
        full_overlap_count += 1

print(full_overlap_count)
print(10 * "-")


## PART TWO

overlap_count = 0
for a, b, c, d in sections:
    # print(a, b, c, d)
    overlap_condition = b >= c and a <= d
    if overlap_condition:
        # print("overlap\n")
        overlap_count += 1
    # else:
    #     print("no overlap\n")

print(overlap_count)