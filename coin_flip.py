# coin flip streaks project in chapter 4

import random
number_of_streaks = 0
for experiment_number in range(10000):

    # code that creates a list of 100 'heads' or 'tails' values
    lst = []
    for _ in range(100):
        lst.append(random.randint(0, 1))

    # code that checks if there is a streak of 6 heads or tails in a row.
    for flip in range(len(lst) - 5):
        if lst[flip] == lst[flip + 1] and lst[flip] == lst[flip + 2] and lst[flip] == lst[flip + 3] and lst[flip] == lst[flip + 4] and lst[flip] == lst[flip + 5]:
            number_of_streaks = number_of_streaks + 1

print(number_of_streaks)
print('Chance of streak: %s%%' % (number_of_streaks / 10000))
