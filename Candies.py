# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Подумайте как наделить бота ""интеллектом""


from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = 150

def rules(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    if x < 0 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = rules(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = rules(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
