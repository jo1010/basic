# #1 какое-то задание - словарь со списком в значении (с использованием форматной строки)
def func(index, count):
    return {
        'ID': index,
        'values': ['{}_{}'.format(index, value) for value in range(count)]
    }

def generate(count):
    return [func(i,j) for i, j in zip(range(count), list(range(count))[::-1])]

r = func(1, 3)
print(r)

# #2 сделать функцию, которая принимает аргумент count и вызывает функцию из предыдущего задакния и передает туда i, j
# где i - значение от 0 до count, а j - значения от count до 0. полученный слвоарь она добавляет в список, делая
# список словарей

r = generate(10)
print(r)

# 3. написати flatten list comprehansion для полученого списка словарей, где финальный результат будет - список
# из распакованных списков 'values' в каждом словаре

f = [value for sublist in r for value in sublist['values']]
print(f)