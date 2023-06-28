'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

def shaw_ex(num):
    num_ex = 1
    print(num_ex, end=' ')
    while num_ex *2 < num:
        num_ex = num_ex * 2
        print(num_ex, end=' ')

num = int(input("Введите число: "))
shaw_ex(num)