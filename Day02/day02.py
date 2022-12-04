## PART ONE 

rounds = []
with open("Day02/day02_input.txt") as f:
    rounds = [round.split() for round in f.readlines()]

letter_value = {'A': 1, 
                'B': 2,
                'C': 3,
                'X': 1,
                'Y': 2,
                'Z': 3}

win_list = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
draw_list = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
lose_list = [('B', 'X'), ('C', 'Y'), ('A', 'Z')]

def my_score(elf_choice, my_choice):
    # default = if I win
    score = 6
    if (elf_choice, my_choice) in lose_list:
        score = 0
    elif (elf_choice, my_choice) in draw_list:
        score = 3
    score += letter_value[my_choice]
    return score

def get_total_score(rounds):
    total_score = 0
    for round in rounds:
        total_score += my_score(round[0], round[1])
    return total_score

print(get_total_score(rounds))
print(10 * "-")


## PART TWO 

total_score = 0

for elf_choice, my_choice in rounds:
    if my_choice == 'X':
        for lose_combination in lose_list:
            if elf_choice == lose_combination[0]:
                my_choice = lose_combination[1]
                score = letter_value[my_choice]
                total_score += score
    elif my_choice == 'Y':
        for draw_combination in draw_list:
            if elf_choice == draw_combination[0]:
                my_choice = draw_combination[1]
                score = 3 + letter_value[my_choice]
                total_score += score
    else:
        for win_combination in win_list:
            if elf_choice == win_combination[0]:
                my_choice = win_combination[1]
                score = 6 + letter_value[my_choice]
                total_score += score

print(total_score)