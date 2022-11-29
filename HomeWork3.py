# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# from decimal import Decimal as Dcm
# number = Dcm(input('Write a number: '))
# count = 0
# while number%1 != 0:
#     number *= 10
#
# new_number = int(number)
# while ((new_number*10)//10) != 0:
#     count += new_number % 10
#     new_number //= 10
# print(count)




# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
#
# n = int(input("Write a number: "))
# my_list = []
#
# for i in range(1, n+1):
#     my_list.append(float(round(((1 + 1 / i) ** i), 2)))
# print(*my_list)
# sum1 = 0
# count = 0
# while count < len(my_list):
#     sum1 += my_list[count]
#     count += 1
# print(sum1)

# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод


# import random, random
#
# num = int(input("Write a size of list: "))
# # my_list = [i for i in range(num)]
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