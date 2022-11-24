# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Пример:
# 67,82 -> 23

number = input("Введите число: ")
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print(sum)

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N. Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
f = 1
if number > 0:
    for i in range(1, number+1):
        f *= i
        print(f, end=' ')


# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму. Пример:
# n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

number = int(input('Введите число: '))
my_dict = {}
for i in range(1, number + 1):
    my_dict[i] = round((1+1/i)**i, 2)
print(my_dict)

# Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на введенных пользователем
# позициях.

number = int(input('Введите число: '))
my_list = []
for i in range(-number, number+1):
    my_list.append(i)
print(my_list)
pos_1 = int(input('Введите индекс из списка для первого числа: '))
pos_2 = int(input('Введите индекс из списка для второго числа: '))
result = my_list[pos_1] * my_list[pos_2]
print('Произведение =', result)

# *Реализуйте алгоритм перемешивания списка.
import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(my_list)-1, 0, -1):
    my_list.append(i)
    j = random.randint(0, i+2)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
    
