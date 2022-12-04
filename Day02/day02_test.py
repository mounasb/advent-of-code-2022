## PART ONE : UNIT TESTING

strategy_guide = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

letter_value = {'A': 1,
                'B': 2,
                'C': 3,
                'X': 1,
                'Y': 2,
                'Z': 3}

win_list = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
draw_list = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
lose_list = [('B', 'X'), ('C', 'Y'), ('A', 'Z')]

def my_score(elf_choice, my_choice):
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

def test_score_is_8_if_round_is_AY():
    assert my_score('A', 'Y') == 8

def test_score_is_9_if_round_is_BZ():
    assert my_score('B', 'Z') == 9

def test_score_is_1_if_round_is_BX():
    assert my_score('B', 'X') == 1

def test_score_is_2_if_round_is_CY():
    assert my_score('C', 'Y') == 2

def test_score_is_4_if_round_is_AX():
    assert my_score('A', 'X') == 4

def test_total_score_is_15():
    assert get_total_score(strategy_guide) == 15

print(get_total_score(strategy_guide))