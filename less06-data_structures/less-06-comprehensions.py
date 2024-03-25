# обычное создание списка
chars = []
for char in 'avssdfg':
    chars.append(char)
print(chars)

# генератор списка
chars = [char for char in 'avssdfg']
print(chars)

print('\n', '='*20, '\n')

names = ['mike', 'john', 'sally']
names = [name.capitalize() for name in names]
print(names)

print('\n', '='*20)

numbers = [number for number in range(1,7)]
# генератор списка с условием - только четные
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
print('\n', '='*20)
# генератор сета с действием
val_list = [1, 3, 3, 5,5, 2,2 ,1, 7]
unique_values = {value ** 2 for value in val_list}
print(unique_values)
print('\n', '='*20)
# генератор словаря
data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)

print('\n', '='*20)
values_squares = {value: value ** 2 for value in range(10)}
print(values_squares)

print('\n', '='*20)
# герератор кортежа
m = tuple(n for n in range(12))
print(m)

print('\n', '='*20)
print('\n', '='*20)
# генерация матриц
matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)

x = 0;