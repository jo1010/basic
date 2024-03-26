import collections
import itertools
import random

text = "blue car is parked right behind the building with blue walls and red door"

# 1. Написати функцію process, яка на вхід приймає рядок. Насамперед усередині функції знайдіть найчастіше слово
# (модуль combinations) і винесіть код в окремий метод get_max_count_word

# 2.  Знайдіть в тексті всі комбінації (пари по 2 слова) із словом, що найчастіше зустрічається. Винесіть код окремим
# методом get_max_count_word_combinations, який поверне список кортежів

# 3. Виберіть випадкову комбінацію зі списку, отриманого в пункті 2, та поверніть її у # методі process

def get_max_count_word(count_dict):
    max_count = 0
    max_count_word = None
    for word, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_count_word = word

    return max_count_word

def get_max_count_word_combinations(word, max_count_word):
    combinations = itertools.combinations(word, 2)
    max_count_word_combinations = [comb for comb in combinations if max_count_word in comb]
    return max_count_word_combinations

def process(text):
    words = text.split(' ')
    counts = collections.Counter(words)
    max_count_word = get_max_count_word(counts)
    max_count_word_combinations = get_max_count_word_combinations(words, max_count_word)
    random_combination = max_count_word_combinations[random.randint(0, len(max_count_word_combinations)-1)]
    return max_count_word, max_count_word_combinations, random_combination

max_count_words, max_count_combs, random_combination = process(text)
print(max_count_words, '\nmax_count_combs: ', max_count_combs, '\n random comb: ', random_combination)


