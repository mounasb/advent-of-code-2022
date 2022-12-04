##  PART ONE

with open("Day01/day01_input.txt") as f:
    numbers = f.read().splitlines()

total = 0
calories = []

for i, number in enumerate(numbers):
    if number:
        total += int(number)
        if i == len(numbers) - 1:
            calories.append(total)      
    else:
        calories.append(total)
        total = 0

print(max(calories))
print(10 * "-")


## PART TWO

top_calories = max(calories)

for i in range(2):
    calories.remove(max(calories))
    top_calories += max(calories)

print(top_calories)