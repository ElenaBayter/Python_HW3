# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

##BEFORE

# import random, random
#
# num = int(input("Write a size of list: "))
#
# my_list = []
# for i in range(num):
#     my_list.append(i)
# print(*my_list)
# new_list=[]
# for i in my_list:
#     i=random.randrange(len(my_list))
#     new_list.append(i)
# print(new_list)



##AFTER

# import random, random
#
# my_list = [random.randint(0,100) for _ in range(10)]
#
# print(*my_list)
#
# for i in range(len(my_list)):
#     k = random.randint(0, (len(my_list) - 1))
#     my_list.append(my_list.pop(k))
# print(my_list)



#  Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

##BEFORE

# text = 'First digit - 1, second digit - 2, sum 3'
# sub_text = input("Write sub string: ")
# count = 0
# for i in range(len(text)):
#     if text[i:i+len(sub_text)] == sub_text:
#         count += 1
# print(f'Sub string {sub_text} met in our text {count} times')

##AFTER

# text = 'First digit - 1, second digit - 2, sum 3'
# sub_text = input("Write sub string: ")
# print(text.count(sub_text))


# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


##BEFORE

# import random, random

# size = int(input("Write a size of list: "))
#
# my_list = []
# for i in range(size):
#     i = random.uniform(0, 10000)
#     my_list.append(round(i, 2))
# print(*my_list)
# new_list = []
# desim = 0
# for i in range(len(my_list)):
#     desim = my_list[i]-int(my_list[i])
#     new_list.append(round(desim, 2))
# print(*new_list)
# max_desim_number = max(new_list)
# print(max_desim_number)
# min_desim_number = min(new_list)
# print(min_desim_number)
# result = max_desim_number - min_desim_number
# print(f'Difference between maximal and minimal fractional parts of elements is {round(result, 2)}')



##AFTER

# import random, random
#
# size = int(input("Write a size of list: "))
#
# my_list = [round(random.uniform(0, 10), 3) for  _ in range(size)]
# print(*my_list)
#
# division = list(map(lambda x: x-int(x), my_list))
# division = list(map(lambda x: round(x, 3), division))
# print(max(division) - min(division))
