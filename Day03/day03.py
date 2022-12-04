## PART ONE

with open("Day03/day03_input.txt") as f:
    rucksacks = f.read().splitlines()
    rucksacks_groups = [list(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)]        # useful for part 2

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total_priorities = 0

for rucksack in rucksacks:
    half_len = len(rucksack)//2     # cut the rucksack in two parts
    first_half = rucksack[:half_len]
    second_half = rucksack[half_len:len(rucksack)]
    common_letter = ''

    for char in first_half:
        # if the letter appears more than once in both rucksack halves, we only take it into account once
        if not common_letter:
            if char in second_half:
                common_letter = char
                char_priority = alphabet.index(char) + 1       # priorities start at 1, indexes start at 0
                total_priorities += char_priority

print(total_priorities)
print(10 * "-")


## PART TWO

total_badge_priorities = 0

for rucksack_group in rucksacks_groups:
    common_letter = ''
    for char in rucksack_group[0]:
        if not common_letter:
            # badge must be in all three elves' rucksacks
            if char in rucksack_group[1] and char in rucksack_group[2]:
                common_letter = char
                badge_priority = alphabet.index(char) + 1
                total_badge_priorities += badge_priority

print(total_badge_priorities)