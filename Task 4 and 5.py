#4)#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

# Реализуйте алгоритм перемешивания списка.

import random

len_list = int(input('Введите число, длину списка :'))
range_random = int(input('Введите число  диапазон чисел от - до + '))

list1 = []
for i in range(len_list):
    list1.append(random.randint(-range_random, range_random))
    
print(f'Это список случайных чисел: {list1}')

list_find_index = []
len_find_index = int(input('Введите число, сколько ходите умножить индексов'))
if len_find_index > len_list:
    
    while  len_find_index > len_list or len_find_index < 0 :
        print('Вы ввели количество сложений ВНЕ заданного списка, попробуйте еще: ')
        len_find_index = int(input('Введите правильное число, сколько ходите умножить индексов'))
    

for i in range (len_find_index):
    index = (int(input('Введи индекс для умножения: ')))
    if index > len_list or index <0:
        
        while  index > len_list or index < 0:
            print('Такого индекса в списке нет, попробуйте еще раз')
            index = (int(input('Введи индекс для умножиения: ')))
        
    list_find_index.append(index)
mult = 0        
print (f' Это список индексов для произведения :{list_find_index}')
for i in range (len_find_index):
    mult *= list1[list_find_index[i]]
print (f'Произведение элементов заданных индексов равна :{mult}')


print('Произвожу произвольное перемешивание списка: ')

random_list = []
num = 0
for i in range (len_list):
    num = (random.randrange(len_list))
    if num not in random_list:
        random_list.append(num)
    else:
        while num in random_list:
            num = (random.randrange(len_list))
        random_list.append(num)
print(f'Это перемешанные индексы списка {random_list}')
list_random_position = []
for i in range (len_list):
    list_random_position.append(list1[random_list[i]])
print(f'Это список по созданным слуйно индексам {list_random_position}')
