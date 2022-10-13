import random

len_list = int(input('Введите число, длину списка :'))
range_random = int(input('Введите число  диапазон чисел от - до + '))

list1 = []
for i in range(len_list):
    list1.append(random.randint(-range_random, range_random))
    
print(list1)

list_find_index = []
len_find_index = int(input('Введите число, сколько ходите сложить индексов'))
if len_find_index > len_list:
    print('Вы ввели количество сложений большего заданного списка, попробуйте еще: ')
    
else:
    for i in range (len_find_index):
        list_find_index.append(int(input('Введи индекс для суммы: ')))
sum = 0        
print (f' Это список индексов для сложения :{list_find_index}')
for i in range (len_find_index):
    sum += list1[list_find_index[i]]
print (f'Сумма заданных индексов равна :{sum}')


print('Произвожу произвольное перемешивание списка: ')
def num_randon(n):
    num = (random.randrange(n))
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
