# 1.Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

# import random
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1, 100)
#     some_list.append(number)
# print(some_list)

# max_number = some_list[1]

# for i in range (count - 1, 1, -1):
#     if  some_list[i - 1] < some_list[i] > some_list[i + 1]:
#         max_number = some_list[i]
#         break

# print(max_number)
# print(i)




# 2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

# import random
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1, 3)
#     some_list.append(number)
# print(some_list)

# max_count = 0
# number = some_list[0]
# count_el = 0

# for i in range (count - 1):
#         count_el = some_list.count(i)
#         if count_el > max_count:
#             max_count = count_el
      
# print(max_count)




# 3.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

import random
count = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(count):
    number = random.randint(1, 10)
    some_list.append(number)
print(some_list)

new_list = list(set(some_list))
print(new_list)
print(new_list[len(new_list)-2])




# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

# import random
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(1, 100)
#     some_list.append(number)
# print(some_list)

# some_set = set(some_list)
# print(len(some_set))