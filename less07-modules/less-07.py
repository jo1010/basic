import collections
import random
import math
import itertools
import re
from datetime import datetime


# counts

a = [1, 1, 2, 2, 3, 3, 3]
counts = collections.Counter(a)
print(counts)

# deaultdict
dict_of_lists = collections.defaultdict(list)
for value in range(1, 11):
    if value % 2 == 0:
        dict_of_lists['even'].append(value)
    else:
        dict_of_lists['odd'].append(value)

print(dict(dict_of_lists))

# deque
d = collections.deque([1, 2, 3])
print(d)
d.popleft()
print(d)
d.append(4)
d.appendleft(-1)
print(d)

# math
# print(math.isnan(1 / 0))

# random
print('RANDOM')
print(random.random()) # from 0 to 1
print(random.randint(0, 10)) # from range 0 -10
print(random.choice([1, 2, 3, 4, 5])) # choice from list
print(random.seed(42)) # generation starts from 42
seq = [1, 2, 3, 4, 6]
random.shuffle(seq) #returns nothing, shuffles the sequence
print(seq)

# intertools
print('intertools'.upper())
combs = itertools.combinations([1, 2, 3, 4], 3) # 1й параметр - что комбинируем,2й - по сколько (по 2, 3, ... n)
print(list(combs))

print(list(itertools.combinations_with_replacement([1, 2, 3, 4], 2))) # комбинирование, допускается совмещение одинаковых элементов

permutations = itertools.permutations([1, 2, 3, 4], 2) # комбинирование, смена порядка, но не допускает одинаковые элементы
print(list(permutations))

print(list(itertools.accumulate([1, 2, 3, 4, 5]))) # вместо элементов подставляет сумму текущего и предыдущих
print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda a, b: a-b))) #вместо элементов подставляет разность текущего и предыдущих

print(list(itertools.filterfalse(lambda x: x%2, range(11)))) # фильтр по условию (остаток от деления на 2 = 0(False)) для неабора значений range(11) (например: отбор только четных)

print('\nРЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ')
text = "Hi @mr_alex ! My name id John and I love coffee. #coffeelover #2021"
print(re.sub(r"[.!?\\-]", '', text)) # ищем набор символов из 1го параметра, заменяем из на 2й параметр. ищем в параметре text

print([e for e in re.finditer(r"#[A-Za-z0-9]*", text)]) # пример поиска. поиск хештегов, которые начинаются с #, содержат буквы цифры

print(re.split(r"[.!?\\-]", text)) # разделение текста по шаблону разделителей

print('\nDATETIME')
now = datetime.now()
print(now) # текущее дата время
print(datetime.time(now))
print(now.year, now.month, now.day)

date_string = "21 June, 2018"
date_object = datetime.strptime(date_string, "%d %B, %Y") # преобразование из строки по шаблону
print(date_object)

