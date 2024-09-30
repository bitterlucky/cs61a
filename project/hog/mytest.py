from hog import *
dice = make_test_dice(*([2] * 55 + [1, 2] * 500))
value = max_scoring_num_rolls(dice, samples_count=1)
print(value)